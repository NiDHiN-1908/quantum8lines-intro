from manim import *

class OperatorSignal:
    def __init__(self, scene):
        self.scene = scene

    def animate(self):
        bars = VGroup(*[
            Rectangle(height=h, width=0.25)
            for h in [1, 2, 1.5, 2.5]
        ]).arrange(RIGHT, buff=0.3)

        return [LaggedStartMap(FadeIn, bars, lag_ratio=0.15)]
