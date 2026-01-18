from manim import *


class Chapter1LinearStructure(Scene):
    def construct(self):

        title = Text("Chapter 1 — Linear Structure", weight=BOLD)
        title.scale(0.9)
        title.to_edge(DOWN)

        self.play(FadeIn(title), run_time=0.8)
        self.wait(0.2)
        self.play(FadeOut(title), run_time=0.6)

        grid = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-3, 3, 1],
            background_line_style={
                "stroke_opacity": 0.4,
                "stroke_width": 1
            }
        )

        self.play(Create(grid), run_time=1.0)

        deformed_grid = grid.copy().apply_matrix([[1, 1], [0, 1]])
        self.play(Transform(grid, deformed_grid), run_time=1.6)

        eigen_1 = Vector([2, 0], color=RED)
        eigen_2 = Vector([-2, 0], color=RED)

        self.play(
            GrowArrow(eigen_1),
            GrowArrow(eigen_2),
            run_time=0.8
        )

        basis_x = Vector([1, 0], color=GREEN)
        basis_y = Vector([0, 1], color=GREEN)

        basis = VGroup(basis_x, basis_y).shift(DOWN * 1.8)

        self.play(FadeIn(basis), run_time=0.6)
        self.play(
            basis_x.animate.shift(RIGHT * 0.6),
            basis_y.animate.shift(UP * 0.6),
            run_time=1.2
        )

        equation = MathTex("A x = \\lambda x")
        equation.scale(1.0)
        equation.to_edge(DOWN)

        self.play(FadeIn(equation), run_time=0.4)
        self.wait(0.6)
        self.play(FadeOut(equation), run_time=0.4)
