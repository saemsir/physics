"""Renderer-neutral sampled trajectory specification for constant acceleration."""

from __future__ import annotations

from dataclasses import asdict, dataclass
import math
from numbers import Integral
from typing import Sequence

from math_engine import MathDomainError
from physics_engine import constant_acceleration


@dataclass(frozen=True)
class MotionSceneSpec:
    coordinate_system: str
    unit_system: str
    time_s: tuple[float, ...]
    position_m: tuple[tuple[float, ...], ...]
    velocity_m_per_s: tuple[tuple[float, ...], ...]
    final_position_m: tuple[float, ...]
    final_velocity_m_per_s: tuple[float, ...]
    invariant: str

    def to_dict(self) -> dict:
        return asdict(self)


def motion_scene_spec(
    initial_position_m: Sequence[float],
    initial_velocity_m_per_s: Sequence[float],
    acceleration_m_per_s2: Sequence[float],
    duration_s: float,
    *,
    samples: int = 31,
) -> MotionSceneSpec:
    if isinstance(samples, bool) or not isinstance(samples, Integral) or samples < 2:
        raise MathDomainError("samples must be an integer greater than or equal to 2")
    try:
        duration = float(duration_s)
    except (TypeError, ValueError, OverflowError) as exc:
        raise MathDomainError("duration_s must be finite and nonnegative") from exc
    if not math.isfinite(duration) or duration < 0:
        raise MathDomainError("duration_s must be finite and nonnegative")

    try:
        position = tuple(initial_position_m)
        velocity = tuple(initial_velocity_m_per_s)
        acceleration = tuple(acceleration_m_per_s2)
    except TypeError as exc:
        raise MathDomainError("motion scene inputs must be finite numeric vectors") from exc
    if not 1 <= len(position) <= 2:
        raise MathDomainError("motion scene currently supports one or two spatial dimensions")

    times = tuple(duration * index / (samples - 1) for index in range(samples))
    states = tuple(
        constant_acceleration(
            position,
            velocity,
            acceleration,
            time,
        )
        for time in times
    )
    final_position, final_velocity = states[-1]
    return MotionSceneSpec(
        coordinate_system="Cartesian physical coordinates",
        unit_system="SI",
        time_s=times,
        position_m=tuple(state[0] for state in states),
        velocity_m_per_s=tuple(state[1] for state in states),
        final_position_m=final_position,
        final_velocity_m_per_s=final_velocity,
        invariant="Samples are generated from the validated constant-acceleration model.",
    )
