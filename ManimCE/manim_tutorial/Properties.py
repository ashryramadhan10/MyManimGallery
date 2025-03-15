from manim import *

class AlignTo(Scene):
    def construct(self):
        c1, c2, c3 = [Circle(radius=1.5 - i / 3, color=WHITE)
                      for i in range(3)]

        self.play(*[Write(o) for o in [c1, c2, c3]])

        # align such that c1 < c2 < c3
        self.play(
            c1.animate.next_to(c2, LEFT),
            c3.animate.next_to(c2, RIGHT),
        )

        # align c1 and c2 such that their bottoms are the same as c2
        self.play(
            c1.animate.align_to(c2, DOWN),
            c3.animate.align_to(c2, DOWN),
        )

        point = [1.0, 2.5, 0]

        # align all circles such that their top touches a line going through the point
        self.play(
            c1.animate.align_to(point, UP),
            c2.animate.align_to(point, UP),
            c3.animate.align_to(point, UP),
        )

class CenterExample(Scene):
    def construct(self):
        square = Square()
        self.add(square)
        print(square.get_center())  # Prints the center coordinates of the square

class CornerExample(Scene):
    def construct(self):
        square = Square()
        corner = square.get_corner(UL)  # Gets the upper-left corner
        dot = Dot(corner)
        self.add(square, dot)

class EdgeCenterExample(Scene):
    def construct(self):
        square = Square()
        dot = Dot(square.get_edge_center(LEFT))  # Dot at the center of the left edge
        self.add(square, dot)

class LineStartEndExample(Scene):
    def construct(self):
        line = Line(LEFT, RIGHT)
        start = line.get_start()  # Start of the line (LEFT)
        end = line.get_end()      # End of the line (RIGHT)
        dot_start = Dot(start).set_color(RED)
        dot_end = Dot(end).set_color(BLUE)
        self.add(line, dot_start, dot_end)

class RotationExample(Scene):
    def construct(self):
        square = Square()
        square.rotate(PI / 4)  # Rotate by 45 degrees
        self.add(square)

class ScaleExample(Scene):
    def construct(self):
        circle = Circle().scale(2)  # Double the size of the circle
        self.add(circle)

class ColorExample(Scene):
    def construct(self):
        square = Square().set_color(RED)  # Set square color to red
        self.add(square)

class StrokeAndFillExample(Scene):
    def construct(self):
        circle = Circle().set_stroke(color=GREEN, width=8)
        circle.set_fill(color=BLUE, opacity=0.5)
        self.add(circle)

class MoveToExample(Scene):
    def construct(self):
        square = Square()
        dot = Dot().move_to(square.get_corner(UR))  # Move dot to square's upper-right corner
        self.add(square, dot)

class ShiftExample(Scene):
    def construct(self):
        square = Square()
        square.shift(UP * 2)  # Move square up by 2 units
        self.add(square)

class NextToExample(Scene):
    def construct(self):
        square = Square()
        circle = Circle().next_to(square, RIGHT)  # Place circle to the right of square
        self.add(square, circle)

class SizeExample(Scene):
    def construct(self):
        square = Square()
        print(f"Width: {square.get_width()}, Height: {square.get_height()}")
        self.add(square)

class StretchExample(Scene):
    def construct(self):
        square = Square()
        square.stretch(2, 0)  # Stretch along the X-axis by a factor of 2
        self.add(square)

class CopyExample(Scene):
    def construct(self):
        square = Square()
        square_copy = square.copy().set_color(RED)
        self.add(square, square_copy)

class SubmobjectExample(Scene):
    def construct(self):
        group = VGroup()
        circle = Circle().set_color(RED)
        square = Square().set_color(BLUE)
        group.add(circle, square)  # Add circle and square to the group
        self.add(group)

class BoundingBoxExample(Scene):
    def construct(self):
        square = Square()
        bounding_box = square.get_bounding_box()  # Get bounding box coordinates
        self.add(square)