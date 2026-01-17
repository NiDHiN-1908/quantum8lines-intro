from manim import *
from core.motion_grammar import *
from core.helpers import eigen_system


class LinearCollapse:
    """
    INTRO MESSAGE THIS SEQUENCE DELIVERS (WITHOUT WORDS):

    - CENTER  : space is being transformed
    - LEFT    : some directions resist change (invariants)
    - RIGHT   : coordinate frame is unstable
    - TOP     : operator leaves a measurable fingerprint
    - OVERLAY : this is eigen-structure (Ax = λx)

    This is orientation, not explanation.
    """

    def __init__(self, scene):
        self.scene = scene

    def build(self):
        # -------------------------------------------------
        # Core mathematical objects
        # -------------------------------------------------
        grid, basis, eigen = eigen_system()

        # Spatial roles (locked)
        grid.move_to(ORIGIN)
        eigen.shift(LEFT * 3)
        basis.shift(RIGHT * 3)

        # -------------------------------------------------
        # Linear operator (shear transformation)
        # -------------------------------------------------
        shear = grid.copy().apply_matrix([[1, 1], [0, 1]])

        # -------------------------------------------------
        # Operator spectrum (analysis layer)
        # -------------------------------------------------
        spectrum = VGroup(*[
            Rectangle(height=h, width=0.18, color=YELLOW)
            for h in [0.8, 1.3, 1.0, 1.8]
        ]).arrange(RIGHT, buff=0.25)

        spectrum.shift(UP * 2.5)

        # -------------------------------------------------
        # Equation anchor (must be seen)
        # -------------------------------------------------
        equation = MathTex("A x = \\lambda x")
        equation.scale(1.0)
        equation.set_opacity(0.95)
        equation.move_to(DOWN * 1.5)
        equation.set_z_index(10)   # Force above all geometry

        # -------------------------------------------------
        # Return contract (objects + animations)
        # -------------------------------------------------
        return {
            "objects": VGroup(grid, basis, eigen, spectrum, equation),

            "animations": [
                # Space appears and deforms
                appear(grid, 0.3),
                morph(grid, shear, 1.2),

                # Coordinate frame instability (right side)
                stagger(
                    flow(basis[0], UP, 0.35, 1.2),
                    flow(basis[1], RIGHT, 0.35, 1.2),
                    lag=0.12
                ),

                # Invariant directions resist (left side)
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

                # Equation overlay (explicitly brought to front)
                self.scene.bring_to_front(equation),
                appear(equation, 0.4),
                Wait(0.6),
                vanish(equation, 0.4),
            ]
        }
