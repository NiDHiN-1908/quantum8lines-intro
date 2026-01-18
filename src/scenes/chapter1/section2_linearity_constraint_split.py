from manim import *

class Section2LinearityConstraintSplit(Scene):
    def construct(self):
        # -----------------------------
        # GLOBAL SETTINGS (SAFE)
        # -----------------------------
        self.camera.background_color = BLACK

        stroke_main = 3
        stroke_box = 2
        arrow_scale = 1.2

        # -----------------------------
        # SPLIT PANELS
        # -----------------------------
        left_panel = Rectangle(
            width=6.5, height=4.5,
            stroke_color=WHITE,
            stroke_width=stroke_box
        ).shift(LEFT * 3.6)

        right_panel = Rectangle(
            width=6.5, height=4.5,
            stroke_color=WHITE,
            stroke_width=stroke_box
        ).shift(RIGHT * 3.6)

        self.play(Create(left_panel), Create(right_panel), run_time=0.8)

        # -----------------------------
        # LEFT: NON-LINEAR / FREE INPUTS
        # -----------------------------
        origin_L = left_panel.get_center()

        free_arrow_1 = Arrow(
            origin_L,
            origin_L + RIGHT * 1.4,
            buff=0,
            stroke_width=stroke_main
        )

        free_arrow_2 = CurvedArrow(
            origin_L + RIGHT * 1.4,
            origin_L + UP * 1.3,
            angle=PI / 3,
            stroke_width=stroke_main
        )

        free_arrow_3 = Arrow(
            origin_L + RIGHT * 1.4,
            origin_L + RIGHT * 2.8 + UP * 1.4,
            buff=0,
            stroke_width=stroke_main
        )

        self.play(
            GrowArrow(free_arrow_1),
            run_time=0.6
        )
        self.play(
            Create(free_arrow_2),
            run_time=0.6
        )
        self.play(
            GrowArrow(free_arrow_3),
            run_time=0.6
        )

        # -----------------------------
        # TRANSFER ARROW (CONSTRAINT)
        # -----------------------------
        transfer_arrow = Arrow(
            left_panel.get_right(),
            right_panel.get_left(),
            buff=0.15,
            stroke_width=stroke_main
        )

        self.play(GrowArrow(transfer_arrow), run_time=0.6)

        # -----------------------------
        # RIGHT: LINEAR CONSTRAINT
        # -----------------------------
        origin_R = right_panel.get_center()

        constrained_arrow = Arrow(
            origin_R,
            origin_R + RIGHT * 3.2,
            buff=0,
            stroke_width=stroke_main
        )

        self.play(GrowArrow(constrained_arrow), run_time=0.8)

        # -----------------------------
        # HOLD (NO LAG)
        # -----------------------------
        self.wait(0.6)
