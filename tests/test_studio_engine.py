from __future__ import annotations

import json
from pathlib import Path
import struct
import tempfile
import unittest
import wave

from studio_engine.engine import StudioEngine, StudioRequestError, validate_request


class StudioRequestTests(unittest.TestCase):
    def test_rejects_unknown_actions_and_dependency_cycles(self) -> None:
        with self.assertRaisesRegex(StudioRequestError, "unsupported action"):
            validate_request(
                {
                    "schema_version": 1,
                    "tasks": [{"id": "bad", "action": "audio.generate"}],
                }
            )
        with self.assertRaisesRegex(StudioRequestError, "unknown parameter"):
            validate_request(
                {
                    "schema_version": 1,
                    "tasks": [
                        {
                            "id": "bad-param",
                            "action": "math.solve_linear",
                            "params": {"matrix": [[1]], "rhs": [1], "typo": True},
                        }
                    ],
                }
            )
        with self.assertRaisesRegex(StudioRequestError, "cycle"):
            validate_request(
                {
                    "schema_version": 1,
                    "tasks": [
                        {"id": "first", "action": "content.summary", "depends_on": ["second"]},
                        {"id": "second", "action": "content.summary", "depends_on": ["first"]},
                    ],
                }
            )

    def test_requires_dependencies_before_references(self) -> None:
        with self.assertRaisesRegex(StudioRequestError, "must appear earlier"):
            validate_request(
                {
                    "schema_version": 1,
                    "tasks": [
                        {
                            "id": "later",
                            "action": "physics.constant_acceleration",
                            "params": {
                                "initial_position_m": {"$ref": "earlier#/solution"},
                                "initial_velocity_m_per_s": [0],
                                "acceleration_m_per_s2": [0],
                                "time_s": 1,
                            },
                        },
                        {
                            "id": "earlier",
                            "action": "math.solve_linear",
                            "params": {"matrix": [[1]], "rhs": [1]},
                        },
                    ],
                }
            )


class StudioEngineTests(unittest.TestCase):
    def test_audio_measurement_and_human_production_review_actions(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            wav_path = root / "voice.wav"
            with wave.open(str(wav_path), "wb") as wav:
                wav.setnchannels(1)
                wav.setsampwidth(2)
                wav.setframerate(8000)
                wav.writeframes(struct.pack("<hh", 100, -100))
            request = {
                "schema_version": 1,
                "run_id": "audio-production",
                "tasks": [
                    {
                        "id": "audio",
                        "action": "audio.analyze_reference",
                        "params": {"wav": "voice.wav"},
                    },
                    {
                        "id": "review",
                        "action": "production.record_review",
                        "params": {
                            "video_title": "Reviewed lesson",
                            "concept_ids": ["physics:kinematics"],
                            "editing": 4,
                            "narration_pacing": 4,
                            "narration_clarity": 5,
                            "narration_sync": 4,
                            "sound": 3,
                            "visual_clarity": 5,
                        },
                    },
                ],
            }
            output = root / "run"
            report = StudioEngine(root).run(request, output_override=output)
            self.assertEqual(report["status"], "succeeded")
            audio = json.loads((output / "audio.json").read_text(encoding="utf-8"))
            review = json.loads((output / "review.json").read_text(encoding="utf-8"))
            self.assertEqual(audio["encoding"], "PCM")
            self.assertEqual(audio["channels"], 1)
            self.assertEqual(review["status"], "recorded")

    def test_reference_driven_tasks_write_portable_run_artifacts(self) -> None:
        request = {
            "schema_version": 1,
            "run_id": "deterministic-example",
            "tasks": [
                {
                    "id": "solve",
                    "action": "math.solve_linear",
                    "params": {"matrix": [[2, 1], [1, 3]], "rhs": [5, 7]},
                },
                {
                    "id": "motion",
                    "action": "physics.constant_acceleration",
                    "params": {
                        "initial_position_m": {"$ref": "solve#/solution"},
                        "initial_velocity_m_per_s": [0, 0],
                        "acceleration_m_per_s2": [1, -1],
                        "time_s": 2,
                    },
                },
            ],
        }
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            report = StudioEngine().run(request, output_override=output)
            self.assertEqual(report["status"], "succeeded")
            self.assertEqual(report["task_counts"]["succeeded"], 2)
            self.assertTrue((output / "solve.json").is_file())
            self.assertTrue((output / "motion.json").is_file())
            self.assertTrue((output / "run.json").is_file())
            motion = json.loads((output / "motion.json").read_text(encoding="utf-8"))
            self.assertAlmostEqual(motion["position_m"][0], 3.6)
            self.assertAlmostEqual(motion["position_m"][1], -0.2)

    def test_failed_task_blocks_dependents_but_runs_independent_tasks(self) -> None:
        request = {
            "schema_version": 1,
            "run_id": "failure-propagation",
            "tasks": [
                {
                    "id": "bad-math",
                    "action": "math.solve_linear",
                    "params": {"matrix": [[1, 2]], "rhs": [3]},
                },
                {
                    "id": "dependent",
                    "action": "physics.constant_acceleration",
                    "depends_on": ["bad-math"],
                    "params": {
                        "initial_position_m": [0],
                        "initial_velocity_m_per_s": [0],
                        "acceleration_m_per_s2": [0],
                        "time_s": 1,
                    },
                },
                {
                    "id": "independent",
                    "action": "physics.constant_acceleration",
                    "params": {
                        "initial_position_m": [0],
                        "initial_velocity_m_per_s": [1],
                        "acceleration_m_per_s2": [0],
                        "time_s": 2,
                    },
                },
            ],
        }
        with tempfile.TemporaryDirectory() as directory:
            report = StudioEngine().run(request, output_override=Path(directory))
        statuses = {task["id"]: task["status"] for task in report["tasks"]}
        self.assertEqual(statuses, {
            "bad-math": "failed",
            "dependent": "blocked",
            "independent": "succeeded",
        })
        self.assertEqual(report["status"], "partial")


if __name__ == "__main__":
    unittest.main()
