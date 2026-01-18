from manim import *

class Section3OperatorSplit(Scene):
    def construct(self):
        # ---------- CONFIG ----------
        self.camera.background_color = BLACK

        PANEL_WIDTH = 6
        PANEL_HEIGHT = 4

        # ---------- PANELS ----------
        left_panel = Rectangle(
            width=PANEL_WIDTH,
            height=PANEL_HEIGHT,
            stroke_color=WHITE,
            stroke_width=2
        ).shift(LEFT * 3.5)

        right_panel = Rectangle(
            width=PANEL_WIDTH,
            height=PANEL_HEIGHT,
            stroke_color=WHITE,
            stroke_width=2
        ).shift(RIGHT * 3.5)

        self.add(left_panel, right_panel)

        # ---------- INPUT VECTOR ----------
        input_vec_left = Arrow(
            start=left_panel.get_center(),
            end=left_panel.get_center() + RIGHT * 1.8,
            color=BLUE,
            stroke_width=5,
            buff=0
        )

        input_vec_right = input_vec_left.copy().move_to(
            right_panel.get_center()
        )

        self.play(
            GrowArrow(input_vec_left),
            GrowArrow(input_vec_right),
            run_time=0.8
        )

        self.wait(0.2)

        # ---------- OPERATOR A (ROTATION) ----------
        rotated_vec = Arrow(
            start=left_panel.get_center(),
            end=left_panel.get_center() + UP * 1.6,
            color=BLUE,
            stroke_width=5,
            buff=0
        )

        # ---------- OPERATOR B (SCALING) ----------
        scaled_vec = Arrow(
            start=right_panel.get_center(),
            end=right_panel.get_center() + RIGHT * 3.0,
            color=BLUE,
            stroke_width=5,
            buff=0
        )

        self.play(
            Transform(input_vec_left, rotated_vec),
            Transform(input_vec_right, scaled_vec),
            run_time=1.2
        )

        self.wait(0.6)

        # ---------- LABEL (MINIMAL) ----------
        label = MathTex(r"x \;\rightarrow\; Ax", color=WHITE)\
            .scale(0.8)\
            .to_edge(DOWN)

        self.play(FadeIn(label), run_time=0.4)
        self.wait(0.6)
