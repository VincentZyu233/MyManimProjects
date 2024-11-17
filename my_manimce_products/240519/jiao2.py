from manim import *

theta0 = 0

class ExplainAngle(MovingCameraScene):
    def construct(self):
        
        self.play( self.camera.frame.animate.set(width = 22.2222) )
        
        # 这 是一个平面直角坐标系
        axes = Axes(
            x_range=[-2, 2, 1], y_range=[-2, 2, 1],
            x_length=7.7777, y_length=7.7777,
            axis_config={"color": BLUE}
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")

        self.play( Create(axes) )
        self.play( Write(axes_labels) )

        # 这 是一条射线 从原点出发，射向x轴正半轴
        ray = Line(start=axes.c2p(0, 0), end=axes.c2p(10, 0), color=YELLOW)
        self.play(Create(ray))
        
        # ray.rotate( angle=PI )
        
        # 把射线旋转到theta1这个角对应的终边位置
        def ray_rotate_to( theta1: float ):
            global theta0
            self.play( ray.animate.rotate( angle=(theta1-theta0) / 180 * PI, about_point=ORIGIN ) )
            theta0 = theta1
            
        ray_rotate_to( 60 )

        # # 画角度弧线
        # arc = Arc(
        #     radius=0.5,
        #     start_angle=start_angle,
        #     angle=end_angle,
        #     color=GREEN,
        # ).move_to(axes.c2p(0, 0))

        # # 标注角度
        # angle_label = MathTex(r"60^\circ")
        # angle_label.next_to(arc, UP)

        # # 添加坐标轴和标签
        # self.play(Create(axes), Write(labels))

        # # 添加单位圆
        # self.play(Create(unit_circle))

        self.wait(2)

if __name__ == "__main__":
    from manim import config
    config.media_width = "100%"
    ExplainAngle().render()
