from manim import *

from sequences.seq_01_disruption import Disruption
from sequences.seq_02_linear import LinearCollapse
from sequences.seq_03_geometry import GeometryInvasion
from sequences.seq_04_operator import OperatorSignal
from sequences.seq_05_overload import ControlledOverload
from sequences.seq_06_identity import IdentityLock


class Quantum8LinesIntro(Scene):
    def construct(self):
        # --- Phase 1: Mathematical World (NO LOGO) ---
        math_sequences = [
            Disruption(self),
            LinearCollapse(self),
            GeometryInvasion(self),
            OperatorSignal(self),
        ]

        for seq in math_sequences:
            data = seq.build()
            self.add(data["objects"])
            self.play(*data["animations"], run_time=1.8)

        # --- Phase 2: Concept Compression ---
        overload = ControlledOverload(self).build()
        self.add(overload["objects"])
        self.play(*overload["animations"], run_time=1.2)

        # --- Phase 3: Identity Lock (LOGO ONLY NOW) ---
        identity = IdentityLock(self).build()
        self.clear()  # <<< THIS IS CRITICAL
        self.add(identity["objects"])
        self.play(*identity["animations"], run_time=1.5)
