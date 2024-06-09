from manim import *

class Pendulum(Scene):
    def construct(self):

        time = ValueTracker(0)
        l = 3
        g = 10
        w = np.sqrt(g/l)
        T = 2*PI / w
        theta_max = 20/180*PI
        p_x = -2
        p_y = 3
        shift_req = p_x*RIGHT+p_y*UP

        vertical_line = DashedLine(start = shift_req, end = shift_req+3*DOWN)
        
        theta = DecimalNumber().move_to(RIGHT*10)
        theta.add_updater(lambda m : m.set_value((theta_max)*np.sin(w*time.get_value())))


        def get_ball(x,y):
            dot = Dot(fill_color = BLUE, fill_opacity = 1).move_to(x*RIGHT+y*UP).scale(3)
            return dot

        ball = always_redraw(lambda : 
        get_ball(shift_req+l*np.sin(theta.get_value()), 
        shift_req - l*np.cos(theta.get_value()))
        )


        def get_string():
            line = Line(color = GREY, start = shift_req, end = ball.get_center())
            return line
        
        string = always_redraw(lambda : get_string())

        def get_angle(theta):
            if theta != 0:
                if theta > 0:
                    angle = Angle(line1 = string, line2 = vertical_line, other_angle = True, radius = 0.5, color = YELLOW)
                else:
                    angle = VectorizedPoint()
            else:
                angle = VectorizedPoint()
            return angle

        angle = always_redraw(lambda : get_angle(theta.get_value()))

        guest_name = Tex("Manoj Dhakal").next_to(vertical_line.get_start(), RIGHT, buff=0.5)

        pendulum = Group(string, ball, vertical_line, guest_name)

        self.add(vertical_line, theta, ball, string, angle)
        self.wait()
        self.play(FadeIn(guest_name))
        self.play(time.animate.set_value(2*T), rate_func = linear, run_time = 2*T)
        self.play(pendulum.animate.set_height(0.6).move_to(ORIGIN), run_time = 2)
        self.remove(theta, angle, ball, string)

        self.wait()