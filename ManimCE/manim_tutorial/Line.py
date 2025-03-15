from manim import *

class LineTest(Scene):
    def construct(self):
        pixel_height = config["pixel_height"]  #  1080 is default
        pixel_width = config["pixel_width"]  # 1920 is default

        # frame is used for zoom in and zoom out
        frame_width = config["frame_width"]
        frame_height = config["frame_height"]

        self.add(Dot(
            point=ORIGIN
        ))
        self.add(Dot(
            point=(frame_width / 2 * LEFT)
        ))
        self.add(Dot(
            point=(frame_width / 2 * RIGHT)
        ))
        d1 = Line(frame_width * LEFT / 2, frame_width * RIGHT / 2).to_edge(DOWN)
        self.add(d1)
        self.add(Text(str(pixel_width)).next_to(d1, UP))
        d2 = Line(frame_height * UP / 2, frame_height * DOWN / 2).to_edge(LEFT)
        self.add(d2)
        self.add(Text(str(pixel_height)).next_to(d2, RIGHT))