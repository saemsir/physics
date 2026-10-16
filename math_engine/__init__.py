"""Deterministic numerical primitives with explicit finite-value checks."""

from .linear_algebra import (
    LinearSolution,
    MathDomainError,
    add,
    dot,
    matvec,
    norm,
    solve_linear_system,
    subtract,
)

__all__ = [
    "LinearSolution",
    "MathDomainError",
    "add",
    "dot",
    "matvec",
    "norm",
    "solve_linear_system",
    "subtract",
]
