import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

from manim import *
from core.chapter_title import chapter_title


class Chapter5OperatorDuality(Scene):
    def construct(self):

        chapter_title(self, "Chapter 5 — Operators & Duality")

        grid_L = NumberPlane(
            background_line_style={"stroke_opacity": 0.35}
        ).shift(LEFT * 3)
        self.add(grid_L)

        v = Vector([1.8, 1], color=BLUE).shift(LEFT * 3)
        self.play(GrowArrow(v), run_time=0.8)

        matrix = [[1.2, 0.3], [0.1, 0.9]]
        self.play(
            grid_L.animate.apply_matrix(matrix),
            v.animate.apply_matrix(matrix),
            run_time=1.2
        )

        grid_R = NumberPlane(
            background_line_style={"stroke_opacity": 0.25}
        ).shift(RIGHT * 3)
        f = Vector([1.5, -0.8], color=YELLOW).shift(RIGHT * 3)

        self.play(FadeIn(grid_R), GrowArrow(f), run_time=1.0)
        self.play(
            f.animate.apply_matrix([[1.2, 0.1], [0.3, 0.9]]),
            run_time=1.0
        )

        eq = MathTex("T^*").to_edge(DOWN)
        self.play(FadeIn(eq), run_time=0.6)
        self.wait(0.6)
        self.play(FadeOut(eq), run_time=0.4)
