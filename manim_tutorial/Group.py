from manim import *
from random import *


class AnimationGroupExample(Scene):
    def construct(self):
        c1 = Square(color=RED)
        c2 = Square(color=GREEN)
        c3 = Square(color=BLUE)

        VGroup(c1, c2, c3).arrange(buff=1)

        # each animation starts in the quarter of the previous one
        self.play(AnimationGroup(Write(c1), Write(c2), Write(c3), lag_ratio=0.25))

        # each animation starts after the first tenth of the previous one
        self.play(AnimationGroup(FadeOut(c1), FadeOut(c2), FadeOut(c3), lag_ratio=0.1))

        # one animation can also be a group, which has different lag_ratio
        self.play(
            AnimationGroup(
                AnimationGroup(Write(c1), Write(c2), lag_ratio=0.1),
                Write(c3),
                lag_ratio=0.5,
            )
        )

        # lag_ratio can also be negative (in which case the animations run in reverse)
        # however, just because it can doesn't mean it should!
        self.play(AnimationGroup(FadeOut(c1), FadeOut(c2), FadeOut(c3), lag_ratio=-0.1))

class VGroupLagRatioExample(Scene):
    def construct(self):
        squares = VGroup(Square(), Square(), Square()).arrange(buff=0.5).scale(1.5)

        # Write has non-zero lag_ratio by default so squares are written with overlap
        self.play(Write(squares))

        # FadeOut has zero lag_ratio by default, so all squares fade concurrently
        self.play(FadeOut(squares))

        squares.set_color(BLUE)

        self.play(Write(squares, lag_ratio=0))

        self.play(FadeOut(squares, lag_ratio=0.5))


class LineExample(Scene):
    def construct(self):
        p1 = Dot()
        p2 = Dot()

        points = VGroup(p1, p2).arrange(buff=2.5)

        line = Line(start=p1.get_center(), end=p2.get_center())

        self.play(Write(p1), Write(p2))

        self.play(Write(line))

class CircleFromPointsExample(Scene):
    def construct(self):
        p1 = Dot().shift(LEFT + UP)
        p2 = Dot().shift(DOWN * 1.5)
        p3 = Dot().shift(RIGHT + UP)

        dots = VGroup(p1, p2, p3)

        # create a circle from three points
        circle = Circle.from_three_points(p1.get_center(), p2.get_center(), p3.get_center(), color=WHITE)

        self.play(Write(dots), run_time=1.5)
        self.play(Write(circle))

class ColorGradientExample(Scene):
    def construct(self):
        rows = 6
        square_count = rows * 9

        # the colors can be either the built-in constants or in hex notation
        # (the builtin ones are just strings in the hex notation too!)
        colors = [RED, "#ffd166", "#06d6a0", BLUE]
        squares = [
            Square(fill_color=WHITE, fill_opacity=1).scale(0.3)
            for _ in range(square_count)
        ]

        group = VGroup(*squares).arrange_in_grid(rows=rows)

        self.play(Write(group, lag_ratio=0.04))

        all_colors = color_gradient(colors, square_count)

        self.play(
            AnimationGroup(
                *[s.animate.set_color(all_colors[i]) for i, s in enumerate(squares)],
                lag_ratio=0.02,
            )
        )

        self.play(FadeOut(group))

class Path(Polygram):
    def __init__(self, points, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_points_as_corners(points)

    def get_important_points(self):
        """Returns the important points of the curve."""
        # shot explanation: Manim uses quadratic Bézier curves to create paths
        # > each curve is determined by 4 points - 2 anchor and 2 control
        # > VMobject's builtin self.points returns *all* points
        # > we, however, only care about the anchors
        # > see https://en.wikipedia.org/wiki/Bézier_curve for more details
        return list(self.get_start_anchors()) + [self.get_end_anchors()[-1]]


class PathExample(Scene):
    def construct(self):
        path = Path([LEFT + UP, LEFT + DOWN, RIGHT + UP, RIGHT + DOWN], color=WHITE)

        self.play(Write(path))

        path_points = VGroup(*[Dot().move_to(point) for point in path.get_important_points()])

        self.play(Write(path_points))

        path2 = path.copy()
        path3 = path.copy()

        self.play(
            path2.animate.next_to(path, LEFT, buff=1),
            path3.animate.next_to(path, RIGHT, buff=1),
        )

        # flip(LEFT) flips top-down, because LEFT is the axis **by which** to flip
        self.play(
            path2.animate.flip(),
            path3.animate.flip(LEFT),
        )

class WriteVsCreate(Scene):
    def construct(self):
        s1 = Square(stroke_width=5)
        t1 = Tex("Write")

        s2 = Square(stroke_width=5)
        t2 = Tex("Create")

        VGroup(
            VGroup(s1, t1).arrange(DOWN),
            VGroup(s2, t2).arrange(DOWN),
        ).arrange(buff=1)

        # write also animates the outline
        self.play(FadeIn(t1))
        self.play(Write(s1, run_time=2))
        self.play(s1.animate.set_color(DARK_GRAY))

        # create does not and is therefore better suited
        # the rate_func parameter is magic for now and is covered in the next part
        self.play(FadeIn(t2))
        self.play(Create(s2, run_time=2, rate_func=linear))
        self.play(s2.animate.set_color(DARK_GRAY))

        self.wait()

class Triangle(Scene):
    def construct(self):
        seed(0xDEADBEEF)

        # scale everything up a bit
        c = 2

        p1 = Dot().scale(c).shift(UP * c)
        p2 = Dot().scale(c).shift(DOWN * c + LEFT * c)
        p3 = Dot().scale(c).shift(DOWN * c + RIGHT * c)

        points = VGroup(p1, p2, p3)

        self.play(Write(points, lag_ratio=0.5), run_time=1.5)

        l1 = Line()
        l2 = Line()
        l3 = Line()

        lines = VGroup(l1, l2, l3)

        def create_line_updater(a, b):
            """Returns a function that acts as an updater for the given segment."""
            return lambda x: x.become(Line(start=a.get_center(), end=b.get_center()))

        l1.add_updater(create_line_updater(p1, p2))
        l2.add_updater(create_line_updater(p2, p3))
        l3.add_updater(create_line_updater(p3, p1))

        self.play(Write(lines, lag_ratio=0.5), run_time=1.5)

        x = Tex("x")
        y = Tex("y")
        z = Tex("z")

        x.add_updater(lambda x: x.next_to(p1, UP))
        y.add_updater(lambda x: x.next_to(p2, DOWN + LEFT))
        z.add_updater(lambda x: x.next_to(p3, DOWN + RIGHT))

        labels = VGroup(x, y, z).scale(c * 0.8)

        self.play(FadeIn(labels, shift=UP * 0.2))

        circle = Circle()
        circle.add_updater(
            lambda c: c.become(
                Circle.from_three_points(
                    p1.get_center(), p2.get_center(), p3.get_center()
                )
            )
        )

        self.play(Write(circle))

        self.play(
            p2.animate.shift(LEFT + UP),
            p1.animate.shift(RIGHT),
        )

class Wave(Scene):
    def construct(self):
        seed(0xDEADBEEF)

        maze_string = """
#######################################################
#  #################            ##                    #
# ##################           ####                   #
# #################            ####                   #
#  ###############             #####               # ##
#      #########               #####               ####
#         ###                  ######            ######
#          ###            ##   #####    ###       #####
#          ####      ########   ####  #####        ## #
#          #####   ##########   ###  ########       # #
#         #####   ###########        ########         #
#         ####   ###########        ##########        #
#        ##      ###########        ##########        #
#      ####     ############      #############       #
#    ######     ############     #############        #
# #########  ## ###########     #########    #        #
# ############### #########     #######               #
# ###############   ######      ######                #
# ###############    #####       ####                 #
#   #############      #                ##            #
#     #  #######                       ########### ####
#          ###         #              #################
# ##                  ####            #################
#####                ######          ##################
######                ######         ##################
# ###      ###        #######  ###   ###############  #
#         ####         ############   ####  #######   #
#        #####          ############          ###     #
#         ###            ##########                   #
#######################################################
"""

        maze = []  # 2D array of squares like we see it
        maze_bool = []  # 2D array of true/false values
        all_squares = VGroup()

        # go line by line
        for row in maze_string.strip().splitlines():
            maze.append([])
            maze_bool.append([])

            for char in row:
                square = Square(
                    side_length=0.23,
                    stroke_width=1,
                    fill_color=WHITE if char == "#" else BLACK,
                    fill_opacity=1,
                )

                maze[-1].append(square)
                maze_bool[-1].append(char == " ")
                all_squares.add(square)

        w = len(maze[0])
        h = len(maze)

        # arrange the squares in the grid
        all_squares.arrange_in_grid(rows=h, buff=0)

        self.play(FadeIn(all_squares), run_time=2)

        x, y = 1, 1

        colors = ["#ef476f", "#ffd166", "#06d6a0", "#118ab2"]

        # create a dictionary of distances from start to other points
        distances = {(x, y): 0}
        stack = [(x, y, 0)]

        while len(stack) != 0:
            x, y, d = stack.pop(0)

            for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                nx, ny = dx + x, dy + y

                if nx < 0 or nx >= w or ny < 0 or ny >= h:
                   continue

                if maze_bool[ny][nx] and (nx, ny) not in distances:
                    stack.append((nx, ny, d + 1))
                    distances[(nx, ny)] = d + 1

        max_distance = max([d for d in distances.values()])

        all_colors = color_gradient(colors, max_distance + 1)

        # create animation groups for each distance from start
        groups = []
        for d in range(max_distance + 1):
            groups.append(
                AnimationGroup(
                    *[
                        maze[y][x].animate.set_fill(all_colors[d])
                        for x, y in distances
                        if distances[x, y] == d
                    ]
                )
            )

        self.play(AnimationGroup(*groups, lag_ratio=0.08))

class Path(VMobject):
    def __init__(self, points, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_points_as_corners(points)

    def get_important_points(self):
        return list(self.get_start_anchors()) + [self.get_end_anchors()[-1]]


class Hilbert(Scene):
    def construct(self):
        points = [LEFT + DOWN, LEFT + UP, RIGHT + UP, RIGHT + DOWN]

        hilbert = Path(points).scale(3)

        self.play(Create(hilbert), rate_func=linear)

        for i in range(1, 6):
            # length of a single segment in the curve
            new_segment_length = 1 / (2 ** (i + 1) - 1)

            # scale the curve such that it it is centered
            new_scale = (1 - new_segment_length) / 2

            # save the previous (large) curve to align smaller ones by it
            lu = hilbert.copy()
            lu, hilbert = hilbert, lu

            self.play(
                lu.animate.scale(new_scale)
                .set_color(DARK_GRAY)
                .align_to(hilbert, points[1])
            )

            ru = lu.copy()
            self.play(ru.animate.align_to(hilbert, points[2]))

            ld, rd = lu.copy(), ru.copy()
            self.play(
                ld.animate.align_to(hilbert, points[0]).rotate(-PI / 2),
                rd.animate.align_to(hilbert, points[3]).rotate(PI / 2),
            )

            new_hilbert = Path(
                list(ld.flip(LEFT).get_important_points())
                + list(lu.get_important_points())
                + list(ru.get_important_points())
                + list(rd.flip(LEFT).get_important_points())
            )

            # Create will be exponentially longer so it looks nice
            self.play(Create(new_hilbert, run_time=1.5 ** (i - 1)), rate_func=linear)

            self.remove(lu, ru, ld, rd)

            hilbert = new_hilbert