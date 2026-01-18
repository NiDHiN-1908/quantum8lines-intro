from manim import *


class Chapter3SpectralDecomposition(Scene):
    def construct(self):

        # -----------------------------
        # Title (authority, 1s)
        # -----------------------------
        title = Text("Chapter 3 — Spectral Decomposition", weight=BOLD)
        title.scale(0.9)
        title.to_edge(DOWN)

        self.play(FadeIn(title), run_time=0.8)
        self.wait(0.2)
        self.play(FadeOut(title), run_time=0.6)

        # -----------------------------
        # Base space
        # -----------------------------
        grid = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-3, 3, 1],
            background_line_style={
                "stroke_opacity": 0.3,
                "stroke_width": 1
            }
        )
        self.add(grid)

        # -----------------------------
        # Multiple directions
        # -----------------------------
        v1 = Vector([2, 0], color=RED)
        v2 = Vector([0, 1.6], color=GREEN)
        v3 = Vector([1, 1], color=BLUE)

        vectors = VGroup(v1, v2, v3)

        self.play(
            GrowArrow(v1),
            GrowArrow(v2),
            GrowArrow(v3),
            run_time=1.0
        )

        # -----------------------------
        # Linear transformation
        # -----------------------------
        matrix = [[1.5, 0.3],
                  [0.0, 0.8]]

        self.play(
            grid.animate.apply_matrix(matrix),
            *[v.animate.apply_matrix(matrix) for v in vectors],
            run_time=1.4
        )

        # -----------------------------
        # Change of basis (alignment)
        # -----------------------------
        self.play(
            v1.animate.set_color(YELLOW),
            v2.animate.set_color(YELLOW),
            FadeOut(v3),
            run_time=0.8
        )

        self.play(
            v1.animate.rotate(0),
            v2.animate.rotate(0),
            run_time=0.8
        )

        # -----------------------------
        # Decomposition clarity
        # -----------------------------
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-2, 2, 1],
            tips=False,
            axis_config={"stroke_opacity": 0.5}
        )

        self.play(
            FadeOut(grid),
            FadeIn(axes),
            run_time=0.8
        )

        # -----------------------------
        # Recognition (equation last)
        # -----------------------------
        equation = MathTex("A = P D P^{-1}")
        equation.scale(1.1)
        equation.to_edge(DOWN)

        self.play(FadeIn(equation), run_time=0.6)
        self.wait(0.8)
        self.play(FadeOut(equation), run_time=0.4)
