from manim import *

class Test1(Scene):
    def construct(self):
        self.camera.background_color = "#FFDE59"
        
        text = Tex("$3x \cdot 5x = 135$",color=BLACK).scale(1.4)
        text2 = MathTex("15x^2=135",color=BLACK).scale(1.4)
        a = [-2, 0, 0]
        b = [2, 0, 0]
        c = [0, 2*np.sqrt(3), 0]
        p = [0.37, 1.4, 0]
        dota = Dot(a, radius=0.06,color=BLACK)
        dotb = Dot(b, radius=0.06,color=BLACK)
        dotc = Dot(c, radius=0.06,color=BLACK)
        dotp = Dot(p, radius=0.06,color=BLACK)
        lineap = Line(dota.get_center(), dotp.get_center()).set_color(BLACK)
        linebp = Line(dotb.get_center(), dotp.get_center()).set_color(BLACK)
        linecp = Line(dotc.get_center(), dotp.get_center()).set_color(BLACK)
        equilateral = Polygon(a,b,c)
        triangle = Polygon(a,b,p)
        self.play(Write(equilateral))
        self.wait()
        self.play(Write(VGroup(lineap,linebp,linecp,triangle)))
        self.wait()
        self.play(triangle.animate.rotate(0.4))
        self.wait()

# To render the scene, you would use the following command in your terminal:
# manim -pql your_script.py CameraAnimationExample
