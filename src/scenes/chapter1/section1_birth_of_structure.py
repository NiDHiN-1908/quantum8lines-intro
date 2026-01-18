import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

from manim import *
from core.chapter_title import chapter_title


class Chapter1BirthOfStructure(Scene):
    def construct(self):

        # -------------------------------------------------
        # Normalized chapter title (LOCKED)
        # -------------------------------------------------
        chapter_title(self, "Chapter 1 — Structure")

        # -------------------------------------------------
        # Scene 1: Passive space
        # -------------------------------------------------
        grid = NumberPlane(
            x_range=[-6, 6, 1],
            y_range=[-4, 4, 1],
            background_line_style={
                "stroke_opacity": 0.35,
                "stroke_width": 1
            }
        )

        axes = Axes(
            x_range=[-6, 6],
            y_range=[-4, 4],
            axis_config={"stroke_opacity": 0.6}
        )

        vectors = VGroup(
            Vector([2, 1], color=BLUE),
            Vector([-1.5, 1], color=BLUE),
            Vector([1, -1.5], color=BLUE),
        )

        self.add(grid, axes, vectors)
        self.wait(1.0)

        # -------------------------------------------------
        # Scene 2: First disturbance (smooth, global)
        # -------------------------------------------------
        A1 = [[1.2, 0.0],
              [0.0, 1.0]]

        self.play(
            grid.animate.apply_matrix(A1),
            axes.animate.apply_matrix(A1),
            *[v.animate.apply_matrix(A1) for v in vectors],
            run_time=3.0
        )

        self.wait(0.5)

        # -------------------------------------------------
        # Scene 3: Directional bias
        # -------------------------------------------------
        A2 = [[1.0, 0.6],
              [0.0, 1.0]]

        self.play(
            grid.animate.apply_matrix(A2),
            axes.animate.apply_matrix(A2),
            *[v.animate.apply_matrix(A2) for v in vectors],
            run_time=3.5
        )

        self.wait(0.5)

        # -------------------------------------------------
        # Scene 4: Structure consistency (reset + replay)
        # -------------------------------------------------
        self.play(
            FadeOut(vectors),
            run_time=0.6
        )

        new_vectors = VGroup(
            Vector([3, 0.5], color=BLUE),
            Vector([-2, -1], color=BLUE),
            Vector([1, 2], color=BLUE),
        )

        self.add(new_vectors)
        self.wait(0.5)

        self.play(
            grid.animate.apply_matrix(A1),
            axes.animate.apply_matrix(A1),
            *[v.animate.apply_matrix(A1) for v in new_vectors],
            run_time=2.5
        )

        self.play(
            grid.animate.apply_matrix(A2),
            axes.animate.apply_matrix(A2),
            *[v.animate.apply_matrix(A2) for v in new_vectors],
            run_time=3.0
        )

        self.wait(0.5)

        # -------------------------------------------------
        # Scene 5: Constraint reveal (line stays straight)
        # -------------------------------------------------
        line = Line(LEFT * 5, RIGHT * 5, color=YELLOW)
        self.add(line)
        self.wait(0.4)

        self.play(
            line.animate.apply_matrix(A1),
            run_time=2.0
        )

        self.play(
            line.animate.apply_matrix(A2),
            run_time=2.5
        )

        # -------------------------------------------------
        # Scene 6: Tension hold
        # -------------------------------------------------
        self.wait(2.0)
