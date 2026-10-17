from __future__ import annotations

import json
from contextlib import redirect_stderr
from io import StringIO
from pathlib import Path
import tempfile
import unittest

from exam_engine.engine import DataValidationError
from video_learning import (
    STYLE_PROFILES,
    _load_observations,
    generate_plan,
    main,
    select_concepts,
)


def make_network() -> dict:
    concept_ids = ["math:derivatives", "math:integrals", "physics:kinematics"]
    return {
        "concepts": [
            {"concept_id": "math:derivatives", "concept_name": "Derivatives", "domain": "mathematics"},
            {"concept_id": "math:integrals", "concept_name": "Integrals", "domain": "mathematics"},
            {"concept_id": "physics:kinematics", "concept_name": "Kinematics", "domain": "physics"},
        ],
        "question_analyses": [
            {
                "question_id": "jee-2025-q001",
                "analysis": {
                    "concepts": [
                        {
                            "concept_id": "physics:kinematics",
                            "direct_score": 1.0,
                            "ranking_score": 1.0,
                        },
                        {
                            "concept_id": "math:derivatives",
                            "direct_score": 0.5,
                            "ranking_score": 0.5,
                        },
                    ]
                },
            }
        ],
        "question_concept_matrix": {
            "row_labels": ["jee-2025-q001"],
            "column_labels": concept_ids,
            "values": [[1.0, 0.0, 0.5]],
        },
        "book_linked_concept_matrix": {
            "row_labels": ["strang-calculus-s001"],
            "column_labels": concept_ids,
            "values": [[1.0, 0.8, 0.0]],
        },
        "book_concept_matrix": {
            "row_labels": ["strang-calculus-s001"],
            "column_labels": concept_ids,
            "values": [[1.0, 0.8, 0.0]],
        },
    }


class VideoLearningTests(unittest.TestCase):
    def test_selects_concepts_from_question_or_book_matrix(self) -> None:
        network = make_network()

        question, question_type = select_concepts(network, question_id="jee-2025-q001")
        book, book_type = select_concepts(network, book_section_id="strang-calculus-s001")

        self.assertEqual(question_type, "question")
        self.assertEqual(question["physics:kinematics"], 1.0)
        self.assertEqual(question["math:derivatives"], 0.5)
        self.assertEqual(book_type, "book-section")
        self.assertEqual(book["math:derivatives"], 1.0)
        self.assertEqual(book["math:integrals"], 0.8)

    def test_generation_is_seeded_and_uses_original_teaching_profiles(self) -> None:
        network = make_network()

        first = generate_plan(network, concept_ids=["math:derivatives"], seed=42)
        second = generate_plan(network, concept_ids=["math:derivatives"], seed=42)

        self.assertEqual(first, second)
        self.assertIn(first["teaching_approach"]["id"], STYLE_PROFILES)
        self.assertEqual(first["selection_type"], "selected-concepts")
        self.assertTrue(first["review_required"])
        self.assertFalse(first["learning_signal"]["raw_video_or_audio_analyzed"])
        self.assertIn("creator", " ".join(first["narration_guidance"]))

    def test_history_prevents_reusing_same_style_visual_audio_combination(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            history = Path(directory) / "history.json"
            first = generate_plan(
                make_network(), concept_ids=["math:integrals"], history_path=history, seed=8
            )
            second = generate_plan(
                make_network(), concept_ids=["math:integrals"], history_path=history, seed=8
            )

        self.assertNotEqual(
            first["uniqueness_fingerprint"], second["uniqueness_fingerprint"]
        )

    def test_reviewed_video_observations_adjust_style_sampling(self) -> None:
        observation = {
            "video_id": "reviewed-local-video-01",
            "concept_ids": ["math:derivatives"],
            "style_id": "geometric_calculus",
            "visual_treatment": "coordinate_plot",
            "audio_palette": "quiet_precision",
            "rating": 5,
        }

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "observations.json"
            path.write_text(json.dumps([observation]), encoding="utf-8")
            loaded = _load_observations(
                path, {"math:derivatives", "physics:kinematics"}
            )

        baseline = generate_plan(make_network(), concept_ids=["math:derivatives"], seed=19)
        learned = generate_plan(
            make_network(),
            concept_ids=["math:derivatives"],
            observations=loaded,
            seed=19,
        )
        self.assertNotEqual(
            baseline["teaching_approach"]["selection_probability"],
            learned["teaching_approach"]["selection_probability"],
        )
        self.assertNotEqual(
            baseline["treatment_probabilities"]["visual"],
            learned["treatment_probabilities"]["visual"],
        )
        self.assertNotEqual(
            baseline["treatment_probabilities"]["audio_palette"],
            learned["treatment_probabilities"]["audio_palette"],
        )
        self.assertEqual(learned["learning_signal"]["reviewed_video_observations"], 1)

    def test_rejects_invalid_observations_and_unknown_selectors(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.json"
            path.write_text(
                json.dumps(
                    [
                        {
                            "video_id": "bad",
                            "concept_ids": ["math:derivatives"],
                            "style_id": "imitate-famous-creator",
                            "visual_treatment": "coordinate_plot",
                            "audio_palette": "quiet_precision",
                            "rating": 5,
                        }
                    ]
                ),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(DataValidationError, "unknown style_id"):
                _load_observations(path, {"math:derivatives"})
        with self.assertRaisesRegex(DataValidationError, "unknown concept ID"):
            select_concepts(make_network(), concept_ids=["math:unknown"])

    def test_cli_builds_network_and_writes_plan(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            books = root / "books"
            papers = root / "papers"
            books.mkdir()
            papers.mkdir()
            (books / "calculus.md").write_text(
                "# Derivatives\nThe derivative is a rate of change and the integral accumulates area.\n",
                encoding="utf-8",
            )
            (papers / "paper.md").write_text(
                "Question 1. A projectile has velocity and acceleration.\n",
                encoding="utf-8",
            )
            (books / "broken.docx").write_bytes(b"not a docx archive")
            output = root / "plan.json"
            history = root / "history.json"

            errors = StringIO()
            with redirect_stderr(errors):
                result = main(
                    [
                        "--concepts", "math:derivatives", "math:integrals",
                        "--books", str(books),
                        "--exam-papers", str(papers),
                        "--history", str(history),
                        "--seed", "2",
                        "--output", str(output),
                    ]
                )

            self.assertEqual(result, 0)
            self.assertEqual(len(json.loads(output.read_text())["concepts"]), 2)
            self.assertTrue(history.is_file())
            self.assertIn("broken.docx", errors.getvalue())
if __name__ == "__main__":
    unittest.main()
