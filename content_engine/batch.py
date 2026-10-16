"""Validate and expand reviewed lesson concepts into a fixed video-batch plan."""

from __future__ import annotations

import json
from pathlib import Path
import re
from typing import Any

from exam_engine.engine import DataValidationError

from .problem import solve_problem

ROOT = Path(__file__).resolve().parents[1]
BRAND_NAME = "Saem Physics"
BRAND_TAGLINE = "NEET JEE MIT"
VIDEO_FORMATS = {
    "vertical": {
        "aspect_ratio": "9:16",
        "width": 1080,
        "height": 1920,
        "duration_seconds": 60,
        "beats": [
            ("hook", 6),
            ("question", 8),
            ("visual_model", 12),
            ("solution", 20),
            ("recap", 10),
            ("branded_end_card", 4),
        ],
    },
    "horizontal": {
        "aspect_ratio": "16:9",
        "width": 1920,
        "height": 1080,
        "duration_seconds": 180,
        "beats": [
            ("hook", 12),
            ("question", 18),
            ("visual_model", 30),
            ("solution", 60),
            ("misconception_check", 30),
            ("recap", 18),
            ("branded_end_card", 12),
        ],
    },
}


def load_batch(path: Path) -> dict[str, Any]:
    try:
        batch = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise DataValidationError(f"cannot read video batch {path}: {exc}") from exc
    if not isinstance(batch, dict):
        raise DataValidationError("video batch must contain a single JSON object")
    return batch


def _require_text(value: Any, field: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise DataValidationError(f"{field} must be a non-empty string")


def _validate_manual_audit(episode: dict[str, Any]) -> None:
    audit = episode.get("manual_audit")
    if audit is None:
        return
    if not isinstance(audit, dict):
        raise DataValidationError(f"{episode['id']}: manual_audit must be an object")
    model = audit.get("model")
    if model == "perfectly-inelastic-collision":
        try:
            m1, v1 = float(audit["mass_1_kg"]), float(audit["velocity_1_m_per_s"])
            m2, v2 = float(audit["mass_2_kg"]), float(audit["velocity_2_m_per_s"])
            common = float(audit["expected_common_velocity_m_per_s"])
            initial_ke = float(audit["expected_initial_kinetic_energy_j"])
            final_ke = float(audit["expected_final_kinetic_energy_j"])
        except (KeyError, TypeError, ValueError, OverflowError) as exc:
            raise DataValidationError(
                f"{episode['id']}: incomplete collision audit"
            ) from exc
        momentum_initial = m1 * v1 + m2 * v2
        momentum_final = (m1 + m2) * common
        kinetic_initial = 0.5 * m1 * v1**2 + 0.5 * m2 * v2**2
        kinetic_final = 0.5 * (m1 + m2) * common**2
        if momentum_initial != momentum_final:
            raise DataValidationError(f"{episode['id']}: collision momentum audit failed")
        if kinetic_initial != initial_ke or kinetic_final != final_ke:
            raise DataValidationError(f"{episode['id']}: collision energy audit failed")
        if kinetic_final >= kinetic_initial:
            raise DataValidationError(
                f"{episode['id']}: inelastic collision must show kinetic energy loss"
            )
    elif model == "falling-energy":
        try:
            mass = float(audit["mass_kg"])
            height = float(audit["height_m"])
            gravity = float(audit["gravity_m_per_s2"])
            speed = float(audit["expected_speed_m_per_s"])
            potential = float(audit["expected_initial_potential_energy_j"])
            kinetic = float(audit["expected_final_kinetic_energy_j"])
        except (KeyError, TypeError, ValueError, OverflowError) as exc:
            raise DataValidationError(f"{episode['id']}: incomplete energy audit") from exc
        if mass <= 0 or height <= 0 or gravity <= 0:
            raise DataValidationError(f"{episode['id']}: energy inputs must be positive")
        if potential != mass * gravity * height:
            raise DataValidationError(f"{episode['id']}: initial potential energy audit failed")
        if kinetic != 0.5 * mass * speed**2 or kinetic != potential:
            raise DataValidationError(f"{episode['id']}: falling-energy audit failed")
    else:
        raise DataValidationError(
            f"{episode['id']}: unsupported manual audit model {model!r}"
        )


def validate_batch(batch: dict[str, Any], root: Path = ROOT) -> list[dict[str, Any]]:
    _require_text(batch.get("batch_id"), "batch_id")
    if batch.get("status") not in {
        "draft-owner-review",
        "approved-for-storyboarding",
    }:
        raise DataValidationError("batch must be a draft or approved-for-storyboarding")
    _require_text(batch.get("narration_language"), "narration_language")
    brand = batch.get("brand")
    if not isinstance(brand, dict) or brand.get("name") != BRAND_NAME:
        raise DataValidationError(f"brand name must be exactly {BRAND_NAME!r}")
    if brand.get("tagline") != BRAND_TAGLINE:
        raise DataValidationError(f"brand tagline must be exactly {BRAND_TAGLINE!r}")
    audience = batch.get("audience")
    if not isinstance(audience, dict) or (
        audience.get("minimum_age"), audience.get("maximum_age")
    ) != (14, 21):
        raise DataValidationError("batch audience must cover ages 14 through 21")

    episodes = batch.get("episodes")
    if not isinstance(episodes, list) or len(episodes) != 10:
        raise DataValidationError("a video batch must contain exactly 10 content episodes")
    seen: set[str] = set()
    for episode in episodes:
        if not isinstance(episode, dict):
            raise DataValidationError("each batch episode must be an object")
        episode_id = episode.get("id")
        _require_text(episode_id, "episode id")
        if not re.fullmatch(r"[a-z0-9][a-z0-9._-]*", episode_id):
            raise DataValidationError(f"invalid episode id {episode_id!r}")
        if episode_id in seen:
            raise DataValidationError(f"duplicate episode id {episode_id!r}")
        seen.add(episode_id)
        if episode.get("status") not in {
            "proposed",
            "approved-for-storyboarding",
        }:
            raise DataValidationError(
                f"{episode_id}: status cannot imply question-bank verification"
            )
        if episode.get("type") not in {"problem", "concept"}:
            raise DataValidationError(f"{episode_id}: type must be problem or concept")
        for field in (
            "title", "topic_id", "question", "answer", "solution", "visual_hook",
            "misconception",
        ):
            _require_text(episode.get(field), f"{episode_id}.{field}")
        reference = episode.get("reference")
        if not isinstance(reference, dict):
            raise DataValidationError(f"{episode_id}: reference must be an object")
        _require_text(reference.get("title"), f"{episode_id}.reference.title")
        _require_text(reference.get("section"), f"{episode_id}.reference.section")
        source_path = reference.get("local_path")
        _require_text(source_path, f"{episode_id}.reference.local_path")
        if Path(source_path).is_absolute() or ".." in Path(source_path).parts:
            raise DataValidationError(f"{episode_id}: reference path must stay in the repository")
        resolved = root / source_path
        if not resolved.is_file():
            raise DataValidationError(f"{episode_id}: missing source file {source_path!r}")
        problem_spec = episode.get("problem_spec")
        if problem_spec is not None:
            result = solve_problem(problem_spec)
            if result.computation_status != "passed":
                raise DataValidationError(f"{episode_id}: physics-engine checks failed")
        _validate_manual_audit(episode)
        _require_text(episode.get("solution_review_status"), f"{episode_id}.solution_review_status")

    if not {"problem", "concept"}.issubset({episode["type"] for episode in episodes}):
        raise DataValidationError("batch must mix concept and problem episodes")
    if batch["status"] == "approved-for-storyboarding" and any(
        episode["status"] != "approved-for-storyboarding" for episode in episodes
    ):
        raise DataValidationError(
            "an approved storyboard batch must contain only owner-approved episodes"
        )
    declared_outputs = batch.get("video_outputs")
    if not isinstance(declared_outputs, list) or len(declared_outputs) != 2:
        raise DataValidationError("video_outputs must declare the batch delivery formats")
    declared = {item.get("format"): item for item in declared_outputs if isinstance(item, dict)}
    if set(declared) != set(VIDEO_FORMATS):
        raise DataValidationError("video_outputs must declare vertical and horizontal formats")
    for format_name, spec in VIDEO_FORMATS.items():
        expected = {
            "count": 10,
            "duration_seconds": spec["duration_seconds"],
            "aspect_ratio": spec["aspect_ratio"],
        }
        actual = declared[format_name]
        if any(actual.get(key) != value for key, value in expected.items()):
            raise DataValidationError(
                f"{format_name} must have 10 videos at {spec['duration_seconds']} seconds "
                f"and {spec['aspect_ratio']}"
            )

    plan: list[dict[str, Any]] = []
    for episode in episodes:
        for format_name, spec in VIDEO_FORMATS.items():
            plan.append(
                {
                    "video_id": f"{episode['id']}-{format_name}",
                    "episode_id": episode["id"],
                    "type": episode["type"],
                    "title": episode["title"],
                    "topic_id": episode["topic_id"],
                    "question": episode["question"],
                    "answer": episode["answer"],
                    "solution": episode["solution"],
                    "misconception": episode["misconception"],
                    "reference": episode["reference"],
                    "status": batch["status"],
                    "narration_language": batch["narration_language"],
                    "format": format_name,
                    "aspect_ratio": spec["aspect_ratio"],
                    "width": spec["width"],
                    "height": spec["height"],
                    "duration_seconds": spec["duration_seconds"],
                    "audience": audience,
                    "brand_overlay": {
                        "name": brand["name"],
                        "tagline": brand["tagline"],
                        "logo_asset": brand.get("logo_asset", ""),
                    },
                    "visual_hook": episode["visual_hook"],
                    "style_guardrail": batch.get("visual_direction", ""),
                    "story_beats": [
                        {"name": name, "duration_seconds": duration}
                        for name, duration in spec["beats"]
                    ],
                }
            )
    if len(plan) != 20:
        raise DataValidationError("batch expansion must produce exactly 20 video deliverables")
    for format_name, spec in VIDEO_FORMATS.items():
        matching = [item for item in plan if item["format"] == format_name]
        if len(matching) != 10:
            raise DataValidationError(f"{format_name} output count must be exactly 10")
        if any(
            sum(beat["duration_seconds"] for beat in item["story_beats"])
            != spec["duration_seconds"]
            for item in matching
        ):
            raise DataValidationError(f"{format_name} storyboard durations do not add up")
    return plan


def write_batch_plan(batch: dict[str, Any], plan: list[dict[str, Any]], path: Path) -> None:
    result = {
        "batch_id": batch["batch_id"],
        "status": batch["status"],
        "source_file": batch.get("source_file", ""),
        "deliverables": plan,
    }
    try:
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        Path(path).write_text(
            json.dumps(result, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    except (OSError, UnicodeError) as exc:
        raise DataValidationError(f"cannot write video batch plan {path}: {exc}") from exc
