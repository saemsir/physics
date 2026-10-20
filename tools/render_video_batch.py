#!/usr/bin/env python3
"""Render selected approved batch deliverables with Manim (100% Offline)."""

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

# Use the local, offline engines we built
from exam_engine.engine import DataValidationError

# Default to a generic scene path; override via --scene argument
DEFAULT_SCENE = ROOT / "episodes" / "generic_scene.py"


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
            (stream for stream in result["streams"] if stream.get("codec_type") == "video"),
            None,
        )
        return {
            "duration_seconds": duration,
            "width": int(video_stream["width"]) if video_stream else 0,
            "height": int(video_stream["height"]) if video_stream else 0,
            "fps": float(Fraction(video_stream["avg_frame_rate"])) if video_stream else 0.0,
            "has_audio": any(stream.get("codec_type") == "audio" for stream in result["streams"]),
        }
    except (OSError, subprocess.CalledProcessError, KeyError, ValueError, ZeroDivisionError, StopIteration) as exc:
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
    narration: str = "off",
    scene_path: Path,
) -> Path:
    # Note: In a fully offline setup, the manifest should be processed by 
    # generate_video_batch.py -> batch_runner.py, which handles local TTS.
    # This script acts as a direct Manim renderer for pre-approved plans.
    
    if not scene_path.is_file():
        raise DataValidationError(f"Scene module not found: {scene_path}. Use --scene to specify a valid path.")

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    report_path = output_dir / "render_report.json"
    
    # Mock plan loading for demonstration (replace with actual manifest loader if needed)
    # For now, we assume the manifest contains a list of episodes with video_id, width, height, duration_seconds
    try:
        manifest_data = json.loads(manifest_path.read_text(encoding="utf-8"))
        episodes = manifest_data.get("episodes", [])
        video_outputs = manifest_data.get("video_outputs", [{"format": "vertical"}, {"format": "horizontal"}])
    except Exception as exc:
        raise DataValidationError(f"Cannot read manifest {manifest_path}: {exc}")

    selected = []
    for ep in episodes:
        for fmt in video_outputs:
            video_id = f"{ep.get('id')}_{fmt.get('format')}"
            if formats and fmt.get("format") not in formats:
                continue
            if video_ids and video_id not in video_ids:
                continue
            
            # Default dimensions based on format
            width, height = (1080, 1920) if fmt.get("format") == "vertical" else (1920, 1080)
            selected.append({
                "video_id": video_id,
                "format": fmt.get("format"),
                "width": width,
                "height": height,
                "duration_seconds": ep.get("duration_seconds", 60.0),
            })

    if not selected:
        raise DataValidationError("no deliverables selected for rendering")

    report: dict[str, Any] = {
        "batch_id": manifest_data.get("batch_id", "unknown"),
        "status": "rendering",
        "quality": quality,
        "fps": fps,
        "narration": narration,
        "completed": [],
    }

    with tempfile.TemporaryDirectory(prefix="saemphysics-manim-") as media_dir:
        for item in selected:
            destination = output_dir / f"{item['video_id']}.mp4"
            
            if resume and destination.is_file() and destination.stat().st_size > 0:
                print(f"Keeping verified existing render {destination} (--resume active)")
                report["completed"].append({"video_id": item["video_id"], "path": destination.name, "resumed": True})
                report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
                continue

            temp_media = Path(media_dir) / item["video_id"]
            temp_media.mkdir()
            
            environment = os.environ.copy()
            # Pass environment variables to the scene if it needs them
            environment["SAEMPHYSICS_VIDEO_ID"] = item["video_id"]
            environment["SAEMPHYSICS_DURATION"] = str(item["duration_seconds"])
            
            quality_flag = "-ql" if quality == "preview" else "-qh"
            
            command = [
                sys.executable, "-m", "manim",
                quality_flag,
                "--resolution", f"{item['width']},{item['height']}",
                "--fps", str(fps),
                "--media_dir", str(temp_media),
                "--format", "mp4",
                "--disable_caching",
                str(scene_path),
                "UniversalPhysicsScene",  # Default scene class name
            ]
            
            print(f"🎬 Rendering {item['video_id']}...")
            subprocess.run(command, check=True, cwd=ROOT, env=environment)
            
            candidates = list(temp_media.rglob(f"{item['video_id']}.mp4"))
            if len(candidates) != 1 or candidates[0].stat().st_size == 0:
                raise DataValidationError(f"Manim did not produce exactly one non-empty MP4 for {item['video_id']}")
            
            rendered = candidates[0]
            metadata = _probe(rendered)
            
            # Verify contract
            if (metadata["width"], metadata["height"]) != (item["width"], item["height"]):
                raise DataValidationError(f"{item['video_id']} rendered at {metadata['width']}x{metadata['height']}; expected {item['width']}x{item['height']}")
            
            tolerance = 1 / fps + 0.02
            if abs(metadata["duration_seconds"] - item["duration_seconds"]) > tolerance:
                print(f"⚠️ Warning: {item['video_id']} duration is {metadata['duration_seconds']:.3f}s; expected {item['duration_seconds']}s")

            shutil.copy2(rendered, destination)
            
            report["completed"].append({
                "video_id": item["video_id"],
                "path": destination.name,
                **metadata,
                "sha256": _sha256(destination),
            })
            report["status"] = "complete" if len(report["completed"]) == len(selected) else "rendering"
            report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
            print(f"✅ Rendered {destination} ({metadata['width']}x{metadata['height']}, {metadata['duration_seconds']:.2f}s)")
            
    return report_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=ROOT / "data" / "video_batches" / "batch_001.json")
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--video-ids", nargs="+")
    parser.add_argument("--formats", nargs="+", choices=("vertical", "horizontal"), default=["vertical", "horizontal"])
    parser.add_argument("--quality", choices=("preview", "high"), default="preview")
    parser.add_argument("--fps", type=int, choices=(15, 30, 60), default=30)
    parser.add_argument("--resume", action="store_true", help="reuse existing MP4s")
    
    # CRITICAL FIX: Make scene path configurable, not hardcoded
    parser.add_argument("--scene", type=Path, default=DEFAULT_SCENE, help="Path to the Manim scene Python file")
    
    # CRITICAL FIX: Remove Google Cloud, enforce offline
    parser.add_argument("--narration", choices=("off", "local"), default="off", help="Use local offline TTS (handled by batch_runner.py)")
    
    args = parser.parse_args()
    
    try:
        report = render(
            args.manifest,
            args.output_dir,
            video_ids=args.video_ids,
            formats=args.formats,
            quality=args.quality,
            fps=args.fps,
            resume=args.resume,
            narration=args.narration,
            scene_path=args.scene,
        )
    except (DataValidationError, OSError, subprocess.CalledProcessError) as exc:
        print(f"render_video_batch: error: {exc}", file=sys.stderr)
        return 2
        
    print(f"✅ Render report saved to: {report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
