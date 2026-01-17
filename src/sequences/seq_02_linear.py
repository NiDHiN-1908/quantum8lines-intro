from manim import *
from core.helpers import eigen_vectors

class LinearCollapse:
    def __init__(self, scene):
        self.scene = scene

    def animate(self):
        grid = NumberPlane()
        ev = eigen_vectors()
        deformed = grid.copy().apply_matrix([[1, 1], [0, 1]])

        return [
            Create(grid, run_time=0.6),
            Transform(grid, deformed, run_time=1.4),
            FadeIn(ev, run_time=0.6),
        ]
