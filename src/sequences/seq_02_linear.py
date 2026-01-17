from manim import *
from core.motion_grammar import *
from core.helpers import eigen_system

class LinearCollapse:
    def __init__(self, scene):
        self.scene = scene

    def build(self):
        # Layer 1: ambient space
        grid, basis, eigen = eigen_system()

        # Layer 2: deformation operator
        shear = grid.copy().apply_matrix([[1, 1], [0, 1]])

        # Layer 3: spectrum hint (operator effect)
        spectrum = VGroup(*[
            Rectangle(height=h, width=0.15, color=YELLOW)
            for h in [0.8, 1.4, 1.1, 1.9]
        ]).arrange(RIGHT, buff=0.2).shift(UP * 2)

        return {
            "objects": VGroup(grid, basis, eigen, spectrum),

            "animations": [
                # Grid appears + immediately deforms
                appear(grid, 0.3),
                morph(grid, shear, 1.2),

                # Basis vectors drift (frame is unstable)
                stagger(
                    flow(basis[0], RIGHT, 0.4, 1.2),
                    flow(basis[1], UP, 0.4, 1.2),
                    lag=0.1
                ),

                # Eigenvectors resist (key invariant)
                stagger(
                    flow(eigen[0], LEFT, 0.1, 1.2),
                    flow(eigen[1], RIGHT, 0.1, 1.2),
                    lag=0.1
                ),

                # Spectrum emerges simultaneously
                stagger(
                    *[appear(bar, 0.3) for bar in spectrum],
                    lag=0.08
                ),
            ]
        }
