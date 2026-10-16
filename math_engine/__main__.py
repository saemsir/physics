"""Small, explicit command-line interface for supported linear algebra."""

from __future__ import annotations

import argparse
import json
import sys

from .linear_algebra import MathDomainError, solve_linear_system


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="python -m math_engine")
    subparsers = parser.add_subparsers(dest="command", required=True)
    solve = subparsers.add_parser("solve-linear", help="solve a square real linear system")
    solve.add_argument(
        "--matrix",
        required=True,
        help='JSON matrix, for example "[[2,1],[1,3]]"',
    )
    solve.add_argument(
        "--rhs",
        required=True,
        help='JSON right-hand-side vector, for example "[5,7]"',
    )
    args = parser.parse_args(argv)
    try:
        matrix = json.loads(args.matrix)
        rhs = json.loads(args.rhs)
        result = solve_linear_system(matrix, rhs)
    except (json.JSONDecodeError, TypeError, MathDomainError) as exc:
        print(f"math_engine: error: {exc}", file=sys.stderr)
        return 2
    print(
        json.dumps(
            {
                "solution": result.values,
                "residual_inf_norm": result.residual_inf_norm,
                "numeric_type": "IEEE-754 binary64",
                "warning": "Check model assumptions and conditioning independently.",
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
