from __future__ import annotations

from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from content_engine.request import build_request, create_interactive_request, write_request
from exam_engine.engine import DataValidationError


class ContentRequestTests(unittest.TestCase):
    def test_request_sets_both_formats_and_evidence_candidates(self) -> None:
        request = build_request(
            "Create an original JEE kinematics lesson batch about projectile motion",
            episodes=4,
        )
        self.assertEqual(request["batch"]["episode_count"], 4)
        self.assertEqual(request["batch"]["deliverable_count"], 8)
        self.assertEqual(
            [item["format"] for item in request["batch"]["formats"]],
            ["vertical", "horizontal"],
        )
        self.assertTrue(request["suggested_concepts"])
        self.assertIn("not confirmed", request["concept_match_note"])
        self.assertEqual(request["status"], "intake-ready-for-original-authoring")

    def test_single_format_request_sets_matching_deliverable_count(self) -> None:
        request = build_request("Explain matrices geometrically", episodes=1, formats="horizontal")
        self.assertEqual(request["batch"]["deliverable_count"], 1)
        self.assertEqual(
            [item["format"] for item in request["batch"]["formats"]],
            ["horizontal"],
        )

    def test_invalid_request_fields_are_rejected(self) -> None:
        with self.assertRaisesRegex(DataValidationError, "brief"):
            build_request(" ")
        with self.assertRaisesRegex(DataValidationError, "1 to 10"):
            build_request("calculus", episodes=11)
        with self.assertRaisesRegex(DataValidationError, "batch_id"):
            build_request("calculus", batch_id="../bad")

    def test_interactive_request_reads_a_plain_language_brief(self) -> None:
        with patch("builtins.input", return_value="Teach JEE electrostatics"):
            request = create_interactive_request(episodes=2)
        self.assertIn("electrostatics", request["owner_brief"])
        self.assertEqual(request["batch"]["deliverable_count"], 4)

    def test_request_is_written_as_readable_json(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "requests" / "batch.json"
            request = build_request("Teach vectors", episodes=1)
            write_request(request, output)
            self.assertIn('"request_id"', output.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
