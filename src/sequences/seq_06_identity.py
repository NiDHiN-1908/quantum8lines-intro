from manim import *

class IdentityLock:
    def __init__(self, scene):
        self.scene = scene

    def animate(self):
        title = Text("Quantum8Lines", weight=BOLD)
        return [Write(title, run_time=1.2)]
