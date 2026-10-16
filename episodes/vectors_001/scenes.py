from manim import *

from config.brand import (
    BACKGROUND,
    GRID,
    TEXT,
    VECTOR,
    X_COMPONENT,
    Y_COMPONENT,
)


class VectorComponents(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        title = Tex("A vector has components", color=TEXT).to_edge(UP)
        plane = NumberPlane(
            x_range=[-1, 5, 1],
            y_range=[-1, 4, 1],
            x_length=8,
            y_length=5,
            axis_config={"color": TEXT},
            background_line_style={"stroke_color": GRID, "stroke_opacity": 0.3},
        ).shift(DOWN * 0.2)

        origin = plane.c2p(0, 0)
        corner = plane.c2p(3, 0)
        tip = plane.c2p(3, 2)

        x_axis_label = MathTex("x", color=TEXT).next_to(
            plane.c2p(4.5, 0), DOWN
        )
        y_axis_label = MathTex("y", color=TEXT).next_to(
            plane.c2p(0, 3.5), LEFT
        )
        vector = Arrow(origin, tip, buff=0, color=VECTOR)
        x_component = Arrow(origin, corner, buff=0, color=X_COMPONENT)
        y_component = Arrow(corner, tip, buff=0, color=Y_COMPONENT)

        vector_label = MathTex(r"\vec A", color=VECTOR).next_to(
            plane.c2p(1.5, 1), UP, buff=0.12
        )
        x_label = MathTex("A_x=3", color=X_COMPONENT).next_to(
            plane.c2p(1.5, 0), DOWN, buff=0.16
        )
        y_label = MathTex("A_y=2", color=Y_COMPONENT).next_to(
            plane.c2p(3, 1), RIGHT, buff=0.16
        )
        formula = VGroup(
            MathTex(r"\vec A = 3\hat{\imath} + 2\hat{\jmath}", color=TEXT),
            MathTex(r"|\vec A|=\sqrt{3^2+2^2}=\sqrt{13}", color=TEXT),
        ).arrange(DOWN, buff=0.1).scale(0.75).to_edge(DOWN)

        self.play(Write(title), Create(plane))
        self.play(FadeIn(x_axis_label), FadeIn(y_axis_label))
        self.wait(5)
        self.play(GrowArrow(vector), FadeIn(vector_label))
        self.wait(4)
        self.play(GrowArrow(x_component), FadeIn(x_label))
        self.wait(5)
        self.play(GrowArrow(y_component), FadeIn(y_label))
        self.wait(5)
        self.play(Write(formula))
        self.wait(8)
        self.wait(4)
