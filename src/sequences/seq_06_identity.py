from manim import *
from core.motion_grammar import *


class IdentityLock:
    def __init__(self, scene):
        self.scene = scene

    def build(self):
        title = Text("Quantum8Lines", weight=BOLD)
        title.scale(0.9)
        title.set_opacity(0.9)

        # Slight offset so it lives INSIDE the math, not on top of it
        title.shift(DOWN * 0.2)

        return {
            "objects": title,
            "animations": [
                FadeIn(title, run_time=0.6),
                flow(title, UP * 0.0, 0.0, 0.6),
            ]
        }
