from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
import tempfile
import unittest

import pymupdf as fitz

from content_engine.batch import load_batch, validate_batch
from tools.render_practice_paper import (
    DEFAULT_INPUT,
    PracticePaperError,
    load_paper,
    render_pair,
)
from studio_engine.engine import StudioEngine

ROOT = Path(__file__).resolve().parents[1]
VIDEO_BATCH = ROOT / "data" / "video_batches" / "batch_002.json"


class PracticePaperTests(unittest.TestCase):
    def test_paper_has_requested_original_question_mix_and_caveat(self) -> None:
        paper = load_paper(DEFAULT_INPUT)
        self.assertEqual(len(paper["questions"]), 10)
        self.assertEqual(
            paper["question_type_mix"],
            {"single_correct": 4, "multiple_correct": 3, "numerical": 3},
        )
        self.assertEqual(
            paper["forecast_basis"]["status"],
            "prior-only-no-verified-exam-records",
        )
        self.assertEqual(
            Counter(question["area"] for question in paper["questions"]),
            {
                "Mechanics": 2,
                "Electricity and Magnetism": 2,
                "Waves and Optics": 2,
                "Thermal Physics": 2,
                "Modern Physics": 2,
            },
        )
        self.assertIn("not a reliable prediction", paper["notice"])
        self.assertTrue(
            all(not question["prompt"].startswith("A previous") for question in paper["questions"])
        )

    def test_candidate_and_solution_pdfs_render_and_reopen(self) -> None:
        paper = load_paper(DEFAULT_INPUT)
        with tempfile.TemporaryDirectory() as directory:
            questions_pdf, solutions_pdf = render_pair(DEFAULT_INPUT, Path(directory))
            self.assertTrue(questions_pdf.is_file())
            self.assertTrue(solutions_pdf.is_file())
            with fitz.open(questions_pdf) as questions:
                self.assertEqual(len(questions), 5)
                text = "\n".join(page.get_text() for page in questions)
                self.assertIn("Question 1", text)
                self.assertIn("NOT AN OFFICIAL PREDICTION", text)
                self.assertNotIn("Conserve momentum during", text)
            with fitz.open(solutions_pdf) as solutions:
                self.assertEqual(len(solutions), 10)
                self.assertIn("Conserve momentum during", "\n".join(page.get_text() for page in solutions))

    def test_studio_coordinator_renders_both_pdf_artifacts(self) -> None:
        request = {
            "schema_version": 1,
            "run_id": "paper-render-test",
            "tasks": [
                {
                    "id": "paper",
                    "action": "exam.render_practice_paper",
                    "params": {"paper": "data/practice_papers/jee_advanced_2027_physics_set_01.json"},
                }
            ],
        }
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            report = StudioEngine(ROOT).run(request, output_override=output)
            self.assertEqual(report["status"], "succeeded")
            result = json.loads((output / "paper.json").read_text(encoding="utf-8"))
            self.assertEqual(result["status"], "rendered")
            self.assertTrue((output / result["questions_pdf"]).is_file())
            self.assertTrue((output / result["solutions_pdf"]).is_file())

    def test_rejects_a_question_count_mismatch(self) -> None:
        paper = json.loads(DEFAULT_INPUT.read_text(encoding="utf-8"))
        paper["questions"].pop()
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.json"
            path.write_text(json.dumps(paper), encoding="utf-8")
            with self.assertRaisesRegex(PracticePaperError, "question_count"):
                load_paper(path)

    def test_video_batch_has_five_concepts_and_five_problems(self) -> None:
        batch = load_batch(VIDEO_BATCH)
        episodes = batch["episodes"]
        self.assertEqual(len(episodes), 10)
        self.assertEqual(sum(item["type"] == "concept" for item in episodes), 5)
        self.assertEqual(sum(item["type"] == "problem" for item in episodes), 5)
        self.assertEqual(batch["status"], "draft-owner-review")
        self.assertEqual(len(validate_batch(batch, ROOT)), 20)


if __name__ == "__main__":
    unittest.main()
