from manim import *

class BatchEpisode(Scene):
    def construct(self):
        # Title
        title = Tex("Perfectly Elastic Collision", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Two balls
        ball1 = Circle(radius=0.5, color=YELLOW, fill_opacity=1).shift(LEFT * 3)
        ball2 = Circle(radius=0.5, color=BLUE, fill_opacity=1).shift(RIGHT * 3)
        
        # Labels
        label1 = Tex("m", font_size=30).next_to(ball1, DOWN)
        label2 = Tex("m", font_size=30).next_to(ball2, DOWN)
        
        # Velocity arrow for ball1
        arrow = Arrow(
            ball1.get_center() + LEFT * 0.6,
            ball1.get_center() + RIGHT * 0.6,
            color=RED,
            buff=0
        )
        v_label = MathTex("v", color=RED).next_to(arrow, UP, buff=0.1)
        
        self.play(FadeIn(ball1), FadeIn(ball2), FadeIn(label1), FadeIn(label2))
        self.play(GrowArrow(arrow), FadeIn(v_label))
        self.wait(1)

        # Animate collision: ball1 moves right, hits ball2
        self.play(
            ball1.animate.shift(RIGHT * 3),
            arrow.animate.shift(RIGHT * 3),
            v_label.animate.shift(RIGHT * 3),
            run_time=1.5,
            rate_func=linear,
        )
        self.wait(0.3)

        # After collision: ball1 stops, ball2 moves right
        self.play(
            FadeOut(arrow),
            FadeOut(v_label),
            ball1.animate.set_fill(opacity=0.3),
        )
        
        arrow2 = Arrow(
            ball2.get_center() + LEFT * 0.6,
            ball2.get_center() + RIGHT * 0.6,
            color=RED,
            buff=0
        )
        v_label2 = MathTex("v", color=RED).next_to(arrow2, UP, buff=0.1)
        
        self.play(
            ball2.animate.shift(RIGHT * 3),
            GrowArrow(arrow2),
            FadeIn(v_label2),
            run_time=1.5,
            rate_func=linear,
        )
        self.wait(1)

        # Conservation text
        conservation = VGroup(
            MathTex("\\text{Momentum: } mv = mv", font_size=32),
            MathTex("\\text{Kinetic Energy: } \\frac{1}{2}mv^2 = \\frac{1}{2}mv^2", font_size=32),
        ).arrange(DOWN, buff=0.3).to_edge(DOWN)
        
        self.play(Write(conservation))
        self.wait(3)
