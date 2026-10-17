from __future__ import annotations

import json
from pathlib import Path
import sqlite3
import tempfile
import unittest
from unittest.mock import patch

from content_engine.__main__ import main as content_main
from exam_engine.engine import DataValidationError
from exam_engine.engine import load_topics
from knowledge.graph import load_graph
from production_knowledge.engine import (
    ROOT,
    ProductionKnowledge,
    _episode_concepts,
    _filename_metadata,
    _validate_matrix,
)


class ProductionKnowledgeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.directory = tempfile.TemporaryDirectory()
        self.root = Path(self.directory.name)
        self.knowledge = ProductionKnowledge(self.root / "production.sqlite")
        self.matrix = {
            "concepts": [
                {
                    "concept_id": "physics:kinematics",
                    "concept_name": "Kinematics",
                    "domain": "physics",
                },
                {
                    "concept_id": "math:derivatives",
                    "concept_name": "Derivatives",
                    "domain": "mathematics",
                },
                {
                    "concept_id": "math:graphs",
                    "concept_name": "Functions and graphs",
                    "domain": "mathematics",
                },
            ],
            "concept_uses_math_matrix": {
                "row_labels": ["physics:kinematics"],
                "column_labels": ["math:derivatives", "math:graphs"],
                "values": [[0.8, 0.0]],
            },
            "question_analyses": [
                {
                    "question_id": "matrix-question-1",
                    "analysis": {
                        "concepts": [
                            {
                                "concept_id": "physics:kinematics",
                                "direct_score": 1.0,
                                "ranking_score": 1.0,
                            }
                        ]
                    },
                }
            ],
        }

    def tearDown(self) -> None:
        self.directory.cleanup()

    def test_database_is_persistent_and_seeds_original_principles(self) -> None:
        self.assertEqual(self.knowledge.counts()["practice_rules"], 12)
        reopened = ProductionKnowledge(self.knowledge.path)
        self.assertEqual(reopened.counts()["practice_rules"], 12)

    def test_segment_names_group_clips_and_keep_offset_metadata(self) -> None:
        self.assertEqual(
            _filename_metadata(Path("Calculus overview_120_240.mp4")),
            ("Calculus overview", 120.0, 240.0),
        )
        self.assertEqual(
            _filename_metadata(Path("unsegmented reference.mp4")),
            ("unsegmented reference", None, None),
        )

    def test_video_indexing_persists_and_repeats_decode_errors(self) -> None:
        output = ROOT / "output"
        output.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=output) as directory:
            videos = Path(directory)
            (videos / "broken_0_10.mp4").write_bytes(b"\r\n")
            with patch(
                "production_knowledge.engine._run_ffmpeg",
                side_effect=DataValidationError("invalid fixture media"),
            ):
                first = self.knowledge.index_videos(videos)
                second = self.knowledge.index_videos(videos)
        self.assertEqual(first["failed"], 1)
        self.assertEqual(second["failed"], 1)
        self.assertEqual(second["unchanged"], 1)
        self.assertEqual(self.knowledge.counts()["failed_media"], 1)

    def test_episode_topic_maps_through_matrix_to_math_prerequisites(self) -> None:
        concepts = {
            item["concept_id"]: item for item in self.matrix["concepts"]
        }
        selected = _episode_concepts(
            {"id": "episode-1", "type": "problem", "topic_id": "kinematics"},
            self.matrix,
            concepts,
            self._graph(),
        )
        self.assertEqual(selected, {"physics:kinematics": 1.0, "math:derivatives": 0.8})

    def test_matrix_question_selection_uses_direct_not_propagated_matches(self) -> None:
        concepts = {
            item["concept_id"]: item for item in self.matrix["concepts"]
        }
        selected = _episode_concepts(
            {"id": "episode-1", "question_id": "matrix-question-1"},
            self.matrix,
            concepts,
            self._graph(),
        )
        self.assertEqual(selected, {"physics:kinematics": 1.0})

    def test_episode_text_matches_shared_matrix_concept_evidence(self) -> None:
        selected = _episode_concepts(
            {
                "id": "episode-vectors",
                "title": "Vector displacement",
                "topic_id": "vectors",
                "question": "Why is the displacement a vector rather than a scalar?",
            },
            self.matrix,
            {
                item["concept_id"]: item for item in self.matrix["concepts"]
            } | {
                "math:scalars-vectors": {
                    "concept_id": "math:scalars-vectors",
                    "concept_name": "Scalars and vectors",
                    "domain": "mathematics",
                }
            },
            self._graph(),
        )
        self.assertIn("math:scalars-vectors", selected)

    def test_advice_is_attached_and_saved_for_each_batch_episode(self) -> None:
        plan = self.knowledge.advise_batch(
            {
                "batch_id": "matrix-batch-1",
                "episodes": [
                    {
                        "id": "episode-1",
                        "type": "problem",
                        "title": "Motion from a graph",
                        "topic_id": "kinematics",
                    }
                ],
            },
            self.matrix,
        )
        self.assertEqual(plan["deliverable_count"], 2)
        episode = plan["episodes"][0]
        self.assertEqual(
            episode["matrix_concepts"][0]["concept_id"], "physics:kinematics"
        )
        self.assertIn("narration", episode["advice_by_area"])
        self.assertIn("sound", episode["advice_by_area"])
        self.assertTrue(episode["review_required"])
        self.assertFalse(episode["video_specific_capture"])
        self.assertEqual(self.knowledge.counts()["batch_recommendations"], 1)
        connection = sqlite3.connect(self.knowledge.path)
        try:
            saved = connection.execute(
                "SELECT plan_json FROM batch_recommendations WHERE batch_id = ?",
                ("matrix-batch-1",),
            ).fetchone()[0]
        finally:
            connection.close()
        self.assertEqual(json.loads(saved)["batch_id"], "matrix-batch-1")

    def test_batch_plan_automatically_attaches_matrix_advice(self) -> None:
        topics = load_topics(ROOT / "data" / "physics_topics.csv")
        graph = load_graph(
            ROOT / "knowledge" / "concepts.csv",
            ROOT / "knowledge" / "links.csv",
            topics,
        )
        concepts = [
            {
                "concept_id": concept.concept_id,
                "concept_name": concept.concept_name,
                "domain": concept.domain,
            }
            for concept in graph.concepts
        ]
        mathematics = [
            concept["concept_id"]
            for concept in concepts
            if concept["domain"] == "mathematics"
        ]
        rows = []
        for concept in graph.concepts:
            link_targets = {
                link.target_id: 0.8
                for link in graph.links
                if link.source_id == concept.concept_id and link.relation == "uses_math"
            }
            rows.append([link_targets.get(math_id, 0.0) for math_id in mathematics])
        matrix = {
            "concepts": concepts,
            "concept_uses_math_matrix": {
                "row_labels": [concept["concept_id"] for concept in concepts],
                "column_labels": mathematics,
                "values": rows,
            },
        }
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            matrix_path = root / "matrix.json"
            matrix_path.write_text(json.dumps(matrix), encoding="utf-8")
            batch_path = root / "batch-plan.json"
            advice_path = root / "advice.json"
            result = content_main(
                [
                    "batch-plan",
                    "--manifest", str(ROOT / "data" / "video_batches" / "batch_001.json"),
                    "--matrix", str(matrix_path),
                    "--production-database", str(root / "knowledge.sqlite"),
                    "--production-advice-output", str(advice_path),
                    "--output", str(batch_path),
                ]
            )
            self.assertEqual(result, 0)
            batch_plan = json.loads(batch_path.read_text(encoding="utf-8"))
            advice = batch_plan["production_advice"]
            self.assertEqual(advice["deliverable_count"], 20)
            self.assertEqual(
                json.loads(advice_path.read_text(encoding="utf-8"))["batch_id"],
                "batch_001",
            )

    def test_review_ratings_adjust_relevant_advice_and_notes_are_bounded(self) -> None:
        self.knowledge.record_review(
            video_title="Reviewed calculus video",
            concept_ids=["math:derivatives"],
            editing=5,
            narration_pacing=4,
            narration_clarity=5,
            narration_sync=4,
            sound=3,
            visual_clarity=5,
            notes="The visual labels remain readable during the explanation.",
        )
        before = self.knowledge._rank_rules(
            {"math:derivatives": 1.0}, "concept"
        )
        self.knowledge.record_review(
            video_title="Second reviewed calculus video",
            concept_ids=["math:derivatives"],
            editing=1,
            narration_pacing=1,
            narration_clarity=1,
            narration_sync=1,
            sound=1,
            visual_clarity=1,
        )
        after = self.knowledge._rank_rules(
            {"math:derivatives": 1.0}, "concept"
        )
        self.assertNotEqual(
            next(item["priority"] for item in before if item["area"] == "narration"),
            next(item["priority"] for item in after if item["area"] == "narration"),
        )
        with self.assertRaisesRegex(DataValidationError, "500 characters"):
            self.knowledge.record_review(
                video_title="x",
                concept_ids=["math:graphs"],
                editing=3,
                narration_pacing=3,
                narration_clarity=3,
                narration_sync=3,
                sound=3,
                visual_clarity=3,
                notes="x" * 501,
            )

    def test_rejects_malformed_matrix_and_unknown_question(self) -> None:
        bad = {"concepts": self.matrix["concepts"], "concept_uses_math_matrix": {
            "row_labels": ["physics:kinematics"],
            "column_labels": ["math:derivatives"],
            "values": [],
        }}
        with self.assertRaisesRegex(DataValidationError, "malformed concept_uses_math_matrix"):
            _validate_matrix(bad)
        with self.assertRaisesRegex(DataValidationError, "unknown matrix question ID"):
            _episode_concepts(
                {"id": "episode-1", "question_id": "missing"},
                self.matrix,
                {item["concept_id"]: item for item in self.matrix["concepts"]},
                self._graph(),
            )

    @staticmethod
    def _graph():
        from exam_engine.engine import load_topics
        from knowledge.graph import load_graph

        topics = load_topics(ROOT / "data" / "physics_topics.csv")
        return load_graph(
            ROOT / "knowledge" / "concepts.csv",
            ROOT / "knowledge" / "links.csv",
            topics,
        )


if __name__ == "__main__":
    unittest.main()
