from manim import *

class MathText(Scene):
    def construct(self):

        def update_move(source, target):
            source.move_to(target.get_center())
            return source
        
        rectangle = RoundedRectangle(stroke_width = 8, 
                                     stroke_color = WHITE, 
                                     fill_color = BLUE_B, 
                                     width = 4.5, 
                                     height = 2).shift(UP*3+LEFT*4)

        mathtext = MathTex(r"\displaystyle \frac{\partial f}{\partial x}")
        mathtext.set_color_by_gradient(GREEN, PINK)
        mathtext.set_height(1.5)

        mathtext.add_updater(lambda x: update_move(x, rectangle))

        self.play(FadeIn(rectangle))
        self.wait()

        self.play(Write(mathtext), run_time=2)
        self.wait()

        self.play(rectangle.animate.shift(RIGHT*1.5 + DOWN*5), run_time=5)
        self.wait()

        mathtext.clear_updaters()

        self.play(rectangle.animate.shift(LEFT*2 + UP*1), run_time=6)
        self.wait()