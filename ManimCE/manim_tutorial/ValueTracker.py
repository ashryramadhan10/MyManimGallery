from manim import *

class SimpleTrackerExample(Scene):
    def construct(self):
        square = Square()

        # Create a tracker
        tracker = ValueTracker(0)

        # Define an updater function that moves the square based on the tracker's value
        def update_position(mobject):
            mobject.move_to(RIGHT * tracker.get_value())

        square.add_updater(update_position)
        self.add(square)

        # Animate the tracker value from 0 to 4
        self.play(tracker.animate.set_value(4), run_time=4)
        self.wait()

class TrackerWithGraph(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 9],
            y_range=[-1, 1],
            axis_config={"color": BLUE},
        )
        graph = axes.plot(lambda x: np.sin(x), color=WHITE)
        point = Dot(color=RED)

        # Create a tracker
        tracker = ValueTracker(0)

        # Define an updater function to move the point on the graph
        def update_point(mobject):
            x = tracker.get_value()
            y = np.sin(x)
            mobject.move_to(axes.c2p(x, y))

        point.add_updater(update_point)
        self.add(axes, graph, point)

        # Animate the tracker value from 0 to 9
        self.play(tracker.animate.set_value(9), run_time=9)
        self.wait()

class CustomAnimationWithTracker(Scene):
    def construct(self):
        square = Square()

        # Create a tracker
        tracker = ValueTracker(0)

        # Define a custom updater function
        def update_custom(mobject):
            mobject.shift(RIGHT * tracker.get_value())
            mobject.set_fill_color(interpolate_color(RED, BLUE, tracker.get_value() / 5))

        square.add_updater(update_custom)
        self.add(square)

        # Animate the tracker value from 0 to 5
        self.play(tracker.animate.set_value(5), run_time=5)
        self.wait()