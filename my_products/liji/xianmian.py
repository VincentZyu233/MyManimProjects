from manim import *
import math

# manim -ql xianmian.py --disable_caching

class Test_camera(ThreeDScene):
    def construct(self):
    
        phi_0, theta_0 = 120*DEGREES, 60*DEGREES # 起始角度
        self.set_camera_orientation(phi=phi_0, theta=theta_0)
        self.move_camera(theta=45*DEGREES,phi=45*DEGREES,run_time=2.2222,distance=4)
        
        mian_alpha = Rectangle().scale(1.1111).rotate(math.pi / 2)
        self.play( Create(mian_alpha) )
        
        plane = Surface(
            lambda u, v: np.array([u, v, 0]),
            u_range=(-4.4444, 4.4444),
            v_range=(-4.4444, 4.4444),
            stroke_width=0.8888,
            # resolution=8.8888
        )
        # 设置平面颜色和透明度
        plane.set_color(YELLOW)
        plane.set_fill(opacity=0.2222)
        self.play( Create(plane) )
        
        self.wait(8.8888)