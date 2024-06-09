from manim import *

class Updater(Scene):
    def construct(self):

        # Create a fixed point and a rotating dot
        fixed_point = Dot()
        rotating_dot = Dot().shift(RIGHT * 2)

        # Define the update function for the rotating dot
        def update_rotating_dot(dot, dt):
            dot.rotate_about_origin(PI * dt)
            return dot

        # Add the updater to the rotating dot
        rotating_dot.add_updater(update_rotating_dot)

        # Add the fixed point and rotating dot to the scene
        self.add(fixed_point, rotating_dot)

        # Keep the animation running for a few seconds
        self.wait(3)

        # Remove the updater
        rotating_dot.remove_updater(update_rotating_dot)

class AlwaysRedraw(Scene):
    def construct(self):

        def update_dot(dot, target):
            dot.move_to(target.get_center())
            return dot

        # create box
        box = Rectangle(stroke_color = GREEN_C, 
                        stroke_opacity=0.7, 
                        fill_color = RED_B, 
                        fill_opacity = 0.5, 
                        height=1, 
                        width=1)
        
        # create always redraw dot in every frame
        # dot = always_redraw(lambda : update_dot(Dot(), box))
        dot = Dot(point=ORIGIN)
        
        self.play(Create(box), run_time=3)
        self.wait()

        self.play(Create(dot))
        self.wait()

        self.play(ApplyMethod(dot.shift, RIGHT *2), ApplyMethod(box.shift, RIGHT *2))
        self.wait()

class ValueTrackers(Scene):
    def construct(self):
        
        r = ValueTracker(0.5) #Tracks the value of the radius
        
        circle = always_redraw(lambda : 
        Circle(radius = r.get_value(), stroke_color = YELLOW, 
        stroke_width = 5))

        self.play(LaggedStart(
            Create(circle),
            run_time = 4, lag_ratio = 0.75
        ))
        self.play(r.animate.set_value(2), run_time = 5)