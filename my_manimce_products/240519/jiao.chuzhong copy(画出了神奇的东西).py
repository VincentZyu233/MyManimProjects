from manim import *
import math

class Ray(Line):
    def __init__(self, start, end, theta0=0.0, **kwargs):
        super().__init__(start, end, **kwargs)
        self.theta0 = theta0

class ExplainAngle(MovingCameraScene):
    def construct(self):
        
        ray1 = Ray(start=ORIGIN, end=2*RIGHT, color=YELLOW)
        ray2 = Ray(start=ORIGIN, end=math.sqrt(3)*RIGHT + 1*UP, theta0=60, color=YELLOW)
        
        self.play(Create(ray1))
        self.play(Create(ray2))
 
        def ray_rotate_to( theta1: float ):
            self.play( ray2.animate.rotate( angle=(theta1-ray2.theta0) / 180 * PI, about_point=ORIGIN ) )
            ray2.theta0 = theta1
            
        # class Arc(radius=1.0, start_angle=0, angle=1.5707963267948966, num_components=9, arc_center=array([0., 0., 0.]), **kwargs)
        
        jiao = always_redraw(
            lambda: Arc( start_angle=0, angle=ray2.theta0, arc_center=ORIGIN  )
        )
        
        self.play( Create(jiao) )
        
        # manim -pql jiao.chuzhong.py
        