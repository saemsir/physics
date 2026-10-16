"""Create a visual specification from a validated two-dimensional vector."""

from __future__ import annotations

import math
from dataclasses import dataclass
from numbers import Real
from typing import Sequence

from math_engine.linear_algebra import MathDomainError, norm


@dataclass(frozen=True)
class ArrowSpec:
    start: tuple[float, float]
    end: tuple[float, float]


@dataclass(frozen=True)
class VectorDecompositionSpec:
    coordinate_system: str
    origin: tuple[float, float]
    x_component: ArrowSpec
    y_component: ArrowSpec
    resultant: ArrowSpec
    components: tuple[float, float]
    magnitude: float
    invariant: tuple[tuple[float, float], tuple[float, float]]


def vector_decomposition_spec(
    components: Sequence[float],
) -> VectorDecompositionSpec:
    """Return diagram coordinates whose component arrows sum to the vector."""
    try:
        raw_components = tuple(components)
        if any(
            isinstance(value, bool) or not isinstance(value, Real)
            for value in raw_components
        ):
            raise MathDomainError("vector components must be real numeric values")
        vector = tuple(float(value) for value in raw_components)
    except (TypeError, ValueError, OverflowError) as exc:
        raise MathDomainError("vector components must be real numeric values") from exc
    if len(vector) != 2:
        raise MathDomainError("vector decomposition animation requires exactly 2 components")
    if not all(math.isfinite(value) for value in vector):
        raise MathDomainError("vector components must be finite")
    x_component, y_component = vector
    if x_component == 0 and y_component == 0:
        raise MathDomainError("zero vector has no visible resultant arrow")
    magnitude = norm(vector)
    return VectorDecompositionSpec(
        coordinate_system="Cartesian, schematic units",
        origin=(0.0, 0.0),
        x_component=ArrowSpec((0.0, 0.0), (x_component, 0.0)),
        y_component=ArrowSpec((x_component, 0.0), (x_component, y_component)),
        resultant=ArrowSpec((0.0, 0.0), (x_component, y_component)),
        components=(x_component, y_component),
        magnitude=magnitude,
        invariant=(
            (x_component, 0.0),
            (0.0, y_component),
        ),
    )
