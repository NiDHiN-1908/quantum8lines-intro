from manim import *

def eigen_system():
    """
    Returns a minimal linear-algebra system with:
    - a grid (ambient space)
    - basis vectors (that can drift/rotate)
    - eigenvectors (that resist change)

    This function is intentionally opinionated.
    It encodes meaning, not convenience.
    """

    # Ambient space
    grid = NumberPlane(
        x_range=[-6, 6, 1],
        y_range=[-4, 4, 1],
        background_line_style={
            "stroke_opacity": 0.4,
            "stroke_width": 1
        }
    )

    # Basis vectors (changeable frame)
    basis = VGroup(
        Vector([1, 0], color=GREEN),
        Vector([0, 1], color=GREEN),
    )

    # Eigenvectors (invariant directions)
    eigen = VGroup(
        Vector([2, 0], color=RED),
        Vector([-2, 0], color=RED),
    )

    return grid, basis, eigen
