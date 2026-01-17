from manim import *
from core.motion_grammar import *

class Disruption:
    def __init__(self, scene):
        self.scene = scene

    def build(self):
        line = Line(LEFT, RIGHT)
        split = VGroup(
            Line(LEFT, ORIGIN),
            Line(ORIGIN, RIGHT)
        )

        return {
            "objects": line,
            "animations": [
                appear(line, 0.3),
                morph(line, split, 0.6),
                flow(split, UP, 0.2, 0.6)
            ]
        }
