from manim import *

BASE_RT = 0.6

def appear(mobj, rt=BASE_RT):
    return FadeIn(mobj, run_time=rt)

def vanish(mobj, rt=BASE_RT):
    return FadeOut(mobj, run_time=rt)

def morph(a, b, rt=1.0):
    return Transform(a, b, run_time=rt)

def flow(mobj, direction=UP, mag=0.4, rt=1.0):
    return mobj.animate.shift(direction * mag).set_run_time(rt)

def stagger(*anims, lag=0.15):
    return LaggedStart(*anims, lag_ratio=lag)
