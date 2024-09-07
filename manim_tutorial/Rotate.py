from manim import *
import numpy as np

class Rotations(Scene):
    def construct(self):

        square = Square(
            side_length=3,
            stroke_width=2,
            stroke_color=BLUE,
            fill_color=GREEN,
            fill_opacity=0.5,
        )
        
        self.play(square.animate.rotate(PI / 2), run_time=1)
        self.play(square.animate.rotate(PI / 2), run_time=1)
        self.wait()

class ManualRotation(Scene):
    def construct(self):

        circle = Circle(radius=3)
        circle_radius = circle.radius

        dot = Dot(color=GREEN)
        dot.move_to(
            circle.get_center() + circle_radius * np.array([
                np.cos(PI / 4), # in radians
                np.sin(PI / 4), # in radians
                0
            ])
        )

        self.add(circle, dot)

class LineRotation(Scene):
    def construct(self):

        def dot_updater(dot, target_point):
            dot.move_to(target_point)
            return dot
    
        # Create a line
        line = Line(start=np.array([-2, 0, 0]), end=np.array([2, 0, 0]))

        # Create a dot
        dot = Dot(fill_color=BLUE)
        dot.move_to(line.get_end())
        dot.add_updater(lambda x: dot_updater(x, line.get_end()))

        # Show the original line
        self.add(line, dot)
        self.wait()

        # Calculate the midpoint of the line
        midpoint = line.get_center_of_mass()

        # Define the rotation angle
        angle = np.pi * 2

        # Rotate the line gradually around its midpoint
        self.play(
            Rotate(line, angle, about_point=midpoint), run_time=2
        )

        # Show the rotated line
        self.wait()

