#!/usr/bin/env python3
"""Offline voice-cloned narration for CI renders. No external API calls."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path

SAMPLE_RATE = 24000
VOICE_TAG = "saem-clone"


def _cache_key(voice: Path, text: str) -> str:
    digest = hashlib.sha256(voice.read_bytes()).hexdigest()[:16]
    return hashlib.sha256(f"{digest}\0{text}".encode("utf-8")).hexdigest()


def synthesize_local_wav(text: str, voice_wav: Path, cache_dir: Path) -> tuple[Path, bool]:
    """Return (wav_path, was_cached). Weights download once, then cache serves reruns."""
    if not text.strip():
        raise ValueError("narration text is empty")
    voice_wav = Path(voice_wav)
    if not voice_wav.is_file():
        raise RuntimeError(
            f"voice reference not found: {voice_wav}. "
            "The workflow must decode SAEM_VOICE_SAMPLE_B64 first."
        )
    cache_dir = Path(cache_dir)
    cache_dir.mkdir(parents=True, exist_ok=True)
    key = _cache_key(voice_wav, text)
    cached = cache_dir / f"{key}.wav"
    if cached.is_file() and cached.stat().st_size > 0:
        return cached, True

    os.environ.setdefault("COQUI_TOS_AGREED", "1")
    import numpy as np
    import soundfile as sf
    import torch
    from TTS.api import TTS

    device = "cuda" if torch.cuda.is_available() else "cpu"
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
    wav = tts.tts(text=text, speaker_wav=str(voice_wav), language="en", split_sentences=True)
    sf.write(str(cached), np.asarray(wav, dtype=np.float32), SAMPLE_RATE)
    (cache_dir / f"{key}.json").write_text(
        json.dumps({"voice": voice_wav.name, "chars": len(text)}), encoding="utf-8"
    )
    return cached, False
