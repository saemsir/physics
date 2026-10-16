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
from exam_engine.engine import DataValidationError

SCENE = ROOT / "episodes" / "batch_001" / "scenes.py"


def _probe(path: Path) -> dict[str, Any]:
    executable = shutil.which("ffprobe")
    if executable is None:
        raise DataValidationError("ffprobe is required to verify rendered duration and dimensions")
    try:
        completed = subprocess.run(
            [
                executable, "-v", "error", "-show_entries",
                "format=duration:stream=width,height,avg_frame_rate",
                "-of", "json", str(path),
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        result = json.loads(completed.stdout)
        duration = float(result["format"]["duration"])
        video_stream = next(
            stream for stream in result["streams"]
            if "width" in stream and "height" in stream
        )
        return {
            "duration_seconds": duration,
            "width": int(video_stream["width"]),
            "height": int(video_stream["height"]),
            "fps": float(Fraction(video_stream["avg_frame_rate"])),
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


def render(
    manifest_path: Path,
    output_dir: Path,
    *,
    video_ids: list[str] | None,
    formats: list[str],
    quality: str,
    fps: int,
    resume: bool = False,
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
    if not SCENE.is_file():
        raise DataValidationError(f"batch scene module not found: {SCENE}")

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    report_path = output_dir / "render_report.json"
    report: dict[str, Any] = {
        "batch_id": batch["batch_id"],
        "status": "rendering",
        "quality": quality,
        "fps": fps,
        "completed": [],
    }
    with tempfile.TemporaryDirectory(prefix="saemphysics-batch-plan-") as plan_dir:
        plan_path = Path(plan_dir) / "render_plan.json"
        write_batch_plan(batch, plan, plan_path)
        with tempfile.TemporaryDirectory(prefix="saemphysics-manim-") as media_dir:
            for item in selected:
                destination = output_dir / f"{item['video_id']}.mp4"
                if resume and destination.is_file():
                    metadata = _probe(destination)
                    if (metadata["width"], metadata["height"]) != (
                        item["width"], item["height"]
                    ) or abs(metadata["duration_seconds"] - item["duration_seconds"]) > (
                        1 / fps + 0.02
                    ) or abs(metadata["fps"] - fps) > 0.01:
                        raise DataValidationError(
                            f"existing output {destination} does not match this batch contract"
                        )
                    report["completed"].append(
                        {
                            "video_id": item["video_id"],
                            "path": destination.name,
                            **metadata,
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
                    str(SCENE),
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
                shutil.copy2(rendered, destination)
                report["completed"].append(
                    {
                        "video_id": item["video_id"],
                        "path": destination.name,
                        **metadata,
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
    parser.add_argument("--fps", type=int, choices=(15, 30), default=None)
    parser.add_argument(
        "--resume",
        action="store_true",
        help="reuse existing MP4s after verifying their size and duration contract",
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
        )
    except (DataValidationError, OSError, subprocess.CalledProcessError) as exc:
        print(f"render_video_batch: error: {exc}", file=sys.stderr)
        return 2
    print(f"Render report: {report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
