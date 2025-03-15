from manim import *
import numpy as np

class ParametricTest1(ThreeDScene):
    def construct(self):

        axes = ThreeDAxes().add_coordinates()
        end = ValueTracker(-4.9)

        graph = always_redraw(lambda : 
        ParametricFunction(lambda u : np.array([4*np.cos(u), 4*np.sin(u), 0.5*u]),
        color = BLUE, t_range = [-5, end.get_value()])
        )

        line = always_redraw(lambda : 
        Line(start = ORIGIN, end = graph.get_end(), color = BLUE).add_tip()
        )

        self.set_camera_orientation(phi = 70*DEGREES, theta = -30*DEGREES)
        self.add(axes, graph, line)
        self.play(end.animate.set_value(5), run_time = 3)
        self.wait()

class ParametricTest2(Scene):
    def construct(self):
        # Define a parametric function

        parametric_curve = ParametricFunction(
            lambda t: np.array([
                t,   # x-coordinate
                np.power(t, 2),   # y-coordinate
                0            # z-coordinate (2D curve, so z is 0)
            ]),
            t_range = np.array([-5, 5]),  # Parameter range from 0 to 2*PI
            color = BLUE
        )
        
        # Add the parametric curve to the scene
        self.add(parametric_curve)
        
        # Display the scene
        self.wait(3)