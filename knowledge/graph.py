"""Validated concept graph for curriculum, question metadata, and math links."""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path

from exam_engine.engine import DataValidationError, Topic

CONCEPT_FIELDS = (
    "concept_id",
    "concept_name",
    "domain",
    "topic_id",
    "summary",
    "reference",
)
LINK_FIELDS = ("source_id", "target_id", "relation")
RELATIONS = {"requires", "uses_math"}


@dataclass(frozen=True)
class Concept:
    concept_id: str
    concept_name: str
    domain: str
    topic_id: str
    summary: str
    reference: str


@dataclass(frozen=True)
class ConceptLink:
    source_id: str
    target_id: str
    relation: str


@dataclass(frozen=True)
class ConceptGraph:
    concepts: tuple[Concept, ...]
    links: tuple[ConceptLink, ...]

    def by_id(self) -> dict[str, Concept]:
        return {concept.concept_id: concept for concept in self.concepts}

    def for_topic(self, topic_id: str) -> tuple[Concept, tuple[Concept, ...], tuple[Concept, ...]]:
        physics_id = f"physics:{topic_id}"
        concepts = self.by_id()
        physics = concepts.get(physics_id)
        if physics is None:
            raise DataValidationError(f"no concept mapping for topic_id {topic_id!r}")
        math_ids = {
            link.target_id
            for link in self.links
            if link.source_id == physics_id and link.relation == "uses_math"
        }
        prerequisite_ids = {
            link.target_id
            for link in self.links
            if link.source_id == physics_id and link.relation == "requires"
        }
        return (
            physics,
            tuple(concepts[concept_id] for concept_id in sorted(math_ids)),
            tuple(concepts[concept_id] for concept_id in sorted(prerequisite_ids)),
        )


def _read_rows(path: Path, fields: tuple[str, ...]) -> list[dict[str, str]]:
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as stream:
            reader = csv.DictReader(stream)
            if tuple(reader.fieldnames or ()) != fields:
                raise DataValidationError(
                    f"{path}: expected columns in this order: {', '.join(fields)}"
                )
            rows = []
            for line, row in enumerate(reader, start=2):
                if None in row or any(value is None for value in row.values()):
                    raise DataValidationError(f"{path}:{line}: malformed CSV row")
                if all(not value.strip() for value in row.values()):
                    continue
                rows.append({key: value.strip() for key, value in row.items()})
            return rows
    except (OSError, UnicodeError, csv.Error) as exc:
        raise DataValidationError(f"cannot read {path}: {exc}") from exc


def _check_acyclic(concepts: dict[str, Concept], links: tuple[ConceptLink, ...]) -> None:
    dependencies: dict[str, list[str]] = {concept_id: [] for concept_id in concepts}
    for link in links:
        if link.relation == "requires":
            dependencies[link.source_id].append(link.target_id)
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(concept_id: str) -> None:
        if concept_id in visiting:
            raise DataValidationError(
                f"concept prerequisite graph contains a cycle through {concept_id!r}"
            )
        if concept_id in visited:
            return
        visiting.add(concept_id)
        for dependency in dependencies[concept_id]:
            visit(dependency)
        visiting.remove(concept_id)
        visited.add(concept_id)

    for concept_id in dependencies:
        visit(concept_id)


def load_graph(
    concepts_path: Path,
    links_path: Path,
    topics: tuple[Topic, ...],
) -> ConceptGraph:
    concept_rows = _read_rows(concepts_path, CONCEPT_FIELDS)
    concepts: list[Concept] = []
    concepts_by_id: dict[str, Concept] = {}
    physics_topic_ids: set[str] = set()
    known_topic_ids = {topic.topic_id for topic in topics}

    for line, row in enumerate(concept_rows, start=2):
        if any(not row[field] for field in CONCEPT_FIELDS if field != "topic_id"):
            raise DataValidationError(f"{concepts_path}:{line}: concept fields cannot be blank")
        if row["domain"] not in {"mathematics", "physics"}:
            raise DataValidationError(
                f"{concepts_path}:{line}: domain must be mathematics or physics"
            )
        concept = Concept(**row)
        if concept.concept_id in concepts_by_id:
            raise DataValidationError(
                f"{concepts_path}:{line}: duplicate concept_id {concept.concept_id!r}"
            )
        if concept.domain == "physics":
            if not concept.topic_id:
                raise DataValidationError(
                    f"{concepts_path}:{line}: physics concepts require a topic_id"
                )
            if concept.topic_id not in known_topic_ids:
                raise DataValidationError(
                    f"{concepts_path}:{line}: unknown physics topic_id {concept.topic_id!r}"
                )
            if concept.topic_id in physics_topic_ids:
                raise DataValidationError(
                    f"{concepts_path}:{line}: duplicate physics mapping for {concept.topic_id!r}"
                )
            physics_topic_ids.add(concept.topic_id)
        elif concept.topic_id:
            raise DataValidationError(
                f"{concepts_path}:{line}: mathematics concepts cannot own an exam topic_id"
            )
        concepts.append(concept)
        concepts_by_id[concept.concept_id] = concept

    missing_topics = known_topic_ids - physics_topic_ids
    if missing_topics:
        raise DataValidationError(
            "concept graph does not map physics topics: " + ", ".join(sorted(missing_topics))
        )
    unrecognized_topics = physics_topic_ids - known_topic_ids
    if unrecognized_topics:
        raise DataValidationError(
            "concept graph contains unmapped physics topic IDs: "
            + ", ".join(sorted(unrecognized_topics))
        )

    links: list[ConceptLink] = []
    seen_links: set[tuple[str, str, str]] = set()
    for line, row in enumerate(_read_rows(links_path, LINK_FIELDS), start=2):
        if any(not value for value in row.values()):
            raise DataValidationError(f"{links_path}:{line}: link fields cannot be blank")
        link = ConceptLink(**row)
        if link.relation not in RELATIONS:
            raise DataValidationError(
                f"{links_path}:{line}: relation must be one of {', '.join(sorted(RELATIONS))}"
            )
        if link.source_id not in concepts_by_id or link.target_id not in concepts_by_id:
            raise DataValidationError(
                f"{links_path}:{line}: link references an unknown concept"
            )
        source = concepts_by_id[link.source_id]
        target = concepts_by_id[link.target_id]
        if link.relation == "uses_math" and (
            source.domain != "physics" or target.domain != "mathematics"
        ):
            raise DataValidationError(
                f"{links_path}:{line}: uses_math must link physics to mathematics"
            )
        key = (link.source_id, link.target_id, link.relation)
        if key in seen_links:
            raise DataValidationError(f"{links_path}:{line}: duplicate concept link")
        seen_links.add(key)
        links.append(link)

    graph = ConceptGraph(tuple(concepts), tuple(links))
    math_concepts = {
        concept.concept_id for concept in graph.concepts if concept.domain == "mathematics"
    }
    linked_math = {
        link.target_id for link in graph.links if link.relation == "uses_math"
    }
    unlinked_math = math_concepts - linked_math
    if unlinked_math:
        raise DataValidationError(
            "mathematics concepts are not connected to physics: "
            + ", ".join(sorted(unlinked_math))
        )
    _check_acyclic(concepts_by_id, graph.links)
    return graph
