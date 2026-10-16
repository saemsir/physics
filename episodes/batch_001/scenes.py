"""Reusable, original Manim scene for the approved first-batch storyboards."""

from __future__ import annotations

import json
import os
from pathlib import Path
import textwrap

from manim import *

from config.brand import BACKGROUND, GRID, TEXT, VECTOR, X_COMPONENT, Y_COMPONENT


def _load_video() -> dict:
    plan_path = Path(os.environ.get("SAEMPHYSICS_BATCH_PLAN", ""))
    video_id = os.environ.get("SAEMPHYSICS_VIDEO_ID", "")
    if not plan_path.is_file() or not video_id:
        raise RuntimeError(
            "set SAEMPHYSICS_BATCH_PLAN and SAEMPHYSICS_VIDEO_ID before rendering"
        )
    try:
        plan = json.loads(plan_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"cannot read batch render plan {plan_path}: {exc}") from exc
    matches = [
        item for item in plan.get("deliverables", [])
        if item.get("video_id") == video_id
    ]
    if len(matches) != 1:
        raise ValueError(f"render plan must contain exactly one {video_id!r} deliverable")
    return matches[0]


def _text_lines(value: str, *, width: int, size: float, color=TEXT) -> VGroup:
    lines = textwrap.wrap(value, width=width, break_long_words=False) or [value]
    group = VGroup(
        *[
            Text(line, font_size=size, color=color, line_spacing=0.8)
            for line in lines
        ]
    ).arrange(DOWN, buff=0.12)
    return group


def _box(left: str, right: str) -> VGroup:
    a = Rectangle(width=1.7, height=1.1, color=X_COMPONENT)
    b = Rectangle(width=1.7, height=1.1, color=Y_COMPONENT)
    a_label = Text(left, font_size=22, color=TEXT).move_to(a)
    b_label = Text(right, font_size=22, color=TEXT).move_to(b)
    a_group = VGroup(a, a_label).shift(LEFT * 2.2)
    b_group = VGroup(b, b_label).shift(RIGHT * 2.2)
    return VGroup(a_group, b_group)


def _diagram(episode_id: str) -> VGroup:
    if episode_id == "b001-e01-projectile-components":
        axes = Axes(
            x_range=[0, 7, 1], y_range=[-1, 4, 1],
            x_length=7, y_length=3.2, tips=False,
            axis_config={"color": GRID, "include_numbers": True},
        )
        path = axes.plot(lambda x: 8 * x / 6 - 10 * (x / 6) ** 2 / 2,
                         x_range=[0, 6], color=VECTOR, stroke_width=5)
        start = Dot(axes.c2p(0, 0), color=Y_COMPONENT)
        end = Dot(axes.c2p(6, 3), color=X_COMPONENT)
        velocity = Arrow(axes.c2p(6, 3), axes.c2p(6.8, 2.6), buff=0, color=Y_COMPONENT)
        return VGroup(axes, path, start, end, velocity)
    if episode_id == "b001-e02-vector-displacement":
        origin, east, finish = ORIGIN, RIGHT * 3, RIGHT * 3 + UP * 4
        path_x = Arrow(origin, east, buff=0, color=X_COMPONENT, stroke_width=7)
        path_y = Arrow(east, finish, buff=0, color=Y_COMPONENT, stroke_width=7)
        displacement = Arrow(origin, finish, buff=0, color=VECTOR, stroke_width=4)
        labels = VGroup(
            Text("3 m east", font_size=22, color=X_COMPONENT).next_to(path_x, DOWN),
            Text("4 m north", font_size=22, color=Y_COMPONENT).next_to(path_y, RIGHT),
            Text("5 m displacement", font_size=22, color=VECTOR).next_to(
                displacement, UP, buff=0.15
            ),
        )
        return VGroup(path_x, path_y, displacement, labels)
    if episode_id == "b001-e03-dropped-stone":
        rail = Line(UP * 2.1, DOWN * 2.1, color=GRID, stroke_width=4)
        start = Dot(rail.get_top(), color=Y_COMPONENT)
        ground = Line(LEFT * 1.2 + DOWN * 2.1, RIGHT * 1.2 + DOWN * 2.1, color=TEXT)
        arrow = Arrow(UP * 1.2, DOWN * 0.6, buff=0, color=VECTOR, stroke_width=6)
        labels = VGroup(
            Text("45 m", font_size=24, color=TEXT).next_to(rail, RIGHT),
            Text("g downward", font_size=20, color=VECTOR).next_to(arrow, RIGHT),
            Text("ground", font_size=18, color=TEXT).next_to(ground, DOWN),
        )
        return VGroup(rail, start, ground, arrow, labels)
    if episode_id == "b001-e04-velocity-graph":
        axes = Axes(
            x_range=[0, 4, 1], y_range=[-1, 4, 1],
            x_length=6.5, y_length=3.2, tips=False,
            axis_config={"color": GRID, "include_numbers": True},
        )
        line = axes.plot(lambda t: t - 1, x_range=[0, 4], color=VECTOR, stroke_width=5)
        above = axes.get_area(line, x_range=[1, 4], color=Y_COMPONENT, opacity=0.35)
        below = axes.get_area(line, x_range=[0, 1], color=X_COMPONENT, opacity=0.35)
        labels = VGroup(
            Text("velocity", font_size=18, color=TEXT).next_to(axes.y_axis, UP),
            Text("time", font_size=18, color=TEXT).next_to(axes.x_axis, RIGHT),
            Text("slope = acceleration", font_size=18, color=Y_COMPONENT).to_edge(UP),
        )
        return VGroup(axes, above, below, line, labels)
    if episode_id == "b001-e05-upward-throw":
        arc = VMobject(color=VECTOR, stroke_width=5).set_points_smoothly(
            [
                LEFT * 2.1 + DOWN * 1.1,
                LEFT * 1.2 + UP * 0.8,
                UP * 1.4,
                RIGHT * 1.2 + UP * 0.8,
                RIGHT * 2.1 + DOWN * 1.1,
            ]
        )
        ball = Dot(UP * 1.4, color=Y_COMPONENT, radius=0.13)
        velocity = Arrow(UP * 1.2, UP * 2.1, buff=0, color=X_COMPONENT, stroke_width=5)
        gravity = Arrow(RIGHT * 1.2 + UP * 1.8, RIGHT * 1.2 + UP * 0.8,
                        buff=0, color=VECTOR, stroke_width=5)
        labels = VGroup(
            Text("v upward", font_size=19, color=X_COMPONENT).next_to(velocity, LEFT),
            Text("g downward", font_size=19, color=VECTOR).next_to(gravity, RIGHT),
        )
        return VGroup(arc, ball, velocity, gravity, labels)
    if episode_id == "b001-e06-newtons-third-law":
        pair = _box("person", "wall")
        left_force = Arrow(LEFT * 0.8, RIGHT * 0.5, buff=0, color=VECTOR, stroke_width=7)
        right_force = Arrow(RIGHT * 0.8, LEFT * 0.5, buff=0, color=Y_COMPONENT, stroke_width=7)
        left_force.shift(LEFT * 2.2 + UP * 1.2)
        right_force.shift(RIGHT * 2.2 + UP * 1.2)
        return VGroup(pair, left_force, right_force)
    if episode_id == "b001-e07-sticking-carts":
        first = VGroup(
            Rectangle(width=1.3, height=0.8, color=X_COMPONENT),
            Text("2 kg", font_size=20, color=TEXT),
        ).shift(LEFT * 2.4)
        second = VGroup(
            Rectangle(width=1.3, height=0.8, color=Y_COMPONENT),
            Text("1 kg", font_size=20, color=TEXT),
        ).shift(RIGHT * 2.4)
        momentum_before = Arrow(LEFT * 3.1, LEFT * 0.7, buff=0, color=VECTOR)
        after = VGroup(
            Rectangle(width=2, height=0.9, color=Y_COMPONENT),
            Text("3 kg at 2 m/s", font_size=20, color=TEXT),
        )
        label = Text("before collision", font_size=19, color=TEXT).to_edge(UP)
        result = VGroup(first, second, momentum_before, after)
        result.scale(0.9)
        after.shift(DOWN * 1.4)
        label.shift(UP * 1.2)
        return VGroup(result, label)
    if episode_id == "b001-e08-momentum-boundary":
        boundary = DashedVMobject(Rectangle(width=6.3, height=2.4, color=VECTOR))
        first, second = _box("cart A", "cart B")
        inner = Arrow(LEFT * 1.1, RIGHT * 1.1, buff=0, color=X_COMPONENT)
        outer = Arrow(LEFT * 3.8, LEFT * 3.0, buff=0, color=Y_COMPONENT)
        note = Text("system boundary", font_size=19, color=VECTOR).next_to(boundary, DOWN)
        return VGroup(boundary, first, second, inner, outer, note)
    if episode_id == "b001-e09-falling-energy":
        potential = Rectangle(width=1.1, height=3, color=VECTOR, fill_opacity=0.45)
        kinetic = Rectangle(width=1.1, height=3, color=Y_COMPONENT, fill_opacity=0.45)
        potential.shift(LEFT * 2.0)
        kinetic.shift(RIGHT * 2.0)
        arrow = Arrow(LEFT * 0.8, RIGHT * 0.8, buff=0, color=TEXT)
        labels = VGroup(
            Text("mgh = 50 J", font_size=21, color=VECTOR).next_to(potential, DOWN),
            Text("1/2 mv^2 = 50 J", font_size=21, color=Y_COMPONENT).next_to(kinetic, DOWN),
        )
        return VGroup(potential, kinetic, arrow, labels)
    if episode_id == "b001-e10-kinetic-energy-collision":
        bars = VGroup()
        labels = VGroup()
        for x, height, color, label in (
            (-2.3, 2.5, VECTOR, "kinetic"),
            (0, 1.6, X_COMPONENT, "internal + sound"),
            (2.3, 2.5, Y_COMPONENT, "total"),
        ):
            bar = Rectangle(width=1.1, height=height, color=color, fill_opacity=0.4)
            bar.move_to(RIGHT * x + UP * (height / 2))
            bars.add(bar)
            labels.add(Text(label, font_size=17, color=color).next_to(bar, DOWN))
        return VGroup(bars, labels)
    raise ValueError(f"no original diagram is defined for {episode_id!r}")


class BatchEpisode(Scene):
    def construct(self):
        video = _load_video()
        self.camera.background_color = BACKGROUND
        vertical = video["format"] == "vertical"
        frame_width = config.frame_width
        frame_height = config.frame_height
        base_size = 26 if vertical else 34
        max_line = 35 if vertical else 66
        text_width = frame_width * 0.88
        body_region = frame_height * 0.54
        brand = VGroup(
            Text("Saem Physics", font_size=24 if vertical else 26, color=VECTOR),
            Text("NEET JEE MIT", font_size=15 if vertical else 17, color=TEXT),
        ).arrange(DOWN, buff=0.02).to_edge(UP, buff=0.2)
        self.add(brand)
        current: Mobject | None = None

        def page(heading: str, body: str, color=TEXT) -> VGroup:
            title = Text(
                heading,
                font_size=base_size + 4,
                color=VECTOR,
                weight=BOLD,
            )
            paragraph = _text_lines(body, width=max_line, size=base_size, color=color)
            group = VGroup(title, paragraph).arrange(DOWN, buff=0.32)
            group.scale_to_fit_width(text_width)
            group.scale_to_fit_height(body_region)
            group.move_to(DOWN * (0.06 * frame_height))
            return group

        def show(group: Mobject, duration: float):
            nonlocal current
            transition = min(1.0, duration / 3)
            if current is None:
                self.play(FadeIn(group, shift=UP * 0.1), run_time=transition)
            else:
                self.play(
                    FadeOut(current),
                    FadeIn(group, shift=UP * 0.1),
                    run_time=transition,
                )
            remaining = duration - transition
            if remaining > 0:
                self.wait(remaining)
            current = group

        visual = _diagram(video["episode_id"])
        visual.scale_to_fit_width(min(frame_width * 0.82, 11.5))
        visual.scale_to_fit_height(frame_height * 0.42)
        visual.move_to(DOWN * (0.06 * frame_height))
        for beat in video["story_beats"]:
            name = beat["name"]
            duration = beat["duration_seconds"]
            if name == "hook":
                group = page(video["title"], video["visual_hook"], VECTOR)
            elif name == "question":
                group = page("THE QUESTION", video["question"])
            elif name == "visual_model":
                cue = _text_lines(
                    video["topic_id"].replace("_", " "),
                    width=max_line,
                    size=max(18, base_size - 4),
                    color=Y_COMPONENT,
                ).next_to(visual, DOWN, buff=0.24)
                group = VGroup(visual, cue)
                group.scale_to_fit_width(text_width)
                group.scale_to_fit_height(body_region)
                group.move_to(DOWN * (0.06 * frame_height))
            elif name == "solution":
                group = page("THINK IT THROUGH", video["solution"], Y_COMPONENT)
            elif name == "misconception_check":
                group = page("CHECK THIS IDEA", video["misconception"], X_COMPONENT)
            elif name == "recap":
                citation = (
                    f"{video['reference']['title']}: {video['reference']['section']}"
                )
                group = VGroup(
                    page("ANSWER", video["answer"], Y_COMPONENT),
                    _text_lines(citation, width=max_line, size=14, color=GRID)
                    .to_edge(DOWN, buff=0.25),
                )
            elif name == "branded_end_card":
                group = VGroup(
                    Text("Saem Physics", font_size=base_size + 14, color=VECTOR, weight=BOLD),
                    Text("NEET JEE MIT", font_size=base_size, color=TEXT),
                ).arrange(DOWN, buff=0.3)
            else:
                raise ValueError(f"unsupported storyboard beat {name!r}")
            show(group, duration)
