from manim import *

class ReplacementTransformTest(Scene):
    def construct(self):
        square = Square()
        circle = Circle()

        self.add(square)
        self.wait(1)
        self.play(ReplacementTransform(square, circle))
        self.wait(1)
