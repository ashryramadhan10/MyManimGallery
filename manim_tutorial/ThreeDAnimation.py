from manim import *

class ImageScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=45 * DEGREES, theta=-60 * DEGREES)  # 2.5D
        self.begin_ambient_camera_rotation(rate=0.5)
        Disp_array= VMobject()
        for x in range(-3, 3):
            for y in range(-3, 3):
                for z in range(-3, 3):
                    dot = Dot(point=(x, y, z))
                    Disp_array.add(dot)
        [Disp_array.submobjects[i].set_color(RED) for i in range(0,100)]
        self.add(Disp_array)
        self.wait(5)

class CameraOrientationExample(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        sphere = Sphere(radius=1, color=BLUE)

        self.set_camera_orientation(phi=75 * DEGREES, theta=-60 * DEGREES)
        self.add(axes, sphere)
        self.begin_ambient_camera_rotation(rate=0.3)  # Slow rotation
        
        self.wait(5)  # Let the camera rotate for 5 seconds

class Function(ThreeDScene):
    def construct(self):

        self.set_camera_orientation(zoom = 0.6) 
        axes = ThreeDAxes()
        cos_graph = axes.plot(lambda x: np.cos(x), color = RED)
        curve = ParametricFunction(lambda x: np.array([np.sin(x), np.cos(x), x/2]), color = BLUE, t_range = (-TAU, TAU)) 

        t = Text("Example").to_edge(UL)
        self.add_fixed_in_frame_mobjects(t) 
        self.play(Write(axes), Write(t))

        self.play(Write(cos_graph))
        self.move_camera(phi=60*DEGREES, theta=-45*DEGREES)
        self.play(Write(curve))
        self.move_camera(phi=30*DEGREES, theta=-45*DEGREES)
        self.wait(2)

        g = VGroup(curve, cos_graph, t, axes)
        self.play(Unwrite(g), run_time = 1.5)
        self.wait()