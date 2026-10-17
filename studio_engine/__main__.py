"""CLI for the portable repository-wide studio coordinator."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

from .engine import ROOT, StudioEngine, StudioRequestError, _read_json, validate_request


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m studio_engine",
        description="Coordinate supported SaemPhysics engines from a portable JSON request.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("actions", help="list registered actions and capability limits")
    validate = subparsers.add_parser("validate", help="validate a studio request JSON")
    validate.add_argument("--request", type=Path, required=True)
    run = subparsers.add_parser("run", help="run the tasks in a studio request JSON")
    run.add_argument("--request", type=Path, required=True)
    run.add_argument("--output-dir", type=Path, help="override output directory for portability")
    run.add_argument("--root", type=Path, default=ROOT, help="repository root")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command == "actions":
        print(
            json.dumps(
                {
                    "actions": [
                        "content.initialize",
                        "content.summary",
                        "content.solve",
                        "content.compile_lesson",
                        "math.solve_linear",
                        "physics.constant_acceleration",
                        "exam.recommend",
                        "exam.backtest",
                        "exam.forecast",
                        "exam.import_candidates",
                        "exam.render_practice_paper",
                        "matrix.build",
                        "audio.analyze_reference",
                        "production.index_references",
                        "production.record_review",
                        "video.request",
                        "video.lesson_plan",
                        "video.batch_plan",
                        "video.render_batch",
                    ],
                    "limits": {
                        "audio": "Read-only PCM WAV metrics and lesson sound-design guidance are available; this repository does not synthesize or mix audio.",
                        "video": "Batch renderer produces silent visual drafts and currently uses the repository's fixed Manim batch scene.",
                        "exam": "Only source-linked rows marked verified affect recommendations or forecasts.",
                        "matrix": "Concept matching is keyword evidence, not question/topic verification.",
                    },
                },
                indent=2,
            )
        )
        return 0
    try:
        request = _read_json(args.request, "studio request")
        if args.command == "validate":
            normalized = validate_request(request)
            print(
                json.dumps(
                    {
                        "valid": True,
                        "run_id": normalized["run_id"],
                        "task_count": len(normalized["tasks"]),
                        "actions": [
                            {"id": task["id"], "action": task["action"]}
                            for task in normalized["tasks"]
                        ],
                    },
                    indent=2,
                )
            )
            return 0
        report = StudioEngine(args.root).run(
            request,
            output_override=args.output_dir,
        )
    except (StudioRequestError, OSError, UnicodeError) as exc:
        print(f"studio_engine: error: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if report["status"] == "succeeded" else 1


if __name__ == "__main__":
    raise SystemExit(main())
