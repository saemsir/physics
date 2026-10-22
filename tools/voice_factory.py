#!/usr/bin/env python3
"""Switchable narration providers: local XTTS clone, Edge, Gemini, gTTS, eSpeak."""
from __future__ import annotations

import asyncio
import hashlib
import os
import shutil
import subprocess
import wave
from pathlib import Path

SAMPLE_RATE = 24000

VOICE_CATALOG = {
    "english": {"edge": "en-US-ChristopherNeural", "gemini": "Kore", "gtts": "en", "espeak": "en-us", "local": "saem-clone"},
    "hindi":   {"edge": "hi-IN-MadhurNeural",      "gemini": "Kore", "gtts": "hi", "espeak": "hi",   "local": "saem-clone"},
    "urdu":    {"edge": "ur-IN-SalmanNeural",      "gemini": "Kore", "gtts": "ur", "espeak": "ur",   "local": None},
    "arabic":  {"edge": "ar-SA-HamedNeural",       "gemini": "Kore", "gtts": "ar", "espeak": "ar",   "local": "saem-clone"},
}
LANG_ALIASES = {
    "en": "english", "hi": "hindi", "ur": "urdu", "ar": "arabic",
    "english": "english", "hindi": "hindi", "urdu": "urdu", "arabic": "arabic",
}
PROVIDERS = ("local", "edge", "gemini", "gtts", "espeak")


def _patch_torch_load_for_coqui() -> None:
    import torch
    if getattr(torch, "_saem_load_patched", False):
        return
    original = torch.load
    def permissive_load(*args, **kwargs):
        kwargs.setdefault("weights_only", False)
        return original(*args, **kwargs)
    torch.load = permissive_load
    torch._saem_load_patched = True


def _edge(text, voice, out):
    import edge_tts
    asyncio.run(edge_tts.Communicate(text, voice).save(str(out)))


def _gtts(text, voice, out):
    from gtts import gTTS
    gTTS(text=text, lang=voice).save(str(out))


def _espeak(text, voice, out):
    exe = shutil.which("espeak-ng") or shutil.which("espeak")
    if not exe:
        raise RuntimeError("espeak-ng not installed (sudo apt-get install -y espeak-ng)")
    subprocess.run([exe, "-v", voice, "-w", str(out), text], check=True)


def _gemini(text, voice, out):
    from google import genai
    from google.genai import types
    key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not key:
        raise RuntimeError("GEMINI_API_KEY secret is not set")
    client = genai.Client(api_key=key)
    resp = client.models.generate_content(
        model="gemini-2.5-flash-preview-tts",
        contents=text,
        config=types.GenerateContentConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name=voice)
                )
            ),
        ),
    )
    pcm = resp.candidates[0].content.parts[0].inline_data.data
    with wave.open(str(out), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SAMPLE_RATE)
        w.writeframes(pcm)


def _local(text, voice, out, voice_wav, lang):
    code = {"english": "en", "hindi": "hi", "arabic": "ar"}.get(lang)
    if code is None:
        raise RuntimeError("local XTTS cannot speak urdu; use provider=edge or gtts")
    os.environ.setdefault("COQUI_TOS_AGREED", "1")
    _patch_torch_load_for_coqui()
    import numpy as np
    import soundfile as sf
    import torch
    from TTS.api import TTS
    device = "cuda" if torch.cuda.is_available() else "cpu"
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
    wav = tts.tts(text=text, speaker_wav=str(voice_wav), language=code, split_sentences=True)
    sf.write(str(out), np.asarray(wav, dtype=np.float32), SAMPLE_RATE)


def synthesize_narration(text, language, provider, cache_dir, voice=None, voice_wav=None):
    """Return (audio_path, was_cached, voice_tag)."""
    if not text.strip():
        raise ValueError("narration text is empty")
    lang = LANG_ALIASES.get(str(language).lower(), "english")
    catalog = VOICE_CATALOG.get(lang, VOICE_CATALOG["english"])
    chosen = voice or catalog.get(provider)
    if chosen is None:
        raise RuntimeError(f"provider '{provider}' has no voice for '{lang}'; try edge, gtts or espeak")
    cache_dir = Path(cache_dir)
    cache_dir.mkdir(parents=True, exist_ok=True)
    ext = ".mp3" if provider == "gtts" else ".wav"
    key = hashlib.sha256(f"{provider}\0{chosen}\0{text}".encode("utf-8")).hexdigest()
    cached_path = cache_dir / f"{key}{ext}"
    if cached_path.is_file() and cached_path.stat().st_size > 0:
        return cached_path, True, chosen
    if provider == "edge":
        _edge(text, chosen, cached_path)
    elif provider == "gtts":
        _gtts(text, chosen, cached_path)
    elif provider == "espeak":
        _espeak(text, chosen, cached_path)
    elif provider == "gemini":
        _gemini(text, chosen, cached_path)
    elif provider == "local":
        _local(text, chosen, cached_path, voice_wav, lang)
    else:
        raise RuntimeError(f"unknown narration provider '{provider}'")
    return cached_path, False, chosen
