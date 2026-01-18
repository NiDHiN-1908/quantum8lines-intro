from manim import *

config.disable_caching = False


class Section2LinearityConstraintSplit(Scene):
    def construct(self):
        # --- Panels ---
        left_frame = Rectangle(
            width=6.5, height=4,
            stroke_width=2
        ).shift(LEFT * 3.5)

        right_frame = Rectangle(
            width=6.5, height=4,
            stroke_width=2
        ).shift(RIGHT * 3.5)

        self.play(Create(left_frame), Create(right_frame), run_time=0.8)

        # --- Left: Non-linear intuition ---
        v1 = Arrow(ORIGIN, RIGHT * 1.8, buff=0).shift(LEFT * 3.5)
        v2 = Arrow(v1.get_end(), UP * 1.2 + RIGHT * 0.6, buff=0)
        v_sum = CurvedArrow(
            ORIGIN, v2.get_end(),
            angle=PI / 3
        ).shift(LEFT * 3.5)

        self.play(Create(v1), run_time=0.6)
        self.play(Create(v2), run_time=0.6)
        self.play(Create(v_sum), run_time=0.8)

        # --- Right: Linearity constraint ---
        r1 = Arrow(ORIGIN, RIGHT * 1.8, buff=0).shift(RIGHT * 3.5)
        r2 = Arrow(ORIGIN, RIGHT * 1.2, buff=0).shift(RIGHT * 3.5)
        r_sum = Arrow(ORIGIN, RIGHT * 3.0, buff=0).shift(RIGHT * 3.5)

        self.play(Create(r1), Create(r2), run_time=0.6)
        self.play(Transform(VGroup(r1, r2), r_sum), run_time=1.0)

        self.wait(0.6)
