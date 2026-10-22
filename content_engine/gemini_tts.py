"""Gemini 2.5 Flash TTS — natural multilingual narration.

Uses the existing GEMINI_API_KEY secret. Free tier (1500 req/day) is more
than enough for a small physics channel. Supports English, Hindi, Urdu,
Arabic, and 30+ other languages out of the box.
"""
from __future__ import annotations

import base64
import hashlib
import json
import os
import wave
from pathlib import Path
from typing import Any

# Gemini voice presets (see https://ai.google.dev/gemini-api/docs/speech-generation)
GEMINI_VOICES = {
    "charon":  "Charon",   # informative, calm — default teacher voice
    "kore":    "Kore",     # firm, confident
    "fenrir":  "Fenrir",   # excitable, energetic
    "leda":    "Leda",     # versatile, warm
    "orus":    "Orus",     # firm, authoritative
    "aoede":   "Aoede",    # lilting, expressive
    "puck":    "Puck",     # upbeat, bright
    "zephyr":  "Zephyr",   # bright, clear
}

DEFAULT_VOICE = "charon"


def _cache_key(text: str, language: str, voice: str) -> str:
    payload = f"{voice}\0{language}\0{text}"
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _write_wav(path: Path, pcm_bytes: bytes, sample_rate: int = 24000) -> None:
    """Gemini returns 24kHz mono 16-bit little-endian PCM."""
    with wave.open(str(path), "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(pcm_bytes)


def synthesize_gemini_wav(
    text: str,
    language_code: str,
    cache_dir: Path,
    *,
    voice: str = DEFAULT_VOICE,
    style: str | None = None,
) -> tuple[Path, bool]:
    """Return (wav_path, was_cached).

    Parameters
    ----------
    text : narration script
    language_code : BCP-47 code, e.g. "en-US", "hi-IN", "ur-PK", "ar-XA"
    voice : key from GEMINI_VOICES
    style : optional style directive, e.g. "warm, patient teacher tone"
    """
    if not text.strip():
        raise ValueError("narration text is empty")
    voice_key = voice.lower()
    if voice_key not in GEMINI_VOICES:
        raise ValueError(f"unknown Gemini voice {voice!r}; choose from {list(GEMINI_VOICES)}")

    cache_dir = Path(cache_dir)
    cache_dir.mkdir(parents=True, exist_ok=True)
    key = _cache_key(text, language_code, voice_key)
    cached = cache_dir / f"{key}.wav"
    if cached.is_file() and cached.stat().st_size > 0:
        return cached, True

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is not set. Add it as a repository secret "
            "or export it locally before running."
        )

    from google import genai
    from google.genai import types

    client = genai.Client(api_key=api_key)

    style_hint = style or (
        "Speak clearly and warmly, like a patient physics teacher explaining "
        "to a 17-year-old student. Pause slightly before equations."
    )
    prompt = (
        f"{style_hint}\n"
        f"Language: {language_code}\n"
        f"Read the following script verbatim:\n\n{text}"
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash-preview-tts",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name=GEMINI_VOICES[voice_key]
                    )
                ),
                language_code=language_code,
            ),
        ),
    )

    # Extract base64 audio from the response
    audio_data: bytes | None = None
    for part in (response.candidates[0].content.parts if response.candidates else []):
        inline = getattr(part, "inline_data", None) or getattr(
            getattr(part, "inlineData", None), "data", None
        )
        if inline is not None:
            audio_data = inline if isinstance(inline, bytes) else base64.b64decode(inline)
            break
    if audio_data is None:
        raise RuntimeError("Gemini returned no audio payload")

    _write_wav(cached, audio_data, sample_rate=24000)
    (cache_dir / f"{key}.json").write_text(
        json.dumps(
            {"voice": GEMINI_VOICES[voice_key], "language": language_code, "chars": len(text)},
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    return cached, False
