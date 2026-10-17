from __future__ import annotations

import copy
from pathlib import Path
import unittest

from content_engine.batch import VIDEO_FORMATS, load_batch, validate_batch
from exam_engine.engine import DataValidationError

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "video_batches" / "batch_001.json"


class VideoBatchTests(unittest.TestCase):
    def setUp(self) -> None:
        self.batch = load_batch(MANIFEST)

    def test_first_batch_expands_to_exactly_twenty_branded_videos(self) -> None:
        plan = validate_batch(self.batch, ROOT)
        self.assertEqual(len(plan), 20)
        self.assertEqual(sum(item["format"] == "vertical" for item in plan), 10)
        self.assertEqual(sum(item["format"] == "horizontal" for item in plan), 10)
        self.assertEqual(
            sum(item["type"] == "problem" for item in plan),
            sum(item["type"] == "concept" for item in plan),
        )
        for item in plan:
            self.assertEqual(item["brand_overlay"]["name"], "Saem Physics")
            self.assertEqual(item["brand_overlay"]["tagline"], "NEET JEE MIT")
            self.assertTrue(item["topic_id"])
            self.assertTrue(item["misconception"])
            self.assertEqual(
                sum(beat["duration_seconds"] for beat in item["story_beats"]),
                VIDEO_FORMATS[item["format"]]["duration_seconds"],
            )
            self.assertEqual(item["status"], "approved-for-storyboarding")
            self.assertEqual(item["narration_language"], "English")

    def test_engine_backed_problems_and_manual_checks_are_present(self) -> None:
        plan = validate_batch(self.batch, ROOT)
        engine_checked = {
            episode["id"]
            for episode in self.batch["episodes"]
            if episode.get("problem_spec")
        }
        self.assertEqual(
            engine_checked,
            {
                "b001-e01-projectile-components",
                "b001-e03-dropped-stone",
                "b001-e05-upward-throw",
            },
        )
        self.assertEqual(len(plan), 20)

    def test_failed_physics_engine_expected_output_blocks_the_batch(self) -> None:
        batch = copy.deepcopy(self.batch)
        episode = batch["episodes"][0]
        episode["problem_spec"]["expected_outputs"]["position_m"] = [6, 4]
        with self.assertRaisesRegex(DataValidationError, "physics-engine checks failed"):
            validate_batch(batch, ROOT)

    def test_failed_manual_conservation_audit_blocks_the_batch(self) -> None:
        batch = copy.deepcopy(self.batch)
        episode = next(item for item in batch["episodes"] if item.get("manual_audit"))
        episode["manual_audit"]["expected_final_kinetic_energy_j"] = 9
        with self.assertRaisesRegex(DataValidationError, "collision energy audit failed"):
            validate_batch(batch, ROOT)

    def test_output_duration_and_audience_are_fixed_contracts(self) -> None:
        batch = copy.deepcopy(self.batch)
        batch["video_outputs"][0]["duration_seconds"] = 61
        with self.assertRaisesRegex(DataValidationError, "vertical must have exactly 10 videos"):
            validate_batch(batch, ROOT)

        batch = copy.deepcopy(self.batch)
        batch["audience"]["maximum_age"] = 22
        with self.assertRaisesRegex(DataValidationError, "audience must cover ages"):
            validate_batch(batch, ROOT)

    def test_single_episode_can_target_one_format(self) -> None:
        batch = copy.deepcopy(self.batch)
        batch["episodes"] = batch["episodes"][:1]
        batch["video_outputs"] = [
            {
                "format": "vertical",
                "count": 1,
                "duration_seconds": 60,
                "aspect_ratio": "9:16",
            }
        ]
        plan = validate_batch(batch, ROOT)
        self.assertEqual(len(plan), 1)
        self.assertEqual(plan[0]["format"], "vertical")

    def test_approved_questions_cannot_be_marked_verified_by_the_batch_tool(self) -> None:
        batch = copy.deepcopy(self.batch)
        batch["episodes"][0]["status"] = "verified"
        with self.assertRaisesRegex(DataValidationError, "cannot imply question-bank verification"):
            validate_batch(batch, ROOT)

    def test_format_specific_narration_is_validated_and_added_to_the_plan(self) -> None:
        batch = copy.deepcopy(self.batch)
        batch["episodes"][0]["narration"] = {
            "vertical": "A short spoken script.",
            "horizontal": "A longer spoken script.",
        }
        plan = validate_batch(batch, ROOT)
        self.assertEqual(
            [item["narration"] for item in plan[:2]],
            [
                {"vertical": "A short spoken script.", "horizontal": "A longer spoken script."},
                {"vertical": "A short spoken script.", "horizontal": "A longer spoken script."},
            ],
        )

    def test_invalid_format_specific_narration_is_rejected(self) -> None:
        batch = copy.deepcopy(self.batch)
        batch["episodes"][0]["narration"] = {"square": "Unsupported format."}
        with self.assertRaisesRegex(DataValidationError, "unsupported video format"):
            validate_batch(batch, ROOT)


if __name__ == "__main__":
    unittest.main()
