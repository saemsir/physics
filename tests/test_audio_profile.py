from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest
import wave

from tools.analyze_voice_sample import analyze

ROOT = Path(__file__).resolve().parents[1]


class AudioProfileTests(unittest.TestCase):
    def test_profile_is_explicitly_provisional_until_sample_analysis(self) -> None:
        profile = json.loads((ROOT / "config" / "audio_profile.json").read_text())
        self.assertEqual(
            profile["status"],
            "provisional-awaiting-private-voice-sample-analysis",
        )
        self.assertEqual(
            profile["sample_analysis"]["analysis_status"],
            "not-run-file-not-found-in-workspace",
        )
        self.assertEqual(profile["mix_targets"]["true_peak_db_tp_max"], -1.0)

    def test_analyzer_reports_pcm_levels_without_changing_source_file(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "voice.wav"
            samples = [0, 0, 1000, -1000, 1000, -1000, 0, 0]
            with wave.open(str(path), "wb") as wav:
                wav.setnchannels(1)
                wav.setsampwidth(2)
                wav.setframerate(8000)
                wav.writeframes(
                    b"".join(sample.to_bytes(2, "little", signed=True) for sample in samples)
                )
            original = path.read_bytes()
            report = analyze(path)
            self.assertEqual(path.read_bytes(), original)
            self.assertEqual(report["channels"], 1)
            self.assertEqual(report["sample_rate_hz"], 8000)
            self.assertEqual(report["bit_depth"], 16)
            self.assertEqual(report["leading_silence_seconds_at_-60dBFS"], 0.0)
            self.assertEqual(report["trailing_silence_seconds_at_-60dBFS"], 0.0)
            self.assertEqual(report["channel_levels"][0]["clipped_samples"], 0)

    def test_analyzer_rejects_missing_file_explicitly(self) -> None:
        with self.assertRaisesRegex(ValueError, "cannot analyze PCM WAV"):
            analyze(Path("/path/that/does/not/exist.wav"))

    def test_analyzer_rejects_truncated_pcm_frames(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "truncated.wav"
            with wave.open(str(path), "wb") as wav:
                wav.setnchannels(1)
                wav.setsampwidth(2)
                wav.setframerate(8000)
                wav.writeframes(b"\x00\x00" * 8)
            path.write_bytes(path.read_bytes()[:-4])
            with self.assertRaisesRegex(ValueError, "truncated WAV"):
                analyze(path)


if __name__ == "__main__":
    unittest.main()
