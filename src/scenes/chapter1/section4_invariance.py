from manim import *

class Section4Invariance(Scene):
    def construct(self):
        # -----------------------------
        # BACKGROUND
        # -----------------------------
        self.camera.background_color = BLACK

        PANEL_W = 6
        PANEL_H = 4

        # -----------------------------
        # PANELS
        # -----------------------------
        left_panel = Rectangle(
            width=PANEL_W,
            height=PANEL_H,
            stroke_width=2,
            stroke_color=WHITE
        ).shift(LEFT * 3.5)

        right_panel = Rectangle(
            width=PANEL_W,
            height=PANEL_H,
            stroke_width=2,
            stroke_color=WHITE
        ).shift(RIGHT * 3.5)

        self.add(left_panel, right_panel)

        # -----------------------------
        # DIFFERENT INPUT VECTORS
        # -----------------------------
        input_left = Arrow(
            left_panel.get_center(),
            left_panel.get_center() + UP * 1.6 + RIGHT * 0.8,
            buff=0,
            stroke_width=5,
            color=BLUE
        )

        input_right = Arrow(
            right_panel.get_center(),
            right_panel.get_center() + DOWN * 1.4 + RIGHT * 1.0,
            buff=0,
            stroke_width=5,
            color=BLUE
        )

        self.play(
            GrowArrow(input_left),
            GrowArrow(input_right),
            run_time=0.8
        )

        self.wait(0.2)

        # -----------------------------
        # SAME OPERATOR EFFECT
        # (forces alignment)
        # -----------------------------
        invariant_left = Arrow(
            left_panel.get_center(),
            left_panel.get_center() + RIGHT * 2.8,
            buff=0,
            stroke_width=5,
            color=BLUE
        )

        invariant_right = Arrow(
            right_panel.get_center(),
            right_panel.get_center() + RIGHT * 2.8,
            buff=0,
            stroke_width=5,
            color=BLUE
        )

        self.play(
            Transform(input_left, invariant_left),
            Transform(input_right, invariant_right),
            run_time=1.2
        )

        # -----------------------------
        # HOLD — INVARIANCE IS FELT
        # -----------------------------
        self.wait(0.8)
