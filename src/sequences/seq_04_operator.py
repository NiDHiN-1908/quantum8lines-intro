from manim import *
from core.motion_grammar import *

class OperatorSignal:
    def __init__(self, scene):
        self.scene = scene

    def build(self):
        bars = VGroup(*[
            Rectangle(height=h, width=0.25)
            for h in [1, 2, 1.5, 2.5]
        ]).arrange(RIGHT, buff=0.3)

        return {
            "objects": bars,
            "animations": [
                stagger(*[appear(b, 0.3) for b in bars], lag=0.1),
                flow(bars, UP, 0.3, 1.0)
            ]
        }
