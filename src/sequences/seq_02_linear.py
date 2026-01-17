from manim import *
from core.motion_grammar import *
from core.helpers import eigen_system


class LinearCollapse:
    """
    Semantic intent of this sequence:

    CENTER  : space is transformed
    LEFT    : invariant directions (eigenvectors)
    RIGHT   : unstable frame (basis)
    TOP     : operator fingerprint (spectrum)
    FLASH   : equation anchor (Ax = λx)

    The equation is an ORIENTATION signal, not a lesson.
    """

    def __init__(self, scene):
        self.scene = scene

    def build(self):
        # -------------------------------------------------
        # Core mathematical objects
        # -------------------------------------------------
        grid, basis, eigen = eigen_system()

        grid.move_to(ORIGIN)
        eigen.shift(LEFT * 3)
        basis.shift(RIGHT * 3)

        # -------------------------------------------------
        # Linear operator (shear)
        # -------------------------------------------------
        shear = grid.copy().apply_matrix([[1, 1], [0, 1]])

        # -------------------------------------------------
        # Spectrum (analysis layer)
        # -------------------------------------------------
        spectrum = VGroup(*[
            Rectangle(height=h, width=0.18, color=YELLOW)
            for h in [0.8, 1.3, 1.0, 1.8]
        ]).arrange(RIGHT, buff=0.25)

        spectrum.shift(UP * 2.5)

        # -------------------------------------------------
        # Equation anchor (TEMPORARY, ALWAYS ON TOP)
        # -------------------------------------------------
        equation = MathTex("A x = \\lambda x")
        equation.scale(1.0)
        equation.set_opacity(0.95)
        equation.move_to(DOWN * 1.5)

        # -------------------------------------------------
        # Return contract
        # -------------------------------------------------
        return {
            # IMPORTANT:
            # Equation is NOT added here — only structural objects
            "objects": VGroup(grid, basis, eigen, spectrum),

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

                # Equation anchor (guaranteed visible)
                Create(equation, run_time=0.4),
                Wait(0.6),
                FadeOut(equation, run_time=0.4),
            ]
        }
