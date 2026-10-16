from __future__ import annotations

import math
import unittest

from animation_engine import motion_scene_spec, vector_decomposition_spec
from math_engine import (
    MathDomainError,
    add,
    dot,
    matvec,
    norm,
    solve_linear_system,
    subtract,
)
from physics_engine import constant_acceleration


class LinearAlgebraTests(unittest.TestCase):
    def test_vector_operations(self) -> None:
        self.assertEqual(add((1, 2), (3, -2)), (4.0, 0.0))
        self.assertEqual(subtract((1, 2), (3, -2)), (-2.0, 4.0))
        self.assertEqual(dot((1, 2), (3, 4)), 11.0)
        self.assertEqual(norm((3, 4)), 5.0)

    def test_matrix_vector_product(self) -> None:
        self.assertEqual(matvec(((2, 1), (1, 3)), (3, 4)), (10.0, 15.0))

    def test_linear_solve_with_row_swap_and_small_residual(self) -> None:
        result = solve_linear_system(((0, 2), (1, 1)), (4, 3))
        self.assertEqual(result.values, (1.0, 2.0))
        self.assertLess(result.residual_inf_norm, 1e-12)

    def test_singular_system_rejected(self) -> None:
        with self.assertRaisesRegex(MathDomainError, "singular"):
            solve_linear_system(((1, 2), (2, 4)), (3, 6))

    def test_dimension_mismatch_rejected(self) -> None:
        with self.assertRaisesRegex(MathDomainError, "equal dimensions"):
            dot((1, 2), (3,))

    def test_non_vector_input_rejected(self) -> None:
        with self.assertRaisesRegex(MathDomainError, "vector of real numbers"):
            norm(3)

    def test_non_finite_input_rejected(self) -> None:
        with self.assertRaisesRegex(MathDomainError, "finite"):
            norm((1, math.inf))

    def test_boolean_is_not_accepted_as_a_physical_number(self) -> None:
        with self.assertRaisesRegex(MathDomainError, "real numeric"):
            norm((True, 2))

    def test_overflow_rejected(self) -> None:
        with self.assertRaisesRegex(MathDomainError, "non-finite"):
            add((1e308,), (1e308,))


class PhysicsAndAnimationTests(unittest.TestCase):
    def test_constant_acceleration_result(self) -> None:
        position, velocity = constant_acceleration(
            (1, 0), (2, 3), (0, -2), 2
        )
        self.assertEqual(position, (5.0, 2.0))
        self.assertEqual(velocity, (2.0, -1.0))

    def test_constant_acceleration_requires_matching_dimensions(self) -> None:
        with self.assertRaisesRegex(MathDomainError, "dimensions must match"):
            constant_acceleration((0, 0), (0, 0), (0,), 1)

    def test_vector_scene_preserves_component_sum(self) -> None:
        spec = vector_decomposition_spec((-3, 4))
        self.assertEqual(spec.x_component.end, spec.y_component.start)
        self.assertEqual(spec.y_component.end, spec.resultant.end)
        self.assertEqual(spec.resultant.end, (-3.0, 4.0))
        self.assertEqual(spec.magnitude, 5.0)

    def test_scene_rejects_non_two_dimensional_input(self) -> None:
        with self.assertRaisesRegex(MathDomainError, "exactly 2"):
            vector_decomposition_spec((1, 2, 3))

    def test_scene_rejects_zero_resultant(self) -> None:
        with self.assertRaisesRegex(MathDomainError, "zero vector"):
            vector_decomposition_spec((0, 0))

    def test_motion_scene_samples_physical_trajectory_and_endpoints(self) -> None:
        spec = motion_scene_spec((0, 0), (5, 12), (0, -2), 4, samples=5)
        self.assertEqual(len(spec.time_s), 5)
        self.assertEqual(spec.time_s[0], 0.0)
        self.assertEqual(spec.position_m[0], (0.0, 0.0))
        self.assertEqual(spec.final_position_m, (20.0, 32.0))
        self.assertEqual(spec.final_velocity_m_per_s, (5.0, 4.0))

    def test_motion_scene_rejects_dimensions_the_renderer_cannot_show(self) -> None:
        with self.assertRaisesRegex(MathDomainError, "one or two spatial dimensions"):
            motion_scene_spec((0, 0, 0), (1, 2, 3), (0, 0, 0), 1)
        with self.assertRaisesRegex(MathDomainError, "duration_s"):
            motion_scene_spec((0,), (1,), (0,), -1)


if __name__ == "__main__":
    unittest.main()
