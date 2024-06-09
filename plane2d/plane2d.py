from manim import *

class Plane2d(Scene):
    def construct(self):

        # create plane and add to coordinate
        plane = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
        ).add_coordinates()

        self.play(Create(plane), run_time=3)
        self.wait()

class Plane2dA(Scene):
    def construct(self):
        
        plane = NumberPlane(x_range=[-7,7,1], y_range=[-4,4,1]).add_coordinates()

        axes = Axes(x_range=[-3,3,1], y_range=[-3,3,1], x_length = 6, y_length=6)
        axes.to_edge(LEFT, buff=0.5)
        
        circle = Circle(stroke_width = 6, stroke_color = YELLOW, fill_color = RED_C, fill_opacity = 0.8)
        circle.set_width(2).to_edge(DR, buff=0)

        triangle = Triangle(stroke_color = ORANGE, stroke_width = 10, 
        fill_color = GREY).set_height(2).shift(DOWN*3+RIGHT*3)

        code = Code(
            file_name="main.py",
            background="window",
            language="python",
            insert_line_no=True,
            tab_width=2,
            line_spacing=0.3,
            font_size=12,  # Adjust font size for better visibility
            font="Monospace"
        ).set_width(6).to_edge(UR, buff=0.5)
        
        self.play(FadeIn(plane), Write(code), run_time=3)
        self.wait()
        # self.play(Write(axes))
        # self.wait()
        # self.play(plane.animate.set_opacity(0.4))
        # self.wait()
        # self.play(DrawBorderThenFill(circle))
        # self.wait()
        # self.play(circle.animate.set_width(1))
        # self.wait()
        # self.play(Transform(circle, triangle), run_time=3)
        # self.wait()
