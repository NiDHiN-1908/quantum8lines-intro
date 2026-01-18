from manim import *
from core.chapter_title import chapter_title


class Chapter1LinearStructure(Scene):
    def construct(self):

        chapter_title(self, "Chapter 1 — Linear Structure")

        grid = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-3, 3, 1],
            background_line_style={"stroke_opacity": 0.35}
        )

        self.play(Create(grid), run_time=1.0)

        deformed = grid.copy().apply_matrix([[1, 1], [0, 1]])
        self.play(Transform(grid, deformed), run_time=1.6)

        v1 = Vector([2, 0], color=RED)
        v2 = Vector([-2, 0], color=RED)
        self.play(GrowArrow(v1), GrowArrow(v2), run_time=0.8)

        basis = VGroup(
            Vector([1, 0], color=GREEN),
            Vector([0, 1], color=GREEN)
        ).shift(DOWN * 1.8)

        self.play(FadeIn(basis), run_time=0.6)
        self.play(
            basis[0].animate.shift(RIGHT * 0.6),
            basis[1].animate.shift(UP * 0.6),
            run_time=1.2
        )

        eq = MathTex("A x = \\lambda x").to_edge(DOWN)
        self.play(FadeIn(eq), run_time=0.4)
        self.wait(0.6)
        self.play(FadeOut(eq), run_time=0.4)
