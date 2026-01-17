from manim import *

class QuantumCamera:
    """
    Camera motion must encode meaning.
    Random zooms are forbidden.
    """

    @staticmethod
    def change_basis(scene, angle=0.25, run_time=1.0):
        return scene.camera.frame.animate.rotate(angle).set_run_time(run_time)

    @staticmethod
    def pan(scene, direction=RIGHT, distance=1.0, run_time=1.0):
        return scene.camera.frame.animate.shift(direction * distance).set_run_time(run_time)
