from manim import *
from core.chapter_title import chapter_title


class Chapter4Degeneracy(Scene):
    def construct(self):

        chapter_title(self, "Chapter 4 — Degeneracy")

        grid = NumberPlane(background_line_style={"stroke_opacity": 0.35})
        self.add(grid)

        vectors = VGroup(
            Vector([2, 0]),
            Vector([0, 2]),
            Vector([-2, 0]),
            Vector([0, -2])
        ).set_color(BLUE)

        self.play(*[GrowArrow(v) for v in vectors], run_time=1.2)

        matrix = [[1.3, 0], [0, 1.3]]

        self.play(
            grid.animate.apply_matrix(matrix),
            *[v.animate.apply_matrix(matrix) for v in vectors],
            run_time=1.4
        )

        self.play(*[v.animate.set_color(YELLOW) for v in vectors], run_time=0.8)

        eq = MathTex("\\lambda_1 = \\lambda_2").to_edge(DOWN)
        self.play(FadeIn(eq), run_time=0.6)
        self.wait(0.6)
        self.play(FadeOut(eq), run_time=0.4)
