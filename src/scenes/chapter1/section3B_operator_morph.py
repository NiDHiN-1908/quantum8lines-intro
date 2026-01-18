from manim import *

config.disable_caching = False
config.frame_rate = 60
config.pixel_width = 1920
config.pixel_height = 1080
config.background_color = BLACK


class Chapter1OperatorMorph(Scene):
    def construct(self):

        # -----------------------------
        # INPUT GEOMETRY
        # -----------------------------
        shape = Square(side_length=3, color=WHITE)
        self.add(shape)
        self.wait(0.6)

        # -----------------------------
        # OPERATOR MORPH (CONTINUOUS)
        # -----------------------------
        matrices = [
            [[1.2, 0.0], [0.0, 1.0]],
            [[1.1, 0.4], [0.0, 1.0]],
            [[0.9, 0.8], [0.0, 1.0]],
            [[1.0, -0.6], [0.0, 1.2]],
        ]

        for A in matrices:
            self.play(
                shape.animate.apply_matrix(A),
                run_time=1.4,
                rate_func=linear,
            )

        self.wait(1.0)
