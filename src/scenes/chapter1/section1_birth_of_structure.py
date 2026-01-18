from manim import *

class Chapter1BirthOfStructure(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # Axes
        axes = Axes(
            x_range=[-6, 6, 1],
            y_range=[-4, 4, 1],
            x_length=14,
            y_length=8,
            axis_config={
                "color": WHITE,
                "stroke_width": 2,
                "include_ticks": True,
                "tick_size": 0.08,
            },
        )

        # Diagonal grid (subtle depth)
        grid = NumberPlane(
            x_range=[-8, 8, 1],
            y_range=[-5, 5, 1],
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 1,
                "stroke_opacity": 0.35,
            },
        )
        grid.rotate(20 * DEGREES)

        # Vectors emerging from origin
        v1 = Arrow(ORIGIN, 2.5 * RIGHT + 1.2 * UP, buff=0, color=BLUE_B)
        v2 = Arrow(ORIGIN, 1.8 * LEFT + 1.0 * UP, buff=0, color=BLUE_B)
        v3 = Arrow(ORIGIN, 1.2 * RIGHT + 0.6 * DOWN, buff=0, color=BLUE_B)

        vectors = VGroup(v1, v2, v3)

        # Invariant horizontal line
        invariant = Line(
            start=LEFT * 7,
            end=RIGHT * 7,
            color=YELLOW,
            stroke_width=3,
        )

        # Equation (minimal, late reveal)
        equation = MathTex(r"\dot{x} = Ax", color=WHITE).scale(1.2)
        equation.to_edge(DOWN)

        # --- ANIMATION SEQUENCE ---

        self.play(FadeIn(grid, run_time=1.5))
        self.play(Create(axes, run_time=1.5))
        self.wait(0.4)

        self.play(
            LaggedStart(
                GrowArrow(v1),
                GrowArrow(v2),
                GrowArrow(v3),
                lag_ratio=0.25,
                run_time=1.6,
            )
        )

        self.wait(0.3)

        self.play(Create(invariant, run_time=1.2))
        self.wait(0.4)

        self.play(FadeIn(equation, shift=UP * 0.3))
        self.wait(2)
