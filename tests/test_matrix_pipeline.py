from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest
from zipfile import ZIP_DEFLATED, ZipFile

from matrix_pipeline import analyze_question, build_network, main, _load_solution_routes
from exam_engine.engine import load_topics
from knowledge.graph import load_graph


ROOT = Path(__file__).parents[1]


def load_concept_graph():
    return load_graph(
        ROOT / "knowledge" / "concepts.csv",
        ROOT / "knowledge" / "links.csv",
        load_topics(ROOT / "data" / "physics_topics.csv"),
    )


class MatrixPipelineTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.papers = self.root / "exam_papers"
        self.books = self.root / "books"
        self.papers.mkdir()
        self.books.mkdir()

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_builds_question_book_concept_and_engine_matrices(self) -> None:
        (self.papers / "paper.md").write_text(
            "Question 1. A projectile has initial velocity, acceleration, and vector components.\n"
            "Q2: Solve the matrix linear system for the circuit current.\n",
            encoding="utf-8",
        )
        (self.books / "notes.txt").write_text(
            "Chemical equilibrium and reaction rate depend on concentration.\n",
            encoding="utf-8",
        )
        report, unsupported = build_network(self.papers, self.books)

        self.assertEqual(unsupported, [])
        self.assertEqual(report["counts"]["questions"], 2)
        self.assertEqual(report["question_concept_matrix"]["shape"][0], 2)
        self.assertEqual(report["book_concept_matrix"]["shape"][0], 1)
        columns = report["question_concept_matrix"]["column_labels"]
        first_row = report["question_concept_matrix"]["values"][0]
        self.assertGreater(first_row[columns.index("physics:kinematics")], 0)
        self.assertGreater(first_row[columns.index("math:scalars-vectors")], 0)
        self.assertEqual(len(report["question_analyses"]), 2)
        self.assertEqual(
            report["question_analyses"][0]["analysis"]["concepts"][0]["concept_id"],
            "physics:kinematics",
        )
        self.assertEqual(
            report["question_analyses"][0]["analysis"]["solution_routes"][0]["capability_id"],
            "constant_acceleration",
        )
        linked_row = report["question_linked_concept_matrix"]["values"][1]
        self.assertGreater(linked_row[columns.index("math:matrices")], 0)
        book_columns = report["book_concept_matrix"]["column_labels"]
        book_row = report["book_concept_matrix"]["values"][0]
        self.assertGreater(book_row[book_columns.index("chemistry:equilibrium")], 0)
        self.assertFalse(report["engine_capabilities"]["chemistry_engine"]["available"])
        self.assertFalse(report["engine_capabilities"]["audio_render"]["available"])
        self.assertNotIn(
            "A projectile has initial velocity, acceleration, and vector components.",
            json.dumps(report),
        )
        self.assertGreater(
            report["concept_to_solver_matrix"]["values"][
                report["concept_to_solver_matrix"]["row_labels"].index("physics:kinematics")
            ][report["concept_to_solver_matrix"]["column_labels"].index("physics_engine")],
            0,
        )

    def test_extracts_docx_text_without_persisting_source_content(self) -> None:
        docx_path = self.books / "study.docx"
        with ZipFile(docx_path, "w", ZIP_DEFLATED) as archive:
            archive.writestr(
                "word/document.xml",
                '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
                "<w:body><w:p><w:r><w:t>Matrix transformations</w:t></w:r></w:p>"
                "</w:body></w:document>",
            )
        report, _ = build_network(self.papers, self.books)
        self.assertEqual(report["counts"]["book_files"], 1)
        self.assertNotIn("Matrix transformations", json.dumps(report))
        matrix = report["book_concept_matrix"]
        self.assertGreater(matrix["values"][0][matrix["column_labels"].index("math:matrices")], 0)

    def test_ignores_readmes_and_prefers_docx_to_same_name_markdown(self) -> None:
        (self.papers / "README.md").write_text(
            "Question 1. This setup note is not an exam question.", encoding="utf-8"
        )
        (self.books / "guide.md").write_text(
            "# Matrices\nMatrix transformations\n\n# Vectors\nVector components",
            encoding="utf-8",
        )
        with ZipFile(self.books / "guide.docx", "w", ZIP_DEFLATED) as archive:
            archive.writestr(
                "word/document.xml",
                '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
                "<w:body><w:p><w:r><w:t>Reaction rate chemical kinetics</w:t></w:r></w:p>"
                "</w:body></w:document>",
            )

        report, _ = build_network(self.papers, self.books)

        self.assertEqual(report["counts"]["questions"], 0)
        self.assertEqual(report["counts"]["book_files"], 1)
        self.assertEqual(report["counts"]["book_sections"], 1)
        matrix = report["book_concept_matrix"]
        self.assertEqual(matrix["row_labels"], ["guide-docx-s001"])
        self.assertGreater(matrix["values"][0][matrix["column_labels"].index("chemistry:kinetics")], 0)

    def test_records_invalid_docx_and_continues_with_valid_sources(self) -> None:
        (self.books / "broken.docx").write_bytes(b"no")
        (self.books / "valid.txt").write_text("Chemical equilibrium", encoding="utf-8")

        report, _ = build_network(self.papers, self.books)

        self.assertEqual(report["status"], "partial-inputs")
        self.assertEqual(report["counts"]["book_files"], 1)
        self.assertEqual(report["input_errors"][0]["path"], "book/broken.docx")

    def test_reports_unsupported_files_and_writes_output(self) -> None:
        (self.papers / "scan.pdf").write_bytes(b"not OCR'd")
        (self.books / "kinematics.txt").write_text("Kinematics and velocity", encoding="utf-8")
        output = self.root / "network.json"
        self.assertEqual(
            main(
                [
                    "--exam-papers", str(self.papers),
                    "--books", str(self.books),
                    "--output", str(output),
                ]
            ),
            0,
        )
        payload = json.loads(output.read_text(encoding="utf-8"))
        self.assertEqual(payload["counts"]["unsupported_files"], 1)
        self.assertEqual(payload["unsupported_files"], ["exam_papers/scan.pdf"])

    def test_question_ranking_explains_evidence_and_only_routes_to_typed_solver(self) -> None:
        graph = load_concept_graph()
        routes = _load_solution_routes(ROOT / "knowledge" / "solution_routes.csv", graph)

        result = analyze_question(
            "A projectile starts with initial velocity and constant acceleration. "
            "Find its position after one second.",
            graph,
            routes,
        )

        self.assertEqual(result["status"], "clear-candidate-review-required")
        self.assertEqual(result["concepts"][0]["concept_id"], "physics:kinematics")
        self.assertIn("projectile", result["concepts"][0]["matched_phrases"])
        self.assertFalse(result["scores_are_probabilities"])
        self.assertFalse(result["automatic_solution"])
        route = next(
            item
            for item in result["solution_routes"]
            if item["capability_id"] == "constant_acceleration"
        )
        self.assertEqual(route["readiness"], "typed-inputs-only")
        self.assertEqual(route["visual_status"], "available")

    def test_unmatched_question_stays_unmatched(self) -> None:
        graph = load_concept_graph()
        routes = _load_solution_routes(ROOT / "knowledge" / "solution_routes.csv", graph)

        result = analyze_question("Describe an unfamiliar abstract idea.", graph, routes)

        self.assertEqual(result["status"], "no-concept-match")
        self.assertEqual(result["concepts"], [])
        self.assertEqual(result["solution_routes"], [])

    def test_question_cli_does_not_write_question_text(self) -> None:
        output = self.root / "analysis.json"
        question = "UNIQUE-PRIVATE projectile velocity acceleration prompt"

        self.assertEqual(
            main(["--question", question, "--output", str(output)]),
            0,
        )

        report_text = output.read_text(encoding="utf-8")
        report = json.loads(report_text)
        self.assertFalse(report["question_text_included"])
        self.assertNotIn(question, report_text)
        self.assertEqual(report["question_analysis"]["status"], "clear-candidate-review-required")


if __name__ == "__main__":
    unittest.main()
