"""Small dense linear algebra routines for inspectable teaching examples.

All values are IEEE-754 Python floats. This module rejects malformed and
non-finite input; it does not claim exact arithmetic or guaranteed accuracy
for ill-conditioned systems.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
from numbers import Real
from typing import Sequence

Vector = tuple[float, ...]
Matrix = tuple[tuple[float, ...], ...]


class MathDomainError(ValueError):
    """Raised when an operation receives malformed or invalid numeric input."""


@dataclass(frozen=True)
class LinearSolution:
    values: Vector
    residual_inf_norm: float


def _finite_vector(values: Sequence[float], name: str) -> Vector:
    try:
        raw_values = tuple(values)
    except TypeError as exc:
        raise MathDomainError(f"{name} must be a vector of real numbers") from exc
    if not raw_values:
        raise MathDomainError(f"{name} must not be empty")
    try:
        if any(
            isinstance(value, bool) or not isinstance(value, Real)
            for value in raw_values
        ):
            raise MathDomainError(f"{name} must contain real numeric values")
        result = tuple(float(value) for value in raw_values)
    except (TypeError, ValueError, OverflowError) as exc:
        raise MathDomainError(f"{name} must contain real numeric values") from exc
    if not all(math.isfinite(value) for value in result):
        raise MathDomainError(f"{name} must contain only finite values")
    return result


def _finite_matrix(values: Sequence[Sequence[float]], name: str) -> Matrix:
    try:
        raw_rows = tuple(tuple(row) for row in values)
    except TypeError as exc:
        raise MathDomainError(f"{name} must be a rectangular numeric matrix") from exc
    if not raw_rows or not raw_rows[0]:
        raise MathDomainError(f"{name} must not be empty")
    width = len(raw_rows[0])
    if any(len(row) != width for row in raw_rows):
        raise MathDomainError(f"{name} must be rectangular")
    result = tuple(_finite_vector(row, f"{name} row") for row in raw_rows)
    return result


def add(left: Sequence[float], right: Sequence[float]) -> Vector:
    a = _finite_vector(left, "left vector")
    b = _finite_vector(right, "right vector")
    if len(a) != len(b):
        raise MathDomainError("vectors must have equal dimensions")
    try:
        result = tuple(x + y for x, y in zip(a, b))
    except OverflowError as exc:
        raise MathDomainError("vector addition overflowed") from exc
    if not all(math.isfinite(value) for value in result):
        raise MathDomainError("vector addition overflowed to a non-finite value")
    return result


def subtract(left: Sequence[float], right: Sequence[float]) -> Vector:
    a = _finite_vector(left, "left vector")
    b = _finite_vector(right, "right vector")
    if len(a) != len(b):
        raise MathDomainError("vectors must have equal dimensions")
    try:
        result = tuple(x - y for x, y in zip(a, b))
    except OverflowError as exc:
        raise MathDomainError("vector subtraction overflowed") from exc
    if not all(math.isfinite(value) for value in result):
        raise MathDomainError("vector subtraction overflowed to a non-finite value")
    return result


def dot(left: Sequence[float], right: Sequence[float]) -> float:
    a = _finite_vector(left, "left vector")
    b = _finite_vector(right, "right vector")
    if len(a) != len(b):
        raise MathDomainError("vectors must have equal dimensions")
    try:
        result = math.fsum(x * y for x, y in zip(a, b))
    except (OverflowError, ValueError) as exc:
        raise MathDomainError("dot product overflowed") from exc
    if not math.isfinite(result):
        raise MathDomainError("dot product overflowed to a non-finite value")
    return result


def norm(vector: Sequence[float]) -> float:
    values = _finite_vector(vector, "vector")
    result = math.hypot(*values)
    if not math.isfinite(result):
        raise MathDomainError("vector norm overflowed to a non-finite value")
    return result


def matvec(matrix: Sequence[Sequence[float]], vector: Sequence[float]) -> Vector:
    rows = _finite_matrix(matrix, "matrix")
    values = _finite_vector(vector, "vector")
    if len(rows[0]) != len(values):
        raise MathDomainError("matrix columns must equal vector dimension")
    return tuple(dot(row, values) for row in rows)


def solve_linear_system(
    matrix: Sequence[Sequence[float]],
    right_hand_side: Sequence[float],
    *,
    relative_pivot_tolerance: float = 1e-12,
) -> LinearSolution:
    """Solve a square system by Gaussian elimination with partial pivoting."""
    coefficients = _finite_matrix(matrix, "matrix")
    rhs = _finite_vector(right_hand_side, "right-hand side")
    size = len(coefficients)
    if len(rhs) != size or any(len(row) != size for row in coefficients):
        raise MathDomainError("matrix must be square and match right-hand-side length")
    if not math.isfinite(relative_pivot_tolerance) or relative_pivot_tolerance <= 0:
        raise MathDomainError("relative_pivot_tolerance must be finite and positive")
    scale = max(abs(value) for row in coefficients for value in row)
    if scale == 0:
        raise MathDomainError("matrix is singular")

    augmented = [list(row) + [rhs[index]] for index, row in enumerate(coefficients)]
    threshold = relative_pivot_tolerance * scale
    for pivot_column in range(size):
        pivot_row = max(
            range(pivot_column, size),
            key=lambda row_index: abs(augmented[row_index][pivot_column]),
        )
        pivot = augmented[pivot_row][pivot_column]
        if abs(pivot) <= threshold:
            raise MathDomainError(
                "matrix is singular or numerically ill-conditioned at the pivot tolerance"
            )
        augmented[pivot_column], augmented[pivot_row] = (
            augmented[pivot_row],
            augmented[pivot_column],
        )
        pivot = augmented[pivot_column][pivot_column]
        for row_index in range(pivot_column + 1, size):
            factor = augmented[row_index][pivot_column] / pivot
            augmented[row_index][pivot_column] = 0.0
            for column in range(pivot_column + 1, size + 1):
                augmented[row_index][column] -= (
                    factor * augmented[pivot_column][column]
                )

    solution = [0.0] * size
    for row_index in range(size - 1, -1, -1):
        try:
            remainder = math.fsum(
                augmented[row_index][column] * solution[column]
                for column in range(row_index + 1, size)
            )
        except (OverflowError, ValueError) as exc:
            raise MathDomainError("back substitution overflowed") from exc
        solution[row_index] = (
            augmented[row_index][size] - remainder
        ) / augmented[row_index][row_index]
        if not math.isfinite(solution[row_index]):
            raise MathDomainError("linear solve produced a non-finite value")

    try:
        residual = tuple(
            math.fsum(
                coefficients[row][column] * solution[column]
                for column in range(size)
            )
            - rhs[row]
            for row in range(size)
        )
    except (OverflowError, ValueError) as exc:
        raise MathDomainError("linear solve residual overflowed") from exc
    residual_inf_norm = max(abs(value) for value in residual)
    if not math.isfinite(residual_inf_norm):
        raise MathDomainError("linear solve residual is non-finite")
    return LinearSolution(tuple(solution), residual_inf_norm)
