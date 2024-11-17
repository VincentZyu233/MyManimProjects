from manim import *
import math


class Ray(Line):
    def __init__(self, start, end, theta0=0.0, **kwargs):
        super().__init__(start, end, **kwargs)
        self.theta0 = theta0

class ExplainAngle(MovingCameraScene):
    def construct(self):
        self.play( self.camera.frame.animate.set(width = 10).shift(RIGHT*1.5+UP*0.5) )
        
        ray1 = Ray(start=ORIGIN, end= 2 * ( 2*RIGHT ), color=YELLOW)
        ray2 = Ray(start=ORIGIN, end= 2 * ( math.sqrt(3)*RIGHT + 1*UP ), theta0=30, color=YELLOW)
        
        self.play(Create(ray1))
        self.play(Create(ray2))
        
        def ray_rotate_to( theta1: float ):
            self.play( ray2.animate.rotate( angle=(theta1-ray2.theta0) * DEGREES, about_point=ORIGIN, axis=OUT ), rate_func=rate_functions.ease_in_out_sine )
            ray2.theta0 = theta1
            
        # class Arc(radius=1.0, start_angle=0, angle=1.5707963267948966, num_components=9, arc_center=array([0., 0., 0.]), **kwargs)
        
        jiao = always_redraw(
            lambda: Arc( start_angle=0, angle=ray2.get_angle() / DEGREES, arc_center=ORIGIN  )
        )
        self.play( Create(jiao) )
        
        dingdian = Dot(ORIGIN, color=RED)
        self.play( Create(dingdian) )
        self.play( Indicate(dingdian) )
        
        self.play( Wiggle( ray1 ), Wiggle( ray2 ) )
        
        jiao_value_label = always_redraw(
            lambda: Tex(f"${ray2.get_angle() / DEGREES:.2f}^\\circ$" ).next_to(ray1, DOWN*2)
        )
        
        def get_background_pattern(obj, color="#CCCCCC", opacity=0.5):
            # 创建一个矩形作为背景底纹
            background = Rectangle(
                width=obj.get_width()*1.2,
                height=obj.get_height()*1.2,
                fill_color=color,
                fill_opacity=opacity,
                stroke_opacity=0,
            ).move_to(obj).set_z_index(-1)

            # 返回添加了背景底纹的物体和 VGroup 对象
            return background
        
        bg_jiao_value_label = get_background_pattern(jiao_value_label)

        self.play(Write(jiao_value_label), Create(bg_jiao_value_label) )
        
        ray_rotate_to(60)
        
        self.play( self.camera.frame.animate.set(width = 15) )
        ray_rotate_to(359.999999)
        ray_rotate_to(180)
        ray_rotate_to(90)

        
        # manim -pql jiao.chuzhong.py
        