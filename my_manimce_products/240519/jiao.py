from manim import *

class ExplainAngle(MovingCameraScene):
    def construct(self):
        
        self.play( self.camera.frame.animate.set(width = 22.2222) )
        
        # 画坐标轴
        axes = Axes(
            x_range=[-2, 2, 1], y_range=[-2, 2, 1],
            x_length=7.7777*2, y_length=7.7777*2,
            axis_config={"color": BLUE}
        )
        labels = axes.get_axis_labels(x_label="x", y_label="y")

        # 画单位圆
        unit_circle = axes.plot_parametric_curve(
            lambda t: np.array([np.cos(t), np.sin(t), 0]),
            t_range=[0, TAU],
            color=WHITE
        )
        
        # 画射线
        start_angle = 0
        end_angle = 60 * DEGREES
        line = Line(start=axes.c2p(0, 0), end=axes.c2p(1, 0), color=YELLOW)

        # 逆时针旋转射线60度
        rotated_line = line.copy().rotate(angle=end_angle, about_point=axes.c2p(0, 0))

        # 画角度弧线
        arc = Arc(
            radius=0.5,
            start_angle=start_angle,
            angle=end_angle,
            color=GREEN,
        ).move_to(axes.c2p(0, 0))

        # 标注角度
        angle_label = MathTex(r"60^\circ")
        angle_label.next_to(arc, UP)

        # 添加坐标轴和标签
        self.play(Create(axes), Write(labels))

        # 添加单位圆
        self.play(Create(unit_circle))

        # 添加初始射线
        self.play(Create(line))

        # 旋转射线并添加角度弧线和标签
        self.play(Transform(line, rotated_line), Create(arc), Write(angle_label))

        # 标注单位圆上的点
        point = Dot(axes.c2p(np.cos(end_angle), np.sin(end_angle)), color=RED)
        point_label = MathTex(r"(\frac{1}{2}, \frac{\sqrt{3}}{2})")
        point_label.next_to(point, UR)
        self.play(Create(point), Write(point_label))

        # # 添加解释文字
        # explanation = Tex(
        #     r"""
        #     这是一个单位圆，圆心在原点，半径为1。
        #     初始射线从原点开始，指向x轴正方向。
        #     射线逆时针旋转60度，形成一个角。
        #     """
        # )
        # explanation.to_edge(DOWN)
        # self.play(Write(explanation))

        self.wait(2)

if __name__ == "__main__":
    from manim import config
    config.media_width = "100%"
    ExplainAngle().render()
