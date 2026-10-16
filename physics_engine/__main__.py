"""Command-line interface for the supported constant-acceleration model."""

from __future__ import annotations

import argparse
import json
import sys

from math_engine.linear_algebra import MathDomainError

from .kinematics import constant_acceleration


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="python -m physics_engine")
    subparsers = parser.add_subparsers(dest="command", required=True)
    motion = subparsers.add_parser(
        "constant-acceleration",
        help="evaluate a constant-acceleration model in SI units",
    )
    motion.add_argument("--position-m", required=True, help="JSON position vector in metres")
    motion.add_argument(
        "--velocity-m-per-s", required=True, help="JSON velocity vector in metres/second"
    )
    motion.add_argument(
        "--acceleration-m-per-s2",
        required=True,
        help="JSON acceleration vector in metres/second squared",
    )
    motion.add_argument("--time-s", required=True, type=float, help="time in seconds")
    args = parser.parse_args(argv)
    try:
        position = json.loads(args.position_m)
        velocity = json.loads(args.velocity_m_per_s)
        acceleration = json.loads(args.acceleration_m_per_s2)
        final_position, final_velocity = constant_acceleration(
            position,
            velocity,
            acceleration,
            args.time_s,
        )
    except (json.JSONDecodeError, TypeError, MathDomainError) as exc:
        print(f"physics_engine: error: {exc}", file=sys.stderr)
        return 2
    print(
        json.dumps(
            {
                "position_m": final_position,
                "velocity_m_per_s": final_velocity,
                "model": "constant acceleration in a specified inertial frame",
                "warning": "Validate model assumptions and initial conditions independently.",
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
