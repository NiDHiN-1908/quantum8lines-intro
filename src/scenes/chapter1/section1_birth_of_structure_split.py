from manim import *

# Optional: explicitly keep caching ON (default, but safe)
config.disable_caching = False


class Section1BirthOfStructureSplit(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # -----------------------------
        # LEFT: original structure
        # -----------------------------
        left_shape = Square(
            side_length=2.2,
            stroke_color=WHITE,
            stroke_width=3
        ).shift(LEFT * 3)

        # -----------------------------
        # RIGHT: transformed structure
        # -----------------------------
        right_shape = Polygon(
            [-1.2, -0.9, 0],
            [ 1.2, -0.9, 0],
            [ 2.0,  0.9, 0],
            [-0.4,  0.9, 0],
            stroke_color=WHITE,
            stroke_width=3
        ).shift(RIGHT * 3)

        # -----------------------------
        # STEP 1 — Birth of structure
        # -----------------------------
        self.play(
            Create(left_shape),
            run_time=0.8
        )
        self.wait(0.3)

        # -----------------------------
        # STEP 2 — Causal motion (ghost)
        # -----------------------------
        ghost = left_shape.copy()
        ghost.set_stroke(color=BLUE, opacity=0.5)

        self.add(ghost)
        self.play(
            ghost.animate.shift(RIGHT * 6),
            run_time=0.9,
            rate_func=smooth
        )

        # -----------------------------
        # STEP 3 — Resolve transformation
        # -----------------------------
        self.play(
            Transform(ghost, right_shape),
            run_time=0.6
        )

        self.remove(ghost)
        self.add(right_shape)

        # -----------------------------
        # STEP 4 — Emphasis pulse (attention lock)
        # -----------------------------
        self.play(
            right_shape.animate.set_stroke(width=5),
            run_time=0.25
        )
        self.play(
            right_shape.animate.set_stroke(width=3),
            run_time=0.25
        )

        self.wait(0.6)
