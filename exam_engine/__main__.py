"""Command-line interface for exam-topic video recommendations."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import sys

from .engine import (
    EXAMS,
    DataValidationError,
    load_backtest,
    load_recommendations,
    load_topics,
    render_video_batch,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m exam_engine",
        description="Create evidence-labelled physics lesson briefs from exam metadata.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    recommend = subparsers.add_parser(
        "recommend",
        help="rank topics and create a batch of 20 video briefs",
    )
    recommend.add_argument("--exam", choices=EXAMS, required=True)
    recommend.add_argument(
        "--data",
        type=Path,
        default=Path("data/exam_question_metadata.csv"),
        help="question metadata CSV (default: data/exam_question_metadata.csv)",
    )
    recommend.add_argument(
        "--topics",
        type=Path,
        default=Path("data/physics_topics.csv"),
        help="physics topic catalog (default: data/physics_topics.csv)",
    )
    recommend.add_argument(
        "--as-of-year",
        type=int,
        default=date.today().year,
        help="final calendar year in the 30-year historical window",
    )
    recommend.add_argument(
        "--output",
        type=Path,
        help="write the Markdown batch to this path instead of standard output",
    )
    backtest = subparsers.add_parser(
        "backtest",
        help="evaluate historical topic rankings against later held-out papers",
    )
    backtest.add_argument("--exam", choices=EXAMS, required=True)
    backtest.add_argument(
        "--data",
        type=Path,
        default=Path("data/exam_question_metadata.csv"),
        help="question metadata CSV (default: data/exam_question_metadata.csv)",
    )
    backtest.add_argument(
        "--topics",
        type=Path,
        default=Path("data/physics_topics.csv"),
        help="physics topic catalog (default: data/physics_topics.csv)",
    )
    backtest.add_argument(
        "--as-of-year",
        type=int,
        default=date.today().year,
        help="final calendar year eligible for held-out evaluation",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        topics = load_topics(args.topics)
        if args.command == "backtest":
            result = load_backtest(
                args.data,
                topics,
                exam=args.exam,
                as_of_year=args.as_of_year,
            )
            years = ", ".join(str(year) for year in result.years_evaluated)
            print(f"Rolling-origin topic-ranking backtest: {args.exam}")
            print(f"Held-out years: {years}")
            print(f"Held-out papers: {result.papers_evaluated}")
            print(f"Model mean multi-class Brier score: {result.model_brier_score:.4f}")
            print(f"Uniform baseline Brier score: {result.uniform_brier_score:.4f}")
            print(
                "Mean top-10 topic coverage: "
                f"{result.mean_top_ten_coverage:.1%}"
            )
            print(
                "Lower Brier is better; these metrics describe only verified "
                "records in the supplied metadata."
            )
            return 0
        recommendations = load_recommendations(
            args.data,
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
        return 0
    except (DataValidationError, OSError) as exc:
        print(f"exam_engine: error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
