from manim import *

# =========================
# GLOBAL CONFIG (MUST BE TOP)
# =========================
config.disable_caching = False
config.frame_rate = 60
config.pixel_width = 1920
config.pixel_height = 1080
config.background_color = BLACK


class Chapter1BirthOfStructure(Scene):
    def construct(self):
        # -------------------------
        # GRID + AXES (STATIC)
        # -------------------------
        plane = NumberPlane(
            x_range=[-10, 10, 1],
            y_range=[-6, 6, 1],
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 1,
                "stroke_opacity": 0.35,
            },
        )

        axes = Axes(
            x_range=[-10, 10, 1],
            y_range=[-6, 6, 1],
            axis_config={"stroke_width": 2},
        )

        self.add(plane, axes)

        # -------------------------
        # EIGEN-DIRECTION VECTORS
        # -------------------------
        v1 = Arrow(
            start=ORIGIN,
            end=2.5 * RIGHT + 1.2 * UP,
            color=BLUE_B,
            buff=0,
            stroke_width=6,
        )

        v2 = Arrow(
            start=ORIGIN,
            end=2.0 * LEFT + 1.0 * UP,
            color=BLUE_B,
            buff=0,
            stroke_width=6,
        )

        v3 = Arrow(
            start=ORIGIN,
            end=1.5 * RIGHT + -1.8 * DOWN,
            color=BLUE_B,
            buff=0,
            stroke_width=6,
        )

        # -------------------------
        # PLAY: STRUCTURE EMERGES
        # -------------------------
        self.play(
            GrowArrow(v1),
            GrowArrow(v2),
            GrowArrow(v3),
            run_time=1.4,
            rate_func=smooth,
        )

        self.wait(0.4)

        # -------------------------
        # DOMINANT AXIS (STRUCTURE)
        # -------------------------
        dominant_axis = Line(
            start=LEFT * 10,
            end=RIGHT * 10,
            color=YELLOW,
            stroke_width=4,
        )

        self.play(
            Create(dominant_axis),
            run_time=0.8,
            rate_func=linear,
        )

        self.wait(0.3)

        # -------------------------
        # EQUATION (NO OVERLAY)
        # -------------------------
        equation = MathTex(
            r"\dot{x} = A x",
            color=WHITE,
        ).scale(1.3)

        equation.to_edge(DOWN, buff=0.6)

        self.play(FadeIn(equation, shift=UP * 0.2), run_time=0.6)
        self.wait(0.6)

        # -------------------------
        # CLEAN EXIT (NO DRAG)
        # -------------------------
        self.play(
            FadeOut(v1),
            FadeOut(v2),
            FadeOut(v3),
            FadeOut(dominant_axis),
            FadeOut(equation),
            run_time=0.8,
        )

        self.wait(0.2)
