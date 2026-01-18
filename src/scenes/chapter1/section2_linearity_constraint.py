from manim import *

# -----------------------------
# GLOBAL CONFIG
# -----------------------------
config.disable_caching = False
config.frame_rate = 60
config.pixel_width = 1920
config.pixel_height = 1080
config.background_color = BLACK


class Chapter1LinearityConstraint(Scene):
    def construct(self):

        # -------------------------------------------------
        # BASE OBJECTS
        # -------------------------------------------------

        # Straight structure
        straight = Line(
            LEFT * 5,
            RIGHT * 5,
            stroke_width=4,
            color=WHITE,
        ).shift(UP * 1.8)

        # Curved structure
        curve = CubicBezier(
            LEFT * 4,
            LEFT * 2 + UP * 2,
            RIGHT * 2 + DOWN * 2,
            RIGHT * 4,
            stroke_width=4,
            color=WHITE,
        ).shift(DOWN * 1.8)

        self.add(straight, curve)
        self.wait(0.6)

        # -------------------------------------------------
        # SAME RULE APPLIED TO BOTH
        # -------------------------------------------------
        A = [[1.4, 0.5],
             [0.0, 1.0]]

        self.play(
            straight.animate.apply_matrix(A),
            curve.animate.apply_matrix(A),
            run_time=2.2,
            rate_func=linear,
        )

        self.wait(0.4)

        # -------------------------------------------------
        # APPLY AGAIN (CONSISTENCY)
        # -------------------------------------------------
        self.play(
            straight.animate.apply_matrix(A),
            curve.animate.apply_matrix(A),
            run_time=2.0,
            rate_func=linear,
        )

        # -------------------------------------------------
        # HOLD — CONSTRAINT IS FELT
        # -------------------------------------------------
        self.wait(1.2)
