#!/usr/bin/env python3
"""Render selected approved batch deliverables with Manim and verify their exports."""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from content_engine.batch import load_batch, validate_batch, write_batch_plan
from content_engine.narration import narration_text, synthesize_google_mp3
from exam_engine.engine import DataValidationError

DEFAULT_SCENE = ROOT / "episodes" / "batch_001" / "scenes.py"


def _probe(path: Path) -> dict[str, Any]:
    executable = shutil.which("ffprobe")
    if executable is None:
        raise DataValidationError("ffprobe is required to verify rendered duration and dimensions")
    try:
        completed = subprocess.run(
            [
                executable, "-v", "error", "-show_entries",
                "format=duration:stream=codec_type,width,height,avg_frame_rate",
                "-of", "json", str(path),
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        result = json.loads(completed.stdout)
        duration = float(result["format"]["duration"])
        video_stream = next(
            (
                stream for stream in result["streams"]
                if stream.get("codec_type") == "video"
            ),
            None,
        )
        return {
            "duration_seconds": duration,
            "width": int(video_stream["width"]) if video_stream else 0,
            "height": int(video_stream["height"]) if video_stream else 0,
            "fps": (
                float(Fraction(video_stream["avg_frame_rate"]))
                if video_stream else 0.0
            ),
            "has_audio": any(
                stream.get("codec_type") == "audio" for stream in result["streams"]
            ),
        }
    except (
        OSError, subprocess.CalledProcessError, KeyError, ValueError,
        ZeroDivisionError, StopIteration,
    ) as exc:
        raise DataValidationError(f"cannot validate rendered video {path}: {exc}") from exc


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _scene_for_batch(batch: dict[str, Any], override: Path | None = None) -> Path:
    """Resolve the Manim scene module: --scene override first, then
    episodes/<batch_id>/scenes.py, then the legacy batch_001 scene."""
    batch_id = str(batch.get("batch_id", "")).strip()
    candidates: list[Path] = []
    if override is not None:
        candidates.append(Path(override))
    if batch_id:
        candidates.append(ROOT / "episodes" / batch_id / "scenes.py")
    candidates.append(DEFAULT_SCENE)
    for candidate in candidates:
        if candidate.is_file():
            if candidate == DEFAULT_SCENE and batch_id not in ("", "batch_001"):
                print(
                    f"warning: no scene module for {batch_id}; "
                    f"falling back to {DEFAULT_SCENE}",
                    file=sys.stderr,
                )
            return candidate
    raise DataValidationError(
        "batch scene module not found; tried: " + ", ".join(str(c) for c in candidates)
    )


def render(
    manifest_path: Path,
    output_dir: Path,
    *,
    video_ids: list[str] | None,
    formats: list[str],
    quality: str,
    fps: int,
    resume: bool = False,
    narration: str = "off",
    voice_name: str = "en-US-Neural2-J",
    scene_override: Path | None = None,
) -> Path:
    batch = load_batch(manifest_path)
    plan = validate_batch(batch, ROOT)
    selected = [
        item for item in plan
        if item["format"] in formats and (video_ids is None or item["video_id"] in video_ids)
    ]
    if video_ids and {item["video_id"] for item in selected} != set(video_ids):
        found = {item["video_id"] for item in selected}
        missing = sorted(set(video_ids) - found)
        raise DataValidationError("unknown or filtered video ID(s): " + ", ".join(missing))
    if not selected:
        raise DataValidationError("no deliverables selected for rendering")
    scene = _scene_for_batch(batch, scene_override)

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    report_path = output_dir / "render_report.json"
    report: dict[str, Any] = {
        "batch_id": batch["batch_id"],
        "status": "rendering",
        "quality": quality,
        "fps": fps,
        "narration": narration,
        "voice_name": voice_name if narration == "google" else ("saem-clone" if narration == "local" else None),
        "completed": [],
    }
    with tempfile.TemporaryDirectory(prefix="saemphysics-batch-plan-") as plan_dir:
        plan_path = Path(plan_dir) / "render_plan.json"
        write_batch_plan(batch, plan, plan_path)
        with tempfile.TemporaryDirectory(prefix="saemphysics-manim-") as media_dir:
            for item in selected:
                destination = output_dir / f"{item['video_id']}.mp4"
                
                # Support both google and local for script extraction
                narration_script = (
                    narration_text(item) if narration in ("google", "local") else None
                )
                expected_voice_tag = voice_name if narration == "google" else "saem-clone"
                narration_signature = (
                    hashlib.sha256(
                        f"{expected_voice_tag}\0{narration_script}".encode("utf-8")
                    ).hexdigest()
                    if narration_script is not None
                    else None
                )
                
                if resume and destination.is_file():
                    metadata = _probe(destination)
                    contract_matches = (metadata["width"], metadata["height"]) == (
                        item["width"], item["height"]
                    ) and abs(
                        metadata["duration_seconds"] - item["duration_seconds"]
                    ) <= (1 / fps + 0.02) and abs(metadata["fps"] - fps) <= 0.01
                    if not contract_matches:
                        raise DataValidationError(
                            f"existing output {destination} does not match this batch contract"
                        )
                    narration_matches = not metadata["has_audio"]
                    sidecar = destination.with_suffix(".narration.json")
                    if narration in ("google", "local") and metadata["has_audio"]:
                        try:
                            sidecar_data = json.loads(
                                sidecar.read_text(encoding="utf-8")
                            )
                            narration_matches = isinstance(
                                sidecar_data, dict
                            ) and (
                                sidecar_data.get("voice_name") == expected_voice_tag
                                and sidecar_data.get("script_sha256")
                                == narration_signature
                            )
                        except (OSError, json.JSONDecodeError):
                            narration_matches = False
                    if narration_matches:
                        report["completed"].append(
                            {
                                "video_id": item["video_id"],
                                "path": destination.name,
                                **metadata,
                                "narration": narration,
                                "voice_name": expected_voice_tag,
                                "sha256": _sha256(destination),
                                "resumed": True,
                            }
                        )
                        report["selected_count"] = len(selected)
                        report["status"] = (
                            "complete"
                            if len(report["completed"]) == len(selected)
                            else "rendering"
                        )
                        report_path.write_text(
                            json.dumps(report, indent=2) + "\n",
                            encoding="utf-8",
                        )
                        print(f"Keeping verified existing render {destination}")
                        continue
                    print(
                        f"Existing render {destination} has a different audio "
                        "configuration; rendering it again."
                    )
                temp_media = Path(media_dir) / item["video_id"]
                temp_media.mkdir()
                environment = os.environ.copy()
                environment["SAEMPHYSICS_BATCH_PLAN"] = str(plan_path)
                environment["SAEMPHYSICS_VIDEO_ID"] = item["video_id"]
                command = [
                    sys.executable, "-m", "manim",
                    "-ql" if quality == "preview" else "-qh",
                    "--resolution", f"{item['width']},{item['height']}",
                    "--fps", str(fps),
                    "--media_dir", str(temp_media),
                    "--format", "mp4",
                    "--disable_caching",
                    "--output_file", item["video_id"],
                    str(scene),
                    "BatchEpisode",
                ]
                subprocess.run(command, check=True, cwd=ROOT, env=environment)
                candidates = list(temp_media.rglob(f"{item['video_id']}.mp4"))
                if len(candidates) != 1 or candidates[0].stat().st_size == 0:
                    raise DataValidationError(
                        f"Manim did not produce exactly one non-empty MP4 for "
                        f"{item['video_id']}"
                    )
                rendered = candidates[0]
                metadata = _probe(rendered)
                if (metadata["width"], metadata["height"]) != (
                    item["width"], item["height"]
                ):
                    raise DataValidationError(
                        f"{item['video_id']} rendered at "
                        f"{metadata['width']}x{metadata['height']}; expected "
                        f"{item['width']}x{item['height']}"
                    )
                tolerance = 1 / fps + 0.02
                if abs(metadata["duration_seconds"] - item["duration_seconds"]) > tolerance:
                    raise DataValidationError(
                        f"{item['video_id']} duration is "
                        f"{metadata['duration_seconds']:.3f}s; expected "
                        f"{item['duration_seconds']}s"
                    )
                if abs(metadata["fps"] - fps) > 0.01:
                    raise DataValidationError(
                        f"{item['video_id']} rendered at {metadata['fps']:.2f} fps; "
                        f"expected {fps} fps"
                    )
                narration_metadata: dict[str, Any] = {
                    "narration": "off",
                    "narration_duration_seconds": 0.0,
                    "narration_words": 0,
                    "voice_name": None,
                    "narration_cached": False,
                }
                
                if narration == "google":
                    text = narration_script or ""
                    language = batch["narration_language"]
                    language_code = {
                        "english": "en-US",
                        "hindi": "hi-IN",
                    }.get(language.lower())
                    if language_code is None:
                        language_code = language
                    audio_path, cached = synthesize_google_mp3(
                        text,
                        voice_name=voice_name,
                        language_code=language_code,
                        output_dir=output_dir / ".narration-cache",
                    )
                    audio_metadata = _probe(audio_path)
                    if audio_metadata["duration_seconds"] > (
                        item["duration_seconds"] + tolerance
                    ):
                        raise DataValidationError(
                            f"{item['video_id']} narration is "
                            f"{audio_metadata['duration_seconds']:.1f}s, longer than "
                            f"the {item['duration_seconds']}s video; shorten the "
                            f"narration.{item['format']} script or choose a faster voice"
                        )
                    muxed = destination.with_suffix(".narrated.mp4")
                    subprocess.run(
                        [
                            shutil.which("ffmpeg") or "ffmpeg",
                            "-v", "error", "-y",
                            "-i", str(rendered),
                            "-i", str(audio_path),
                            "-map", "0:v:0",
                            "-map", "1:a:0",
                            "-c:v", "copy",
                            "-c:a", "aac",
                            "-b:a", "192k",
                            "-af", "apad",
                            "-t", str(item["duration_seconds"]),
                            str(muxed),
                        ],
                        check=True,
                        cwd=ROOT,
                    )
                    muxed_metadata = _probe(muxed)
                    if not muxed_metadata["has_audio"]:
                        raise DataValidationError(
                            f"narration audio is missing from muxed video {muxed}"
                        )
                    if abs(
                        muxed_metadata["duration_seconds"] - item["duration_seconds"]
                    ) > tolerance:
                        raise DataValidationError(
                            f"narrated video {muxed} does not match the duration contract"
                        )
                    rendered = muxed
                    metadata = muxed_metadata
                    narration_metadata = {
                        "narration": "google-cloud-text-to-speech",
                        "narration_duration_seconds": audio_metadata["duration_seconds"],
                        "narration_words": len(text.split()),
                        "narration_coverage": round(
                            audio_metadata["duration_seconds"]
                            / item["duration_seconds"],
                            3,
                        ),
                        "voice_name": voice_name,
                        "narration_cached": cached,
                    }
                    if narration_metadata["narration_coverage"] < 0.75:
                        print(
                            f"Warning: {item['video_id']} narration covers "
                            f"{narration_metadata['narration_coverage']:.0%} of the "
                            "video; add a fuller format-specific script if desired.",
                            file=sys.stderr,
                        )
                
                elif narration == "local":
                    from tools.local_narration import synthesize_local_wav, VOICE_TAG
                    
                    text = narration_script or ""
                    voice_wav = ROOT / "saem_voice_sample.wav"
                    cache_dir = output_dir / ".narration-cache"
                    
                    audio_path, cached = synthesize_local_wav(text, voice_wav, cache_dir)
                    audio_metadata = _probe(audio_path)
                    
                    if audio_metadata["duration_seconds"] > (item["duration_seconds"] + tolerance):
                        raise DataValidationError(
                            f"{item['video_id']} narration is "
                            f"{audio_metadata['duration_seconds']:.1f}s, longer than "
                            f"the {item['duration_seconds']}s video; shorten the script."
                        )
                    
                    muxed = destination.with_suffix(".narrated.mp4")
                    subprocess.run(
                        [
                            shutil.which("ffmpeg") or "ffmpeg",
                            "-v", "error", "-y",
                            "-i", str(rendered),
                            "-i", str(audio_path),
                            "-map", "0:v:0",
                            "-map", "1:a:0",
                            "-c:v", "copy",
                            "-c:a", "aac",
                            "-b:a", "192k",
                            "-af", "apad",
                            "-t", str(item["duration_seconds"]),
                            str(muxed),
                        ],
                        check=True,
                        cwd=ROOT,
                    )
                    muxed_metadata = _probe(muxed)
                    if not muxed_metadata["has_audio"]:
                        raise DataValidationError(
                            f"narration audio is missing from muxed video {muxed}"
                        )
                    if abs(muxed_metadata["duration_seconds"] - item["duration_seconds"]) > tolerance:
                        raise DataValidationError(
                            f"narrated video {muxed} does not match the duration contract"
                        )
                    rendered = muxed
                    metadata = muxed_metadata
                    
                    narration_metadata = {
                        "narration": "local-voice-clone-xtts",
                        "narration_duration_seconds": audio_metadata["duration_seconds"],
                        "narration_words": len(text.split()),
                        "narration_coverage": round(
                            audio_metadata["duration_seconds"] / item["duration_seconds"], 3
                        ),
                        "voice_name": VOICE_TAG,
                        "narration_cached": cached,
                    }
                    if narration_metadata["narration_coverage"] < 0.75:
                        print(
                            f"Warning: {item['video_id']} narration covers "
                            f"{narration_metadata['narration_coverage']:.0%} of the "
                            "video; add a fuller format-specific script if desired.",
                            file=sys.stderr,
                        )

                shutil.copy2(rendered, destination)
                if narration in ("google", "local"):
                    destination.with_suffix(".narration.json").write_text(
                        json.dumps(
                            {
                                "voice_name": expected_voice_tag,
                                "script_sha256": narration_signature,
                                "narration_duration_seconds": narration_metadata["narration_duration_seconds"],
                            },
                            indent=2,
                        ) + "\n",
                        encoding="utf-8",
                    )
                else:
                    destination.with_suffix(".narration.json").unlink(missing_ok=True)
                report["completed"].append(
                    {
                        "video_id": item["video_id"],
                        "path": destination.name,
                        **metadata,
                        **narration_metadata,
                        "sha256": _sha256(destination),
                    }
                )
                report["status"] = (
                    "complete" if len(report["completed"]) == len(selected) else "rendering"
                )
                report["selected_count"] = len(selected)
                report_path.write_text(
                    json.dumps(report, indent=2) + "\n",
                    encoding="utf-8",
                )
                print(
                    f"Rendered {destination} "
                    f"({metadata['width']}x{metadata['height']}, "
                    f"{metadata['duration_seconds']:.2f}s)"
                )
    return report_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--manifest",
        type=Path,
        default=ROOT / "data" / "video_batches" / "batch_001.json",
    )
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--video-ids", nargs="+")
    parser.add_argument(
        "--formats", nargs="+", choices=("vertical", "horizontal"),
        default=["vertical", "horizontal"],
    )
    parser.add_argument("--quality", choices=("preview", "high"), default="preview")
    parser.add_argument(
        "--narration",
        choices=("off", "google", "local"),
        default="off",
        help="synthesize and mux a narration track (local uses offline XTTS voice cloning)",
    )
    parser.add_argument(
        "--voice-name",
        default="en-US-Neural2-J",
        help="Google Cloud TTS voice name (used only with --narration google)",
    )
    parser.add_argument("--fps", type=int, choices=(15, 30), default=None)
    parser.add_argument(
        "--resume",
        action="store_true",
        help="reuse existing MP4s after verifying their size and duration contract",
    )
    parser.add_argument(
        "--scene",
        type=Path,
        default=None,
        help="override the Manim scene module (default: episodes/<batch_id>/scenes.py)",
    )
    args = parser.parse_args()
    fps = args.fps or (15 if args.quality == "preview" else 30)
    try:
        report = render(
            args.manifest,
            args.output_dir,
            video_ids=args.video_ids,
            formats=args.formats,
            quality=args.quality,
            fps=fps,
            resume=args.resume,
            narration=args.narration,
            voice_name=args.voice_name,
            scene_override=args.scene,
        )
    except (DataValidationError, OSError, subprocess.CalledProcessError) as exc:
        print(f"render_video_batch: error: {exc}", file=sys.stderr)
        return 2
    print(f"Render report: {report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
