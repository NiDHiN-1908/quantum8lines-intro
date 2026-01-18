from manim import *
from src.core.chapter_title import chapter_title


class Chapter3SpectralDecomposition(Scene):
    def construct(self):

        chapter_title(self, "Chapter 3 — Spectral Decomposition")

        grid = NumberPlane(background_line_style={"stroke_opacity": 0.3})
        self.add(grid)

        v1 = Vector([2, 0], color=RED)
        v2 = Vector([0, 1.6], color=GREEN)
        v3 = Vector([1, 1], color=BLUE)

        self.play(GrowArrow(v1), GrowArrow(v2), GrowArrow(v3), run_time=1.0)

        matrix = [[1.5, 0.3], [0, 0.8]]

        self.play(
            grid.animate.apply_matrix(matrix),
            v1.animate.apply_matrix(matrix),
            v2.animate.apply_matrix(matrix),
            v3.animate.apply_matrix(matrix),
            run_time=1.4
        )

        self.play(FadeOut(v3), v1.animate.set_color(YELLOW), v2.animate.set_color(YELLOW), run_time=0.8)

        eq = MathTex("A = P D P^{-1}").to_edge(DOWN)
        self.play(FadeIn(eq), run_time=0.6)
        self.wait(0.6)
        self.play(FadeOut(eq), run_time=0.4)
