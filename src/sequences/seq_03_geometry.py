from manim import *
import numpy as np
from core.motion_grammar import *

class GeometryInvasion:
    def __init__(self, scene):
        self.scene = scene

    def build(self):
        surface = Surface(
            lambda u, v: np.array([u, v, 0.3*np.sin(u*v)]),
            u_range=(-3, 3),
            v_range=(-3, 3)
        ).set_style(fill_opacity=0.35)

        return {
            "objects": surface,
            "animations": [
                appear(surface, 0.6),
                flow(surface, OUT, 0.3, 1.2)
            ]
        }
