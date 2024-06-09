from manim import *

class TransformTest(Scene):
    def construct(self):

        square = Square(
            side_length=3,
            stroke_width=2,
            stroke_color=WHITE,
            fill_color=GREEN,
            fill_opacity=0.5,
        )

        circle = Circle(
            radius=3,
            stroke_width=2,
            stroke_color=WHITE,
            fill_color=BLUE,
            fill_opacity=0.5,
        )

        self.play(Create(square), run_time=2)
        self.wait()

        self.play(Transform(square, circle), run_time=3)
        self.wait()