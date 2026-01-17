from manim import *

from sequences.seq_01_disruption import Disruption
from sequences.seq_02_linear import LinearCollapse
from sequences.seq_03_geometry import GeometryInvasion
from sequences.seq_04_operator import OperatorSignal
from sequences.seq_05_overload import ControlledOverload
from sequences.seq_06_identity import IdentityLock

class Quantum8LinesIntro(Scene):
    def construct(self):
        self.play(*Disruption(self).animate())
        self.play(*LinearCollapse(self).animate())
        self.play(*GeometryInvasion(self).animate())
        self.play(*OperatorSignal(self).animate())
        self.play(*ControlledOverload(self).animate())
        self.play(*IdentityLock(self).animate())
