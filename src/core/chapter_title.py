from manim import *


def chapter_title(scene, text):
    title = Text(text, weight=BOLD)
    title.scale(0.9)
    title.to_edge(DOWN)

    scene.play(FadeIn(title), run_time=0.5)
    scene.wait(0.2)
    scene.play(FadeOut(title), run_time=0.3)
