from manim import *

# -------------------------------
# GLOBAL CONFIG (SAFE & FAST)
# -------------------------------
config.disable_caching = True
config.background_color = BLACK


# ======================================================
# SECTION 1 — Birth of Structure (Split Layout)
# ======================================================
def play_section1(scene: Scene):
    # --- Frames ---
    left_frame = Rectangle(width=6, height=4, stroke_width=2).shift(LEFT * 3.5)
    right_frame = Rectangle(width=6, height=4, stroke_width=2).shift(RIGHT * 3.5)

    scene.add(left_frame, right_frame)

    # --- Left: vector decomposition ---
    origin_L = left_frame.get_center()
    v1 = Arrow(origin_L, origin_L + RIGHT * 1.8, buff=0, color=WHITE)
    v2 = Arrow(origin_L, origin_L + UP * 1.5, buff=0, color=WHITE)

    scene.play(GrowArrow(v1), run_time=0.6)
    scene.play(GrowArrow(v2), run_time=0.6)

    # --- Right: linear outcome ---
    origin_R = right_frame.get_center()
    out = Arrow(origin_R, origin_R + RIGHT * 2.2, buff=0, color=WHITE)

    scene.play(GrowArrow(out), run_time=0.8)
    scene.wait(0.5)


# ======================================================
# SECTION 2 — Linearity Constraint (Split)
# ======================================================
def play_section2(scene: Scene):
    left_frame = Rectangle(width=6, height=4, stroke_width=2).shift(LEFT * 3.5)
    right_frame = Rectangle(width=6, height=4, stroke_width=2).shift(RIGHT * 3.5)

    scene.add(left_frame, right_frame)

    # Left: nonlinear attempt (curve)
    curve = Arc(
        radius=1.5,
        angle=PI / 2,
        start_angle=0,
        color=WHITE
    ).move_to(left_frame.get_center())

    scene.play(Create(curve), run_time=0.8)

    # Right: linear constraint (straight)
    line = Arrow(
        right_frame.get_center(),
        right_frame.get_center() + RIGHT * 2.3,
        buff=0,
        color=WHITE
    )

    scene.play(GrowArrow(line), run_time=0.8)
    scene.wait(0.5)


# ======================================================
# SECTION 3 — Operator as Machine (Split)
# ======================================================
def play_section3(scene: Scene):
    left_frame = Rectangle(width=6, height=4, stroke_width=2).shift(LEFT * 3.5)
    right_frame = Rectangle(width=6, height=4, stroke_width=2).shift(RIGHT * 3.5)

    scene.add(left_frame, right_frame)

    # Input vector
    v_in = Arrow(
        left_frame.get_center(),
        left_frame.get_center() + RIGHT * 1.8,
        buff=0,
        color=WHITE
    )

    scene.play(GrowArrow(v_in), run_time=0.6)

    # Transformation arrow crossing frames
    connector = Arrow(
        left_frame.get_right(),
        right_frame.get_left(),
        buff=0.2,
        color=WHITE
    )

    scene.play(GrowArrow(connector), run_time=0.6)

    # Output vector
    v_out = Arrow(
        right_frame.get_center(),
        right_frame.get_center() + UP * 1.8,
        buff=0,
        color=WHITE
    )

    scene.play(GrowArrow(v_out), run_time=0.6)
    scene.wait(0.5)


# ======================================================
# SECTION 4 — Invariance
# ======================================================
def play_section4(scene: Scene):
    axes = Axes(
        x_range=[-4, 4, 1],
        y_range=[-3, 3, 1],
        tips=True,
        axis_config={"stroke_width": 2}
    )

    scene.play(Create(axes), run_time=1)

    v = Arrow(ORIGIN, RIGHT * 2, buff=0, color=WHITE)
    scene.play(GrowArrow(v), run_time=0.6)

    # Rotate space, vector stays aligned
    scene.play(
        Rotate(axes, angle=PI / 6),
        run_time=1
    )

    scene.wait(0.5)


# ======================================================
# MASTER SCENE — Chapter 1
# ======================================================
class Chapter1Master(Scene):
    def construct(self):
        # Section 1
        play_section1(self)
        self.clear()

        # Section 2
        play_section2(self)
        self.clear()

        # Section 3
        play_section3(self)
        self.clear()

        # Section 4
        play_section4(self)
        self.wait(1)
