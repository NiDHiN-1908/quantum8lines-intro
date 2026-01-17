from manim import *
from core.motion_grammar import *
from core.helpers import eigen_system


class LinearCollapse:
    """
    What this sequence communicates (even without narration):

    CENTER  : space is being transformed
    LEFT    : some directions resist change (invariants)
    RIGHT   : coordinate frame is unstable
    TOP     : operator has a measurable fingerprint
    OVERLAY : this is eigen-structure (Ax = λx)

    This is an ORIENTATION signal, not a lesson.
    """

    def __init__(self, scene):
        self.scene = scene

    def build(self):
        # -------------------------------------------------
        # Core mathematical system
        # -------------------------------------------------
        grid, basis, eigen = eigen_system()

        # Spatial roles (LOCKED)
        grid.move_to(ORIGIN)
        eigen.shift(LEFT * 3)
        basis.shift(RIGHT * 3)

        # -------------------------------------------------
        # Linear operator (shear)
        # -------------------------------------------------
        shear = grid.copy().apply_matrix([[1, 1], [0, 1]])

        # -------------------------------------------------
        # Spectrum (operator fingerprint)
        # -------------------------------------------------
        spectrum = VGroup(*[
            Rectangle(height=h, width=0.18, color=YELLOW)
            for h in [0.8, 1.3, 1.0, 1.8]
        ]).arrange(RIGHT, buff=0.25)

        spectrum.shift(UP * 2.5)

        # -------------------------------------------------
        # Equation anchor (VISIBLE, BRIEF, ORIENTING)
        # -------------------------------------------------
        equation = MathTex("A x = \\lambda x")
        equation.scale(1.0)
        equation.set_opacity(0.9)
        equation.move_to(DOWN * 1.5)

        # -------------------------------------------------
        # Return data contract
        # -------------------------------------------------
        return {
            "objects": VGroup(grid, basis, eigen, spectrum, equation),

            "animations": [
                # Space appears and deforms
                appear(grid, 0.3),
                morph(grid, shear, 1.2),

                # Coordinate frame instability (right)
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

                # Operator spectrum emerges (top)
                stagger(
                    *[appear(bar, 0.25) for bar in spectrum],
                    lag=0.1
                ),

                # Equation anchor (must be noticed)
                appear(equation, 0.4),
                Wait(0.6),
                vanish(equation, 0.4),
            ]
        }
