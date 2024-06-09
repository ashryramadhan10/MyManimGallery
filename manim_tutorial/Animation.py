from manim import *
import numpy as np
import math

class AnimationTest(Scene):
    def construct(self):

        text_index = ValueTracker(0)
        
        text = Text("Hello World")
        text_len = len(text.text)
        colors = np.random.randint(0, 255, (text_len, 3))
        text.add_updater(lambda text, dt: self.text_updater(text, dt, text_index, colors))

        for i in range(text_len):
            r = colors[i][0]
            g = colors[i][1]
            b = colors[i][2]

            text[i].set_color(ManimColor.from_rgb((r, g, b)))

        self.add(text)
        self.wait(3)

    def text_updater(self, text, dt, text_index, colors):

        text_index.increment_value(len(text.text) * dt)
        i = int(text_index.get_value() % len(text.text))
        
        if i > 0:
            r = colors[i][0]
            g = colors[i][1]
            b = colors[i][2]

            text[i].set_color(text[i-1].get_color())
            text[i-1].set_color(ManimColor.from_rgb((r, g, b)))
        else:
            r = colors[i][0]
            g = colors[i][1]
            b = colors[i][2]

            text[i].set_color(ManimColor.from_rgb((r, g, b)))

        return text