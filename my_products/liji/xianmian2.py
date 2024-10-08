from manim import *

class ThreeDAnimation(ThreeDScene):
    def construct(self):
        # 创建直线 m
        line_m = Line(start=[0, 0, -10], end=[0, 0, 10], color=WHITE)
        label_m = Tex('m').next_to(line_m)
        # 创建平面 alpha
        plane_alpha = Rectangle(width=10, height=10, color=BLUE, fill_opacity=0.8888).move_to(ORIGIN)
        # 创建直线 n（初始位置为与 x 轴重合）
        line_n = Line(start=[-10, 0, 0], end=[10, 0, 0], color=WHITE)

        self.set_camera_orientation(phi=60 * DEGREES, theta=60 * DEGREES)

        self.move_camera(zoom=0.5555,run_time=0.5555)
        
        self.play( Create(line_m) )
        self.play( Write(label_m) )
        self.play( Create(plane_alpha) )
        self.play( Create(line_n) )

        # 创建旋转控制器
        self.play(Rotate(line_n, angle=PI/2, axis=OUT, about_point=[0, 0, 0]), run_time=0.8888)
        self.play(Rotate(line_n, angle=-PI, axis=OUT, about_point=[0, 0, 0]), run_time=0.8888)
        
        # manim -pql xianmian2.py

