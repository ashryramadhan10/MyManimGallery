from manimlib import *

class Tutorial1(Scene):
    def construct(self):
        
        # 1. create a circle
        circle = Circle()
        circle.set_fill(GREEN, opacity=0.5)
        circle.set_stroke(WHITE, width=0.5)
        circle.next_to(ORIGIN)

        self.play(ShowCreation(circle))

        # 2. create square next to circle
        square = Square()
        square.set_fill(BLUE, opacity=0.5)
        square.set_stroke(WHITE, width=3.0)
        square.next_to(circle, RIGHT * 3)

        self.play(ShowCreation(square))

        # 3. create triangle left to circle
        triangle = Triangle()
        triangle.set_fill(YELLOW, opacity=0.5)
        triangle.next_to(circle, LEFT * 3)
        self.play(ShowCreation(triangle))

        self.embed()

        # 4. second square will try to use z_index
        square2 = Square()
        square2.set_fill(ORANGE, opacity=1.0)
        square2.set_z_index(2)
        square2.move_to(circle.get_right())
        self.play(ShowCreation(square2))

        # 5. draw circle at square2 center
        circle2 = Circle(radius=0.5)
        circle2.set_fill(WHITE, opacity=1.0)
        circle2.set_z_index(3)
        circle2.next_to(square2, ORIGIN)
        self.play(ShowCreation(circle2))