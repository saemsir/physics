from __future__ import annotations

import csv
from pathlib import Path
import tempfile
import unittest

from exam_engine.engine import (
    DataValidationError,
    REQUIRED_RECORD_FIELDS,
    Topic,
    forecast_test,
    load_backtest,
    load_recommendations,
    load_topics,
    render_test_forecast,
    render_video_batch,
)


TOPICS = (
    Topic("kinematics", "Kinematics", "Mechanics", "Explain motion graphs.", "What does slope mean?"),
    Topic("optics", "Optics", "Optics", "Trace image formation.", "Where is the image?"),
)
VIDEO_TOPICS = load_topics(
    Path(__file__).parents[1] / "data" / "physics_topics.csv"
)


def record(
    question_id: str,
    year: int,
    paper: str,
    topic: str,
    *,
    review_status: str = "verified",
) -> dict[str, str]:
    return {
        "question_id": question_id,
        "exam": "jee-main",
        "exam_name": "JEE Main",
        "year": str(year),
        "session": "January",
        "paper_id": paper,
        "subject": "Physics",
        "topic_id": topic,
        "source_name": "Official archive",
        "source_url": "https://example.org/paper",
        "source_type": "official",
        "rights_status": "metadata-only",
        "rights_reference": "",
        "question_locator": f"Q{question_id}",
        "question_format": "single-correct",
        "difficulty": "medium",
        "marks": "4",
        "answer_verified": "false",
        "review_status": review_status,
        "reviewer": "Reviewer",
        "reviewed_at": "2026-01-01",
        "notes": "",
    }


class ExamEngineTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.data_path = Path(self.temp_dir.name) / "records.csv"

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def write_records(self, rows: list[dict[str, str]]) -> None:
        with self.data_path.open("w", encoding="utf-8", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=REQUIRED_RECORD_FIELDS)
            writer.writeheader()
            writer.writerows(rows)

    def test_empty_dataset_returns_explicit_uniform_baseline(self) -> None:
        self.write_records([])
        results = load_recommendations(
            self.data_path, VIDEO_TOPICS, exam="jee-main", as_of_year=2026
        )
        self.assertTrue(
            all(result.basis == "uniform-curriculum-baseline" for result in results)
        )
        self.assertAlmostEqual(sum(result.historical_share for result in results), 1)
        output = render_video_batch(results, exam="jee-main", as_of_year=2026)
        self.assertIn("uniform curriculum-baseline topic list", output)
        self.assertEqual(output.count("### H"), 10)
        self.assertEqual(output.count("### V"), 10)

    def test_topic_catalog_must_support_ten_unique_video_topics(self) -> None:
        small_catalog = Path(self.temp_dir.name) / "topics.csv"
        with small_catalog.open("w", encoding="utf-8", newline="") as stream:
            writer = csv.writer(stream)
            writer.writerow(("topic_id", "topic_name", "unit", "horizontal_angle", "vertical_hook"))
            for topic in TOPICS:
                writer.writerow(
                    (
                        topic.topic_id,
                        topic.topic_name,
                        topic.unit,
                        topic.horizontal_angle,
                        topic.vertical_hook,
                    )
                )
        with self.assertRaisesRegex(DataValidationError, "at least 10 topics"):
            load_topics(small_catalog)

    def test_paper_normalization_and_recency_weighting(self) -> None:
        self.write_records(
            [
                record("1", 2026, "recent", "kinematics"),
                record("2", 2026, "recent", "kinematics"),
                record("3", 2026, "recent", "kinematics"),
                record("4", 2026, "recent", "optics"),
                record("5", 2000, "old", "optics"),
                record("6", 2000, "old", "optics"),
                record("7", 2000, "old", "optics"),
                record("8", 2000, "old", "kinematics"),
            ]
        )
        results = load_recommendations(
            self.data_path, TOPICS, exam="jee-main", as_of_year=2026
        )
        by_topic = {result.topic.topic_id: result for result in results}
        self.assertGreater(
            by_topic["kinematics"].historical_share,
            by_topic["optics"].historical_share,
        )
        self.assertAlmostEqual(sum(item.historical_share for item in results), 1)
        self.assertEqual(by_topic["kinematics"].total_papers, 2)
        self.assertEqual(by_topic["kinematics"].supported_papers, 2)

    def test_pending_rows_do_not_influence_recommendations(self) -> None:
        self.write_records(
            [
                record("1", 2026, "verified", "kinematics"),
                record("2", 2026, "pending", "optics", review_status="pending"),
            ]
        )
        results = load_recommendations(
            self.data_path, TOPICS, exam="jee-main", as_of_year=2026
        )
        by_topic = {result.topic.topic_id: result for result in results}
        self.assertEqual(by_topic["optics"].question_records, 0)
        self.assertEqual(by_topic["kinematics"].question_records, 1)

    def test_out_of_window_records_are_excluded(self) -> None:
        self.write_records([record("1", 1996, "old", "optics")])
        results = load_recommendations(
            self.data_path, TOPICS, exam="jee-main", as_of_year=2026
        )
        self.assertTrue(
            all(result.basis == "uniform-curriculum-baseline" for result in results)
        )

    def test_unknown_topic_is_rejected_instead_of_silently_skipped(self) -> None:
        self.write_records([record("1", 2026, "paper", "invented-topic")])
        with self.assertRaisesRegex(DataValidationError, "unknown topic_id"):
            load_recommendations(
                self.data_path, TOPICS, exam="jee-main", as_of_year=2026
            )

    def test_open_license_requires_rights_reference(self) -> None:
        row = record("1", 2026, "paper", "kinematics")
        row["rights_status"] = "open-license"
        self.write_records([row])
        with self.assertRaisesRegex(DataValidationError, "requires rights_reference"):
            load_recommendations(
                self.data_path, TOPICS, exam="jee-main", as_of_year=2026
            )

    def test_backtest_uses_later_year_as_held_out_data(self) -> None:
        self.write_records(
            [
                record("1", 2025, "prior", "kinematics"),
                record("2", 2025, "prior", "kinematics"),
                record("3", 2025, "prior", "optics"),
                record("4", 2026, "held-out-a", "kinematics"),
                record("5", 2026, "held-out-a", "kinematics"),
                record("6", 2026, "held-out-b", "optics"),
            ]
        )
        result = load_backtest(
            self.data_path, VIDEO_TOPICS, exam="jee-main", as_of_year=2026
        )
        self.assertEqual(result.years_evaluated, (2026,))
        self.assertEqual(result.papers_evaluated, 2)
        self.assertGreaterEqual(result.model_brier_score, 0)
        self.assertGreaterEqual(result.uniform_brier_score, 0)
        self.assertAlmostEqual(result.mean_top_ten_coverage, 1)

    def test_backtest_requires_an_earlier_training_year(self) -> None:
        self.write_records([record("1", 2026, "single-year", "kinematics")])
        with self.assertRaisesRegex(DataValidationError, "not enough verified"):
            load_backtest(
                self.data_path, VIDEO_TOPICS, exam="jee-main", as_of_year=2026
            )

    def test_forecast_is_seeded_and_uses_verified_target_exam_records(self) -> None:
        rows = [
            record("1", 2024, "paper-a", "kinematics"),
            record("2", 2024, "paper-a", "kinematics"),
            record("3", 2025, "paper-b", "kinematics"),
            record("4", 2025, "paper-b", "optics", review_status="pending"),
            record("6", 2000, "historic-paper", "optics"),
        ]
        for row in rows:
            row["exam"] = "jee-advanced"
        unrelated_exam = record("5", 2025, "main-paper", "optics")
        self.write_records(rows + [unrelated_exam])

        forecast = forecast_test(
            self.data_path,
            VIDEO_TOPICS,
            target_year=2026,
            question_count=8,
            simulations=2_000,
            seed=17,
        )
        repeated = forecast_test(
            self.data_path,
            VIDEO_TOPICS,
            target_year=2026,
            question_count=8,
            simulations=2_000,
            seed=17,
        )
        self.assertEqual(forecast.sampled_topic_ids, repeated.sampled_topic_ids)
        self.assertEqual(
            forecast.topic_appearance_probabilities,
            repeated.topic_appearance_probabilities,
        )
        self.assertEqual(forecast.status, "historical-data-informed")
        self.assertEqual(forecast.verified_question_records, 4)
        self.assertEqual(forecast.verified_papers, 3)
        self.assertEqual((forecast.first_verified_year, forecast.last_verified_year), (2000, 2025))
        self.assertEqual(len(forecast.sampled_topic_ids), 8)
        forecast_by_topic = {
            item.topic.topic_id: item.historical_share
            for item in forecast.topic_shares
        }
        self.assertGreater(
            forecast_by_topic["kinematics"],
            forecast_by_topic["optics"],
        )
        appearance_by_topic = dict(forecast.topic_appearance_probabilities)
        self.assertGreater(
            appearance_by_topic["kinematics"],
            appearance_by_topic["optics"],
        )
        self.assertTrue(
            all(0 <= probability <= 1 for probability in appearance_by_topic.values())
        )
        self.assertEqual(
            render_test_forecast(forecast)["scope"],
            "Physics topic blueprint only; not an exact-question or full-exam prediction",
        )

    def test_empty_history_is_explicitly_labeled_prior_only(self) -> None:
        self.write_records([])
        forecast = forecast_test(
            self.data_path,
            VIDEO_TOPICS,
            target_year=2026,
            question_count=3,
            simulations=100,
        )
        self.assertEqual(forecast.status, "prior-only-no-verified-exam-records")
        self.assertEqual(forecast.verified_papers, 0)
        self.assertAlmostEqual(
            sum(item.historical_share for item in forecast.topic_shares),
            1.0,
        )
        report = render_test_forecast(forecast)
        self.assertIn("uniform prior", " ".join(report["limitations"]))

    def test_forecast_accepts_future_target_year_without_future_records(self) -> None:
        advanced_record = record("1", 2025, "paper-a", "kinematics")
        advanced_record["exam"] = "jee-advanced"
        self.write_records([advanced_record])
        forecast = forecast_test(
            self.data_path,
            VIDEO_TOPICS,
            target_year=2027,
            question_count=3,
            simulations=100,
        )
        self.assertEqual(forecast.target_year, 2027)
        self.assertEqual(forecast.status, "historical-data-informed")
        self.assertEqual(forecast.last_verified_year, 2025)

    def test_forecast_rejects_invalid_simulation_parameters(self) -> None:
        self.write_records([])
        with self.assertRaisesRegex(DataValidationError, "question_count"):
            forecast_test(self.data_path, VIDEO_TOPICS, question_count=0)
        with self.assertRaisesRegex(DataValidationError, "simulations"):
            forecast_test(self.data_path, VIDEO_TOPICS, simulations=99)


if __name__ == "__main__":
    unittest.main()
