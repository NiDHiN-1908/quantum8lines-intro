from manim import *

class ControlledOverload:
    def __init__(self, scene):
        self.scene = scene

    def animate(self):
        words = VGroup(
            Text("STRUCTURE"),
            Text("FLOW"),
            Text("INVARIANCE"),
        ).arrange(RIGHT, buff=0.6)

        return [
            FadeIn(words, run_time=0.8),
            FadeOut(words, run_time=0.8),
        ]
