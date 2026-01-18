from manim import *

# -----------------------------
# GLOBAL CONFIG (TOP ONLY)
# -----------------------------
config.disable_caching = False
config.frame_rate = 60
config.pixel_width = 1920
config.pixel_height = 1080
config.background_color = BLACK


class Chapter1BirthOfStructureSplit(Scene):
    def construct(self):

        # =================================================
        # LEFT SPACE — CAUSE (active deformation)
        # =================================================
        left_plane = NumberPlane(
            x_range=[-6, 6, 1],
            y_range=[-4, 4, 1],
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_opacity": 0.4,
                "stroke_width": 1,
            },
        ).shift(LEFT * 4)

        left_axes = Axes(
            x_range=[-6, 6],
            y_range=[-4, 4],
            axis_config={"stroke_opacity": 0.6},
        ).shift(LEFT * 4)

        # =================================================
        # RIGHT SPACE — CONSISTENCY (delayed, calmer)
        # =================================================
        right_plane = NumberPlane(
            x_range=[-6, 6, 1],
            y_range=[-4, 4, 1],
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_opacity": 0.25,
                "stroke_width": 1,
            },
        ).shift(RIGHT * 4)

        right_axes = Axes(
            x_range=[-6, 6],
            y_range=[-4, 4],
            axis_config={"stroke_opacity": 0.45},
        ).shift(RIGHT * 4)

        # -------------------------------------------------
        # BASELINE (nothing moves yet)
        # -------------------------------------------------
        self.add(left_plane, left_axes, right_plane, right_axes)
        self.wait(0.6)

        # =================================================
        # TRANSFORMATION MATRICES (same rule)
        # =================================================
        A1 = [[1.25, 0.0],
              [0.0, 1.0]]

        A2 = [[1.0, 0.6],
              [0.0, 1.0]]

        # =================================================
        # LEFT: RULE ACTS FIRST (cause)
        # =================================================
        self.play(
            left_plane.animate.apply_matrix(A1),
            left_axes.animate.apply_matrix(A1),
            run_time=1.4,
            rate_func=linear,
        )

        self.play(
            left_plane.animate.apply_matrix(A2),
            left_axes.animate.apply_matrix(A2),
            run_time=1.6,
            rate_func=linear,
        )

        # =================================================
        # RIGHT: SAME RULE, DELAYED (consistency)
        # =================================================
        self.play(
            right_plane.animate.apply_matrix(A1),
            right_axes.animate.apply_matrix(A1),
            run_time=1.4,
            rate_func=linear,
        )

        self.play(
            right_plane.animate.apply_matrix(A2),
            right_axes.animate.apply_matrix(A2),
            run_time=1.6,
            rate_func=linear,
        )

        # =================================================
        # HOLD — let the brain connect them
        # =================================================
        self.wait(1.0)
