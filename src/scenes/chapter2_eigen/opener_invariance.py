import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

from manim import *
from core.chapter_title import chapter_title


class Chapter2EigenInvariance(Scene):
    def construct(self):

        chapter_title(self, "Chapter 2 — Invariance")

        grid = NumberPlane(background_line_style={"stroke_opacity": 0.35})
        self.add(grid)

        invariant = Vector([2, 0], color=YELLOW)
        moving1 = Vector([1, 1], color=BLUE)
        moving2 = Vector([-1, 1], color=BLUE)

        self.play(
            GrowArrow(invariant),
            GrowArrow(moving1),
            GrowArrow(moving2),
            run_time=1.0
        )

        matrix = [[1.2, 0.4], [0, 1]]

        for _ in range(3):
            self.play(
                grid.animate.apply_matrix(matrix),
                moving1.animate.apply_matrix(matrix),
                moving2.animate.apply_matrix(matrix),
                run_time=0.9
            )

        self.play(FadeOut(moving1), FadeOut(moving2), run_time=0.8)

        eq = MathTex("A x = \\lambda x").to_edge(DOWN)
        self.play(FadeIn(eq), run_time=0.6)
        self.wait(0.6)
        self.play(FadeOut(eq), run_time=0.4)
