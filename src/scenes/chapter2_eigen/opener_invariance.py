from manim import *


class Chapter2EigenInvariance(Scene):
    def construct(self):

        # -----------------------------
        # Phase 0 — Silent title (1s)
        # -----------------------------
        title = Text("Chapter 2 — Invariance", weight=BOLD)
        title.scale(0.9)
        title.to_edge(DOWN)

        self.play(FadeIn(title), run_time=0.8)
        self.wait(0.2)
        self.play(FadeOut(title), run_time=0.6)

        # -----------------------------
        # Phase 1 — Space (baseline)
        # -----------------------------
        grid = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-3, 3, 1],
            background_line_style={
                "stroke_opacity": 0.35,
                "stroke_width": 1
            }
        )

        self.add(grid)

        # -----------------------------
        # Phase 2 — Vectors
        # -----------------------------
        invariant = Vector([2, 0], color=YELLOW)
        moving_1 = Vector([1, 1], color=BLUE)
        moving_2 = Vector([-1, 1], color=BLUE)

        vectors = VGroup(invariant, moving_1, moving_2)

        self.play(
            GrowArrow(invariant),
            GrowArrow(moving_1),
            GrowArrow(moving_2),
            run_time=1.0
        )

        # -----------------------------
        # Phase 3 — Repeated transformation
        # -----------------------------
        matrix = [[1.2, 0.4], [0.0, 1.0]]

        for _ in range(3):
            self.play(
                grid.animate.apply_matrix(matrix),
                moving_1.animate.apply_matrix(matrix),
                moving_2.animate.apply_matrix(matrix),
                run_time=0.9
            )
            self.wait(0.15)

        # -----------------------------
        # Phase 4 — Isolation
        # -----------------------------
        self.play(
            FadeOut(moving_1),
            FadeOut(moving_2),
            invariant.animate.set_color(RED),
            run_time=0.8
        )

        # -----------------------------
        # Phase 5 — Recognition (equation last)
        # -----------------------------
        equation = MathTex("A x = \\lambda x")
        equation.scale(1.1)
        equation.to_edge(DOWN)

        self.play(FadeIn(equation), run_time=0.6)
        self.wait(0.8)
        self.play(FadeOut(equation), run_time=0.4)
