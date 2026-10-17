"""Profile local reference-video metadata and advise original lesson batches."""

from __future__ import annotations

import argparse
from collections import defaultdict
from datetime import datetime, timezone
import json
import math
import re
from pathlib import Path
import statistics
import sqlite3
import subprocess
import sys
from typing import Any

from exam_engine.engine import DataValidationError, load_topics
from matrix_pipeline import ROOT, match_concepts
from knowledge.graph import load_graph


DEFAULT_DATABASE = ROOT / "output" / "production_knowledge.sqlite"
DEFAULT_REFERENCE_VIDEOS = ROOT / "3b1b"
SCHEMA_VERSION = 1
_SEGMENT = re.compile(r"^(?P<title>.+)_(?P<start>\d+)_(?P<end>\d+)$")
_SCENE_TIME = re.compile(r"pts_time:\s*(-?\d+(?:\.\d+)?)")
_DURATION = re.compile(r"Duration:\s*(\d+):(\d+):(\d+(?:\.\d+)?)")
_VIDEO_STREAM = re.compile(
    r"Video:\s*([^,\s]+).*?(\d{2,5})x(\d{2,5}).*?(\d+(?:\.\d+)?)\s*fps",
    re.IGNORECASE,
)
_AUDIO_STREAM = re.compile(
    r"Audio:\s*([^,\s]+).*?(\d+)\s*Hz,\s*([^,\r\n]+)", re.IGNORECASE
)
_AUDIO_LEVEL = re.compile(r"(mean|max)_volume:\s*(-?\d+(?:\.\d+)?)\s*dB")
_SILENCE_START = re.compile(r"silence_start:\s*(-?\d+(?:\.\d+)?)")
_SILENCE_END = re.compile(
    r"silence_end:\s*(-?\d+(?:\.\d+)?).*?silence_duration:\s*(\d+(?:\.\d+)?)"
)
PRACTICE_RULES: tuple[dict[str, Any], ...] = (
    {
        "rule_id": "question-first",
        "area": "story",
        "concept_ids": [],
        "content_types": ["problem", "concept"],
        "weight": 1.0,
        "guidance": "Open with one concrete question; make its answer explicit by the close.",
        "reason": "A specific question gives the learner a reason to track each step.",
    },
    {
        "rule_id": "model-before-algebra",
        "area": "story",
        "concept_ids": [],
        "content_types": ["problem", "concept"],
        "weight": 1.0,
        "guidance": "State the model, coordinate/sign convention, and assumptions before calculating.",
        "reason": "The equations are only meaningful when their model and conventions are clear.",
    },
    {
        "rule_id": "reasoning-beats",
        "area": "editing",
        "concept_ids": [],
        "content_types": ["problem", "concept"],
        "weight": 0.9,
        "guidance": "Cut or transition at a change in the reasoning, not at an arbitrary beat; hold each new diagram long enough to inspect.",
        "reason": "The reference clips have measurable scene-change candidates, but their rates are observations, not editing targets.",
    },
    {
        "rule_id": "visual-encodes-operation",
        "area": "visuals",
        "concept_ids": [],
        "content_types": ["problem", "concept"],
        "weight": 1.0,
        "guidance": "Make each motion, construction, or color change encode a named quantity or mathematical operation.",
        "reason": "A visual should let the learner inspect the same relationship used in the derivation.",
    },
    {
        "rule_id": "math-readable",
        "area": "narration",
        "concept_ids": ["math:matrices", "math:linear-systems", "math:derivatives", "math:integrals", "math:fourier"],
        "content_types": ["problem", "concept"],
        "weight": 1.2,
        "guidance": "Pause on dense notation; narrate signs, grouping, units, and variable meaning without racing ahead of the display.",
        "reason": "The learner needs time to connect spoken mathematics to the visible symbols.",
    },
    {
        "rule_id": "spoken-visual-complement",
        "area": "narration",
        "concept_ids": [],
        "content_types": ["problem", "concept"],
        "weight": 0.9,
        "guidance": "Use short original narration to explain what to notice; do not read every visible label aloud.",
        "reason": "The voice and diagram can carry complementary parts of the explanation.",
    },
    {
        "rule_id": "speech-priority",
        "area": "sound",
        "concept_ids": [],
        "content_types": ["problem", "concept"],
        "weight": 1.0,
        "guidance": "Keep speech intelligible above any original music; lower or remove the bed under equations and important claims.",
        "reason": "The reference audio-level measurements do not identify whether a signal is speech, music, or effects.",
    },
    {
        "rule_id": "sound-has-a-job",
        "area": "sound",
        "concept_ids": [],
        "content_types": ["problem", "concept"],
        "weight": 0.85,
        "guidance": "Use an original sound cue only when it marks a meaningful transition or result; silence is a valid choice.",
        "reason": "Avoid adding effects that compete with mathematical attention.",
    },
    {
        "rule_id": "derive-and-check",
        "area": "verification",
        "concept_ids": [],
        "content_types": ["problem", "concept"],
        "weight": 1.0,
        "guidance": "End the derivation with an independent check such as units, substitution, a limiting case, or a geometric interpretation.",
        "reason": "A result should be inspectable rather than accepted on authority.",
    },
    {
        "rule_id": "matrix-meaning",
        "area": "visuals",
        "concept_ids": ["math:matrices", "math:linear-maps", "math:eigenmodes"],
        "content_types": ["problem", "concept"],
        "weight": 1.35,
        "guidance": "Show what a matrix does to a meaningful vector or state; keep input, transformation, and output visible.",
        "reason": "The representation connects matrix algebra to geometry or a model state.",
    },
    {
        "rule_id": "calculus-meaning",
        "area": "visuals",
        "concept_ids": ["math:derivatives", "math:integrals", "math:graphs"],
        "content_types": ["problem", "concept"],
        "weight": 1.35,
        "guidance": "Connect slope or accumulated area to a defined quantity and its units before presenting a symbolic shortcut.",
        "reason": "The geometric interpretation and the algebra should check one another.",
    },
    {
        "rule_id": "exam-solution-audit",
        "area": "exam-problem",
        "concept_ids": [],
        "content_types": ["problem"],
        "weight": 1.25,
        "guidance": "For an exam-style problem, distinguish verified source material from an original practice problem and independently check the answer.",
        "reason": "Topic matching alone does not establish PYQ provenance or answer correctness.",
    },
)


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _connect(path: Path) -> sqlite3.Connection:
    path = Path(path)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        connection = sqlite3.connect(path)
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys = ON")
        return connection
    except (OSError, sqlite3.Error) as exc:
        raise DataValidationError(f"cannot open production knowledge database {path}: {exc}") from exc


def _schema(connection: sqlite3.Connection) -> None:
    try:
        connection.executescript(
            """
            CREATE TABLE IF NOT EXISTS production_schema (
                version INTEGER PRIMARY KEY,
                created_at TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS media_profiles (
                id INTEGER PRIMARY KEY,
                relative_path TEXT NOT NULL UNIQUE,
                file_size INTEGER NOT NULL,
                mtime_ns INTEGER NOT NULL,
                group_title TEXT NOT NULL,
                segment_start_seconds REAL,
                segment_end_seconds REAL,
                duration_seconds REAL NOT NULL,
                width INTEGER NOT NULL,
                height INTEGER NOT NULL,
                frame_rate REAL NOT NULL,
                video_codec TEXT NOT NULL,
                has_audio INTEGER NOT NULL CHECK (has_audio IN (0, 1)),
                audio_codec TEXT,
                audio_sample_rate_hz INTEGER,
                audio_channels TEXT,
                scene_change_candidates INTEGER NOT NULL,
                scene_change_candidates_per_minute REAL NOT NULL,
                audio_mean_db REAL,
                audio_peak_db REAL,
                silence_seconds REAL,
                concept_ids_json TEXT NOT NULL,
                analysis_status TEXT NOT NULL CHECK (analysis_status IN ('complete', 'failed')),
                analysis_error TEXT NOT NULL,
                analyzed_at TEXT NOT NULL
            );
            CREATE INDEX IF NOT EXISTS media_profiles_group_idx
                ON media_profiles(group_title);
            CREATE TABLE IF NOT EXISTS practice_rules (
                rule_id TEXT PRIMARY KEY,
                area TEXT NOT NULL,
                concept_ids_json TEXT NOT NULL,
                content_types_json TEXT NOT NULL,
                weight REAL NOT NULL CHECK (weight > 0),
                guidance TEXT NOT NULL,
                reason TEXT NOT NULL,
                origin TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS human_reviews (
                id INTEGER PRIMARY KEY,
                video_title TEXT NOT NULL,
                concept_ids_json TEXT NOT NULL,
                editing_rating INTEGER NOT NULL CHECK (editing_rating BETWEEN 1 AND 5),
                narration_pacing_rating INTEGER NOT NULL CHECK (narration_pacing_rating BETWEEN 1 AND 5),
                narration_clarity_rating INTEGER NOT NULL CHECK (narration_clarity_rating BETWEEN 1 AND 5),
                narration_sync_rating INTEGER NOT NULL CHECK (narration_sync_rating BETWEEN 1 AND 5),
                sound_rating INTEGER NOT NULL CHECK (sound_rating BETWEEN 1 AND 5),
                visual_clarity_rating INTEGER NOT NULL CHECK (visual_clarity_rating BETWEEN 1 AND 5),
                notes TEXT NOT NULL,
                reviewed_at TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS batch_recommendations (
                id INTEGER PRIMARY KEY,
                batch_id TEXT NOT NULL,
                selected_concepts_json TEXT NOT NULL,
                plan_json TEXT NOT NULL,
                generated_at TEXT NOT NULL
            );
            INSERT OR IGNORE INTO production_schema(version, created_at)
                VALUES (1, '2026-10-17T00:00:00+00:00');
            """
        )
        version = connection.execute(
            "SELECT MAX(version) AS version FROM production_schema"
        ).fetchone()["version"]
        if version != SCHEMA_VERSION:
            raise DataValidationError(
                f"production database schema {version} is not supported (expected {SCHEMA_VERSION})"
            )
        with connection:
            for rule in PRACTICE_RULES:
                connection.execute(
                    """
                    INSERT OR IGNORE INTO practice_rules
                    (rule_id, area, concept_ids_json, content_types_json, weight,
                     guidance, reason, origin)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        rule["rule_id"],
                        rule["area"],
                        json.dumps(rule["concept_ids"]),
                        json.dumps(rule["content_types"]),
                        rule["weight"],
                        rule["guidance"],
                        rule["reason"],
                        "original-general-teaching-principle",
                    ),
                )
    except sqlite3.Error as exc:
        raise DataValidationError(f"cannot initialize production knowledge database: {exc}") from exc


def _filename_metadata(path: Path) -> tuple[str, float | None, float | None]:
    match = _SEGMENT.fullmatch(path.stem)
    if not match:
        return path.stem, None, None
    start = float(match.group("start"))
    end = float(match.group("end"))
    if end <= start:
        return match.group("title"), start, end
    return match.group("title").strip(), start, end


def _concept_matches(title: str, graph: Any) -> list[str]:
    return list(match_concepts(title, graph))


def _run_ffmpeg(path: Path) -> dict[str, Any]:
    try:
        import imageio_ffmpeg
    except ImportError as exc:
        raise DataValidationError(
            "local media profiling requires imageio-ffmpeg; install project requirements"
        ) from exc
    executable = imageio_ffmpeg.get_ffmpeg_exe()
    command = [
        executable,
        "-hide_banner",
        "-i",
        str(path),
        "-vf",
        "select='gt(scene,0.30)',showinfo",
        "-af",
        "volumedetect,silencedetect=noise=-45dB:d=0.25",
        "-vsync",
        "0",
        "-f",
        "null",
        "-",
    ]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=False)
    except OSError as exc:
        raise DataValidationError(f"cannot run the bundled FFmpeg decoder: {exc}") from exc
    if result.returncode:
        detail = result.stderr.strip().splitlines()[-1:] or ["unknown FFmpeg error"]
        raise DataValidationError(f"cannot analyze video {path.name}: {detail[0]}")
    stderr = result.stderr
    duration_match = _DURATION.search(stderr)
    video_match = _VIDEO_STREAM.search(stderr)
    if duration_match is None or video_match is None:
        raise DataValidationError(f"cannot read video duration or video stream in {path.name}")
    hours, minutes, seconds = duration_match.groups()
    duration = int(hours) * 3600 + int(minutes) * 60 + float(seconds)
    if duration <= 0:
        raise DataValidationError(f"video has invalid duration: {path.name}")
    audio_match = _AUDIO_STREAM.search(stderr)
    audio_levels = {
        name: float(value)
        for name, value in _AUDIO_LEVEL.findall(stderr)
    }
    scene_times = [float(value) for value in _SCENE_TIME.findall(stderr)]
    silence_duration = sum(float(value) for _, value in _SILENCE_END.findall(stderr))
    open_silences = _SILENCE_START.findall(stderr)
    if open_silences:
        silence_duration += max(0.0, duration - float(open_silences[-1]))
    silence_duration = min(duration, silence_duration)
    return {
        "duration_seconds": duration,
        "width": int(video_match.group(2)),
        "height": int(video_match.group(3)),
        "frame_rate": float(video_match.group(4)),
        "video_codec": video_match.group(1),
        "has_audio": audio_match is not None,
        "audio_codec": audio_match.group(1) if audio_match else None,
        "audio_sample_rate_hz": int(audio_match.group(2)) if audio_match else None,
        "audio_channels": audio_match.group(3).split(",")[0].strip() if audio_match else None,
        "scene_change_candidates": len(scene_times),
        "scene_change_candidates_per_minute": len(scene_times) / (duration / 60.0),
        "audio_mean_db": audio_levels.get("mean"),
        "audio_peak_db": audio_levels.get("max"),
        "silence_seconds": silence_duration if audio_match else None,
    }


def _media_relative_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT.resolve()).as_posix()
    except ValueError as exc:
        raise DataValidationError(
            f"reference video must be stored inside the repository: {path}"
        ) from exc


class ProductionKnowledge:
    """Own SQLite store for local media measurements, reviews, and advice."""

    def __init__(self, path: Path = DEFAULT_DATABASE):
        self.path = Path(path)
        connection = _connect(self.path)
        try:
            _schema(connection)
        finally:
            connection.close()

    def index_videos(
        self, videos_dir: Path = DEFAULT_REFERENCE_VIDEOS
    ) -> dict[str, Any]:
        videos_dir = Path(videos_dir)
        if not videos_dir.is_dir():
            raise DataValidationError(f"reference video folder does not exist: {videos_dir}")
        paths = sorted(
            path for path in videos_dir.rglob("*")
            if path.is_file() and path.suffix.lower() in {".mp4", ".mov", ".mkv", ".webm"}
        )
        if not paths:
            raise DataValidationError(f"no supported local video files found in {videos_dir}")
        topics = load_topics(ROOT / "data" / "physics_topics.csv")
        graph = load_graph(
            ROOT / "knowledge" / "concepts.csv",
            ROOT / "knowledge" / "links.csv",
            topics,
        )

        indexed = 0
        unchanged = 0
        errors: list[dict[str, str]] = []
        connection = _connect(self.path)
        try:
            with connection:
                for path in paths:
                    relative_path = _media_relative_path(path)
                    try:
                        metadata = path.stat()
                        old = connection.execute(
                            "SELECT file_size, mtime_ns, analysis_status, analysis_error "
                            "FROM media_profiles WHERE relative_path = ?",
                            (relative_path,),
                        ).fetchone()
                        if old and (
                            old["file_size"], old["mtime_ns"]
                        ) == (metadata.st_size, metadata.st_mtime_ns):
                            unchanged += 1
                            if old["analysis_status"] == "failed":
                                errors.append(
                                    {"path": relative_path, "error": old["analysis_error"]}
                                )
                            continue
                        group_title, start, end = _filename_metadata(path)
                        profile = _run_ffmpeg(path)
                        concept_ids = _concept_matches(group_title, graph)
                        connection.execute(
                            """
                            INSERT INTO media_profiles (
                                relative_path, file_size, mtime_ns, group_title,
                                segment_start_seconds, segment_end_seconds,
                                duration_seconds, width, height, frame_rate, video_codec,
                                has_audio, audio_codec, audio_sample_rate_hz, audio_channels,
                                scene_change_candidates, scene_change_candidates_per_minute,
                                audio_mean_db, audio_peak_db, silence_seconds, concept_ids_json,
                                analysis_status, analysis_error, analyzed_at
                            ) VALUES (
                                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                                'complete', '', ?
                            )
                            ON CONFLICT(relative_path) DO UPDATE SET
                                file_size = excluded.file_size,
                                mtime_ns = excluded.mtime_ns,
                                group_title = excluded.group_title,
                                segment_start_seconds = excluded.segment_start_seconds,
                                segment_end_seconds = excluded.segment_end_seconds,
                                duration_seconds = excluded.duration_seconds,
                                width = excluded.width, height = excluded.height,
                                frame_rate = excluded.frame_rate,
                                video_codec = excluded.video_codec,
                                has_audio = excluded.has_audio,
                                audio_codec = excluded.audio_codec,
                                audio_sample_rate_hz = excluded.audio_sample_rate_hz,
                                audio_channels = excluded.audio_channels,
                                scene_change_candidates = excluded.scene_change_candidates,
                                scene_change_candidates_per_minute =
                                    excluded.scene_change_candidates_per_minute,
                                audio_mean_db = excluded.audio_mean_db,
                                audio_peak_db = excluded.audio_peak_db,
                                silence_seconds = excluded.silence_seconds,
                                concept_ids_json = excluded.concept_ids_json,
                                analysis_status = 'complete', analysis_error = '',
                                analyzed_at = excluded.analyzed_at
                            """,
                            (
                                relative_path, metadata.st_size, metadata.st_mtime_ns,
                                group_title, start, end, profile["duration_seconds"],
                                profile["width"], profile["height"], profile["frame_rate"],
                                profile["video_codec"], int(profile["has_audio"]),
                                profile["audio_codec"], profile["audio_sample_rate_hz"],
                                profile["audio_channels"], profile["scene_change_candidates"],
                                profile["scene_change_candidates_per_minute"],
                                profile["audio_mean_db"], profile["audio_peak_db"],
                                profile["silence_seconds"], json.dumps(concept_ids), _utc_now(),
                            ),
                        )
                        indexed += 1
                    except (DataValidationError, OSError) as exc:
                        error = str(exc)
                        errors.append({"path": relative_path, "error": error})
                        metadata = path.stat()
                        group_title, start, end = _filename_metadata(path)
                        connection.execute(
                            """
                            INSERT INTO media_profiles (
                                relative_path, file_size, mtime_ns, group_title,
                                segment_start_seconds, segment_end_seconds,
                                duration_seconds, width, height, frame_rate, video_codec,
                                has_audio, scene_change_candidates,
                                scene_change_candidates_per_minute, concept_ids_json,
                                analysis_status, analysis_error, analyzed_at,
                                audio_channels
                            ) VALUES (?, ?, ?, ?, ?, ?, 0, 0, 0, 0, '', 0, 0, 0, '[]',
                                      'failed', ?, ?, '')
                            ON CONFLICT(relative_path) DO UPDATE SET
                                file_size = excluded.file_size, mtime_ns = excluded.mtime_ns,
                                analysis_status = 'failed', analysis_error = excluded.analysis_error,
                                analyzed_at = excluded.analyzed_at
                            """,
                            (
                                relative_path, metadata.st_size, metadata.st_mtime_ns,
                                group_title, start, end, error, _utc_now(),
                            ),
                        )
        finally:
            connection.close()
        return {
            "indexed": indexed,
            "unchanged": unchanged,
            "failed": len(errors),
            "errors": errors,
            "database": str(self.path),
        }

    def record_review(
        self,
        *,
        video_title: str,
        concept_ids: list[str],
        editing: int,
        narration_pacing: int,
        narration_clarity: int,
        narration_sync: int,
        sound: int,
        visual_clarity: int,
        notes: str = "",
    ) -> int:
        if not video_title.strip():
            raise DataValidationError("video_title cannot be empty")
        if not concept_ids or any(not value.strip() for value in concept_ids):
            raise DataValidationError("at least one non-empty concept ID is required")
        ratings = (
            editing, narration_pacing, narration_clarity, narration_sync,
            sound, visual_clarity,
        )
        if any(not isinstance(value, int) or isinstance(value, bool) or not 1 <= value <= 5 for value in ratings):
            raise DataValidationError("all review ratings must be integers from 1 to 5")
        if len(notes) > 500:
            raise DataValidationError("review notes must not exceed 500 characters")
        connection = _connect(self.path)
        try:
            with connection:
                cursor = connection.execute(
                    """
                    INSERT INTO human_reviews (
                        video_title, concept_ids_json, editing_rating,
                        narration_pacing_rating, narration_clarity_rating,
                        narration_sync_rating, sound_rating, visual_clarity_rating,
                        notes, reviewed_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        video_title.strip(), json.dumps(sorted(set(concept_ids))),
                        editing, narration_pacing, narration_clarity, narration_sync,
                        sound, visual_clarity, notes.strip(), _utc_now(),
                    ),
                )
                return int(cursor.lastrowid)
        except sqlite3.Error as exc:
            raise DataValidationError(f"cannot record production review: {exc}") from exc
        finally:
            connection.close()

    def advise_batch(
        self,
        manifest: dict[str, Any],
        matrix: dict[str, Any],
    ) -> dict[str, Any]:
        _validate_matrix(matrix)
        topics = load_topics(ROOT / "data" / "physics_topics.csv")
        graph = load_graph(
            ROOT / "knowledge" / "concepts.csv",
            ROOT / "knowledge" / "links.csv",
            topics,
        )
        batch_id = manifest.get("batch_id")
        episodes = manifest.get("episodes")
        if not isinstance(batch_id, str) or not batch_id.strip():
            raise DataValidationError("batch manifest needs a non-empty batch_id")
        if not isinstance(episodes, list) or not episodes:
            raise DataValidationError("batch manifest needs a non-empty episodes list")
        concepts = {
            item.get("concept_id"): item for item in matrix["concepts"]
        }
        advice_items = []
        batch_concepts: set[str] = set()
        for episode in episodes:
            if not isinstance(episode, dict):
                raise DataValidationError("every batch episode must be an object")
            episode_id = episode.get("id")
            if not isinstance(episode_id, str) or not episode_id.strip():
                raise DataValidationError("every batch episode needs a non-empty id")
            concept_scores = _episode_concepts(episode, matrix, concepts, graph)
            if not concept_scores:
                raise DataValidationError(
                    f"{episode_id}: no matching concepts in the provided matrix"
                )
            batch_concepts.update(concept_scores)
            content_type = episode.get("type", "concept")
            if content_type not in {"problem", "concept"}:
                content_type = "concept"
            rules = self._rank_rules(concept_scores, content_type)
            reference_summary = self._reference_summary(set(concept_scores))
            advice_items.append(
                {
                    "episode_id": episode_id,
                    "title": episode.get("title", ""),
                    "topic_id": episode.get("topic_id", ""),
                    "matrix_concepts": [
                        {
                            "concept_id": concept_id,
                            "name": concepts[concept_id].get("concept_name", concept_id),
                            "evidence_score": round(score, 4),
                        }
                        for concept_id, score in sorted(
                            concept_scores.items(), key=lambda item: (-item[1], item[0])
                        )
                    ],
                    "advice_by_area": _group_rules(rules),
                    "local_reference_measurements": reference_summary,
                    "formats": ["vertical", "horizontal"],
                    "video_specific_capture": False,
                    "review_required": True,
                }
            )
        plan = {
            "schema_version": SCHEMA_VERSION,
            "batch_id": batch_id,
            "status": "advisory-draft-not-a-render-instruction",
            "reference_corpus": "local technical video measurements and original general principles",
            "imitation_guardrail": (
                "Do not copy any creator's narration, scripts, distinctive visuals, pacing signature, "
                "music, sound design, or scene sequence. Use the evidence only to inform original work."
            ),
            "limitations": [
                "No speech recognition, transcript extraction, voice identity analysis, or source frames are stored.",
                "FFmpeg scene-change candidates are technical estimates, not a human edit-quality judgment.",
                "Audio level and silence measures cannot identify speech, music, or sound effects.",
                "Reference video titles provide only tentative concept tags; manually review them.",
                "Matrix matches and source question tags do not verify a PYQ or its answer.",
                "Use only videos that you have the right to analyze; the database stores derived measurements and local paths only.",
            ],
            "deliverable_count": len(advice_items) * 2,
            "episode_count": len(advice_items),
            "episodes": advice_items,
        }
        connection = _connect(self.path)
        try:
            with connection:
                connection.execute(
                    """
                    INSERT INTO batch_recommendations (
                        batch_id, selected_concepts_json, plan_json, generated_at
                    ) VALUES (?, ?, ?, ?)
                    """,
                    (
                        batch_id, json.dumps(sorted(batch_concepts)),
                        json.dumps(plan, ensure_ascii=False), _utc_now(),
                    ),
                )
        except sqlite3.Error as exc:
            raise DataValidationError(f"cannot persist batch advice: {exc}") from exc
        finally:
            connection.close()
        return plan

    def _rank_rules(
        self, selected: dict[str, float], content_type: str
    ) -> list[dict[str, Any]]:
        connection = _connect(self.path)
        try:
            rules = connection.execute("SELECT * FROM practice_rules").fetchall()
            reviews = connection.execute("SELECT * FROM human_reviews").fetchall()
        except sqlite3.Error as exc:
            raise DataValidationError(f"cannot read production knowledge: {exc}") from exc
        finally:
            connection.close()
        ranked: list[dict[str, Any]] = []
        for row in rules:
            applicable_types = json.loads(row["content_types_json"])
            if content_type not in applicable_types:
                continue
            rule_concepts = set(json.loads(row["concept_ids_json"]))
            overlaps = rule_concepts.intersection(selected)
            if rule_concepts and not overlaps:
                continue
            evidence_score = sum(selected[concept_id] for concept_id in overlaps)
            feedback: list[int] = []
            for review in reviews:
                reviewed_concepts = set(json.loads(review["concept_ids_json"]))
                if not reviewed_concepts.intersection(selected):
                    continue
                rating_field = {
                    "editing": "editing_rating",
                    "sound": "sound_rating",
                    "visuals": "visual_clarity_rating",
                }.get(row["area"])
                if row["area"] == "narration":
                    feedback.extend(
                        int(review[field])
                        for field in (
                            "narration_pacing_rating",
                            "narration_clarity_rating",
                            "narration_sync_rating",
                        )
                    )
                elif rating_field:
                    feedback.append(int(review[rating_field]))
            priority = float(row["weight"]) * (1.0 + evidence_score)
            if feedback:
                priority *= 0.75 + statistics.fmean(feedback) / 10.0
            ranked.append(
                {
                    "rule_id": row["rule_id"],
                    "area": row["area"],
                    "guidance": row["guidance"],
                    "reason": row["reason"],
                    "priority": round(priority, 4),
                    "matched_concepts": sorted(overlaps),
                    "evidence": (
                        "concept-specific-original-principle" if overlaps
                        else "general-original-teaching-principle"
                    ),
                    "review_sample_count": len(feedback),
                }
            )
        ranked.sort(key=lambda item: (-item["priority"], item["rule_id"]))
        by_area: dict[str, int] = defaultdict(int)
        limited = []
        for rule in ranked:
            if by_area[rule["area"]] >= 2:
                continue
            by_area[rule["area"]] += 1
            limited.append(rule)
        return limited

    def _reference_summary(self, selected_concepts: set[str]) -> dict[str, Any]:
        connection = _connect(self.path)
        try:
            rows = connection.execute(
                "SELECT * FROM media_profiles WHERE analysis_status = 'complete'"
            ).fetchall()
        except sqlite3.Error as exc:
            raise DataValidationError(f"cannot summarize local media profiles: {exc}") from exc
        finally:
            connection.close()
        matching: dict[str, list[sqlite3.Row]] = defaultdict(list)
        for row in rows:
            tags = set(json.loads(row["concept_ids_json"]))
            overlap = tags.intersection(selected_concepts)
            if overlap:
                matching[row["group_title"]].append(row)
        group_metrics = []
        for title, segments in matching.items():
            duration = sum(float(row["duration_seconds"]) for row in segments)
            cuts = sum(int(row["scene_change_candidates"]) for row in segments)
            mean_levels = [
                (float(row["audio_mean_db"]), float(row["duration_seconds"]))
                for row in segments if row["audio_mean_db"] is not None
            ]
            peak_levels = [float(row["audio_peak_db"]) for row in segments if row["audio_peak_db"] is not None]
            group_metrics.append(
                {
                    "group_title": title,
                    "segment_count": len(segments),
                    "approximate_duration_seconds": duration,
                    "scene_change_candidates_per_minute": (
                        cuts / (duration / 60) if duration else 0.0
                    ),
                    "duration_weighted_mean_audio_db": (
                        sum(level * seconds for level, seconds in mean_levels)
                        / sum(seconds for _, seconds in mean_levels)
                        if mean_levels else None
                    ),
                    "max_audio_peak_db": max(peak_levels) if peak_levels else None,
                }
            )
        cut_rates = [item["scene_change_candidates_per_minute"] for item in group_metrics]
        audio_means = [
            item["duration_weighted_mean_audio_db"]
            for item in group_metrics
            if item["duration_weighted_mean_audio_db"] is not None
        ]
        return {
            "matched_reference_video_groups": len(group_metrics),
            "measurements_by_group": group_metrics,
            "median_scene_change_candidates_per_minute": (
                statistics.median(cut_rates) if cut_rates else None
            ),
            "median_audio_mean_db": statistics.median(audio_means) if audio_means else None,
            "interpretation": (
                "Descriptive technical measurements only; not style targets, speech metrics, "
                "or quality ratings."
            ),
        }

    def counts(self) -> dict[str, int]:
        connection = _connect(self.path)
        try:
            return {
                "media_profiles": int(connection.execute("SELECT COUNT(*) FROM media_profiles").fetchone()[0]),
                "analyzed_media": int(connection.execute(
                    "SELECT COUNT(*) FROM media_profiles WHERE analysis_status = 'complete'"
                ).fetchone()[0]),
                "failed_media": int(connection.execute(
                    "SELECT COUNT(*) FROM media_profiles WHERE analysis_status = 'failed'"
                ).fetchone()[0]),
                "practice_rules": int(connection.execute("SELECT COUNT(*) FROM practice_rules").fetchone()[0]),
                "human_reviews": int(connection.execute("SELECT COUNT(*) FROM human_reviews").fetchone()[0]),
                "batch_recommendations": int(connection.execute(
                    "SELECT COUNT(*) FROM batch_recommendations"
                ).fetchone()[0]),
            }
        except sqlite3.Error as exc:
            raise DataValidationError(f"cannot read production database counts: {exc}") from exc
        finally:
            connection.close()


def _validate_matrix(matrix: Any) -> None:
    if not isinstance(matrix, dict) or not isinstance(matrix.get("concepts"), list):
        raise DataValidationError("matrix report must contain a concepts list")
    if not matrix["concepts"]:
        raise DataValidationError("matrix report has no concepts")
    ids = set()
    for item in matrix["concepts"]:
        if not isinstance(item, dict) or not isinstance(item.get("concept_id"), str):
            raise DataValidationError("matrix report contains a malformed concept")
        if item["concept_id"] in ids:
            raise DataValidationError(f"matrix report repeats {item['concept_id']!r}")
        ids.add(item["concept_id"])
    for key in (
        "concept_uses_math_matrix",
        "book_concept_matrix",
        "book_linked_concept_matrix",
        "question_concept_matrix",
    ):
        candidate = matrix.get(key)
        if candidate is None:
            continue
        if (
            not isinstance(candidate, dict)
            or not isinstance(candidate.get("row_labels"), list)
            or not isinstance(candidate.get("column_labels"), list)
            or not isinstance(candidate.get("values"), list)
            or len(candidate["row_labels"]) != len(candidate["values"])
            or any(not isinstance(label, str) for label in candidate["row_labels"])
            or any(not isinstance(label, str) for label in candidate["column_labels"])
            or any(
                not isinstance(row, list)
                or len(row) != len(candidate["column_labels"])
                or any(
                    not isinstance(value, (int, float))
                    or isinstance(value, bool)
                    or not math.isfinite(value)
                    or value < 0
                    for value in row
                )
                for row in candidate["values"]
            )
        ):
            raise DataValidationError(f"matrix report has a malformed {key}")
    analyses = matrix.get("question_analyses", [])
    if not isinstance(analyses, list) or any(
        not isinstance(item, dict)
        or not isinstance(item.get("question_id"), str)
        or not isinstance(item.get("analysis"), dict)
        or not isinstance(item["analysis"].get("concepts"), list)
        for item in analyses
    ):
        raise DataValidationError("matrix report has malformed question_analyses")


def _episode_concepts(
    episode: dict[str, Any],
    matrix: dict[str, Any],
    catalog: dict[str, dict[str, Any]],
    graph: Any,
) -> dict[str, float]:
    for field in ("matrix_question_id", "question_id"):
        question_id = episode.get(field)
        if question_id:
            analyses = matrix.get("question_analyses", [])
            match = next(
                (item for item in analyses if item.get("question_id") == question_id),
                None,
            )
            if match is None:
                raise DataValidationError(
                    f"{episode.get('id')}: unknown matrix question ID {question_id!r}"
                )
            rankings = match["analysis"]["concepts"]
            direct: dict[str, float] = {}
            for item in rankings:
                if not isinstance(item, dict):
                    raise DataValidationError(
                        f"{episode.get('id')}: malformed concept ranking for {question_id!r}"
                    )
                concept_id = item.get("concept_id")
                score = item.get("direct_score")
                if concept_id not in catalog:
                    continue
                if (
                    not isinstance(score, (int, float))
                    or isinstance(score, bool)
                    or not math.isfinite(score)
                    or score < 0
                ):
                    raise DataValidationError(
                        f"{episode.get('id')}: invalid direct score for {concept_id!r}"
                    )
                if score > 0:
                    direct[concept_id] = float(score)
            if direct:
                return _normalize_concepts(direct)
    section_id = episode.get("matrix_book_section_id")
    if section_id:
        return _matrix_row_scores(
            matrix.get("book_concept_matrix"), section_id, episode.get("id", "")
        )

    explicit = episode.get("concept_ids")
    problem_spec = episode.get("problem_spec")
    if not explicit and isinstance(problem_spec, dict):
        explicit = [problem_spec.get("concept_id")]
    topic_id = episode.get("topic_id")
    if not explicit and isinstance(topic_id, str):
        physics_id = f"physics:{topic_id}"
        if physics_id in catalog:
            explicit = [physics_id]
    if not isinstance(explicit, list):
        explicit = []
    selected = {
        concept_id: 1.0 for concept_id in explicit
        if isinstance(concept_id, str) and concept_id in catalog
    }
    if not selected:
        candidate_text = " ".join(
            str(episode.get(key, ""))
            for key in (
                "title", "topic_id", "question", "answer", "solution",
                "visual_hook", "misconception",
            )
        )
        evidence = match_concepts(candidate_text, graph)
        selected = {
            concept_id: float(item["score"])
            for concept_id, item in evidence.items()
            if concept_id in catalog
        }
        if not selected:
            raise DataValidationError(
                f"{episode.get('id')}: no concept IDs or matrix row mapping found"
            )
        selected = _trim_concept_scores(selected)
    links = matrix.get("concept_uses_math_matrix")
    if links:
        related_math: list[tuple[str, float]] = []
        for concept_id in tuple(selected):
            if concept_id not in links["row_labels"]:
                continue
            row = links["values"][links["row_labels"].index(concept_id)]
            for math_id, score in zip(links["column_labels"], row):
                if (
                    math_id in catalog
                    and isinstance(score, (int, float))
                    and not isinstance(score, bool)
                    and math.isfinite(score)
                    and score > 0
                ):
                    related_math.append((math_id, float(score)))
        for math_id, score in sorted(
            related_math, key=lambda item: (-item[1], item[0])
        )[:3]:
            selected[math_id] = max(selected.get(math_id, 0.0), score)
    return _normalize_concepts(selected)


def _matrix_row_scores(
    matrix: Any, row_id: str, episode_id: str
) -> dict[str, float]:
    if not isinstance(matrix, dict) or row_id not in matrix.get("row_labels", []):
        raise DataValidationError(
            f"{episode_id}: unknown matrix book section ID {row_id!r}"
        )
    index = matrix["row_labels"].index(row_id)
    return _normalize_concepts(
        {
            concept_id: float(score)
            for concept_id, score in zip(matrix["column_labels"], matrix["values"][index])
            if score > 0
        }
    )


def _normalize_concepts(scores: dict[str, float]) -> dict[str, float]:
    valid = {
        concept_id: score for concept_id, score in scores.items()
        if isinstance(score, (int, float))
        and not isinstance(score, bool)
        and math.isfinite(score)
        and score >= 0
    }
    if not valid or max(valid.values(), default=0.0) <= 0:
        raise DataValidationError("selected matrix row has no positive concept evidence")
    scale = max(valid.values())
    return {
        concept_id: score / scale for concept_id, score in valid.items()
        if score > 0
    }


def _trim_concept_scores(scores: dict[str, float]) -> dict[str, float]:
    if not scores:
        return {}
    scale = max(scores.values())
    ranked = sorted(
        (
            (concept_id, score)
            for concept_id, score in scores.items()
            if score >= 0.35 * scale
        ),
        key=lambda item: (-item[1], item[0]),
    )
    return dict(ranked[:5])


def _group_rules(rules: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for rule in rules:
        grouped[rule["area"]].append(rule)
    return dict(grouped)


def _read_json(path: Path, description: str) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise DataValidationError(f"cannot read {description} {path}: {exc}") from exc


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Index local reference-video measurements and create matrix-informed batch advice."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    index = subparsers.add_parser("index", help="measure local video edit/audio metadata")
    index.add_argument("--videos", type=Path, default=DEFAULT_REFERENCE_VIDEOS)
    index.add_argument("--database", type=Path, default=DEFAULT_DATABASE)
    advise = subparsers.add_parser("advise", help="add production advice to a selected batch")
    advise.add_argument("--manifest", type=Path, required=True)
    advise.add_argument("--matrix", type=Path, required=True)
    advise.add_argument("--database", type=Path, default=DEFAULT_DATABASE)
    advise.add_argument(
        "--output", type=Path, default=ROOT / "output" / "production_batch_advice.json"
    )
    review = subparsers.add_parser(
        "review", help="store your ratings of editing, narration, sound, and clarity"
    )
    review.add_argument("--video-title", required=True)
    review.add_argument("--concepts", nargs="+", required=True)
    review.add_argument("--editing", type=int, choices=range(1, 6), required=True)
    review.add_argument(
        "--narration-pacing", type=int, choices=range(1, 6), required=True
    )
    review.add_argument(
        "--narration-clarity", type=int, choices=range(1, 6), required=True
    )
    review.add_argument(
        "--narration-sync", type=int, choices=range(1, 6), required=True
    )
    review.add_argument("--sound", type=int, choices=range(1, 6), required=True)
    review.add_argument("--visual-clarity", type=int, choices=range(1, 6), required=True)
    review.add_argument("--notes", default="")
    review.add_argument("--database", type=Path, default=DEFAULT_DATABASE)
    summary = subparsers.add_parser("summary", help="show local knowledge-database counts")
    summary.add_argument("--database", type=Path, default=DEFAULT_DATABASE)
    args = parser.parse_args(argv)
    try:
        knowledge = ProductionKnowledge(args.database)
        if args.command == "index":
            result = knowledge.index_videos(args.videos)
            print(json.dumps(result, indent=2))
            return 1 if result["failed"] else 0
        if args.command == "advise":
            manifest = _read_json(args.manifest, "batch manifest")
            matrix = _read_json(args.matrix, "matrix report")
            plan = knowledge.advise_batch(manifest, matrix)
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(
                json.dumps(plan, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )
            print(
                f"Wrote production guidance for {plan['episode_count']} episodes "
                f"({plan['deliverable_count']} video formats) to {args.output}"
            )
            return 0
        if args.command == "review":
            review_id = knowledge.record_review(
                video_title=args.video_title,
                concept_ids=args.concepts,
                editing=args.editing,
                narration_pacing=args.narration_pacing,
                narration_clarity=args.narration_clarity,
                narration_sync=args.narration_sync,
                sound=args.sound,
                visual_clarity=args.visual_clarity,
                notes=args.notes,
            )
            print(f"Stored local review {review_id}")
            return 0
        print(json.dumps(knowledge.counts(), indent=2))
        return 0
    except (DataValidationError, OSError, UnicodeError, sqlite3.Error) as exc:
        print(f"production_knowledge: error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
