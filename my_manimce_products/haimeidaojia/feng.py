from manim import *
import manimpango

class feng(MovingCameraScene):
    def construct(self):
        
        # 定义一个函数 func，用于计算每个点的位置
        # func = lambda pos: np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT
        func = lambda pos: np.sin(pos[0]) * UR + np.cos(pos[1]) * LEFT + pos / 5
        
        # 创建一个 StreamLines 对象，用于生成和绘制流线动画
        # 参数 func 表示采用 func 函数作为向量场
        # stroke_width 表示流线的宽度为 2
        # max_anchors_per_line 表示每条流线上的锚点数量上限为 30
        # stream_lines = StreamLines(func, stroke_width=2, max_anchors_per_line=30)
        stream_lines = StreamLines(func,padding=1)
        
        # 将 stream_lines 添加到场景中，使其能够在场景中显示
        self.add(stream_lines)
        
        # 启动流线动画的播放
        # warm_up=False 表示不需要预热动画
        # flow_speed=1.5 表示流线动画的速度为 1.5
        stream_lines.start_animation(warm_up=True, flow_speed=1.5)
        
        print(manimpango.list_fonts())
        # text = Text(
        #     "得意黑",
        #     font='Smiley Sans Oblique',
        # )
        # self.add(text)

        MyTexTemplate = TexTemplate(
            tex_compiler="xelatex",
            output_format='.xdv',
        )
        MyTexTemplate.add_to_preamble(r"\usepackage{fontspec}\setmainfont{Smiley Sans Oblique}")

        l1 = Tex(
            "得意黑",
            tex_template=MyTexTemplate,
            # color = BLUE,
            stroke_width = 1.5
        )
        self.play( FadeIn(l1) )
        
        self.wait(7.777777)