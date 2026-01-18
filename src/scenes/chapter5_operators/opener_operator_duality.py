from manim import *


class Chapter5OperatorDuality(Scene):
    def construct(self):

        # -----------------------------
        # Title
        # -----------------------------
        title = Text("Chapter 5 — Operators & Duality", weight=BOLD)
        title.scale(0.9)
        title.to_edge(DOWN)

        self.play(FadeIn(title), run_time=0.8)
        self.wait(0.2)
        self.play(FadeOut(title), run_time=0.6)

        # -----------------------------
        # Primal space
        # -----------------------------
        grid_primal = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            background_line_style={
                "stroke_opacity": 0.35,
                "stroke_width": 1
            }
        ).shift(LEFT * 3)

        self.add(grid_primal)

        v = Vector([1.8, 1.0], color=BLUE).shift(LEFT * 3)

        self.play(GrowArrow(v), run_time=0.8)

        # -----------------------------
        # Operator action
        # -----------------------------
        matrix = [[1.2, 0.3],
                  [0.1, 0.9]]

        self.play(
            grid_primal.animate.apply_matrix(matrix),
            v.animate.apply_matrix(matrix),
            run_time=1.2
        )

        # -----------------------------
        # Dual space (response)
        # -----------------------------
        grid_dual = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            background_line_style={
                "stroke_opacity": 0.25,
                "stroke_width": 1
            }
        ).shift(RIGHT * 3)

        functional = Vector([1.5, -0.8], color=YELLOW).shift(RIGHT * 3)

        self.play(
            FadeIn(grid_dual),
            GrowArrow(functional),
            run_time=1.0
        )

        # -----------------------------
        # Coupling (duality)
        # -----------------------------
        self.play(
            functional.animate.apply_matrix([[1.2, 0.1],
                                              [0.3, 0.9]]),
            run_time=1.0
        )

        # -----------------------------
        # Recognition (symbol last)
        # -----------------------------
        equation = MathTex("T^*")
        equation.scale(1.2)
        equation.to_edge(DOWN)

        self.play(FadeIn(equation), run_time=0.6)
        self.wait(0.8)
        self.play(FadeOut(equation), run_time=0.4)
