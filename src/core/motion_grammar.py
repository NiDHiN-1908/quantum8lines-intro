from manim import *

class MotionGrammar:
    """
    Motion is language, not decoration.
    """

    BASE_RT = 0.6

    @staticmethod
    def appear(mobj, rt=None):
        return FadeIn(mobj, run_time=rt or MotionGrammar.BASE_RT)

    @staticmethod
    def vanish(mobj, rt=None):
        return FadeOut(mobj, run_time=rt or MotionGrammar.BASE_RT)

    @staticmethod
    def morph(src, target, rt=1.0):
        return Transform(src, target, run_time=rt)

    @staticmethod
    def flow(mobj, direction=UP, mag=0.4, rt=1.0):
        return mobj.animate.shift(direction * mag).set_run_time(rt)
