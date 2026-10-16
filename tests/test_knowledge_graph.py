from __future__ import annotations

from pathlib import Path
import tempfile
import unittest

from exam_engine.engine import DataValidationError, load_topics
from knowledge.graph import load_graph


ROOT = Path(__file__).parents[1]
TOPICS = load_topics(ROOT / "data" / "physics_topics.csv")


class KnowledgeGraphTests(unittest.TestCase):
    def test_catalog_maps_every_physics_topic_and_math_bridge(self) -> None:
        graph = load_graph(
            ROOT / "knowledge" / "concepts.csv",
            ROOT / "knowledge" / "links.csv",
            TOPICS,
        )
        by_id = graph.by_id()
        for topic in TOPICS:
            physics, mathematics, prerequisites = graph.for_topic(topic.topic_id)
            self.assertEqual(physics.topic_id, topic.topic_id)
            self.assertTrue(mathematics)
            self.assertNotIn(physics.concept_id, {item.concept_id for item in prerequisites})
            self.assertTrue(all(by_id[item.concept_id].domain == "mathematics" for item in mathematics))

    def test_unknown_link_target_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            links_path = Path(directory) / "links.csv"
            links_path.write_text(
                "source_id,target_id,relation\n"
                "physics:kinematics,math:not-real,uses_math\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(DataValidationError, "unknown concept"):
                load_graph(
                    ROOT / "knowledge" / "concepts.csv",
                    links_path,
                    TOPICS,
                )

    def test_prerequisite_cycle_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            concepts_path = Path(directory) / "concepts.csv"
            links_path = Path(directory) / "links.csv"
            concepts_path.write_text(
                "concept_id,concept_name,domain,topic_id,summary,reference\n"
                "physics:units_measurement,Measurement,physics,units_measurement,Units,source\n"
                "physics:kinematics,Kinematics,physics,kinematics,Motion,source\n",
                encoding="utf-8",
            )
            links_path.write_text(
                "source_id,target_id,relation\n"
                "physics:units_measurement,physics:kinematics,requires\n"
                "physics:kinematics,physics:units_measurement,requires\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(DataValidationError, "contains a cycle"):
                load_graph(concepts_path, links_path, TOPICS[:2])

    def test_graph_accepts_future_domains_and_general_math_links(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            concepts_path = Path(directory) / "concepts.csv"
            links_path = Path(directory) / "links.csv"
            concepts = (ROOT / "knowledge" / "concepts.csv").read_text(
                encoding="utf-8"
            ).rstrip("\n")
            links = (ROOT / "knowledge" / "links.csv").read_text(
                encoding="utf-8"
            ).rstrip("\n")
            concepts_path.write_text(
                concepts + "\n"
                + "cs:algorithms,Algorithms,computer_science,,Reason about procedures,project\n",
                encoding="utf-8",
            )
            links_path.write_text(
                links + "\n" + "cs:algorithms,math:graphs,uses_math\n",
                encoding="utf-8",
            )
            graph = load_graph(concepts_path, links_path, TOPICS)
            self.assertEqual(graph.by_id()["cs:algorithms"].domain, "computer_science")
