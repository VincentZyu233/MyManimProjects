# 先说结论，我们都知道空间中的任意两条直线的夹角的取值范围是[0,pi], 那么如何来看待这件事情呢？
# 想象空间中有任意两条直线，位置关系可以是随机的，所以当然，他们可以是不相交的。
# 现在，我们把其中一条直线平移，使得他与另一个直线有交点，那么， 这两条直线就确定了一个平面，
# 在这个平面上，我们就能画出这两条直线的所成角。

from manim import *
import math

class test(ThreeDScene):
    def construct(self):
        
        # disp_theta =  always_redraw( lambda: 
        #     Tex(r"{:.2f}".format(self.camera.theta))
        # )
        
        # self.add_fixed_in_frame_mobjects(disp_theta)
        
        self.set_camera_orientation(phi=45*DEGREES, theta=45*DEGREES)
        self.move_camera(theta=45*DEGREES,phi=45*DEGREES,run_time=2.8888,distance=8.8888)
        self.begin_ambient_camera_rotation(rate=0.0202)
        
        ax = ThreeDAxes(
            z_length=8.8888,
            x_axis_config={"include_ticks": False},  # 隐藏 x 轴的刻度线
            y_axis_config={"include_ticks": False},  # 隐藏 y 轴的刻度线
            z_axis_config={"include_ticks": False},
        ).set_opacity(0.8888)
        ax.x_axis.set_stroke(width=2.2222)
        ax.y_axis.set_stroke(width=2.2222)
        ax.z_axis.set_stroke(width=2.2222)
        self.play(Create(ax))
          
        line1 = Line3D(start=np.array([-4.4444-8.8888, -2.2222, 0.8888]), end=np.array([4.4444+8.8888, -2.2222, 0.8888]), thickness=0.0202, color=BLUE_D)
        line2 = Line3D(start=np.array([-4.4444+1.1111-4.4444*2, -1.1111, 0-1.1111*2]), end=np.array([4.4444+1.1111+4.4444*2, -1.1111, 2.2222+1.1111*2]), thickness=0.0202, color=YELLOW_D)
        
        line11 = line1.copy().shift( [0,1.1111,0] )
        
        self.move_camera(zoom=0.8888,run_time=0.8888)
        
        
        # xianjiao = Angle(line11,line2)
        # xianjiao = always_redraw( lambda:Angle(line11,line2)  )
        # self.play( Create(xianjiao) )
        
        self.play( Create(line1) )
        self.play( Create(line2) )
        
        rate_functions.ease_in_back
        def change_ambient_rotation_rate( origin:float, target:float, func, run_time:float ):
            dt = run_time / 1000.0
            for i in range(1,1000):
                self.begin_ambient_camera_rotation( rate=origin+(target-origin)*func(i/1000.0) )
                self.wait(dt)
            
        
        self.begin_ambient_camera_rotation(rate=0.4444)
        # change_ambient_rotation_rate( 0.0202, 0.4444, rate_functions.ease_in_out_quart, 2.2222 )
        self.move_camera(phi=60*DEGREES,run_time=2.8888,distance=8.8888)
        self.wait(4.4444)
        
        self.move_camera(phi=30*DEGREES,run_time=2.8888,distance=8.8888)
        self.wait(8.8888)

        self.move_camera(zoom = 2.2222)
        self.play( line1.animate.shift( [0,1.1111,0] ), run_time = 1.1111 )
        
        # jiaodian = Dot(
        #     ax.c2p
        # )
        
        self.wait(0.8888)
        self.stop_ambient_camera_rotation()

        self.move_camera(theta=200*DEGREES,phi=80*DEGREES,run_time=2.8888,distance=8.8888)
        self.move_camera(zoom=2.2222, theta=90*DEGREES,phi=90*DEGREES,run_time=1.4444,distance=4.4444)

        

        
        self.wait(2.2222)
        
        # manim -ql xianjiao.py