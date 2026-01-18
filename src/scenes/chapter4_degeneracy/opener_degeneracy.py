from manim import *


class Chapter4Degeneracy(Scene):
    def construct(self):

        # -----------------------------
        # Title
        # -----------------------------
        title = Text("Chapter 4 — Degeneracy", weight=BOLD)
        title.scale(0.9)
        title.to_edge(DOWN)

        self.play(FadeIn(title), run_time=0.8)
        self.wait(0.2)
        self.play(FadeOut(title), run_time=0.6)

        # -----------------------------
        # Symmetric space
        # -----------------------------
        grid = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            background_line_style={
                "stroke_opacity": 0.35,
                "stroke_width": 1
            }
        )
        self.add(grid)

        # -----------------------------
        # Degenerate directions
        # -----------------------------
        v1 = Vector([2, 0], color=BLUE)
        v2 = Vector([0, 2], color=BLUE)
        v3 = Vector([-2, 0], color=BLUE)
        v4 = Vector([0, -2], color=BLUE)

        vectors = VGroup(v1, v2, v3, v4)

        self.play(*[GrowArrow(v) for v in vectors], run_time=1.2)

        # -----------------------------
        # Degenerate transformation
        # -----------------------------
        matrix = [[1.3, 0.0],
                  [0.0, 1.3]]

        self.play(
            grid.animate.apply_matrix(matrix),
            *[v.animate.apply_matrix(matrix) for v in vectors],
            run_time=1.4
        )

        # -----------------------------
        # Ambiguity emphasis
        # -----------------------------
        self.play(
            *[v.animate.set_color(YELLOW) for v in vectors],
            run_time=0.8
        )

        self.play(
            Rotate(v1, angle=PI / 6),
            Rotate(v2, angle=PI / 6),
            Rotate(v3, angle=PI / 6),
            Rotate(v4, angle=PI / 6),
            run_time=1.0
        )

        # -----------------------------
        # Recognition (equation last)
        # -----------------------------
        equation = MathTex("\\lambda_1 = \\lambda_2")
        equation.scale(1.1)
        equation.to_edge(DOWN)

        self.play(FadeIn(equation), run_time=0.6)
        self.wait(0.8)
        self.play(FadeOut(equation), run_time=0.4)
