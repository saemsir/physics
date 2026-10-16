"""CLI for the linked question, concept, computation, and lesson workflow."""

from __future__ import annotations

import argparse
from datetime import date
import json
from pathlib import Path
import sqlite3
import sys
import tempfile

from exam_engine.engine import (
    EXAMS,
    DataValidationError,
    load_backtest,
    load_recommendations,
    load_topics,
    render_video_batch,
)

from .batch import load_batch, validate_batch, write_batch_plan
from .database import ContentDatabase, ROOT
from .lesson import compile_lesson, persist_lesson, write_lesson
from .problem import load_problem, record_problem_run, solve_problem


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m content_engine",
        description="Build and query SaemPhysics' source-linked content network.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    init = subparsers.add_parser("init", help="build/refresh SQLite from tracked catalogs")
    init.add_argument("--database", type=Path, default=ROOT / "data" / "saemphysics.sqlite")

    summary = subparsers.add_parser("summary", help="show database counts")
    summary.add_argument("--database", type=Path, default=ROOT / "data" / "saemphysics.sqlite")

    papers = subparsers.add_parser("papers", help="list indexed exam-paper source files")
    papers.add_argument("--database", type=Path, default=ROOT / "data" / "saemphysics.sqlite")

    sources = subparsers.add_parser("sources", help="list indexed books, courses, and papers")
    sources.add_argument("--database", type=Path, default=ROOT / "data" / "saemphysics.sqlite")

    map_topic = subparsers.add_parser("map-topic", help="show a topic's linked concepts")
    map_topic.add_argument("--topic", required=True)
    map_topic.add_argument("--database", type=Path, default=ROOT / "data" / "saemphysics.sqlite")

    map_paper = subparsers.add_parser("map-paper", help="show curated questions and concept links")
    map_paper.add_argument("--paper-id", required=True)
    map_paper.add_argument("--database", type=Path, default=ROOT / "data" / "saemphysics.sqlite")

    solve = subparsers.add_parser("solve", help="validate and calculate a typed problem JSON")
    solve.add_argument("--problem", type=Path, required=True)
    solve.add_argument("--database", type=Path, default=ROOT / "data" / "saemphysics.sqlite")

    compile_command = subparsers.add_parser(
        "compile-lesson", help="solve and compile a renderer-neutral lesson IR"
    )
    compile_command.add_argument("--problem", type=Path, required=True)
    compile_command.add_argument("--output", type=Path)
    compile_command.add_argument(
        "--database", type=Path, default=ROOT / "data" / "saemphysics.sqlite"
    )
    recommend = subparsers.add_parser(
        "recommend", help="rank topics using verified linked question records"
    )
    recommend.add_argument("--exam", choices=EXAMS, required=True)
    recommend.add_argument("--as-of-year", type=int, default=date.today().year)
    recommend.add_argument("--output", type=Path)
    recommend.add_argument("--database", type=Path, default=ROOT / "data" / "saemphysics.sqlite")
    backtest = subparsers.add_parser(
        "backtest", help="evaluate linked question records against a uniform baseline"
    )
    backtest.add_argument("--exam", choices=EXAMS, required=True)
    backtest.add_argument("--as-of-year", type=int, default=date.today().year)
    backtest.add_argument("--database", type=Path, default=ROOT / "data" / "saemphysics.sqlite")
    batch = subparsers.add_parser(
        "batch-plan", help="validate a 10-episode batch and expand its 20 video deliverables"
    )
    batch.add_argument(
        "--manifest",
        type=Path,
        default=ROOT / "data" / "video_batches" / "batch_001.json",
    )
    batch.add_argument("--output", type=Path)
    return parser


def _require_initialized(database: ContentDatabase) -> None:
    if not database.path.is_file():
        raise DataValidationError(
            f"database not found: {database.path}; run `python -m content_engine init` first"
        )
    connection = database.connect()
    try:
        row = connection.execute("SELECT MAX(version) FROM schema_migrations").fetchone()
        if row is None or row[0] is None:
            raise DataValidationError(
                f"database is not initialized: {database.path}; run "
                "`python -m content_engine init` first"
            )
    except sqlite3.Error as exc:
        raise DataValidationError(f"database is not initialized: {exc}") from exc
    finally:
        connection.close()


def _run_problem(database: ContentDatabase, problem_path: Path):
    _require_initialized(database)
    problem = load_problem(problem_path)
    result = solve_problem(problem)
    connection = database.connect()
    try:
        with connection:
            run_id = record_problem_run(connection, problem, result)
    except sqlite3.Error as exc:
        raise DataValidationError(f"cannot persist engine run: {exc}") from exc
    finally:
        connection.close()
    return problem, result, run_id


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    database = ContentDatabase(args.database) if hasattr(args, "database") else None
    try:
        if args.command == "init":
            database.initialize(ROOT)
            print(f"Initialized {database.path}")
            for name, count in database.summary().items():
                print(f"{name}: {count}")
            return 0
        if args.command == "batch-plan":
            manifest = load_batch(args.manifest)
            plan = validate_batch(manifest, ROOT)
            if args.output:
                write_batch_plan(manifest, plan, args.output)
                print(
                    f"Wrote {len(plan)} {manifest['status']} video render briefs "
                    f"to {args.output}"
                )
            else:
                print(json.dumps({
                    "batch_id": manifest["batch_id"],
                    "status": manifest["status"],
                    "deliverable_count": len(plan),
                    "vertical_60s": sum(item["format"] == "vertical" for item in plan),
                    "horizontal_180s": sum(item["format"] == "horizontal" for item in plan),
                    "problem_episodes": sum(
                        item["type"] == "problem" and item["format"] == "vertical"
                        for item in plan
                    ),
                    "concept_episodes": sum(
                        item["type"] == "concept" and item["format"] == "vertical"
                        for item in plan
                    ),
                    "engine_checked_solutions": sum(
                        episode.get("problem_spec") is not None
                        for episode in manifest["episodes"]
                    ),
                    "owner_review_required": True,
                }, indent=2))
            return 0
        if args.command == "summary":
            _require_initialized(database)
            for name, count in database.summary().items():
                print(f"{name}: {count}")
            return 0
        if args.command == "papers":
            _require_initialized(database)
            for paper in database.list_papers():
                print(
                    f"{paper['paper_id']}\t{paper['exam_name']} {paper['year']} "
                    f"{paper['paper_name']}\t{paper['review_status']}\t"
                    f"rights={paper['rights_status']}\textraction={paper['extraction_status']}\t"
                    f"{paper['local_path']}"
                )
            return 0
        if args.command == "sources":
            _require_initialized(database)
            for source in database.list_sources():
                location = source["local_path"] or source["source_url"] or "no URL/path"
                print(
                    f"{source['source_id']}\t{source['title']}\t"
                    f"rights={source['rights_status']}\t"
                    f"extraction={source['extraction_status']}\t{location}"
                )
            return 0
        if args.command == "map-topic":
            _require_initialized(database)
            topic, links = database.topic_map(args.topic)
            print(f"{topic['concept_name']} ({topic['concept_id']})")
            print(topic["summary"])
            print("Links:")
            for link in links:
                print(f"- {link['relation']}: {link['concept_name']} ({link['concept_id']})")
            references = database.topic_references(args.topic)
            if references:
                print("Source references (check rights and review status before reuse):")
                for reference in references:
                    location = reference["local_path"] or reference["source_url"] or "no URL/path"
                    print(
                        f"- {reference['title']} — {reference['concept_name']}, "
                        f"{reference['source_locator']} "
                        f"[{reference['review_status']}; rights={reference['rights_status']}] "
                        f"({location})"
                    )
            return 0
        if args.command == "map-paper":
            _require_initialized(database)
            paper, questions = database.map_paper(args.paper_id)
            print(
                f"{paper['exam_name']} {paper['year']} {paper['paper_name']} "
                f"({paper['paper_id']})"
            )
            print(
                f"Review: {paper['review_status']}; rights: {paper['rights_status']}; "
                f"extraction: {paper['extraction_status']}; source: {paper['local_path']}"
            )
            if not questions:
                print("No manually curated question records linked yet.")
            for question in questions:
                print(
                    f"- {question['question_id']} locator={question['question_locator']} "
                    f"topic={question['topic_id']} review={question['review_status']} "
                    f"answer_verified={question['answer_verified']}"
                )
                if question["concept_id"]:
                    print(
                        f"  {question['relation']}: {question['concept_name']} "
                        f"({question['link_review_status']})"
                    )
            return 0
        if args.command == "solve":
            problem, result, run_id = _run_problem(database, args.problem)
            print(json.dumps({**result.to_dict(), "run_id": run_id}, indent=2))
            return 0 if result.computation_status == "passed" else 2
        if args.command == "compile-lesson":
            problem, result, run_id = _run_problem(database, args.problem)
            if result.computation_status != "passed":
                raise DataValidationError(
                    "lesson compilation stopped because one or more computational "
                    "checks failed; inspect the stored engine run before retrying"
                )
            connection = database.connect()
            try:
                with connection:
                    ir = compile_lesson(connection, problem, result.to_dict())
                    persist_lesson(connection, ir)
            except sqlite3.Error as exc:
                raise DataValidationError(f"cannot persist lesson IR: {exc}") from exc
            finally:
                connection.close()
            output = args.output or (
                ROOT / "output" / "lessons" / f"{ir['lesson_id']}.json"
            )
            write_lesson(ir, output)
            print(
                f"Wrote lesson IR {output} (run {run_id}); "
                "physics/design/release approvals remain pending."
            )
            return 0 if result.computation_status == "passed" else 2
        if args.command in {"recommend", "backtest"}:
            _require_initialized(database)
            topics = load_topics(ROOT / "data" / "physics_topics.csv")
            with tempfile.TemporaryDirectory(prefix="saemphysics-recommend-") as workdir:
                metadata = Path(workdir) / "verified-questions.csv"
                count = database.export_exam_metadata(metadata)
                if args.command == "recommend":
                    recommendations = load_recommendations(
                        metadata,
                        topics,
                        exam=args.exam,
                        as_of_year=args.as_of_year,
                    )
                    output = render_video_batch(
                        recommendations,
                        exam=args.exam,
                        as_of_year=args.as_of_year,
                    )
                    if args.output:
                        args.output.parent.mkdir(parents=True, exist_ok=True)
                        args.output.write_text(output, encoding="utf-8")
                        print(f"Wrote 20 video briefs to {args.output}")
                    else:
                        print(output, end="")
                    print(
                        f"\nRecommendation evidence: {count} verified, source-linked "
                        "question record(s) across supported exams."
                    )
                    return 0
                result = load_backtest(
                    metadata,
                    topics,
                    exam=args.exam,
                    as_of_year=args.as_of_year,
                )
                years = ", ".join(str(year) for year in result.years_evaluated) or "none"
                print(f"Linked-network backtest: {args.exam}")
                print(f"Held-out years: {years}")
                print(f"Held-out papers: {result.papers_evaluated}")
                print(f"Model mean multi-class Brier score: {result.model_brier_score:.4f}")
                print(f"Uniform baseline Brier score: {result.uniform_brier_score:.4f}")
                print(f"Mean top-10 topic coverage: {result.mean_top_ten_coverage:.1%}")
                return 0
        parser.error(f"unsupported command {args.command!r}")
    except (DataValidationError, OSError, sqlite3.Error) as exc:
        print(f"content_engine: error: {exc}", file=sys.stderr)
        return 2
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
