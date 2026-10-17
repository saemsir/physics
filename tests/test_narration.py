from __future__ import annotations

from pathlib import Path
import tempfile
import unittest

from content_engine.batch import load_batch, validate_batch
from content_engine.narration import narration_text, synthesize_google_mp3
from exam_engine.engine import DataValidationError

ROOT = Path(__file__).resolve().parents[1]


class NarrationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.item = validate_batch(
            load_batch(ROOT / "data" / "video_batches" / "batch_002.json"),
            ROOT,
        )[0]

    def test_default_script_uses_reviewable_episode_content(self) -> None:
        text = narration_text(self.item)
        for part in (
            self.item["title"],
            self.item["question"],
            self.item["solution"],
            self.item["answer"],
        ):
            self.assertIn(part, text)
        self.item["format"] = "horizontal"
        horizontal = narration_text(self.item)
        self.assertIn(self.item["visual_hook"], horizontal)
        self.assertIn(self.item["misconception"], horizontal)

    def test_custom_script_is_selected_by_output_format(self) -> None:
        self.item["narration"] = {
            "vertical": "A concise vertical script.",
            "horizontal": "A detailed horizontal script.",
        }
        self.assertEqual(narration_text(self.item), "A concise vertical script.")
        self.item["format"] = "horizontal"
        self.assertEqual(narration_text(self.item), "A detailed horizontal script.")

    def test_missing_format_script_is_not_silently_filled(self) -> None:
        self.item["narration"] = {"vertical": "Vertical only."}
        self.item["format"] = "horizontal"
        with self.assertRaisesRegex(DataValidationError, "narration.horizontal"):
            narration_text(self.item)

    def test_batch_draft_scripts_aim_for_both_video_durations(self) -> None:
        plan = validate_batch(
            load_batch(ROOT / "data" / "video_batches" / "batch_002.json"),
            ROOT,
        )
        vertical = [item for item in plan if item["format"] == "vertical"]
        horizontal = [item for item in plan if item["format"] == "horizontal"]
        self.assertEqual(len(vertical), 10)
        self.assertEqual(len(horizontal), 10)
        self.assertTrue(
            all(100 <= len(narration_text(item).split()) <= 180 for item in vertical)
        )
        self.assertTrue(
            all(320 <= len(narration_text(item).split()) <= 450 for item in horizontal)
        )

    def test_synthesis_reuses_cached_mp3_without_cloud_credentials(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            cache = Path(temporary)
            cached = cache / "existing.mp3"
            cached.write_bytes(b"voice")
            import hashlib

            digest = hashlib.sha256(
                b"en-US-Neural2-J\0en-US\0Narrate this."
            ).hexdigest()
            cached.rename(cache / f"{digest}.mp3")
            result, reused = synthesize_google_mp3(
                "Narrate this.",
                voice_name="en-US-Neural2-J",
                language_code="en-US",
                output_dir=cache,
            )
            self.assertTrue(reused)
            self.assertEqual(result.read_bytes(), b"voice")


if __name__ == "__main__":
    unittest.main()
