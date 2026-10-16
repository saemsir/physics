"""Constant-acceleration kinematics using explicit SI-valued vectors."""

from __future__ import annotations

import math
from numbers import Real
from typing import Sequence

from math_engine.linear_algebra import MathDomainError, Vector, add


def _vector(values: Sequence[float], name: str) -> Vector:
    try:
        raw_values = tuple(values)
        if any(
            isinstance(value, bool) or not isinstance(value, Real)
            for value in raw_values
        ):
            raise MathDomainError(f"{name} must contain real numeric values")
        result = tuple(float(value) for value in raw_values)
    except (TypeError, ValueError, OverflowError) as exc:
        raise MathDomainError(f"{name} must contain real numeric values") from exc
    if not result:
        raise MathDomainError(f"{name} must not be empty")
    if not all(math.isfinite(value) for value in result):
        raise MathDomainError(f"{name} must contain only finite values")
    return result


def constant_acceleration(
    initial_position_m: Sequence[float],
    initial_velocity_m_per_s: Sequence[float],
    acceleration_m_per_s2: Sequence[float],
    time_s: float,
) -> tuple[Vector, Vector]:
    """Return position (m) and velocity (m/s) for constant acceleration."""
    position = _vector(initial_position_m, "initial_position_m")
    velocity = _vector(initial_velocity_m_per_s, "initial_velocity_m_per_s")
    acceleration = _vector(acceleration_m_per_s2, "acceleration_m_per_s2")
    if len(position) != len(velocity) or len(position) != len(acceleration):
        raise MathDomainError("position, velocity, and acceleration dimensions must match")
    try:
        if isinstance(time_s, bool) or not isinstance(time_s, Real):
            raise MathDomainError("time_s must be a finite real number")
        time = float(time_s)
    except (TypeError, ValueError, OverflowError) as exc:
        raise MathDomainError("time_s must be a finite real number") from exc
    if not math.isfinite(time):
        raise MathDomainError("time_s must be finite")
    final_velocity = add(velocity, tuple(value * time for value in acceleration))
    final_position = add(
        add(position, tuple(value * time for value in velocity)),
        tuple(0.5 * value * time * time for value in acceleration),
    )
    if not all(math.isfinite(value) for value in (*final_position, *final_velocity)):
        raise MathDomainError("kinematics result is non-finite")
    return final_position, final_velocity
