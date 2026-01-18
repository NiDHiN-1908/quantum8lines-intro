import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

from manim import *
from core.chapter_title import chapter_title


class Chapter6ContinuousTime(Scene):
    def construct(self):

        # -----------------------------
        # Normalized title (LOCKED)
        # -----------------------------
        chapter_title(self, "Chapter 6 — Continuous Time")

        # -----------------------------
        # Discrete dynamics (left)
        # -----------------------------
        grid_left = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            background_line_style={"stroke_opacity": 0.35}
        ).shift(LEFT * 3)

        self.add(grid_left)

        point = Dot(point=LEFT * 3 + RIGHT * 0.5 + UP * 0.5, color=RED)

        self.play(FadeIn(point), run_time=0.3)

        jump_matrix = [[1.1, 0.4],
                       [0.0, 1.0]]

        for _ in range(5):
            self.play(
                point.animate.apply_matrix(jump_matrix),
                run_time=0.25
            )

        self.wait(0.2)

        # -----------------------------
        # Continuous flow (right)
        # -----------------------------
        grid_right = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            background_line_style={"stroke_opacity": 0.25}
        ).shift(RIGHT * 3)

        self.play(FadeIn(grid_right), run_time=0.4)

        flow_dot = Dot(point=RIGHT * 3 + RIGHT * 0.5 + UP * 0.5, color=BLUE)
        self.play(FadeIn(flow_dot), run_time=0.3)

        def flow_func(mob, dt):
            A = [[1.1, 0.4],
                 [0.0, 1.0]]
            x, y, _ = mob.get_center() - RIGHT * 3
            dx = A[0][0] * x + A[0][1] * y
            dy = A[1][1] * y
            mob.shift((dx * RIGHT + dy * UP) * dt * 0.4)

        flow_dot.add_updater(flow_func)

        self.wait(2.2)

        flow_dot.remove_updater(flow_func)

        # -----------------------------
        # Recognition (symbol LAST)
        # -----------------------------
        equation = MathTex("\\dot{x} = A x")
        equation.to_edge(DOWN)

        self.play(FadeIn(equation), run_time=0.6)
        self.wait(0.8)
        self.play(FadeOut(equation), run_time=0.4)
