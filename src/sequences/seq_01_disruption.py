from manim import *

class Disruption:
    def __init__(self, scene):
        self.scene = scene

    def animate(self):
        line = Line(LEFT, RIGHT)
        split = VGroup(
            Line(LEFT, ORIGIN),
            Line(ORIGIN, RIGHT)
        )

        return [
            Create(line, run_time=0.5),
            Transform(line, split, run_time=0.7),
        ]
