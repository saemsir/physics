"""Calculation-backed animation specifications."""

from .vector_scene import (
    ArrowSpec,
    VectorDecompositionSpec,
    vector_decomposition_spec,
)
from .motion_scene import MotionSceneSpec, motion_scene_spec

__all__ = [
    "ArrowSpec",
    "MotionSceneSpec",
    "VectorDecompositionSpec",
    "motion_scene_spec",
    "vector_decomposition_spec",
]
