from manim import *

# --------------------------------
# GLOBAL CONFIG (STABLE FOR LONG RUNS)
# --------------------------------
config.background_color = BLACK
config.disable_caching = False


# ======================================================
# SECTION 1 — Birth of Structure (Split Layout)
# ======================================================
def play_section1(scene):
    left = Rectangle(width=6, height=4, stroke_width=2).shift(LEFT * 3.5)
    right = Rectangle(width=6, height=4, stroke_width=2).shift(RIGHT * 3.5)

    origin_L = left.get_center()
    origin_R = right.get_center()

    v1 = Arrow(origin_L, origin_L + RIGHT * 1.8, buff=0)
    v2 = Arrow(origin_L, origin_L + UP * 1.5, buff=0)
    out = Arrow(origin_R, origin_R + RIGHT * 2.2, buff=0)

    scene.play(Create(left), Create(right), run_time=0.8)
    scene.play(GrowArrow(v1), GrowArrow(v2), run_time=0.8)
    scene.play(GrowArrow(out), run_time=0.8)
    scene.wait(0.5)

    return VGroup(left, right, v1, v2, out)


# ======================================================
# SECTION 2 — Linearity Constraint (Split)
# ======================================================
def play_section2(scene):
    left = Rectangle(width=6, height=4, stroke_width=2).shift(LEFT * 3.5)
    right = Rectangle(width=6, height=4, stroke_width=2).shift(RIGHT * 3.5)

    curve = Arc(radius=1.5, angle=PI / 2).move_to(left.get_center())
    line = Arrow(right.get_center(), right.get_center() + RIGHT * 2.3, buff=0)

    scene.play(Create(left), Create(right), run_time=0.8)
    scene.play(Create(curve), run_time=0.8)
    scene.play(GrowArrow(line), run_time=0.8)
    scene.wait(0.5)

    return VGroup(left, right, curve, line)


# ======================================================
# SECTION 3 — Operator as Machine (Split)
# ======================================================
def play_section3(scene):
    left = Rectangle(width=6, height=4, stroke_width=2).shift(LEFT * 3.5)
    right = Rectangle(width=6, height=4, stroke_width=2).shift(RIGHT * 3.5)

    vin = Arrow(left.get_center(), left.get_center() + RIGHT * 1.8, buff=0)
    connector = Arrow(left.get_right(), right.get_left(), buff=0.2)
    vout = Arrow(right.get_center(), right.get_center() + UP * 1.8, buff=0)

    scene.play(Create(left), Create(right), run_time=0.8)
    scene.play(GrowArrow(vin), run_time=0.6)
    scene.play(GrowArrow(connector), run_time=0.6)
    scene.play(GrowArrow(vout), run_time=0.6)
    scene.wait(0.5)

    return VGroup(left, right, vin, connector, vout)


# ======================================================
# SECTION 4 — Invariance
# ======================================================
def play_section4(scene):
    axes = Axes(
        x_range=[-4, 4, 1],
        y_range=[-3, 3, 1],
        tips=True,
        axis_config={"stroke_width": 2},
    )

    v = Arrow(ORIGIN, RIGHT * 2, buff=0)

    scene.play(Create(axes), run_time=1)
    scene.play(GrowArrow(v), run_time=0.6)

    # rotate space, keep vector visually invariant
    scene.play(Rotate(axes, PI / 6, about_point=ORIGIN), run_time=1)
    scene.wait(0.5)

    return VGroup(axes, v)


# ======================================================
# MASTER SCENE — Chapter 1 (NO BLACK FRAMES)
# ======================================================
class Chapter1Master(Scene):
    def construct(self):
        g1 = play_section1(self)
        self.play(FadeOut(g1), run_time=0.6)

        g2 = play_section2(self)
        self.play(FadeOut(g2), run_time=0.6)

        g3 = play_section3(self)
        self.play(FadeOut(g3), run_time=0.6)

        play_section4(self)
        self.wait(1)
