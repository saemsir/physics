"""Build and query the local SQLite knowledge network from Git-tracked sources."""

from __future__ import annotations

import csv
from datetime import datetime, timezone
import math
from pathlib import Path
import sqlite3
from typing import Iterable

from exam_engine.engine import DataValidationError, load_topics
from knowledge.graph import ConceptGraph, load_graph

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_VERSION = 3
SOURCES_FIELDS = (
    "source_id", "title", "creator", "publication", "source_kind", "source_url",
    "local_path", "rights_status", "rights_reference", "citation", "extraction_status",
)
PAPERS_FIELDS = (
    "paper_id", "exam", "exam_name", "year", "session", "paper_name", "subject",
    "source_id", "review_status", "notes",
)
QUESTIONS_FIELDS = (
    "question_id", "paper_id", "source_id", "question_locator", "question_format",
    "difficulty", "marks", "topic_id", "review_status", "answer_verified", "reviewer",
    "reviewed_at", "notes",
)
QUESTION_CONCEPT_FIELDS = (
    "question_id", "concept_id", "relation", "confidence", "review_status", "reviewer",
    "source_locator", "notes",
)
CONCEPT_SOURCE_FIELDS = (
    "concept_id", "source_id", "source_locator", "relation", "review_status",
    "reviewer", "notes",
)


def _read_csv(path: Path, fields: tuple[str, ...]) -> list[dict[str, str]]:
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as stream:
            reader = csv.DictReader(stream)
            if tuple(reader.fieldnames or ()) != fields:
                raise DataValidationError(
                    f"{path}: expected columns in this order: {', '.join(fields)}"
                )
            records: list[dict[str, str]] = []
            for line, row in enumerate(reader, start=2):
                if None in row or any(value is None for value in row.values()):
                    raise DataValidationError(f"{path}:{line}: malformed CSV row")
                if all(not value.strip() for value in row.values()):
                    continue
                records.append({key: value.strip() for key, value in row.items()})
            return records
    except (OSError, UnicodeError, csv.Error) as exc:
        raise DataValidationError(f"cannot read {path}: {exc}") from exc


class ContentDatabase:
    """A generated SQLite view of the Git-versioned CSV catalogs and paper index."""

    def __init__(self, path: Path) -> None:
        self.path = Path(path)

    def connect(self) -> sqlite3.Connection:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        connection = sqlite3.connect(self.path)
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys = ON")
        return connection

    def initialize(self, root: Path = ROOT) -> None:
        root = Path(root)
        schema_path = root / "data" / "content_schema.sql"
        schema = schema_path.read_text(encoding="utf-8")
        topics = load_topics(root / "data" / "physics_topics.csv")
        graph = load_graph(
            root / "knowledge" / "concepts.csv",
            root / "knowledge" / "links.csv",
            topics,
        )
        sources = _read_csv(root / "data" / "sources.csv", SOURCES_FIELDS)
        papers = _read_csv(root / "data" / "papers.csv", PAPERS_FIELDS)
        questions = _read_csv(root / "data" / "questions.csv", QUESTIONS_FIELDS)
        question_concepts = _read_csv(
            root / "data" / "question_concepts.csv", QUESTION_CONCEPT_FIELDS
        )
        concept_sources = _read_csv(
            root / "data" / "concept_sources.csv", CONCEPT_SOURCE_FIELDS
        )

        connection = self.connect()
        try:
            connection.executescript(schema)
            self._upgrade_schema(connection)
            connection.executescript(schema)
            with connection:
                connection.execute(
                    "INSERT OR IGNORE INTO schema_migrations(version, applied_at) "
                    "VALUES (?, ?)",
                    (SCHEMA_VERSION, datetime.now(timezone.utc).isoformat()),
                )
                self._replace_sources(connection, sources, root)
                self._replace_graph(connection, graph)
                self._replace_concept_sources(connection, concept_sources)
                self._replace_papers(connection, papers)
                self._replace_questions(connection, questions, question_concepts)
        except (sqlite3.Error, ValueError) as exc:
            raise DataValidationError(f"cannot initialize content database: {exc}") from exc
        finally:
            connection.close()

    @staticmethod
    def _upgrade_schema(connection: sqlite3.Connection) -> None:
        row = connection.execute(
            "SELECT COALESCE(MAX(version), 0) FROM schema_migrations"
        ).fetchone()
        current_version = int(row[0])
        if current_version > SCHEMA_VERSION:
            raise DataValidationError(
                f"database schema version {current_version} is newer than "
                f"supported version {SCHEMA_VERSION}"
            )
        if current_version < 2:
            connection.execute("PRAGMA foreign_keys = OFF")
            try:
                connection.execute("BEGIN IMMEDIATE")
                connection.execute("DROP VIEW IF EXISTS question_knowledge_map")
                connection.execute("DROP TABLE IF EXISTS concepts_v2")
                connection.execute(
                    """CREATE TABLE concepts_v2 (
                        concept_id TEXT PRIMARY KEY,
                        concept_name TEXT NOT NULL,
                        domain TEXT NOT NULL CHECK (domain <> ''),
                        topic_id TEXT UNIQUE,
                        summary TEXT NOT NULL,
                        reference TEXT NOT NULL
                    )"""
                )
                connection.execute(
                    """INSERT INTO concepts_v2
                       SELECT concept_id, concept_name, domain, topic_id, summary,
                              reference
                       FROM concepts"""
                )
                connection.execute("DROP TABLE concepts")
                connection.execute("ALTER TABLE concepts_v2 RENAME TO concepts")
                connection.execute(
                    "INSERT INTO schema_migrations(version, applied_at) VALUES (?, ?)",
                    (2, datetime.now(timezone.utc).isoformat()),
                )
                connection.commit()
            except sqlite3.Error:
                connection.rollback()
                raise
            finally:
                connection.execute("PRAGMA foreign_keys = ON")

            violations = connection.execute("PRAGMA foreign_key_check").fetchall()
            if violations:
                raise DataValidationError(
                    f"database migration left {len(violations)} foreign-key violation(s)"
                )

        if current_version < 3:
            lesson_columns = {
                row["name"]
                for row in connection.execute("PRAGMA table_info(lessons)")
            }
            connection.execute("BEGIN IMMEDIATE")
            try:
                if "release_status" not in lesson_columns:
                    connection.execute(
                        """ALTER TABLE lessons ADD COLUMN release_status TEXT NOT NULL
                           DEFAULT 'pending' CHECK (
                               release_status IN ('pending', 'approved', 'rejected')
                           )"""
                    )
                connection.execute(
                    "INSERT INTO schema_migrations(version, applied_at) VALUES (?, ?)",
                    (3, datetime.now(timezone.utc).isoformat()),
                )
                connection.commit()
            except sqlite3.Error:
                connection.rollback()
                raise

    @staticmethod
    def _replace_sources(
        connection: sqlite3.Connection,
        records: Iterable[dict[str, str]],
        root: Path,
    ) -> None:
        seen: set[str] = set()
        for row in records:
            source_id = row["source_id"]
            if not source_id or source_id in seen:
                raise DataValidationError(f"duplicate or blank source_id {source_id!r}")
            seen.add(source_id)
            if any(not row[field] for field in (
                "title", "creator", "publication", "source_kind", "rights_status",
                "citation", "extraction_status",
            )):
                raise DataValidationError(f"source {source_id!r} has a blank required field")
            local_path = row["local_path"]
            if local_path:
                source_path = (root / local_path).resolve()
                try:
                    source_path.relative_to(root.resolve())
                except ValueError as exc:
                    raise DataValidationError(
                        f"source {source_id!r} local_path must remain inside the repository"
                    ) from exc
                if not source_path.is_file():
                    raise DataValidationError(
                        f"source {source_id!r} points to missing file {local_path!r}"
                    )
            connection.execute(
                """INSERT INTO sources VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                   ON CONFLICT(source_id) DO UPDATE SET
                     title=excluded.title, creator=excluded.creator,
                     publication=excluded.publication, source_kind=excluded.source_kind,
                     source_url=excluded.source_url, local_path=excluded.local_path,
                     rights_status=excluded.rights_status,
                     rights_reference=excluded.rights_reference,
                     citation=excluded.citation,
                     extraction_status=excluded.extraction_status""",
                (
                    source_id, row["title"], row["creator"], row["publication"],
                    row["source_kind"], row["source_url"], local_path,
                    row["rights_status"], row["rights_reference"], row["citation"],
                    row["extraction_status"],
                ),
            )

    @staticmethod
    def _replace_graph(
        connection: sqlite3.Connection,
        graph: ConceptGraph,
    ) -> None:
        connection.execute("DELETE FROM concept_links")
        for concept in graph.concepts:
            connection.execute(
                """INSERT INTO concepts VALUES (?, ?, ?, ?, ?, ?)
                   ON CONFLICT(concept_id) DO UPDATE SET
                     concept_name=excluded.concept_name, domain=excluded.domain,
                     topic_id=excluded.topic_id, summary=excluded.summary,
                     reference=excluded.reference""",
                (
                    concept.concept_id, concept.concept_name, concept.domain,
                    concept.topic_id or None, concept.summary, concept.reference,
                ),
            )
        for link in graph.links:
            connection.execute(
                """INSERT INTO concept_links VALUES (?, ?, ?)
                   ON CONFLICT(source_id, target_id, relation) DO NOTHING""",
                (link.source_id, link.target_id, link.relation),
            )

    @staticmethod
    def _replace_concept_sources(
        connection: sqlite3.Connection,
        records: Iterable[dict[str, str]],
    ) -> None:
        seen: set[tuple[str, str, str]] = set()
        for row in records:
            if not all(row[field] for field in (
                "concept_id", "source_id", "source_locator", "relation", "review_status",
            )):
                raise DataValidationError(f"concept-source row has a blank required value: {row!r}")
            key = (row["concept_id"], row["source_id"], row["source_locator"])
            if key in seen:
                raise DataValidationError(f"duplicate concept-source link {key!r}")
            seen.add(key)
            connection.execute(
                """INSERT INTO concept_sources VALUES (?, ?, ?, ?, ?, ?, ?)
                   ON CONFLICT(concept_id, source_id, source_locator) DO UPDATE SET
                     relation=excluded.relation, review_status=excluded.review_status,
                     reviewer=excluded.reviewer, notes=excluded.notes""",
                (
                    row["concept_id"], row["source_id"], row["source_locator"],
                    row["relation"], row["review_status"], row["reviewer"], row["notes"],
                ),
            )

    @staticmethod
    def _replace_papers(
        connection: sqlite3.Connection,
        records: Iterable[dict[str, str]],
    ) -> None:
        seen: set[str] = set()
        for row in records:
            paper_id = row["paper_id"]
            if not paper_id or paper_id in seen:
                raise DataValidationError(f"duplicate or blank paper_id {paper_id!r}")
            seen.add(paper_id)
            if any(not row[field] for field in (
                "exam", "exam_name", "session", "paper_name", "subject",
                "source_id", "review_status",
            )):
                raise DataValidationError(f"paper {paper_id!r} has a blank required field")
            try:
                year = int(row["year"])
            except ValueError as exc:
                raise DataValidationError(f"paper {paper_id!r}: year must be an integer") from exc
            connection.execute(
                """INSERT INTO papers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                   ON CONFLICT(paper_id) DO UPDATE SET
                     exam=excluded.exam, exam_name=excluded.exam_name,
                     year=excluded.year, session=excluded.session,
                     paper_name=excluded.paper_name, subject=excluded.subject,
                     source_id=excluded.source_id,
                     review_status=excluded.review_status, notes=excluded.notes""",
                (
                    paper_id, row["exam"], row["exam_name"], year, row["session"],
                    row["paper_name"], row["subject"], row["source_id"],
                    row["review_status"], row["notes"],
                ),
            )

    @staticmethod
    def _replace_questions(
        connection: sqlite3.Connection,
        questions: Iterable[dict[str, str]],
        links: Iterable[dict[str, str]],
    ) -> None:
        seen_questions: set[str] = set()
        for row in questions:
            if not all(row[field] for field in (
                "question_id", "paper_id", "source_id", "question_locator",
                "question_format", "topic_id", "review_status",
            )):
                raise DataValidationError(
                    f"question row has a blank required value: {row!r}"
                )
            if row["question_id"] in seen_questions:
                raise DataValidationError(
                    f"duplicate question_id {row['question_id']!r}"
                )
            seen_questions.add(row["question_id"])
            try:
                marks = float(row["marks"]) if row["marks"] else None
                if marks is not None and (not math.isfinite(marks) or marks < 0):
                    raise ValueError
                answer_verified = int(row["answer_verified"] or "0")
                if answer_verified not in (0, 1):
                    raise ValueError
            except ValueError as exc:
                raise DataValidationError(
                    f"question {row['question_id']!r}: marks must be nonnegative "
                    "and answer_verified must be 0 or 1"
                ) from exc
            connection.execute(
                """INSERT INTO questions VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                   ON CONFLICT(question_id) DO UPDATE SET
                     paper_id=excluded.paper_id, source_id=excluded.source_id,
                     question_locator=excluded.question_locator,
                     question_format=excluded.question_format,
                     difficulty=excluded.difficulty, marks=excluded.marks,
                     topic_id=excluded.topic_id, review_status=excluded.review_status,
                     answer_verified=excluded.answer_verified, reviewer=excluded.reviewer,
                     reviewed_at=excluded.reviewed_at, notes=excluded.notes""",
                (
                    row["question_id"], row["paper_id"], row["source_id"],
                    row["question_locator"], row["question_format"], row["difficulty"],
                    marks, row["topic_id"], row["review_status"], answer_verified,
                    row["reviewer"], row["reviewed_at"], row["notes"],
                ),
            )
        seen_links: set[tuple[str, str, str]] = set()
        for row in links:
            if not all(row[field] for field in (
                "question_id", "concept_id", "relation", "confidence", "review_status",
            )):
                raise DataValidationError(
                    f"question-concept link has a blank required value: {row!r}"
                )
            key = (row["question_id"], row["concept_id"], row["relation"])
            if key in seen_links:
                raise DataValidationError(f"duplicate question-concept link {key!r}")
            seen_links.add(key)
            try:
                confidence = float(row["confidence"])
            except ValueError as exc:
                raise DataValidationError(
                    f"question-concept link confidence must be numeric: {row!r}"
                ) from exc
            if not math.isfinite(confidence) or not 0 <= confidence <= 1:
                raise DataValidationError(
                    f"question-concept link confidence must be finite and between 0 and 1: {row!r}"
                )
            connection.execute(
                """INSERT INTO question_concepts VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                   ON CONFLICT(question_id, concept_id, relation) DO UPDATE SET
                     confidence=excluded.confidence,
                     review_status=excluded.review_status,
                     reviewer=excluded.reviewer,
                     source_locator=excluded.source_locator, notes=excluded.notes""",
                (
                    row["question_id"], row["concept_id"], row["relation"], confidence,
                    row["review_status"], row["reviewer"], row["source_locator"],
                    row["notes"],
                ),
            )

    def summary(self) -> dict[str, int | str]:
        connection = self.connect()
        try:
            migration = connection.execute(
                "SELECT MAX(version) FROM schema_migrations"
            ).fetchone()[0]
            result: dict[str, int | str] = {"schema_version": migration or 0}
            for table in (
                "sources", "papers", "concepts", "concept_links", "concept_sources",
                "questions", "question_concepts",
            ):
                result[table] = connection.execute(
                    f"SELECT COUNT(*) FROM {table}"
                ).fetchone()[0]
            return result
        except sqlite3.Error as exc:
            raise DataValidationError(f"cannot read content database: {exc}") from exc
        finally:
            connection.close()

    def list_papers(self) -> list[sqlite3.Row]:
        connection = self.connect()
        try:
            return connection.execute(
                """SELECT p.paper_id, p.exam_name, p.year, p.paper_name,
                          p.review_status, s.local_path, s.rights_status,
                          s.extraction_status
                   FROM papers p JOIN sources s USING (source_id)
                   ORDER BY p.year, p.paper_name"""
            ).fetchall()
        except sqlite3.Error as exc:
            raise DataValidationError(f"cannot list papers: {exc}") from exc
        finally:
            connection.close()

    def list_sources(self) -> list[sqlite3.Row]:
        connection = self.connect()
        try:
            return connection.execute(
                """SELECT source_id, title, creator, publication, source_kind,
                          rights_status, rights_reference, source_url, local_path,
                          extraction_status
                   FROM sources ORDER BY source_kind, title"""
            ).fetchall()
        except sqlite3.Error as exc:
            raise DataValidationError(f"cannot list sources: {exc}") from exc
        finally:
            connection.close()

    def topic_map(self, topic_id: str) -> tuple[sqlite3.Row, list[sqlite3.Row]]:
        connection = self.connect()
        try:
            topic = connection.execute(
                "SELECT * FROM concepts WHERE topic_id = ?", (topic_id,)
            ).fetchone()
            if topic is None:
                raise DataValidationError(f"unknown physics topic_id {topic_id!r}")
            links = connection.execute(
                """SELECT c.concept_id, c.concept_name, c.domain, l.relation
                   FROM concept_links l JOIN concepts c ON c.concept_id = l.target_id
                   WHERE l.source_id = ? ORDER BY l.relation, c.concept_id""",
                (topic["concept_id"],),
            ).fetchall()
            return topic, links
        except sqlite3.Error as exc:
            raise DataValidationError(f"cannot map topic: {exc}") from exc
        finally:
            connection.close()

    def topic_references(self, topic_id: str) -> list[sqlite3.Row]:
        topic, links = self.topic_map(topic_id)
        concept_ids = [topic["concept_id"], *(row["concept_id"] for row in links)]
        placeholders = ", ".join("?" for _ in concept_ids)
        connection = self.connect()
        try:
            return connection.execute(
                f"""SELECT cs.concept_id, c.concept_name, s.source_id, s.title,
                           s.source_url, s.local_path, s.rights_status,
                           cs.source_locator, cs.review_status
                    FROM concept_sources cs
                    JOIN concepts c ON c.concept_id = cs.concept_id
                    JOIN sources s ON s.source_id = cs.source_id
                    WHERE cs.concept_id IN ({placeholders})
                    ORDER BY cs.concept_id, s.title""",
                concept_ids,
            ).fetchall()
        except sqlite3.Error as exc:
            raise DataValidationError(f"cannot list topic references: {exc}") from exc
        finally:
            connection.close()

    def map_paper(self, paper_id: str) -> tuple[sqlite3.Row, list[sqlite3.Row]]:
        connection = self.connect()
        try:
            paper = connection.execute(
                """SELECT p.*, s.local_path, s.rights_status, s.extraction_status
                   FROM papers p JOIN sources s USING (source_id)
                   WHERE p.paper_id = ?""",
                (paper_id,),
            ).fetchone()
            if paper is None:
                raise DataValidationError(f"unknown paper_id {paper_id!r}")
            questions = connection.execute(
                """SELECT q.question_id, q.question_locator, q.topic_id,
                          q.review_status, q.answer_verified,
                          c.concept_id, c.concept_name, qc.relation,
                          qc.review_status AS link_review_status
                   FROM questions q
                   JOIN concepts topic ON topic.topic_id = q.topic_id
                   LEFT JOIN question_concepts qc ON qc.question_id = q.question_id
                   LEFT JOIN concepts c ON c.concept_id = qc.concept_id
                   WHERE q.paper_id = ?
                   ORDER BY q.question_locator, c.concept_id""",
                (paper_id,),
            ).fetchall()
            return paper, questions
        except sqlite3.Error as exc:
            raise DataValidationError(f"cannot map paper: {exc}") from exc
        finally:
            connection.close()

    def export_exam_metadata(self, destination: Path) -> int:
        """Export only verified modern-exam rows accepted by the recommendation engine."""
        destination = Path(destination)
        destination.parent.mkdir(parents=True, exist_ok=True)
        fields = (
            "question_id", "exam", "exam_name", "year", "session", "paper_id",
            "subject", "topic_id", "source_name", "source_url", "source_type",
            "rights_status", "rights_reference", "question_locator", "question_format",
            "difficulty", "marks", "answer_verified", "review_status", "reviewer",
            "reviewed_at", "notes",
        )
        connection = self.connect()
        try:
            rows = connection.execute(
                """SELECT * FROM exam_question_records
                   WHERE review_status = 'verified'
                     AND paper_id IN (
                         SELECT paper_id FROM papers WHERE review_status = 'verified'
                     )
                     AND source_url IS NOT NULL
                     AND source_url <> ''
                   ORDER BY exam, year, session, paper_id, question_id"""
            ).fetchall()
            with destination.open("w", encoding="utf-8", newline="") as stream:
                writer = csv.DictWriter(stream, fieldnames=fields)
                writer.writeheader()
                for row in rows:
                    writer.writerow({field: row[field] or "" for field in fields})
            return len(rows)
        except (OSError, sqlite3.Error, csv.Error) as exc:
            raise DataValidationError(f"cannot export recommendation metadata: {exc}") from exc
        finally:
            connection.close()
