from manim import *

class BecomeUpdaterExample(Scene):
    def format_point(self, point) -> str:
        """Format the given point to look presentable."""
        return f"[{point[0]:.2f}, {point[1]:.2f}]"

    def construct(self):
        circle = Circle(color=WHITE)

        def circle_label_updater(obj):
            """An updater that displays the circle's position above it."""
            obj.become(Tex(f"p = {self.format_point(circle.get_center())}"))
            obj.next_to(circle, UP, buff=0.35)

        self.play(Write(circle))

        circle_label = Tex()

        # a bit of a hack - we're calling the updater to create the initial label
        circle_label_updater(circle_label)

        self.play(FadeIn(circle_label, shift=UP * 0.3))

        # start updating the label
        circle_label.add_updater(circle_label_updater)

        self.play(circle.animate.shift(RIGHT))
        self.play(circle.animate.shift(LEFT * 3 + UP))
        self.play(circle.animate.shift(DOWN * 2 + RIGHT * 2))
        self.play(circle.animate.shift(UP))

class SimpleUpdater(Scene):
    def construct(self):
        square = Square().to_edge(LEFT)
        circle = Circle().set_color(RED).to_edge(RIGHT)

        def update_circle(mob):
            mob.next_to(square, RIGHT)

        # Add the updater to the circle
        circle.add_updater(lambda x: update_circle(x))

        self.add(square, circle)
        self.play(square.animate.shift(RIGHT * 4))
        self.wait(2)
        circle.clear_updaters()  # Stop updating the circle

class ColorPulseUpdater(Scene):
    def construct(self):
        square = Square().set_color(WHITE)

        # Variable to keep track of time
        self.elapsed_time = 0

        # Define the updater function
        def update_color(mob, dt):
            self.elapsed_time += 1 * dt
            # Cycle through colors based on elapsed time
            colors = [BLUE, GREEN, YELLOW, RED]
            color_index = int(self.elapsed_time) % len(colors)
            mob.set_color(colors[color_index])

        # Add the updater to the square
        square.add_updater(update_color)
        
        self.add(square)
        self.wait(3)  # Colors will cycle through BLUE, GREEN, YELLOW, REDnction(custom_transformation, square))
        self.wait(2)

class BreathingEffectUpdater(Scene):
    def construct(self):
        circle = Circle(radius=2).set_color(BLUE)
        
        self.x = 1
        self.y = 1
        self.prev_y = -1

        def update_circle(mob, dt):

            self.x += dt
            self.y = 1.5 + np.sin(self.x * 3)

            if self.prev_y == -1:
                mob.scale(self.y)
            else:
                mob.scale(1/self.prev_y) # reverse to base scale
                mob.scale(self.y) # scale to a new scale from base scale

            self.prev_y = self.y

        circle.add_updater(update_circle)

        self.add(circle)
        self.wait(5)

class FallingObjectUpdater(Scene):
    def construct(self):
        ball = Dot().set_color(RED).to_edge(UP)
        floor = Line(LEFT, RIGHT).shift(DOWN * 3)

        gravity = 9.8  # Acceleration due to gravity
        self.velocity = 0  # Initial velocity

        def update_ball(mob, dt):
            self.velocity  # To modify the velocity variable
            self.velocity += gravity * dt  # Update velocity due to gravity
            mob.shift(DOWN * self.velocity * dt)  # Move the ball based on current velocity
            
            # Stop the ball when it hits the floor
            if mob.get_center()[1] <= floor.get_center()[1]:
                mob.clear_updaters()

        ball.add_updater(update_ball)

        self.add(ball, floor)
        self.wait(5)

class SimpleUpdaterExample(Scene):
    def construct(self):
        square = Square()

        # Define an updater function that continuously moves the square right
        def move_square(mobject, dt):
            mobject.shift(RIGHT * dt * 2)  # Shift square to the right every frame

        square.add_updater(move_square)
        self.add(square)
        self.wait(2)  # Wait 2 seconds, while the square moves to the right

        square.remove_updater(move_square)

class AddAndRemoveUpdater(Scene):
    def construct(self):
        square = Square()

        # Define an updater to rotate the square continuously
        def rotate_square(mobject, dt):
            mobject.rotate(PI * dt)  # Rotate square based on time

        square.add_updater(rotate_square)
        self.add(square)
        self.wait(2)  # Square rotates for 2 seconds

        square.remove_updater(rotate_square)
        self.wait(2)  # Now, the square stops rotating

class MultipleUpdaters(Scene):
    def construct(self):
        square = Square()

        # Move the square upwards
        def move_up(mobject, dt):
            mobject.shift(UP * dt)

        # Rotate the square
        def rotate(mobject, dt):
            mobject.rotate(PI * dt)

        square.add_updater(move_up)
        square.add_updater(rotate)
        self.add(square)
        self.wait(3)  # Square moves and rotates at the same time

class PlayWithUpdaters(Scene):
    def construct(self):
        square = Square().shift(LEFT * 3)

        # Rotate the square continuously
        def rotate_square(mobject, dt):
            mobject.rotate(PI * dt)

        square.add_updater(rotate_square)

        # Animate the square moving to the right while it rotates
        self.add(square)
        self.play(square.animate.shift(RIGHT * 6), run_time=3)
        self.wait(2)

class CircularMotionUpdater(Scene):
    def construct(self):
        dot = Dot(color=YELLOW)
        circle = Circle(radius=3)
        dot.move_to(circle.get_start())

        def update_dot(mob, dt):
            mob.rotate_about_origin(PI * dt)  # Rotate dot around the origin

        dot.add_updater(update_dot)

        self.add(dot, circle)
        self.wait(10)  # The dot will keep moving in circular motion

class CircularMotionUpdater2(Scene):
    def construct(self):
        # Create a circle and move it to the left edge
        circle = Circle(radius=2)
        circle.to_edge(LEFT)

        # Create a center dot at the center of the screen
        center_dot = Dot(color=GREEN)

        # Create a yellow dot at the edge of the circle
        dot = Dot(color=YELLOW)
        dot.move_to(circle.get_start())  # Position the dot at the start of the circle

        # Circle's radius to use for rotation constraint
        radius = circle.radius

        # Variable to track the rotation angle
        self.angle = 0

        # Updater function to move the circle towards the center
        def move_to_center(mob, dt):
            direction = center_dot.get_center() - mob.get_center()  # Move towards the center
            mob.shift(direction * dt)  # Move the circle by a small fraction each frame

        # Updater function to rotate the dot around the circle's circumference
        def update_dot(mob, dt):
            # Update the rotation angle (increase speed by multiplying with a factor)
            self.angle += TAU * dt * 0.3  # Adjust the 0.5 factor to control speed

            # Get the center of the moving circle
            center_of_circle = circle.get_center()

            # Rotate the dot around the circle with its radius constraint
            mob.move_to(
                center_of_circle + radius * np.array([
                    np.cos(self.angle),
                    np.sin(self.angle),
                    0
                ])
            )

        # Add the updaters to the circle and dot
        circle.add_updater(move_to_center)
        dot.add_updater(update_dot)

        # Add the circle, center dot, and the rotating dot to the scene
        self.add(center_dot, circle, dot)
        self.wait(5)

        # Stop the updaters to finish the animation
        circle.clear_updaters()
        dot.clear_updaters()

