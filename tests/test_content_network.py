from __future__ import annotations

import csv
from pathlib import Path
import sqlite3
import tempfile
import unittest

from content_engine.database import ContentDatabase, ROOT
from content_engine.lesson import compile_lesson, persist_lesson
from content_engine.problem import load_problem, record_problem_run, solve_problem
from exam_engine.engine import DataValidationError
from exam_engine.engine import load_recommendations, load_topics


class ContentDatabaseTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.database = ContentDatabase(
            Path(self.temporary_directory.name) / "content.sqlite"
        )
        self.database.initialize(ROOT)

    def test_initialization_indexes_papers_without_inventing_questions(self) -> None:
        summary = self.database.summary()
        self.assertEqual(summary["schema_version"], 3)
        self.assertEqual(summary["papers"], 9)
        self.assertEqual(summary["concept_sources"], 7)
        self.assertEqual(summary["questions"], 0)
        self.assertEqual(summary["question_concepts"], 0)
        papers = {row["paper_id"]: row for row in self.database.list_papers()}
        self.assertEqual(
            papers["iitjee-2007-1"]["extraction_status"], "invalid-file"
        )
        self.assertEqual(papers["iitjee-2008-1"]["rights_status"], "unknown")

    def test_reinitialization_refreshes_canonical_data_safely(self) -> None:
        first = self.database.summary()
        self.database.initialize(ROOT)
        self.assertEqual(self.database.summary(), first)

    def test_v1_database_migrates_domain_check_without_breaking_foreign_keys(self) -> None:
        legacy_path = Path(self.temporary_directory.name) / "legacy.sqlite"
        connection = sqlite3.connect(legacy_path)
        try:
            connection.executescript(
                """CREATE TABLE schema_migrations (
                       version INTEGER PRIMARY KEY, applied_at TEXT NOT NULL
                   );
                   INSERT INTO schema_migrations VALUES (1, 'legacy');
                   CREATE TABLE lessons (lesson_id TEXT PRIMARY KEY);
                   CREATE TABLE concepts (
                       concept_id TEXT PRIMARY KEY,
                       concept_name TEXT NOT NULL,
                       domain TEXT NOT NULL CHECK (
                           domain IN ('mathematics', 'physics')
                       ),
                       topic_id TEXT UNIQUE,
                       summary TEXT NOT NULL,
                       reference TEXT NOT NULL
                   );
                   CREATE TABLE legacy_concept_refs (
                       concept_id TEXT REFERENCES concepts(concept_id)
                   );
                   INSERT INTO concepts VALUES (
                       'legacy:concept', 'Legacy concept', 'physics', NULL, 'Retained',
                       'legacy:test'
                   );
                   INSERT INTO legacy_concept_refs VALUES ('legacy:concept');"""
            )
        finally:
            connection.close()

        migrated = ContentDatabase(legacy_path)
        migrated.initialize(ROOT)
        connection = migrated.connect()
        try:
            self.assertEqual(
                connection.execute(
                    "SELECT domain FROM concepts WHERE concept_id = ?",
                    ("cs:procedural_abstraction",),
                ).fetchone()["domain"],
                "computer_science",
            )
            self.assertEqual(
                connection.execute("SELECT COUNT(*) FROM legacy_concept_refs").fetchone()[0],
                1,
            )
            self.assertIn(
                "release_status",
                {row["name"] for row in connection.execute("PRAGMA table_info(lessons)")},
            )
            self.assertEqual(connection.execute("PRAGMA foreign_key_check").fetchall(), [])
            self.assertEqual(migrated.summary()["schema_version"], 3)
        finally:
            connection.close()

    def test_topic_map_resolves_physics_to_math_concepts(self) -> None:
        topic, links = self.database.topic_map("kinematics")
        self.assertEqual(topic["concept_id"], "physics:kinematics")
        self.assertIn("math:derivatives", {link["concept_id"] for link in links})

    def test_computation_book_references_are_linked_with_review_status(self) -> None:
        references = self.database.topic_references("laws_of_motion")
        strang = next(
            item for item in references
            if item["source_id"] == "strang-18-085-fall-2008"
        )
        self.assertEqual(strang["rights_status"], "unknown")
        self.assertEqual(strang["review_status"], "needs-review")
        self.assertIn("Chapter 1", strang["source_locator"])
        connection = self.database.connect()
        try:
            candidates = connection.execute(
                """SELECT c.concept_id, s.source_id, cs.review_status
                   FROM concept_sources cs
                   JOIN concepts c USING (concept_id)
                   JOIN sources s USING (source_id)
                   WHERE c.domain = 'computer_science'"""
            ).fetchall()
            self.assertEqual(len(candidates), 2)
            self.assertEqual(
                {row["source_id"] for row in candidates},
                {"sussman-sicp", "feynman-lectures-computation"},
            )
            self.assertTrue(
                all(row["review_status"] == "needs-review" for row in candidates)
            )
        finally:
            connection.close()

    def test_unreviewed_paper_is_explicitly_empty_of_curated_questions(self) -> None:
        paper, questions = self.database.map_paper("iitjee-2008-1")
        self.assertEqual(paper["review_status"], "needs-source-review")
        self.assertEqual(questions, [])

    def test_question_concept_edges_link_to_the_existing_graph(self) -> None:
        connection = self.database.connect()
        try:
            with connection:
                connection.execute(
                    """INSERT INTO questions
                       (question_id, paper_id, source_id, question_locator,
                        question_format, topic_id, review_status)
                       VALUES (?, ?, ?, ?, ?, ?, ?)""",
                    (
                        "fixture-question", "iitjee-2008-1", "iitjee-2008-paper-1",
                        "Section I, Q1", "single-correct", "kinematics", "needs-review",
                    ),
                )
                connection.execute(
                    """INSERT INTO question_concepts
                       (question_id, concept_id, relation, confidence, review_status)
                       VALUES (?, ?, ?, ?, ?)""",
                    (
                        "fixture-question", "math:derivatives", "uses", 0.9, "needs-review",
                    ),
                )
            paper, questions = self.database.map_paper("iitjee-2008-1")
            self.assertEqual(paper["paper_id"], "iitjee-2008-1")
            self.assertEqual(questions[0]["concept_id"], "math:derivatives")
            self.assertEqual(questions[0]["link_review_status"], "needs-review")
        finally:
            connection.close()

    def test_verified_question_requires_a_source_url(self) -> None:
        connection = self.database.connect()
        try:
            with self.assertRaisesRegex(sqlite3.IntegrityError, "traceable HTTP"):
                with connection:
                    connection.execute(
                        """INSERT INTO questions
                           (question_id, paper_id, source_id, question_locator,
                            question_format, topic_id, review_status)
                           VALUES (?, ?, ?, ?, ?, ?, ?)""",
                        (
                            "unverifiable-question", "iitjee-2008-1",
                            "iitjee-2008-paper-1", "Q1", "single-correct",
                            "kinematics", "verified",
                        ),
                    )
        finally:
            connection.close()

    def test_verified_records_export_into_the_recommendation_engine(self) -> None:
        connection = self.database.connect()
        try:
            with connection:
                connection.execute(
                    """UPDATE sources SET source_url = ?, rights_status = ?
                       WHERE source_id = ?""",
                    (
                        "https://example.test/paper", "metadata-only",
                        "project-original",
                    ),
                )
                connection.execute(
                    """INSERT INTO papers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    (
                        "fixture-jee-main-paper", "jee-main", "JEE Main", 2026,
                        "January", "Test paper", "physics", "project-original",
                        "verified", "Synthetic integration-test paper.",
                    ),
                )
                connection.execute(
                    """INSERT INTO questions
                       (question_id, paper_id, source_id, question_locator,
                        question_format, topic_id, review_status, answer_verified,
                        reviewer, reviewed_at)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    (
                        "fixture-jee-main-question", "fixture-jee-main-paper",
                        "project-original", "Q1", "single-correct", "kinematics",
                        "verified", 1, "test-reviewer", "2026-10-16",
                    ),
                )
            output = Path(self.temporary_directory.name) / "exam-rows.csv"
            self.assertEqual(self.database.export_exam_metadata(output), 1)
            with output.open("r", encoding="utf-8", newline="") as stream:
                rows = list(csv.DictReader(stream))
            self.assertEqual(rows[0]["question_id"], "fixture-jee-main-question")
            rankings = load_recommendations(
                output,
                load_topics(ROOT / "data" / "physics_topics.csv"),
                exam="jee-main",
                as_of_year=2026,
            )
            kinematics = next(item for item in rankings if item.topic.topic_id == "kinematics")
            self.assertEqual(kinematics.question_records, 1)
            self.assertEqual(kinematics.basis, "recency-weighted-historical-paper-mix")
        finally:
            connection.close()


class ProblemToLessonTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.database = ContentDatabase(
            Path(self.temporary_directory.name) / "content.sqlite"
        )
        self.database.initialize(ROOT)
        self.problem = load_problem(ROOT / "data" / "kinematics_demo.json")

    def test_problem_uses_physics_solver_and_independent_check(self) -> None:
        result = solve_problem(self.problem)
        self.assertEqual(result.position_m, (20.0, 32.0))
        self.assertEqual(result.velocity_m_per_s, (5.0, 4.0))
        self.assertEqual(result.computation_status, "passed")
        self.assertEqual(result.physics_review_status, "pending-human-review")
        self.assertTrue(all(check["passed"] for check in result.checks))

    def test_wrong_reference_answer_fails_without_auto_approval(self) -> None:
        problem = {
            **self.problem,
            "expected_outputs": {"position_m": [20.0, 33.0]},
        }
        result = solve_problem(problem)
        self.assertEqual(result.computation_status, "failed")
        self.assertEqual(result.physics_review_status, "pending-human-review")

    def test_unknown_model_and_missing_assumptions_are_rejected(self) -> None:
        with self.assertRaisesRegex(DataValidationError, "unsupported model_type"):
            solve_problem({**self.problem, "model_type": "free-form-language-model"})
        with self.assertRaisesRegex(DataValidationError, "assumptions"):
            solve_problem({**self.problem, "assumptions": []})

    def test_compile_persists_concept_links_checks_and_visual_samples(self) -> None:
        result = solve_problem(self.problem)
        connection = self.database.connect()
        try:
            with connection:
                run_id = record_problem_run(connection, self.problem, result)
                ir = compile_lesson(connection, self.problem, result.to_dict())
                persist_lesson(connection, ir)
            self.assertTrue(run_id)
            self.assertEqual(ir["ir_version"], 1)
            self.assertEqual(ir["approvals"]["physics"], "pending")
            self.assertEqual(ir["approvals"]["release"], "pending")
            self.assertIn(
                "math:derivatives", {concept["concept_id"] for concept in ir["concepts"]}
            )
            motion_scene = next(
                scene for scene in ir["scenes"]
                if scene["scene_id"] == "motion-solution"
            )
            trajectory = motion_scene["visual_spec"]["trajectory"]
            self.assertEqual(len(trajectory["time_s"]), 31)
            self.assertEqual(tuple(trajectory["position_m"][-1]), (20.0, 32.0))
            stored_scenes = connection.execute(
                "SELECT COUNT(*) FROM lesson_scenes WHERE lesson_id = ?",
                (ir["lesson_id"],),
            ).fetchone()[0]
            self.assertEqual(stored_scenes, 2)
            stored_release_gate = connection.execute(
                "SELECT release_status FROM lessons WHERE lesson_id = ?",
                (ir["lesson_id"],),
            ).fetchone()[0]
            self.assertEqual(stored_release_gate, "pending")
            stored_run = connection.execute(
                "SELECT check_status FROM engine_runs WHERE run_id = ?", (run_id,)
            ).fetchone()[0]
            self.assertEqual(stored_run, "passed")
            self.assertEqual(ir["claims"][0]["rights_status"], "project-original")
            self.assertIn(
                "original illustrative example",
                ir["claims"][0]["source_citation"].lower(),
            )
        finally:
            connection.close()


if __name__ == "__main__":
    unittest.main()
