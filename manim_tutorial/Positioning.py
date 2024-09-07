from manim import *

class Sort(Scene):
    def construct(self):
        c11 = Circle(color=WHITE).shift(UP * 1.5 + LEFT * 2)
        c12 = Circle(color=WHITE).shift(UP * 1.5 + RIGHT * 2)
        c21 = Circle(color=WHITE).shift(DOWN * 1.5 + LEFT * 2)
        c22 = Circle(color=WHITE).shift(DOWN * 1.5 + RIGHT * 2)

        self.play(Write(c11), Write(c12), Write(c21), Write(c22))

        self.play(Swap(c11, c21))

        self.play(Swap(c12, c22, path_arc=160 * DEGREES))

class Positioning1(Scene):
    def construct(self):

        square = Square()
        circle = Circle()

        circle.next_to(square, RIGHT * 2)
        
        self.play(Create(square), Create(circle))
        self.wait()

class Positioning2(Scene):
    def construct(self):

        def vector_label_updater(vector_label, vector):
            vector_label.next_to(vector, UP)
            return vector_label

        def vector_updater_1(vector, numberline, numberline_tracker):
            # use n2p to get the position of number in the numberline
            vector.next_to(numberline.n2p(numberline_tracker.get_value()), ORIGIN)
            return vector
        
        def vector_updater_2(vector, numberline, numberline_tracker):
            # use n2p to get the position of number in the numberline
            vector.move_to(numberline.n2p(numberline_tracker.get_value()))
            return vector

        numberline_tracker = ValueTracker(0)
        numberline = NumberLine(
            x_range=[-7, 7, 1]
        ).add_numbers()

        vector = Vector(DOWN)
        vector_label = MathTex(r"x").add_updater(lambda vl : vector_label_updater(vl, vector))
        vector.add_updater(lambda vector: vector_updater_1(vector, numberline, numberline_tracker))

        self.play(Create(numberline), run_time=5)
        self.wait()
        
        self.play(Create(vector), Create(vector_label), run_time=2)
        self.wait()

        self.play(numberline_tracker.animate.set_value(3))
        self.wait()

        self.play(numberline_tracker.animate.set_value(-2))
        self.wait()

        self.play(numberline_tracker.animate.increment_value(2))
        self.wait()

        vector.clear_updaters()
        vector_label.clear_updaters()

