#!/usr/bin/env python3
"""Render an original practice-paper JSON file as candidate and solution PDFs."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys
import textwrap
from typing import Any

import pymupdf as fitz

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "data" / "practice_papers" / "jee_advanced_2027_physics_set_01.json"
DEFAULT_OUTPUT = ROOT / "output" / "practice_papers"
ALLOWED_TYPES = {"single_correct", "multiple_correct", "numerical"}


class PracticePaperError(ValueError):
    """Raised when a practice-paper source is incomplete or malformed."""


def load_paper(path: Path) -> dict[str, Any]:
    try:
        paper = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise PracticePaperError(f"cannot read practice paper {path}: {exc}") from exc
    if not isinstance(paper, dict) or paper.get("schema_version") != 1:
        raise PracticePaperError("practice paper must be a JSON object with schema_version 1")
    paper_id = paper.get("paper_id")
    if not isinstance(paper_id, str) or not re.fullmatch(r"[a-z0-9][a-z0-9._-]*", paper_id):
        raise PracticePaperError("paper_id must use lowercase letters, digits, '.', '_' or '-'")
    questions = paper.get("questions")
    if not isinstance(questions, list) or len(questions) != paper.get("question_count"):
        raise PracticePaperError("questions must match the declared question_count")
    seen: set[str] = set()
    for index, question in enumerate(questions, start=1):
        if not isinstance(question, dict):
            raise PracticePaperError(f"question {index} must be an object")
        question_id = question.get("id")
        if not isinstance(question_id, str) or question_id in seen:
            raise PracticePaperError(f"question {index} needs a unique string id")
        seen.add(question_id)
        if question.get("type") not in ALLOWED_TYPES:
            raise PracticePaperError(f"{question_id}: unsupported question type")
        for field in ("area", "topic_id", "prompt", "answer", "solution"):
            if not isinstance(question.get(field), str) or not question[field].strip():
                raise PracticePaperError(f"{question_id}.{field} must be non-empty text")
        if question["type"] in {"single_correct", "multiple_correct"}:
            choices = question.get("choices")
            if not isinstance(choices, list) or len(choices) < 2:
                raise PracticePaperError(f"{question_id} needs at least two choices")
        if question["type"] == "numerical" and question.get("choices") is not None:
            raise PracticePaperError(f"{question_id}: numerical questions must not have choices")
    return paper


def _wrapped(text: str, width: int = 94) -> list[str]:
    return textwrap.wrap(
        text,
        width=width,
        break_long_words=False,
        break_on_hyphens=False,
    ) or [""]


def _header(page: fitz.Page, paper: dict[str, Any], *, solutions: bool) -> float:
    page.draw_rect(fitz.Rect(0, 0, page.rect.width, 83), color=None, fill=(0.035, 0.09, 0.16))
    page.insert_text((42, 31), "SAEM PHYSICS", fontname="hebo", fontsize=10, color=(0.32, 0.78, 0.94))
    page.insert_text(
        (42, 55),
        "ANSWER KEY & SOLUTIONS" if solutions else "PRACTICE QUESTION PAPER",
        fontname="hebo",
        fontsize=18,
        color=(1, 1, 1),
    )
    page.insert_text(
        (42, 72),
        f"{paper['target_exam']} {paper['target_year']} | Physics | 10 original questions",
        fontname="helv",
        fontsize=9,
        color=(0.82, 0.89, 0.95),
    )
    y = 103
    for line in _wrapped(paper["notice"], 105):
        page.insert_text((42, y), line, fontname="hebo", fontsize=8.5, color=(0.62, 0.18, 0.12))
        y += 12
    page.draw_line(
        fitz.Point(42, y + 3),
        fitz.Point(page.rect.width - 42, y + 3),
        color=(0.75, 0.8, 0.84),
        width=0.7,
    )
    return y + 20


def _footer(page: fitz.Page, page_number: int, solutions: bool) -> None:
    label = "SOLUTIONS - TEACHER REVIEW REQUIRED" if solutions else "ORIGINAL PRACTICE - NOT AN OFFICIAL PREDICTION"
    page.draw_line(
        fitz.Point(42, page.rect.height - 37),
        fitz.Point(page.rect.width - 42, page.rect.height - 37),
        color=(0.78, 0.82, 0.85),
        width=0.6,
    )
    page.insert_text((42, page.rect.height - 22), label, fontname="helv", fontsize=7.5, color=(0.35, 0.4, 0.45))
    page.insert_text((page.rect.width - 57, page.rect.height - 22), str(page_number), fontname="helv", fontsize=8, color=(0.35, 0.4, 0.45))


def _question_text(question: dict[str, Any]) -> str:
    kind = {
        "single_correct": "SINGLE CORRECT",
        "multiple_correct": "MULTIPLE CORRECT",
        "numerical": "NUMERICAL ANSWER",
    }[question["type"]]
    number = int(question["id"][1:])
    pieces = [f"Question {number}  |  {kind}  |  {question['area']}"]
    pieces.extend(_wrapped(question["prompt"]))
    pieces.extend(question.get("choices", []))
    if question["type"] == "numerical":
        pieces.append(f"Answer unit: {question.get('unit', 'as requested in the question')}")
    return "\n".join(pieces)


def _draw_card(
    page: fitz.Page,
    question: dict[str, Any],
    top: float,
    *,
    solutions: bool,
) -> float:
    question_lines = _question_text(question).splitlines()
    body_lines = (
        [f"Answer: {question['answer']}", *_wrapped(question["solution"])]
        if solutions
        else []
    )
    checks = (
        [
            line
            for item in question.get("checks", [])
            for line in _wrapped(f"Check: {item}")
        ]
        if solutions
        else []
    )
    all_lines = question_lines + body_lines + checks
    size = 9.2 if not solutions else 8.6
    line_height = 13.1 if not solutions else 12.2
    height = max(130, 26 + len(all_lines) * line_height)
    rect = fitz.Rect(42, top, page.rect.width - 42, top + height)
    page.draw_rect(rect, color=(0.82, 0.86, 0.89), fill=(0.98, 0.99, 1.0), width=0.7)
    text = "\n".join(all_lines)
    result = page.insert_textbox(
        fitz.Rect(rect.x0 + 12, rect.y0 + 12, rect.x1 - 12, rect.y1 - 9),
        text,
        fontname="helv",
        fontsize=size,
        lineheight=line_height / size,
        color=(0.12, 0.16, 0.2),
    )
    if result < 0:
        raise PracticePaperError(f"{question['id']}: text did not fit in the PDF layout")
    return rect.y1


def render_pdf(paper: dict[str, Any], destination: Path, *, solutions: bool) -> Path:
    document = fitz.open()
    questions_per_page = 1 if solutions else 2
    groups = [
        paper["questions"][index:index + questions_per_page]
        for index in range(0, len(paper["questions"]), questions_per_page)
    ]
    for page_number, group in enumerate(groups, start=1):
        page = document.new_page(width=595, height=842)
        y = _header(page, paper, solutions=solutions)
        if page_number == 1 and not solutions:
            page.insert_text(
                (42, y),
                f"Suggested time: {paper['time_limit_minutes']} minutes. "
                "No official marking scheme is implied.",
                fontname="hebo",
                fontsize=9,
                color=(0.12, 0.2, 0.28),
            )
            y += 24
            for instruction in paper["instructions"]:
                lines = _wrapped("- " + instruction, 105)
                for line in lines:
                    page.insert_text((42, y), line, fontname="helv", fontsize=8, color=(0.22, 0.27, 0.31))
                    y += 11
            y += 14
        for question in group:
            y = _draw_card(page, question, y, solutions=solutions) + 12
        _footer(page, page_number, solutions)
    destination.parent.mkdir(parents=True, exist_ok=True)
    document.set_metadata(
        {
            "title": f"{paper['title']} - {'Solutions' if solutions else 'Questions'}",
            "author": "Saem Physics",
            "subject": paper["notice"],
            "keywords": "original practice, JEE Advanced, Physics, prior-only topic baseline",
        }
    )
    document.save(destination, garbage=4, deflate=True)
    document.close()
    check = fitz.open(destination)
    if len(check) != len(groups):
        raise PracticePaperError(f"PDF page-count verification failed for {destination}")
    check.close()
    return destination


def render_pair(paper_path: Path, output_dir: Path) -> tuple[Path, Path]:
    paper = load_paper(paper_path)
    question_pdf = output_dir / f"{paper['paper_id']}.pdf"
    solution_pdf = output_dir / f"{paper['paper_id']}-solutions.pdf"
    return (
        render_pdf(paper, question_pdf, solutions=False),
        render_pdf(paper, solution_pdf, solutions=True),
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args(argv)
    try:
        question_pdf, solution_pdf = render_pair(args.input, args.output_dir)
    except (PracticePaperError, OSError, RuntimeError) as exc:
        print(f"render_practice_paper: error: {exc}", file=sys.stderr)
        return 2
    print(f"Question paper: {question_pdf}")
    print(f"Solutions: {solution_pdf}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
