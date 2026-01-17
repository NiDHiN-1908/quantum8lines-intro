from manim import *

from sequences.seq_01_disruption import Disruption
from sequences.seq_02_linear import LinearCollapse
from sequences.seq_03_geometry import GeometryInvasion
from sequences.seq_04_operator import OperatorSignal
from sequences.seq_05_overload import ControlledOverload
from sequences.seq_06_identity import IdentityLock

class Quantum8LinesIntro(Scene):
    def construct(self):
        sequences = [
            Disruption(self),
            LinearCollapse(self),
            GeometryInvasion(self),
            OperatorSignal(self),
            ControlledOverload(self),
            IdentityLock(self),
        ]

        for seq in sequences:
            data = seq.build()
            self.add(data["objects"])
            self.play(*data["animations"], run_time=1.8)
