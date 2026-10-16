from manim import *

from config.brand import (
    BACKGROUND,
    GRID,
    TEXT,
    VECTOR,
    X_COMPONENT,
    Y_COMPONENT,
)
from animation_engine import vector_decomposition_spec


class VectorComponents(Scene):
    def construct(self):
        spec = vector_decomposition_spec((3.0, 2.0))
        x_value, y_value = spec.components
        x_margin = max(0.75, abs(x_value) * 0.2)
        y_margin = max(0.75, abs(y_value) * 0.2)
        x_min = min(0.0, x_value) - x_margin
        x_max = max(0.0, x_value) + x_margin
        y_min = min(0.0, y_value) - y_margin
        y_max = max(0.0, y_value) + y_margin
        plane_scale = min(
            8.0 / (x_max - x_min),
            4.3 / (y_max - y_min),
        )
        self.camera.background_color = BACKGROUND
        title = Tex("A vector has components", color=TEXT).to_edge(UP)
        plane = NumberPlane(
            x_range=[x_min, x_max, 1],
            y_range=[y_min, y_max, 1],
            x_length=(x_max - x_min) * plane_scale,
            y_length=(y_max - y_min) * plane_scale,
            axis_config={"color": TEXT},
            background_line_style={"stroke_color": GRID, "stroke_opacity": 0.3},
        ).shift(DOWN * 0.2)

        origin = plane.c2p(*spec.origin)
        corner = plane.c2p(*spec.x_component.end)
        tip = plane.c2p(*spec.resultant.end)
        x_value, y_value = spec.components

        x_axis_label = MathTex("x", color=TEXT).next_to(plane.c2p(x_max, 0), DOWN)
        y_axis_label = MathTex("y", color=TEXT).next_to(plane.c2p(0, y_max), LEFT)
        vector = Arrow(origin, tip, buff=0, color=VECTOR)
        x_component = (
            Arrow(origin, corner, buff=0, color=X_COMPONENT)
            if x_value != 0
            else Dot(corner, color=X_COMPONENT)
        )
        y_component = (
            Arrow(corner, tip, buff=0, color=Y_COMPONENT)
            if y_value != 0
            else Dot(tip, color=Y_COMPONENT)
        )

        vector_label = MathTex(r"\vec A", color=VECTOR).next_to(
            plane.c2p(x_value / 2, y_value / 2), UP, buff=0.12
        )
        x_label = MathTex(f"A_x={x_value:g}", color=X_COMPONENT).next_to(
            plane.c2p(x_value / 2, 0), DOWN if y_value >= 0 else UP, buff=0.16
        )
        y_label = MathTex(f"A_y={y_value:g}", color=Y_COMPONENT).next_to(
            plane.c2p(x_value, y_value / 2),
            LEFT if x_value < 0 else RIGHT,
            buff=0.16,
        )
        y_sign = "+" if y_value >= 0 else "-"
        formula = VGroup(
            MathTex(
                rf"\vec A = {x_value:g}\hat{{\imath}} {y_sign} "
                rf"{abs(y_value):g}\hat{{\jmath}}",
                color=TEXT,
            ),
            MathTex(
                rf"|\vec A|=\sqrt{{({x_value:g})^2+({y_value:g})^2}}"
                rf"={spec.magnitude:g}",
                color=TEXT,
            ),
        ).arrange(DOWN, buff=0.1).scale(0.75).to_edge(DOWN)

        self.play(Write(title), Create(plane))
        self.play(FadeIn(x_axis_label), FadeIn(y_axis_label))
        self.wait(5)
        self.play(GrowArrow(vector), FadeIn(vector_label))
        self.wait(4)
        self.play(Create(x_component), FadeIn(x_label))
        self.wait(5)
        self.play(Create(y_component), FadeIn(y_label))
        self.wait(5)
        self.play(Write(formula))
        self.wait(8)
        self.wait(4)
