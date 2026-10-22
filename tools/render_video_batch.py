#!/usr/bin/env python3
"""Render selected approved batch deliverables with Manim and verify their exports.

Narration providers:
  off     silent draft
  google  Google Cloud TTS (needs GOOGLE_TTS_SERVICE_ACCOUNT_JSON secret)
  gemini  Gemini 2.5 Flash TTS free tier (preset voices, multilingual)
  local   offline Coqui XTTS v2 clone of saem_voice_sample.wav
  edge    free Microsoft Edge neural TTS (best for hindi/urdu/arabic)
  gtts    free Google Translate TTS fallback
  espeak  offline eSpeak-ng emergency fallback
"""

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
AUDIO_PROVIDERS = ("google", "gemini", "local", "edge", "gtts", "espeak")

LANGUAGE_CODES = {
    "english": "en-US",
    "hindi": "hi-IN",
    "urdu": "ur-PK",
    "arabic": "ar-XA",
}


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
    episodes/<batch
