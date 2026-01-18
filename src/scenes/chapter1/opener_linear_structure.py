from manim import *


class Chapter1LinearStructure(Scene):
    def construct(self):

        # -----------------------------
        # Title (Z4)
        # -----------------------------
        title = Text("Chapter 1 — Linear Structure", weight=BOLD)
        title.scale(0.9)
        title.to_edge(DOWN)

        self.play(FadeIn(title), run_time=0.8)
        self.wait(0.2)
        self.play(FadeOut(title), run_time=0.6)

        # -----------------------------
        # Core structure (Z2)
        # -----------------------------
        grid = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-3, 3, 1],
            background_line_style={
                "stroke_opacity": 0.35,
                "stroke_width": 1
            }
        )

        self.play(Create(grid), run_time=1.0)

        deformed_grid = grid.copy().apply_matrix([[1, 1], [0, 1]])
        self.play(Transform(grid, deformed_grid), run_time=1.6)

        # -----------------------------
        # Eigenvectors (Z2 sides)
        # -----------------------------
        eigen_1 = Vector([2, 0], color=RED)
        eigen_2 = Vector([-2, 0], color=RED)

        self.play(
            GrowArrow(eigen_1),
            GrowArrow(eigen_2),
            run_time=0.8
        )

        # -----------------------------
        # Basis drift (Z3)
        # -----------------------------
        basis_x = Vector([1, 0], color=GREEN)
        basis_y = Vector([0, 1], color=GREEN)

        basis = VGroup(basis_x, basis_y).shift(DOWN * 1.8)

        self.play(FadeIn(basis), run_time=0.6)
        self.play(
            basis_x.animate.shift(RIGHT * 0.6),
            basis_y.animate.shift(UP * 0.6),
            run_time=1.2
        )

        # -----------------------------
        # Spectrum micro-layer (v2 upgrade)
        # -----------------------------
        spectrum = VGroup(*[
            Rectangle(height=h, width=0.12, color=YELLOW, fill_opacity=0.6)
            for h in [0.6, 1.0, 0.8, 1.4]
        ]).arrange(RIGHT, buff=0.15)

        spectrum.scale(0.9)
        spectrum.to_corner(UR)
        spectrum.set_opacity(0.6)

        self.play(FadeIn(spectrum), run_time=0.4)
        self.play(
            *[bar.animate.stretch(1.15, 1) for bar in spectrum],
            run_time=0.4
        )
        self.play(FadeOut(spectrum), run_time=0.4)

        # -----------------------------
        # Equation anchor (Z4)
        # -----------------------------
        equation = MathTex("A x = \\lambda x")
        equation.scale(1.0)
        equation.to_edge(DOWN)

        self.play(FadeIn(equation), run_time=0.4)
        self.wait(0.6)
        self.play(FadeOut(equation), run_time=0.4)
