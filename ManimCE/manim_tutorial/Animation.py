from manim import *
import numpy as np
import math

class TransformMatchingShapesExample(Scene):
    def construct(self):
        rr = Tex("WYAY").scale(5)

        # \parbox is a TeX command for setting paragraphs of certain width
        rr_full = Tex(
            # kindly ignore the contents of this string
            r"""\parbox{20em}{We're no strangers to love.
            You know the rules and so do I.
            A full commitment's what I'm thinking of.
            You wouldn't get this from any other guy.}"""
        )

        self.play(Write(rr))

        self.play(TransformMatchingShapes(rr, rr_full))

        # careful! behaves the same as ReplacementTransform, so we need to use rr_full
        self.play(FadeOut(rr_full))



class AttentionExample(Scene):
    def construct(self):
        c1 = Square()

        labels = [
            Tex("Flash"),
            Tex("Indicate"),
            Tex("Wiggle"),
            Tex("FocusOn"),
            Tex("Circumscribe"),
        ]

        # move labels below the square
        for label in labels:
            label.next_to(c1, DOWN).scale(1.5)

        def switch_labels(i: int):
            """Animate switching one label for another. Notice the shift parameter!"""
            return AnimationGroup(
                FadeOut(labels[i], shift=UP * 0.5),
                FadeIn(labels[i + 1], shift=UP * 0.5),
            )

        self.play(Write(c1))

        self.play(FadeIn(labels[0], shift=UP * 0.5), c1.animate.shift(UP))

        self.play(Flash(c1, flash_radius=1.6, num_lines=20))

        self.play(AnimationGroup(switch_labels(0), Indicate(c1), lag_ratio=0.7))

        self.play(AnimationGroup(switch_labels(1), Wiggle(c1), lag_ratio=0.7))

        self.play(AnimationGroup(switch_labels(2), FocusOn(c1), lag_ratio=0.7))

        self.play(AnimationGroup(switch_labels(3), Circumscribe(c1), lag_ratio=0.7))

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
    
class IndicateExample(Scene):
    def construct(self):
        square = Square()
        self.play(Create(square))
        self.play(Indicate(square))
        self.wait(2)

class ApplyWaveExample(Scene):
    def construct(self):
        text = Text("Wave Effect")
        self.play(Create(text))
        self.play(ApplyWave(text))
        self.wait(2)

class ShrinkToCenterExample(Scene):
    def construct(self):
        square = Square()
        self.play(Create(square))
        self.play(ShrinkToCenter(square))
        self.wait(2)

class GrowFromCenterExample(Scene):
    def construct(self):
        square = Square()
        self.play(GrowFromCenter(square))
        self.wait(2)

class WiggleExample(Scene):
    def construct(self):
        square = Square()
        self.play(Create(square))
        self.play(Wiggle(square))
        self.wait(2)

class ApplyFunctionExample(Scene):
    def construct(self):
        square = Square()

        def custom_transformation(mobject):
            mobject.rotate(PI/2)
            mobject.shift(UP)
            return mobject

        self.play(Create(square))
        self.play(ApplyFunction(custom_transformation, square))
        self.wait(2)