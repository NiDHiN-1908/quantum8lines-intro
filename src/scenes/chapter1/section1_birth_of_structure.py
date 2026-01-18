import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

from manim import *
from core.chapter_title import chapter_title


class Chapter1BirthOfStructure(Scene):
    def construct(self):

        # -------------------------------------------------
        # Chapter title (normalized)
        # -------------------------------------------------
        chapter_title(self, "Chapter 1 — Structure")

        # -------------------------------------------------
        # Grid (SPACE IS THE PROTAGONIST)
        # -------------------------------------------------
        grid = NumberPlane(
            x_range=[-6, 6, 1],
            y_range=[-4, 4, 1],
            background_line_style={
                "stroke_opacity": 0.45,   # slightly stronger
                "stroke_width": 1.2
            }
        )

        axes = Axes(
            x_range=[-6, 6],
            y_range=[-4, 4],
            axis_config={"stroke_opacity": 0.55}
        )

        # Subtle grid intersection emphasis (anchors the field)
        dots = VGroup(*[
            Dot(grid.c2p(x, y), radius=0.015, color=BLUE_E)
            for x in range(-6, 7)
            for y in range(-4, 5)
        ])
        dots.set_opacity(0.25)

        self.add(grid, dots, axes)
        self.wait(2.0)

        # -------------------------------------------------
        # Witness vectors (DE-EMPHASIZED)
        # -------------------------------------------------
        vectors = VGroup(
            Vector([2, 1], color=BLUE_C, buff=0, stroke_width=3, tip_length=0.15),
            Vector([-1.5, 1], color=BLUE_C, buff=0, stroke_width=3, tip_length=0.15),
        )
        vectors.set_opacity(0.65)

        self.add(vectors)
        self.wait(0.6)

        # -------------------------------------------------
        # First global action
        # -------------------------------------------------
        A1 = [[1.25, 0.0],
              [0.0, 1.0]]

        self.play(
            grid.animate.apply_matrix(A1),
            axes.animate.apply_matrix(A1),
            dots.animate.apply_matrix(A1),
            *[v.animate.apply_matrix(A1) for v in vectors],
            run_time=3.2
        )

        self.wait(0.6)

        # -------------------------------------------------
        # Directional bias (still space-first)
        # -------------------------------------------------
        A2 = [[1.0, 0.55],
              [0.0, 1.0]]

        self.play(
            grid.animate.apply_matrix(A2),
            axes.animate.apply_matrix(A2),
            dots.animate.apply_matrix(A2),
            *[v.animate.apply_matrix(A2) for v in vectors],
            run_time=3.6
        )

        self.wait(0.8)

        # -------------------------------------------------
        # Constraint reveal (line appears late)
        # -------------------------------------------------
        line = Line(LEFT * 5, RIGHT * 5, color=YELLOW)
        line.set_stroke(width=3)

        self.play(FadeIn(line), run_time=0.6)

        self.play(
            line.animate.apply_matrix(A1),
            run_time=2.2
        )

        self.play(
            line.animate.apply_matrix(A2),
            run_time=2.6
        )

        # -------------------------------------------------
        # Hold (authority)
        # -------------------------------------------------
        self.wait(2.2)
