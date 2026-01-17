from manim import *
from core.motion_grammar import *

class ControlledOverload:
    def __init__(self, scene):
        self.scene = scene

    def build(self):
        words = VGroup(
            Text("STRUCTURE"),
            Text("FLOW"),
            Text("INVARIANCE")
        ).arrange(RIGHT, buff=0.6)

        return {
            "objects": words,
            "animations": [
                stagger(*[appear(w, 0.3) for w in words], lag=0.15),
                vanish(words, 0.6)
            ]
        }
