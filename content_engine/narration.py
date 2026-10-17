"""Google Cloud Text-to-Speech support for original episode narration."""

from __future__ import annotations

import hashlib
import re
from pathlib import Path
from typing import Any

from exam_engine.engine import DataValidationError


def narration_text(item: dict[str, Any]) -> str:
    scripts = item.get("narration")
    if scripts is not None:
        if not isinstance(scripts, dict):
            raise DataValidationError(
                f"{item['video_id']}: narration must map formats to reviewed scripts"
            )
        text = scripts.get(item["format"])
        if not isinstance(text, str) or not text.strip():
            raise DataValidationError(
                f"{item['video_id']}: narration.{item['format']} must be non-empty"
            )
        return re.sub(r"\s+", " ", text).strip()

    # A compact vertical draft and a more reflective horizontal draft. Owners
    # can supply format-specific scripts for pacing that matches the full runtime.
    if item["format"] == "vertical":
        parts = [
            item["title"],
            "Here is the question.",
            item["question"],
            "Let's reason it through.",
            item["solution"],
            "The answer is:",
            item["answer"],
        ]
    else:
        parts = [
            item["title"],
            item["visual_hook"],
            "Let's name the physical situation before we use an equation.",
            "Here is the question.",
            item["question"],
            "Pause and predict what the first step should be.",
            "Now let's reason it through.",
            item["solution"],
            "Check this common misconception:",
            item["misconception"],
            "The answer is:",
            item["answer"],
            "Keep the central idea: start from the physical picture, make the "
            "mathematical step explicit, and check that the result makes sense.",
            "Before we calculate, freeze the physical situation in one sentence. "
            "Which object or region are we studying? What assumptions are we "
            "making? Which law applies under those assumptions? Naming those "
            "choices first helps us avoid carrying a useful equation into a "
            "situation where it no longer applies. Pause here and predict the "
            "next step before listening again.",
            "Now audit the result independently. Check the units on both sides "
            "of each equation. Check the sign against the direction we chose. "
            "Then ask whether the size of the answer makes sense in the original "
            "picture. These checks do not replace a derivation; they are a second "
            "route for catching an arithmetic slip or a hidden assumption.",
            "Return to the diagram and trace the reasoning from the physical "
            "question, through the governing idea, to the final answer. That "
            "chain is more useful than memorizing a formula by itself. When a "
            "new problem changes one condition, ask which link in the chain "
            "changes first. That is how one solved example becomes a method "
            "you can use again.",
        ]
    if item["format"] == "vertical" and len(" ".join(parts).split()) < 110:
        parts.append(
            "Separate the information the question gives from what it asks. "
            "Keep the symbols and units visible, then check that the result "
            "fits the physical picture."
        )
    return re.sub(r"\s+", " ", " ".join(parts)).strip()


def synthesize_google_mp3(
    text: str,
    *,
    voice_name: str,
    language_code: str,
    output_dir: Path,
) -> tuple[Path, bool]:
    """Synthesize and cache one MP3 using Google Application Default Credentials."""
    digest = hashlib.sha256(
        f"{voice_name}\0{language_code}\0{text}".encode("utf-8")
    ).hexdigest()
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / f"{digest}.mp3"
    if destination.is_file() and destination.stat().st_size > 0:
        return destination, True

    try:
        from google.cloud import texttospeech
    except ImportError as exc:
        raise DataValidationError(
            "Google narration requires google-cloud-texttospeech; "
            "install the project requirements"
        ) from exc

    from google.api_core.exceptions import GoogleAPICallError
    from google.auth.exceptions import GoogleAuthError

    try:
        client = texttospeech.TextToSpeechClient()
        response = client.synthesize_speech(
            input=texttospeech.SynthesisInput(text=text),
            voice=texttospeech.VoiceSelectionParams(
                language_code=language_code,
                name=voice_name,
            ),
            audio_config=texttospeech.AudioConfig(
                audio_encoding=texttospeech.AudioEncoding.MP3,
                speaking_rate=1.0,
            ),
        )
        if not response.audio_content:
            raise DataValidationError("Google Text-to-Speech returned empty audio")
        temporary = destination.with_suffix(".mp3.tmp")
        temporary.write_bytes(response.audio_content)
        temporary.replace(destination)
    except DataValidationError:
        raise
    except (GoogleAPICallError, GoogleAuthError, OSError, ValueError) as exc:
        raise DataValidationError(
            f"Google Text-to-Speech failed for voice {voice_name!r}: {exc}"
        ) from exc
    return destination, False
