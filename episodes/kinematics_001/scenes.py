"""Render the calculation-backed trajectory from a compiled lesson IR."""

from __future__ import annotations

import json
import os
from pathlib import Path

from manim import *

from config.brand import BACKGROUND, GRID, TEXT, VECTOR, Y_COMPONENT


def _lesson_ir() -> dict:
    default = (
        Path(__file__).resolve().parents[2]
        / "output"
        / "lessons"
        / "lesson-constant-acceleration-demo.json"
    )
    path = Path(os.environ.get("SAEMPHYSICS_LESSON_IR", default))
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"cannot load lesson IR {path}: {exc}") from exc


class KinematicsMotion(Scene):
    def construct(self):
        lesson = _lesson_ir()
        scene_data = next(
            (
                scene["visual_spec"]
                for scene in lesson["scenes"]
                if scene["scene_id"] == "motion-solution"
            ),
            None,
        )
        if scene_data is None or "trajectory" not in scene_data:
            raise ValueError("lesson IR is missing the calculation-backed motion scene")

        trajectory_data = scene_data["trajectory"]
        positions = trajectory_data["position_m"]
        coordinates = [
            (position[0], position[1] if len(position) > 1 else 0.0)
            for position in positions
        ]
        x_values = [point[0] for point in coordinates]
        y_values = [point[1] for point in coordinates]
        x_margin = max((max(x_values) - min(x_values)) * 0.12, 0.5)
        y_margin = max((max(y_values) - min(y_values)) * 0.12, 0.5)
        x_range = [min(x_values) - x_margin, max(x_values) + x_margin, 1]
        y_range = [min(y_values) - y_margin, max(y_values) + y_margin, 1]

        self.camera.background_color = BACKGROUND
        title = Text(lesson["title"], color=TEXT, font_size=34).to_edge(UP)
        axes = Axes(
            x_range=x_range,
            y_range=y_range,
            x_length=9.4,
            y_length=4.1,
            axis_config={"color": TEXT},
            tips=False,
        ).shift(UP * 0.1)
        axes.add_coordinates()
        axes.set_color(GRID)

        points = [axes.c2p(x, y) for x, y in coordinates]
        path = VMobject(color=VECTOR, stroke_width=5).set_points_as_corners(points)
        particle = Dot(points[0], color=Y_COMPONENT, radius=0.11)
        final_position = scene_data["position_m"]
        final_velocity = scene_data["velocity_m_per_s"]
        final_x = final_position[0]
        final_y = final_position[1] if len(final_position) > 1 else 0.0
        velocity_x = final_velocity[0]
        velocity_y = final_velocity[1] if len(final_velocity) > 1 else 0.0
        result = MathTex(
            rf"\vec r_f=({final_x:.2f},{final_y:.2f})\,\mathrm{{m}}",
            rf"\qquad \vec v_f=({velocity_x:.2f},{velocity_y:.2f})\,\mathrm{{m/s}}",
            color=TEXT,
        ).scale(0.72).to_edge(DOWN, buff=0.35)
        note = Text(
            "Axes in metres; trajectory sampled from the stated constant-acceleration model.",
            color=TEXT,
            font_size=16,
        ).next_to(result, UP, buff=0.12)

        self.play(Write(title), Create(axes))
        self.add(particle)
        self.play(Create(path), run_time=1.2)
        self.play(MoveAlongPath(particle, path), run_time=4, rate_func=linear)
        self.play(FadeIn(result), FadeIn(note))
        self.wait(2)
