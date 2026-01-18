import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

from manim import *
from core.chapter_title import chapter_title


class Chapter6ContinuousTime(Scene):
    def construct(self):

        # -----------------------------
        # Normalized title
        # -----------------------------
        chapter_title(self, "Chapter 6 — Continuous Time")

        # =====================================================
        # LEFT — DISCRETE TIME (JUMPS)
        # =====================================================
        grid_left = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            background_line_style={"stroke_opacity": 0.35}
        ).shift(LEFT * 3)

        self.add(grid_left)

        point = Dot(LEFT * 3 + RIGHT * 0.6 + UP * 0.4, color=RED)
        self.add(point)

        jump_matrix = [[1.2, 0.5],
                       [0.0, 1.0]]

        for _ in range(5):
            x, y, _ = point.get_center() - LEFT * 3
            nx = jump_matrix[0][0] * x + jump_matrix[0][1] * y
            ny = jump_matrix[1][1] * y

            self.play(
                point.animate.move_to(LEFT * 3 + nx * RIGHT + ny * UP),
                run_time=0.15
            )
            self.wait(0.08)

        # =====================================================
        # RIGHT — CONTINUOUS TIME (FLOW)
        # =====================================================
        grid_right = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            background_line_style={"stroke_opacity": 0.25}
        ).shift(RIGHT * 3)

        self.play(FadeIn(grid_right), run_time=0.4)

        flow_dot = Dot(RIGHT * 3 + RIGHT * 0.6 + UP * 0.4, color=BLUE)
        self.add(flow_dot)

        # Properly initialized path
        path = VMobject(color=BLUE, stroke_width=3)
        path.start_new_path(flow_dot.get_center())
        self.add(path)

        def flow_updater(mob, dt):
            A = [[1.2, 0.5],
                 [0.0, 1.0]]

            x, y, _ = mob.get_center() - RIGHT * 3
            dx = A[0][0] * x + A[0][1] * y
            dy = A[1][1] * y

            mob.shift((dx * RIGHT + dy * UP) * dt * 0.35)
            path.add_points_as_corners([mob.get_center()])

        flow_dot.add_updater(flow_updater)

        self.wait(2.2)

        flow_dot.remove_updater(flow_updater)

        # -----------------------------
        # Recognition (symbol LAST)
        # -----------------------------
        equation = MathTex("\\dot{x} = A x")
        equation.to_edge(DOWN)

        self.play(FadeIn(equation), run_time=0.6)
        self.wait(0.8)
        self.play(FadeOut(equation), run_time=0.4)
