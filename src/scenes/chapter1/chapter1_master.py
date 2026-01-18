from manim import *

# Import sections as modules
from section1_birth_of_structure_split import Section1BirthOfStructureSplit
from section2_linearity_constraint import Chapter1LinearityConstraint
from section2_linearity_constraint_split import Section2LinearityConstraintSplit
from section3_operator_split import Section3OperatorSplit
from section4_invariance import Section4Invariance


class Chapter1Master(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # -------------------------------------------------
        # Helper: play a section cleanly
        # -------------------------------------------------
        def play_section(section_class, buffer_time=0.4):
            section = section_class()
            section.construct()
            self.wait(buffer_time)
            self.clear()

        # -------------------------------------------------
        # SECTION 1 — Birth of Structure
        # -------------------------------------------------
        play_section(Section1BirthOfStructureSplit, buffer_time=0.5)

        # -------------------------------------------------
        # SECTION 2 — Linearity as Constraint
        # (simple → split, increasing density)
        # -------------------------------------------------
        play_section(Chapter1LinearityConstraint, buffer_time=0.4)
        play_section(Section2LinearityConstraintSplit, buffer_time=0.5)

        # -------------------------------------------------
        # SECTION 3 — Operator as Machine
        # -------------------------------------------------
        play_section(Section3OperatorSplit, buffer_time=0.5)

        # -------------------------------------------------
        # SECTION 4 — Invariance
        # -------------------------------------------------
        play_section(Section4Invariance, buffer_time=0.8)

        # -------------------------------------------------
        # CHAPTER HOLD (viewer breath)
        # -------------------------------------------------
        self.wait(1.2)
