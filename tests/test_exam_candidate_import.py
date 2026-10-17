from __future__ import annotations

from pathlib import Path
import unittest

from exam_engine.engine import load_recommendations
from exam_engine.engine import load_topics
from tools.import_exam_candidates import ROOT, build_candidate_rows


class ExamCandidateImportTests(unittest.TestCase):
    def test_local_papers_become_pending_non_duplicate_topic_candidates(self) -> None:
        sources, papers, questions, counts = build_candidate_rows(
            ROOT / "exam_papers",
            ROOT / "data" / "physics_topics.csv",
            ROOT / "knowledge" / "concepts.csv",
            ROOT / "knowledge" / "links.csv",
        )
        self.assertEqual(counts["local_pdf_copies"], 30)
        self.assertEqual(counts["distinct_papers"], 26)
        self.assertEqual(len(sources), 30)
        self.assertEqual(len(papers), 26)
        self.assertTrue(questions)
        self.assertTrue(all(row["review_status"] == "pending" for row in questions))
        self.assertTrue(all(row["answer_verified"] == "false" for row in questions))
        self.assertTrue(all(row["rights_status"] == "unknown" for row in questions))
        self.assertEqual(
            len({row["question_id"] for row in questions}),
            len(questions),
        )
        self.assertEqual(
            {row["review_status"] for row in papers},
            {"needs-source-review"},
        )
        self.assertEqual(
            {row["creator"] for row in sources},
            {"Career Point Ltd.", "Unknown"},
        )
        self.assertTrue(
            all(
                "requires independent question, topic, and source review" in row["notes"]
                for row in questions
            )
        )

    def test_pending_candidates_do_not_affect_exam_recommendations(self) -> None:
        topics = load_topics(ROOT / "data" / "physics_topics.csv")
        recommendations = load_recommendations(
            ROOT / "data" / "exam_question_metadata.csv",
            topics,
            exam="jee-advanced",
            as_of_year=2026,
        )
        self.assertTrue(
            all(
                item.basis == "uniform-curriculum-baseline"
                for item in recommendations
            )
        )
        self.assertTrue(all(item.question_records == 0 for item in recommendations))


if __name__ == "__main__":
    unittest.main()
