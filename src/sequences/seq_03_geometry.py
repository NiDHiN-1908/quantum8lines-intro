from manim import *
import numpy as np

class GeometryInvasion:
    def __init__(self, scene):
        self.scene = scene

    def animate(self):
        surface = Surface(
            lambda u, v: np.array([u, v, 0.3 * np.sin(u * v)]),
            u_range=(-3, 3),
            v_range=(-3, 3),
        ).set_style(fill_opacity=0.35)

        return [FadeIn(surface, run_time=2.0)]
