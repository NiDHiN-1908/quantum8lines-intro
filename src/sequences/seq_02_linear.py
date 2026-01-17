from manim import *
from core.motion_grammar import *
from core.helpers import eigen_system


class LinearCollapse:
    """
    Semantic contract:
    CENTER  : space is transformed
    LEFT    : invariants (eigenvectors)
    RIGHT   : unstable frame (basis)
    TOP     : operator fingerprint (spectrum)
    OVERLAY : eigen-structure anchor (Ax = λx)
    """

    def __init__(self, scene):
        self.scene = scene

    def build(self):
        # -----------------------------
        # Core mathematical objects
        # -----------------------------
        grid, basis, eigen = eigen_system()

        grid.move_to(ORIGIN)
        eigen.shift(LEFT * 3)
        basis.shift(RIGHT * 3)

        # -----------------------------
        # Linear operator (shear)
        # -----------------------------
        shear = grid.copy().apply_matrix([[1, 1], [0, 1]])

        # -----------------------------
        # Spectrum (analysis layer)
        # -----------------------------
        spectrum = VGroup(*[
            Rectangle(height=h, width=0.18, color=YELLOW)
            for h in [0.8, 1.3, 1.0, 1.8]
        ]).arrange(RIGHT, buff=0.25)

        spectrum.shift(UP * 2.5)

        # -----------------------------
        # Equation anchor (VISIBLE)
        # -----------------------------
        equation = MathTex("A x = \\lambda x")
        equation.scale(1.0)
        equation.set_opacity(0.95)
        equation.move_to(DOWN * 1.5)
        equation.set_z_index(100)   # force top layer safely

        # -----------------------------
        # Return contract
        # -----------------------------
        return {
            "objects": VGroup(grid, basis, eigen, spectrum, equation),

            "animations": [
                # Space appears and deforms
                appear(grid, 0.3),
                morph(grid, shear, 1.2),

                # Frame instability (right)
                stagger(
                    flow(basis[0], UP, 0.35, 1.2),
                    flow(basis[1], RIGHT, 0.35, 1.2),
                    lag=0.12
                ),

                # Invariant directions resist (left)
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

                # Equation anchor (no Scene calls here!)
                appear(equation, 0.4),
                Wait(0.6),
                vanish(equation, 0.4),
            ]
        }
