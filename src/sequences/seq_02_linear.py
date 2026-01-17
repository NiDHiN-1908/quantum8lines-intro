from manim import *
from core.motion_grammar import *
from core.helpers import eigen_system

class LinearCollapse:
    def __init__(self, scene):
        self.scene = scene

    def build(self):
        grid, basis, eigen = eigen_system()

        deformed = grid.copy().apply_matrix([[1, 1], [0, 1]])

        return {
            "objects": VGroup(grid, basis, eigen),
            "animations": [
                appear(grid, 0.4),
                stagger(
                    morph(grid, deformed, 1.2),
                    flow(basis, RIGHT, 0.3, 1.2),
                    lag=0.1
                ),
                flow(eigen, UP, 0.2, 1.2),
            ]
        }
