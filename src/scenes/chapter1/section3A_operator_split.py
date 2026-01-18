from manim import *

config.disable_caching = False
config.frame_rate = 60
config.pixel_width = 1920
config.pixel_height = 1080
config.background_color = BLACK


class Chapter1OperatorSplit(Scene):
    def construct(self):

        # -----------------------------
        # SAME INPUT (BOTH SIDES)
        # -----------------------------
        base_left = Square(side_length=2.5, color=WHITE).shift(LEFT * 4)
        base_right = base_left.copy().shift(RIGHT * 8)

        self.add(base_left, base_right)
        self.wait(0.6)

        # -----------------------------
        # DIFFERENT OPERATORS
        # -----------------------------
        A_left = [[1.4, 0.0],
                  [0.0, 1.0]]

        A_right = [[1.0, 0.6],
                   [0.0, 1.0]]

        self.play(
            base_left.animate.apply_matrix(A_left),
            base_right.animate.apply_matrix(A_right),
            run_time=2.2,
            rate_func=linear,
        )

        self.wait(0.8)
