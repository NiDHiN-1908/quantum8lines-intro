from manim import *
from core.motion_grammar import *
from core.helpers import eigen_system


class LinearCollapse:
    """
    Semantic contract of this scene:
    - CENTER  : space being transformed
    - LEFT    : invariants (eigenvectors)
    - RIGHT   : unstable frame (basis)
    - TOP     : operator fingerprint (spectrum)
    - OVERLAY : equation anchor (domain orientation)
    """

    def __init__(self, scene):
        self.scene = scene

    def build(self):
        # ===== Core system =====
        grid, basis, eigen = eigen_system()

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

        # ===== Equation anchor (NOT a lesson) =====
        equation = MathTex("A x = \\lambda x")
        equation.scale(0.9)
        equation.set_opacity(0.65)
        equation.next_to(grid, DOWN, buff=0.4)

        # ===== Returned structure =====
        return {
            "objects": VGroup(grid, basis, eigen, spectrum, equation),

            "animations": [
                # Space appears and deforms
                appear(grid, 0.3),
                morph(grid, shear, 1.2),

                # Basis instability (right)
                stagger(
                    flow(basis[0], UP, 0.35, 1.2),
                    flow(basis[1], RIGHT, 0.35, 1.2),
                    lag=0.12
                ),

                # Eigenvectors resist (left)
                stagger(
                    flow(eigen[0], LEFT, 0.12, 1.2),
                    flow(eigen[1], RIGHT, 0.12, 1.2),
                    lag=0.12
                ),

                # Spectrum emerges (top)
                stagger(
                    *[appear(bar, 0.25) for bar in spectrum],
                    lag=0.1
                ),

                # Equation flashes briefly, then leaves
                appear(equation, 0.25),
                vanish(equation, 0.4),
            ]
        }
