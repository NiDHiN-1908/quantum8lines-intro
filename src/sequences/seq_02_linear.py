from manim import *
from core.motion_grammar import *
from core.helpers import eigen_system


class LinearCollapse:
    """
    Spatial grammar (locked):
    - CENTER  : ambient space (grid deformation)
    - LEFT    : eigenvectors (invariants / resistance)
    - RIGHT   : basis vectors (frame instability)
    - TOP     : spectrum (operator fingerprint)
    """

    def __init__(self, scene):
        self.scene = scene

    def build(self):
        # ===== Core system =====
        grid, basis, eigen = eigen_system()

        # Positioning (spatial roles)
        grid.move_to(ORIGIN)
        eigen.shift(LEFT * 3)
        basis.shift(RIGHT * 3)

        # ===== Operator deformation =====
        shear = grid.copy().apply_matrix([[1, 1], [0, 1]])

        # ===== Spectrum (top layer) =====
        spectrum = VGroup(*[
            Rectangle(height=h, width=0.18, color=YELLOW)
            for h in [0.8, 1.3, 1.0, 1.8]
        ]).arrange(RIGHT, buff=0.25)

        spectrum.shift(UP * 2.5)

        # ===== Returned structure =====
        return {
            "objects": VGroup(grid, basis, eigen, spectrum),

            "animations": [
                # Ambient space: appears and deforms
                appear(grid, 0.3),
                morph(grid, shear, 1.2),

                # Basis: frame instability (right side)
                stagger(
                    flow(basis[0], UP, 0.35, 1.2),
                    flow(basis[1], RIGHT, 0.35, 1.2),
                    lag=0.12
                ),

                # Eigenvectors: resistance (left side)
                stagger(
                    flow(eigen[0], LEFT, 0.12, 1.2),
                    flow(eigen[1], RIGHT, 0.12, 1.2),
                    lag=0.12
                ),

                # Spectrum: operator signature (top)
                stagger(
                    *[appear(bar, 0.25) for bar in spectrum],
                    lag=0.1
                ),
            ]
        }
