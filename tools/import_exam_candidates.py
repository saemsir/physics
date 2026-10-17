#!/usr/bin/env python3
"""Index local JEE Advanced papers and add unverified physics-topic candidates."""

from __future__ import annotations

import argparse
import csv
import hashlib
from pathlib import Path
import re
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from exam_engine.engine import (  # noqa: E402
    REQUIRED_RECORD_FIELDS,
    DataValidationError,
    load_topics,
)
from knowledge.graph import load_graph  # noqa: E402
from matrix_pipeline import match_concepts  # noqa: E402

SOURCE_FIELDS = (
    "source_id",
    "title",
    "creator",
    "publication",
    "source_kind",
    "source_url",
    "local_path",
    "rights_status",
    "rights_reference",
    "citation",
    "extraction_status",
)
PAPER_FIELDS = (
    "paper_id",
    "exam",
    "exam_name",
    "year",
    "session",
    "paper_name",
    "subject",
    "source_id",
    "review_status",
    "notes",
)
PAPER_FILE = re.compile(r"^JEE Advanced.*\.md$", re.IGNORECASE)
YEAR_IN_NAME = re.compile(r"\b(20\d{2})\b")
PAPER_IN_COVER = re.compile(r"\bpaper\s*[-–]?\s*([12])\b", re.IGNORECASE)
PAGE_HEADING = re.compile(r"(?m)^## Page (\d+)\s*$")
QUESTION_HEADING = re.compile(r"(?m)^\s*Q\.\s*(\d{1,2})\s*(?:$|\s)")
PHYSICS_HEADER = re.compile(
    r"(?im)^\s*(?:part\s*[- ]?(?:i|1)\b.*\bphysics\b|physics)\s*\)?\s*$"
)
OTHER_SUBJECT_HEADER = re.compile(
    r"(?im)^\s*(?:part\s*[- ]?(?:i|ii|iii|1|2|3)\b.*\b(?:chemistry|mathematics)\b|"
    r"chemistry|mathematics)\s*\)?\s*$"
)
PUBLISHER_URLS = {
    "Career Point Ltd.": "https://www.careerpoint.ac.in/",
    "Unknown": "https://jeeadv.ac.in/",
}


def _read_csv(path: Path, fields: tuple[str, ...]) -> list[dict[str, str]]:
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as stream:
            reader = csv.DictReader(stream)
            if tuple(reader.fieldnames or ()) != fields:
                raise DataValidationError(
                    f"{path}: expected columns in this exact order: {', '.join(fields)}"
                )
            rows = []
            for line_number, row in enumerate(reader, start=2):
                if None in row or any(value is None for value in row.values()):
                    raise DataValidationError(f"{path}:{line_number}: malformed CSV row")
                if any((value or "").strip() for value in row.values()):
                    rows.append({key: value.strip() for key, value in row.items()})
            return rows
    except (OSError, UnicodeError, csv.Error) as exc:
        raise DataValidationError(f"cannot read {path}: {exc}") from exc


def _write_csv(path: Path, fields: tuple[str, ...], rows: list[dict[str, str]]) -> None:
    try:
        with path.open("w", encoding="utf-8", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)
    except (OSError, UnicodeError, csv.Error) as exc:
        raise DataValidationError(f"cannot write {path}: {exc}") from exc


def _append_unseen(
    existing: list[dict[str, str]],
    candidates: list[dict[str, str]],
    key: str,
) -> tuple[list[dict[str, str]], int]:
    seen = {row[key] for row in existing}
    additions = [row for row in candidates if row[key] not in seen]
    return existing + additions, len(additions)


def _paper_identity(path: Path, text: str) -> tuple[int, int]:
    cover = text.split("## Page 1", 1)[-1].split("## Page 2", 1)[0]
    year_match = YEAR_IN_NAME.search(path.name)
    paper_match = PAPER_IN_COVER.search(cover)
    if year_match is None or paper_match is None:
        raise DataValidationError(
            f"{path}: cannot identify year and paper number from filename and cover"
        )
    return int(year_match.group(1)), int(paper_match.group(1))


def _publisher(cover: str) -> tuple[str, str, str]:
    if "career point" in cover.casefold():
        return (
            "Career Point Ltd.",
            "coaching-institute-local-copy",
            PUBLISHER_URLS["Career Point Ltd."],
        )
    return (
        "Unknown",
        "local-paper-copy-origin-unconfirmed",
        PUBLISHER_URLS["Unknown"],
    )


def _discover_sources(papers_dir: Path) -> tuple[list[dict[str, Any]], dict[tuple[int, int], dict[str, Any]]]:
    if not papers_dir.is_dir():
        raise DataValidationError(f"paper directory does not exist: {papers_dir}")

    files: list[dict[str, Any]] = []
    groups: dict[tuple[int, int], list[dict[str, Any]]] = {}
    for markdown_path in sorted(papers_dir.glob("JEE Advanced*.md")):
        if not PAPER_FILE.fullmatch(markdown_path.name):
            continue
        try:
            text = markdown_path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            raise DataValidationError(f"cannot read paper extraction {markdown_path}: {exc}") from exc
        year, paper_number = _paper_identity(markdown_path, text)
        cover = text.split("## Page 1", 1)[-1].split("## Page 2", 1)[0]
        publisher, source_kind, source_url = _publisher(cover)
        pdf_path = markdown_path.with_suffix(".pdf")
        if not pdf_path.is_file():
            raise DataValidationError(f"{markdown_path}: matching PDF {pdf_path} is missing")
        page_count = max((int(value) for value in re.findall(r"(?m)^## Page (\d+)$", text)), default=0)
        source_id = "local-ja-" + hashlib.sha256(
            markdown_path.relative_to(ROOT).as_posix().encode("utf-8")
        ).hexdigest()[:14]
        source = {
            "source_id": source_id,
            "title": f"JEE Advanced {year} Paper {paper_number} local copy",
            "creator": publisher,
            "publication": "Local PDF copy; publication details unconfirmed",
            "source_kind": source_kind,
            "source_url": source_url,
            "local_path": pdf_path.relative_to(ROOT).as_posix(),
            "rights_status": "unknown",
            "rights_reference": "",
            "citation": (
                f"Cover of {pdf_path.name} identifies {publisher}."
                if publisher != "Unknown"
                else f"{pdf_path.name} states JEE (Advanced) {year}, Paper {paper_number}; "
                "original download source is not recorded."
            ),
            "extraction_status": "local-extraction-imported-topic-tags-pending-review",
            "_text": text,
            "_cover": cover,
            "_page_count": page_count,
            "_publisher": publisher,
            "_source_kind": source_kind,
            "_source_url": source_url,
            "_markdown_path": markdown_path,
            "_year": year,
            "_paper_number": paper_number,
        }
        files.append(source)
        groups.setdefault((year, paper_number), []).append(source)

    if not files:
        raise DataValidationError(f"no JEE Advanced Markdown extractions found under {papers_dir}")

    canonical: dict[tuple[int, int], dict[str, Any]] = {}
    for key, candidates in groups.items():
        canonical[key] = max(
            candidates,
            key=lambda item: (
                int(key[0] == 2025 and item["_publisher"] == "Unknown"),
                item["_page_count"],
            ),
        )
    return files, canonical


def _physics_questions(source: dict[str, Any]) -> list[dict[str, Any]]:
    text = source["_text"]
    subject_matches = list(PHYSICS_HEADER.finditer(text))
    if not subject_matches:
        raise DataValidationError(f"{source['_markdown_path']}: Physics section not found")
    start = subject_matches[0].end()
    end_match = OTHER_SUBJECT_HEADER.search(text, start)
    subject_text = text[start : end_match.start() if end_match else len(text)]
    headings = [
        match for match in QUESTION_HEADING.finditer(subject_text)
        if int(match.group(1)) > 0
    ]
    if not headings:
        raise DataValidationError(
            f"{source['_markdown_path']}: no numbered Physics questions found"
        )

    questions = []
    occurrences: dict[int, int] = {}
    for index, heading in enumerate(headings):
        number = int(heading.group(1))
        occurrences[number] = occurrences.get(number, 0) + 1
        body_start = heading.start()
        body_end = headings[index + 1].start() if index + 1 < len(headings) else len(subject_text)
        page_count = len(PAGE_HEADING.findall(subject_text[:body_start]))
        questions.append(
            {
                "number": number,
                "occurrence": occurrences[number],
                "page": page_count or 1,
                "text": subject_text[body_start:body_end],
            }
        )
    return questions


def build_candidate_rows(
    papers_dir: Path,
    topics_path: Path,
    concepts_path: Path,
    links_path: Path,
) -> tuple[list[dict[str, str]], list[dict[str, str]], list[dict[str, str]], dict[str, int]]:
    topics = load_topics(topics_path)
    topic_ids = {topic.topic_id for topic in topics}
    graph = load_graph(concepts_path, links_path, topics)
    concept_catalog = graph.by_id()
    all_sources, canonical = _discover_sources(papers_dir)

    source_rows = [
        {field: str(source[field]) for field in SOURCE_FIELDS}
        for source in all_sources
    ]
    paper_rows: list[dict[str, str]] = []
    question_rows: list[dict[str, str]] = []
    counts = {
        "local_pdf_copies": len(all_sources),
        "distinct_papers": len(canonical),
        "physics_questions_found": 0,
        "topic_candidates": 0,
        "questions_without_topic_evidence": 0,
    }

    for (year, paper_number), source in sorted(canonical.items()):
        paper_id = f"jee-advanced-{year}-paper-{paper_number}"
        publisher = source["_publisher"]
        markdown_name = source["_markdown_path"].name
        alternatives = [
            item["_markdown_path"].name
            for item in all_sources
            if (item["_year"], item["_paper_number"]) == (year, paper_number)
            and item is not source
        ]
        source_notes = (
            f"Cover identifies {publisher}; exact publication URL and PDF integrity have not "
            "been independently checked. Topic matches below are machine-generated candidates."
            if publisher != "Unknown"
            else "Local file is in JEE Advanced paper format, but no issuer/publisher mark or "
            "exact original download URL was found; source verification is pending."
        )
        if alternatives:
            source_notes += " Alternate local copies: " + ", ".join(alternatives) + "."
        paper_rows.append(
            {
                "paper_id": paper_id,
                "exam": "jee-advanced",
                "exam_name": "JEE Advanced",
                "year": str(year),
                "session": "annual",
                "paper_name": f"Paper {paper_number}",
                "subject": "physics",
                "source_id": source["source_id"],
                "review_status": "needs-source-review",
                "notes": f"{source_notes} Canonical extraction: {markdown_name}.",
            }
        )
        questions = _physics_questions(source)
        counts["physics_questions_found"] += len(questions)
        for question in questions:
            evidence = match_concepts(question["text"], graph)
            candidates = [
                (
                    concept_catalog[concept_id].topic_id,
                    float(item["score"]),
                    tuple(item["phrases"]),
                )
                for concept_id, item in evidence.items()
                if concept_id in concept_catalog
                and concept_catalog[concept_id].domain.casefold() == "physics"
                and concept_catalog[concept_id].topic_id in topic_ids
            ]
            if not candidates:
                counts["questions_without_topic_evidence"] += 1
                continue
            topic_id, _, phrases = sorted(
                candidates, key=lambda item: (-item[1], item[0])
            )[0]
            counts["topic_candidates"] += 1
            question_id = (
                f"ja{year}p{paper_number}q{question['number']:02d}"
                f"v{question['occurrence']:02d}"
            )
            question_rows.append(
                {
                    "question_id": question_id,
                    "exam": "jee-advanced",
                    "exam_name": "JEE Advanced",
                    "year": str(year),
                    "session": "annual",
                    "paper_id": paper_id,
                    "subject": "Physics",
                    "topic_id": topic_id,
                    "source_name": publisher if publisher != "Unknown" else "Unidentified local copy",
                    "source_url": source["_source_url"],
                    "source_type": source["_source_kind"],
                    "rights_status": "unknown",
                    "rights_reference": "",
                    "question_locator": (
                        f"Physics Q.{question['number']} occurrence {question['occurrence']}, "
                        f"extracted page {question['page']}"
                    ),
                    "question_format": "unclassified",
                    "difficulty": "unrated",
                    "marks": "",
                    "answer_verified": "false",
                    "review_status": "pending",
                    "reviewer": "",
                    "reviewed_at": "",
                    "notes": (
                        "Machine-generated topic candidate from local extracted text; requires "
                        "independent question, topic, and source review before use. Matched "
                        "phrases: " + "; ".join(phrases) + f". Local extraction: {markdown_name}."
                    ),
                }
            )

    return source_rows, paper_rows, question_rows, counts


def import_candidates(root: Path = ROOT) -> dict[str, int]:
    sources_path = root / "data" / "sources.csv"
    papers_path = root / "data" / "papers.csv"
    metadata_path = root / "data" / "exam_question_metadata.csv"
    source_rows, paper_rows, question_rows, counts = build_candidate_rows(
        root / "exam_papers",
        root / "data" / "physics_topics.csv",
        root / "knowledge" / "concepts.csv",
        root / "knowledge" / "links.csv",
    )
    existing_sources = _read_csv(sources_path, SOURCE_FIELDS)
    existing_papers = _read_csv(papers_path, PAPER_FIELDS)
    existing_questions = _read_csv(metadata_path, REQUIRED_RECORD_FIELDS)
    source_rows, counts["source_records_added"] = _append_unseen(
        existing_sources, source_rows, "source_id"
    )
    paper_rows, counts["paper_records_added"] = _append_unseen(
        existing_papers, paper_rows, "paper_id"
    )
    question_rows, counts["question_candidates_added"] = _append_unseen(
        existing_questions, question_rows, "question_id"
    )
    _write_csv(sources_path, SOURCE_FIELDS, source_rows)
    _write_csv(papers_path, PAPER_FIELDS, paper_rows)
    _write_csv(metadata_path, REQUIRED_RECORD_FIELDS, question_rows)
    return counts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=ROOT,
        help="repository root (default: this checkout)",
    )
    args = parser.parse_args()
    try:
        counts = import_candidates(args.root.resolve())
    except DataValidationError as exc:
        print(f"import_exam_candidates: error: {exc}", file=sys.stderr)
        return 2
    print(
        f"Indexed {counts['local_pdf_copies']} local PDF copies into "
        f"{counts['distinct_papers']} distinct paper records."
    )
    print(
        f"Found {counts['physics_questions_found']} Physics question headings; "
        f"created {counts['topic_candidates']} pending topic candidates and left "
        f"{counts['questions_without_topic_evidence']} unmatched."
    )
    print(
        f"Added {counts['source_records_added']} source records, "
        f"{counts['paper_records_added']} paper records, and "
        f"{counts['question_candidates_added']} question candidates."
    )
    print(
        "All imported paper records require source review; all question tags are pending "
        "and excluded from forecasts until independently reviewed."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
