from manim import *

class VMobjectDemo(Scene):
    def construct(self):
        plane = NumberPlane()
        my_vmobject = VMobject(color=GREEN)
        my_vmobject.points = [
            np.array([-2, -1, 0]),  # start of first curve
            np.array([-3, 1, 0]),
            np.array([0, 3, 0]),
            np.array([1, 3, 0]),  # end of first curve

            np.array([1, 3, 0]),  # start of second curve
            np.array([0, 1, 0]),
            np.array([4, 3, 0]),
            np.array([4, -2, 0]),  # end of second curve
        ]
        handles = [
            Dot(point, color=RED) for point in
            [[-3, 1, 0], [0, 3, 0], [0, 1, 0], [4, 3, 0]]
        ]
        handle_lines = [
            Line(
                my_vmobject.points[ind],
                my_vmobject.points[ind+1],
                color=RED,
                stroke_width=2
            ) for ind in range(0, len(my_vmobject.points), 2)
        ]
        self.add(plane, *handles, *handle_lines, my_vmobject)

class HalfCircle(Scene):
    def construct(self):
        plane = NumberPlane()
        shape = VMobject(color=GREEN)
        shape.points = [
            np.array([-5, 0, 0]),
            np.array([-3, 3, 0]),
            np.array([0, 5, 0]),
            np.array([3, 3, 0]),

            np.array([3, 3, 0]),
            np.array([5, 0, 0]),
            np.array([3, -3, 0]),
            np.array([0, -5, 0]),
        ]

        handles = [
            Dot(point, color=RED) for point in shape.points
        ]

        self.add(plane, shape, *handles)


class CustomShape(Scene):
    def construct(self):
        # Create a VMobject
        shape = VMobject()
        
        # Define points for the shape
        shape.set_points_as_corners([
            [-2, 1, 0],  # Top left
            [2, 1, 0],   # Top right
            [1, -1, 0],  # Bottom right
            [-1, -1, 0], # Bottom left
            [-2, 1, 0],  # Back to top left
        ])

        # Set stroke color and width
        shape.set_stroke(color=YELLOW, width=6)
        
        # Add the custom shape to the scene
        self.play(Create(shape))
        self.wait(2)

class SmoothShape(Scene):
    def construct(self):
        shape = VMobject()
        shape.set_points_as_corners([
            [-3, 0, 0],
            [0, 2, 0],
            [3, 0, 0],
            [0, -2, 0],
            [-3, 0, 0]
        ])
        shape.make_smooth()  # Smooth out the corners
        shape.set_stroke(color=RED, width=8)

        self.play(Create(shape))
        self.wait(2)

class PathAnimation(Scene):
    def construct(self):
        # Create a path using VMobject
        path = VMobject()
        path.set_points_as_corners([
            [-4, -2, 0],
            [-1, 2, 0],
            [3, -1, 0],
        ])
        path.set_stroke(color=BLUE, width=4)
        
        # Create a dot that will follow the path
        dot = Dot(point=path.get_start())
        
        # Animate the dot moving along the path
        self.play(Create(path))
        self.play(MoveAlongPath(dot, path), run_time=3)
        self.wait(2)

from manim import *

class BezierShape(Scene):
    def construct(self):
        shape = VMobject()
        shape.set_points_smoothly([
            [-2, 0, 0],
            [0, 2, 0],
            [2, 0, 0],
            [0, -2, 0],
            [-2, 0, 0]
        ])
        
        shape.set_stroke(color=PURPLE, width=5)
        shape.set_fill(color=ORANGE, opacity=0.5)

        # Display the shape on the screen
        self.add(shape)

