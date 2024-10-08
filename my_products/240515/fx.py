from manim import *

class PlotOddFunction(MovingCameraScene):
    def construct(self):
                
        # 画坐标轴
        axes = Axes(
            x_range=[-10, 10, 1],
            y_range=[-4, 4, 1],
            x_length=20,
            y_length=10,
            axis_config={"color": BLUE},
        )

        # 添加坐标轴标签，并设置字体大小和颜色
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y=f(x)")
        axes_labels.set_color(BLUE)
        axes_labels.set_font_size(24)

        # 将坐标轴添加到场景中

        # 添加文本，并设置字体大小和换行
        # text = Text(
        #     "f(x)是R上的奇函数，\n"
        #     "满足f(1+x) = f(1-x)，\n"
        #     "当x属于[-1,0), f(x) = log₂(-6x+2)，\n"
        #     "求解f(25/3)",
        # ).scale(0.4444)
        # text.to_edge(UP).shift(LEFT*2.2222+LEFT*0.7777)
        # self.play(Write(text))
        
        text1 = Text("f(x)是R上的奇函数，").scale(0.4444)
        text2 = Text("满足f(1+x) = f(1-x)，").scale(0.4444)
        text3 = Text("当x属于[-1,0), f(x) = log₂(-6x+2)，").scale(0.4444)
        text4 = Text("求解f(25/3)").scale(0.4444)

        # 将四个 Text 对象组成一个 VGroup 并左对齐
        text_group = VGroup(text1, text2, text3, text4).arrange(DOWN, aligned_edge=LEFT)
        
        text_group.to_edge(UP).shift(LEFT*2.2222+LEFT*0.7777)
        self.play(Write(text_group))
        
        self.play( Create(axes), self.camera.frame.animate.set(width = 22.2222), run_time = 1.1111 )
        
        self.play( Write(axes_labels) )

        # 定义函数f(x)在x属于[-1,0)时的部分
        def func1(x):
            return np.log2(-6 * x + 2)

        graph1 = axes.plot(func1, x_range=[-1, 0], color=YELLOW, use_smoothing=False)
        graph1_label = axes.get_graph_label(graph1, label="x \in [-1,0), \, f(x) = \log_2(-6x+2)").move_to(graph1, LEFT).shift(UP*2.2222+LEFT*0.7777)

        # 绘制函数图像
        self.play(Create(graph1), Write(graph1_label))

        # 对原点进行指示
        dot = Dot(axes.c2p(0, 0), color=RED)
        
        self.play( ApplyWave(graph1) )
        self.play(GrowFromCenter(dot))
        self.play(Indicate(dot))

        # 绘制关于原点对称的图像
        def func2(x):
            return -np.log2(6 * x + 2)

        graph2 = axes.plot(func2, x_range=[0, 1], color=YELLOW, use_smoothing=False)
        graph2_label = axes.get_graph_label(graph2,label="x \in (0, 1], \, f(x) = -\log_2(6x + 2)").shift(DOWN*2.2222+RIGHT*0.7777+UP*0.7777)

        # 绘制对称图像
        self.play(Create(graph2), Write(graph2_label))
        self.play( Indicate(graph2) )
        
        dashed_line = DashedLine(
            start=axes.coords_to_point(1, -4),
            end=axes.coords_to_point(1, 4),
            color=RED,
        )

        # 添加虚线直线到场景中
        self.play( Write(dashed_line) )
        self.play( Indicate(dashed_line) )
        
        
        self.play( ApplyWave(VGroup(graph1, graph2)) ) 
        
        def func3(x):
            return -np.log2(-6 * x + 14)
        def func4(x):
            return np.log2(6 * x - 10)
        graph3 = axes.plot(func3, x_range=[1, 2], color=YELLOW, use_smoothing=False)
        graph4 = axes.plot(func4, x_range=[2, 3], color=YELLOW, use_smoothing=False)
        
        self.play( Create(graph3) )
        self.play( Create(graph4) )
        self.play( Indicate(dashed_line) )
        
        self.play( ApplyWave(graph1),ApplyWave(graph4) )
        self.play( ApplyWave(graph2),ApplyWave(graph3) )
        self.play( Indicate(dashed_line) )

        self.play( FocusOn(dot) )
        self.play( Indicate(dot) )
        self.play( ApplyWave(graph2) )
        self.play( ApplyWave(graph3) )
        self.play( ApplyWave(graph4) )
        
        def func5(x):
            return np.log2(6 * x + 14)
        def func6(x):
            return -func4(-x) #与func4关于原点对称
        def func7(x):
            return func3(-x-2) 
        def func8(x):
            return func4(-x-2) 
        
        graph5 = axes.plot(func5, x_range=[-2, -1], color=YELLOW, use_smoothing=False)
        graph6 = axes.plot(func6, x_range=[-3, -2], color=YELLOW, use_smoothing=False)
        graph7 = axes.plot(func7, x_range=[-4, -3], color=YELLOW, use_smoothing=False)
        graph8 = axes.plot(func8, x_range=[-5, -4], color=YELLOW, use_smoothing=False)
        
        self.play( Create(graph5) )
        # self.play( Create(graph6) )
        
        
        dashed_line2 = DashedLine(
            start=axes.coords_to_point(-1, -4),
            end=axes.coords_to_point(-1, 4),
            color=RED,
        )
        
        self.play( Create(dashed_line2) )
        self.play( ApplyWave(VGroup(graph5,graph1,graph2,graph3,graph4)) )
        
        self.play( Indicate(VGroup(graph1,graph2,graph3,graph4)) )
        self.play( Indicate(dashed_line2) )
        
        self.play( Create(VGroup(graph6,graph7,graph8)) )
        self.play( Indicate(VGroup(graph5,graph6,graph7,graph8)) )
        
        # 停留几秒
        self.wait(22.2222)

# 要运行这个脚本，请保存为 plot_odd_function.py 并在命令行中运行：
# manim -pql plot_odd_function.py PlotOddFunction
