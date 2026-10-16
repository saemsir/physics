#!/usr/bin/env python3
"""Read-only, local technical inspection of a PCM WAV voice sample."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import struct
import sys
import wave


def _dbfs(ratio: float) -> float | None:
    if ratio <= 0:
        return None
    return round(20 * math.log10(ratio), 2)


def analyze(path: Path) -> dict:
    path = Path(path)
    try:
        with wave.open(str(path), "rb") as wav:
            channels = wav.getnchannels()
            sample_rate = wav.getframerate()
            frames = wav.getnframes()
            sample_width = wav.getsampwidth()
            compression = wav.getcomptype()
            if compression != "NONE":
                raise ValueError(f"unsupported WAV compression {compression!r}; use PCM")
            if channels < 1 or sample_rate < 1 or frames < 1:
                raise ValueError("WAV must have channels, sample rate, and audio frames")
            if sample_width not in (1, 2, 3, 4):
                raise ValueError(f"unsupported PCM sample width: {sample_width} bytes")

            full_scale = 1 << (sample_width * 8 - 1)
            sums = [0] * channels
            sums_squares = [0] * channels
            peaks = [0] * channels
            clipped = [0] * channels
            threshold = full_scale * 0.001
            first_active: int | None = None
            last_active: int | None = None
            frame_offset = 0
            if sample_width == 2:
                decoder = struct.Struct("<" + "h" * channels)
            elif sample_width == 4:
                decoder = struct.Struct("<" + "i" * channels)
            else:
                decoder = None

            while block := wav.readframes(8192):
                if len(block) % (sample_width * channels):
                    raise ValueError("WAV ends with an incomplete PCM frame")
                if sample_width == 1:
                    values = (value - 128 for value in block)
                    frame_samples = []
                    sample_iter = iter(values)
                    for _ in range(len(block) // channels):
                        frame_samples.append(
                            [next(sample_iter) for _ in range(channels)]
                        )
                elif sample_width == 3:
                    frame_samples = []
                    for start in range(0, len(block), 3 * channels):
                        frame = []
                        for channel in range(channels):
                            start_sample = start + channel * 3
                            integer = int.from_bytes(
                                block[start_sample:start_sample + 3],
                                "little",
                                signed=False,
                            )
                            if integer & 0x800000:
                                integer -= 0x1000000
                            frame.append(integer)
                        frame_samples.append(frame)
                else:
                    frame_samples = [
                        decoder.unpack_from(block, offset)
                        for offset in range(0, len(block), decoder.size)
                    ]

                for frame in frame_samples:
                    frame_peak = 0
                    for channel, value in enumerate(frame):
                        magnitude = abs(value)
                        sums[channel] += value
                        sums_squares[channel] += value * value
                        peaks[channel] = max(peaks[channel], magnitude)
                        if magnitude >= full_scale * 0.99999:
                            clipped[channel] += 1
                        frame_peak = max(frame_peak, magnitude)
                    if frame_peak >= threshold:
                        if first_active is None:
                            first_active = frame_offset
                        last_active = frame_offset
                    frame_offset += 1

            if frame_offset != frames:
                raise ValueError(
                    f"truncated WAV: header declares {frames} frames, read {frame_offset}"
                )

    except (OSError, EOFError, wave.Error, struct.error, ValueError) as exc:
        raise ValueError(f"cannot analyze PCM WAV {path}: {exc}") from exc

    channel_results = []
    for channel in range(channels):
        rms = math.sqrt(sums_squares[channel] / frames) / full_scale
        peak = peaks[channel] / full_scale
        channel_results.append(
            {
                "channel": channel + 1,
                "peak_dbfs": _dbfs(peak),
                "rms_dbfs": _dbfs(rms),
                "dc_offset": round(sums[channel] / frames / full_scale, 6),
                "clipped_samples": clipped[channel],
                "clipped_sample_percent": round(clipped[channel] / frames * 100, 6),
            }
        )

    leading_silence = first_active if first_active is not None else frames
    trailing_silence = (
        frames - last_active - 1 if last_active is not None else frames
    )
    duration = frames / sample_rate
    return {
        "file_name": path.name,
        "duration_seconds": round(duration, 3),
        "channels": channels,
        "sample_rate_hz": sample_rate,
        "bit_depth": sample_width * 8,
        "encoding": "PCM",
        "leading_silence_seconds_at_-60dBFS": round(
            leading_silence / sample_rate, 3
        ),
        "trailing_silence_seconds_at_-60dBFS": round(
            trailing_silence / sample_rate, 3
        ),
        "channel_levels": channel_results,
        "interpretation": (
            "These are technical signal measurements only. Listen locally for "
            "room noise, plosives, sibilance, and reverberation before choosing EQ."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("wav_path", type=Path)
    args = parser.parse_args()
    try:
        report = analyze(args.wav_path)
    except ValueError as exc:
        print(f"analyze_voice_sample: error: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
