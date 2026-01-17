from manim import *
from core.motion_grammar import *

class IdentityLock:
    def __init__(self, scene):
        self.scene = scene

    def build(self):
        title = Text("Quantum8Lines", weight=BOLD)

        return {
            "objects": title,
            "animations": [
                appear(title, 0.8),
                flow(title, DOWN, 0.1, 0.8)
            ]
        }
