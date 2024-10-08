from manim import *
import math
import os
import numpy as np
from scipy.optimize import newton


class FunctionGraph(MovingCameraScene):
    def construct(self):
        
        # self.play( self.camera.frame.animate.set(width = 22).shift( DOWN*0.22 ) )
        # 设置镜头宽度
        self.play( self.camera.frame.animate.set(width = 20) )
        
        #tex_template 设置中文兼容
        MyTexTemplate = TexTemplate(
            tex_compiler="xelatex",
            output_format='.xdv',
        )
        # MyTexTemplate.add_to_preamble(r"\usepackage{fontspec}\setmainfont{Smiley Sans Oblique}")

        # tex = Tex(
        #     "得意黑",
        #     tex_template=MyTexTemplate,
        #     color = BLUE,
        # )
        # self.add(tex)
        
        
        # 创建坐标轴
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-2, 10, 1],
            x_length=12,
            y_length=6,
            axis_config={"color": BLUE},
            tips=False
        )

  # 创建函数图像
        positive_graph = axes.plot(lambda x: np.exp(x), color=GREEN, x_range=(0, 3))
        negative_graph = axes.plot(lambda x: -2*x*x - 4*x + 1, color=RED, x_range=(-3.7777, 0))
        graph_label_positive = axes.get_graph_label(positive_graph, label="e^x", direction=UP)
        graph_label_negative = axes.get_graph_label(negative_graph, label="-2x^2 - 4x + 1", direction=DOWN).next_to(negative_graph, LEFT)

        # 添加文字说明
        function_label = MathTex("f(x) = \\begin{cases} e^x, & x > 0 \\\\ -2x^2 - 4x + 1, & x \leq 0 \\end{cases}")
        function_label.next_to(axes, direction=UP).shift(LEFT*2.2222)

        # 添加动画
        self.play(Create(axes), Write(function_label))
        self.play(Create(negative_graph), Write(graph_label_negative))
        self.play(Create(positive_graph), Write(graph_label_positive))
        
        self.wait(2.2222)
        
        
        text1 = Text("g(x) = f(x) - kx 有两个零点", color=WHITE).next_to(axes, LEFT).shift(RIGHT*4.4444 + UP*2.2222 ).scale(0.8888)
        text2 = Text("f(x) - kx = 0  有两个解", color=WHITE).next_to(axes, LEFT).shift(RIGHT*4.4444 + UP*2.2222).scale(0.8888)
        text3 = Text("y = f(x) 和 y = kx 有两个交点", color=WHITE).next_to(axes, LEFT).shift(RIGHT*4.4444 + UP*2.2222).scale(0.8888)
 
        self.play( Write(text1) )

    
        self.play(Transform(text1, text2))
        self.wait(2.2222)
        self.play(Transform(text1, text3))
        self.wait(2.2222)
        
        k_tracker = ValueTracker(2)
        
        k_label = always_redraw(
            lambda: Text( f"k = { round( k_tracker.get_value(), 2 )}" ).next_to( axes, DOWN )
        )
         
        line = always_redraw(
            lambda: axes.plot(
                lambda x: k_tracker.get_value() * x, color=WHITE, x_range=(-5, 5)
            )
        )
        
        self.wait(2.2222)
        self.play( Write(line) )
        
        self.play( ApplyWave(negative_graph) )
        self.play( ApplyWave(positive_graph) )
        self.play( Indicate(positive_graph) )
        self.play( Indicate(negative_graph) )
        
        self.play( Indicate(line) )
        
        self.wait(0.8888)
        self.play( Write(k_label) )
        
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
        
        k_bg = get_background_pattern(k_label)
        self.play( Write(k_bg) )
        self.wait(2.2222)
        
        
        # k的值不知道，也就是可以看做是一个 可以绕着原点旋转的直线
        # 现在让你求斜率的范围，也就是让你求 当这个直线旋转到哪些位置的时候，与这个函数图像有两个交点
        self.play( k_tracker.animate.set_value(10), run_time = 1.1111 )
        self.play( k_tracker.animate.set_value(0), run_time = 1.1111 )
        self.play( k_tracker.animate.set_value(-10), run_time = 2.2222 )
        
        self.wait(0.8888)
        
        ellipse_ykx = Ellipse(width=2.0, height=1.1111, color=ORANGE).move_to(text3)
        self.play( Write(ellipse_ykx) )
        self.wait(5.5555)
        self.play( FadeOut(ellipse_ykx) )
        self.wait(2.2222)
        
        # 先简单讨论一下k的范围
        # 第一种情况 k>=0

        taolun1 = Text("①k>=0", color=WHITE).next_to(axes, RIGHT).shift(UP*2.2222 ).scale(0.8888)
        self.play(
            Write(taolun1,  run_time = 1.1111),
            k_tracker.animate.set_value(0)
        )

        # 也就是这个范围
        self.play( k_tracker.animate.set_value(20), run_time = 0.8888, rate_func=rate_functions.ease_in_out_sine)
        self.play( k_tracker.animate.set_value(0), run_time = 0.8888, rate_func=rate_functions.ease_in_out_sine)
        self.play( k_tracker.animate.set_value(20), run_time = 0.8888, rate_func=rate_functions.ease_in_out_sine)
        
        
        self.play( k_tracker.animate.set_value(0), run_time = 0.8888 )
        
        # 先观察f(x)的负数部分 也就是y轴左半边的部分与直线y=kx的交点，我们不难发现， 当k＞=0的时候，直线和f(x)的负数部分是永远有交点的
        self.play( FocusOn(negative_graph) )
        self.play( ApplyWave(negative_graph) )
        self.play( Indicate(negative_graph) )
        self.play( self.camera.frame.animate.set(width = 30).shift(DOWN*2.2222) )
        
        
        func_k_to_x = lambda k:  (k + 4 + ((k * k + 8 * k + 24) ** 0.5)) / (-4)
        zuo_jiaodian = always_redraw(
            lambda: Dot().move_to( 
                axes.coords_to_point( 
                    func_k_to_x( k_tracker.get_value() ), 
                    func_k_to_x( k_tracker.get_value() )*k_tracker.get_value()
                ) 
            ).scale(2.2222)
        )
        
        self.play( FadeIn(zuo_jiaodian) )
        self.play( Flash(zuo_jiaodian) )
        
        self.play( k_tracker.animate.set_value(2.2222), run_time = 1.1111, rate_func=rate_functions.ease_in_out_sine)
        self.play( k_tracker.animate.set_value(0), run_time = 1.1111, rate_func=rate_functions.ease_in_out_sine)
        self.play( k_tracker.animate.set_value(2.2222), run_time = 1.1111, rate_func=rate_functions.ease_in_out_sine)
        self.play( k_tracker.animate.set_value(1.1111), run_time = 1.1111, rate_func=rate_functions.ease_in_out_sine)
        
        self.play( self.camera.frame.animate.set(width = 22.2222).shift(UP*2.2222) )
        taolun2 = Text("直线与f(x)曲线图像的x<0部分的交点情况：", color=WHITE).next_to(taolun1, DOWN).shift( RIGHT*0.2222 ).scale(0.4444)
        taolun3 = Text("直线与f(x) (x<0) 永远有且只有一个交点", color=WHITE).next_to(taolun1, DOWN).shift( RIGHT*0.2222 ).scale(0.4444)
        # self.play(Write(taolun2))
        self.play(Write(taolun3))
        self.play( Indicate(zuo_jiaodian) )
        self.play( Flash(zuo_jiaodian) )
        self.play( FadeOut(zuo_jiaodian) )
        self.wait(0.7777)
        
        print(math.e)
        
        # 再看f(x)曲线的Y轴右边部分，  我们这样子看： 当k大于0的时候，从小到大看一下k的不同情况 在图像上的表现
        
        self.play( FocusOn(positive_graph) )
        self.play( ApplyWave(positive_graph) )
        self.play( Indicate(positive_graph) )
        self.wait(2.2222)
        
        # 显然，当k很小的时候， 直线与右半部分没有交点
        self.play( k_tracker.animate.set_value(0), run_time = 1.1111, rate_func=rate_functions.ease_in_out_sine)
        self.wait(0.7777)
        self.play( k_tracker.animate.set_value(1.1111), run_time = 1.1111, rate_func=rate_functions.ease_in_out_sine)
        self.wait(2.2222)
        
        # 经过简单的计算可以得到， 当斜率为e的时候，直线与曲线的右半部分相切

        self.play( k_tracker.animate.set_value(math.e), run_time = 1.1111 )
        self.wait(7.7777)
        
        # 当斜率更大的时候，显然，直线和曲线的右边部分有两个交点
        self.play( k_tracker.animate.set_value(5.55555), run_time = 1.1111, rate_func=rate_functions.ease_in_out_sine)
        self.wait(7.7777)
        
        # 总结一下，当斜率的范围是[0,e)左闭右开, 直线和曲线没有交点
        # 当直线的斜率是e，直线和曲线的右半部分刚好相切，只有一个交点
        # 当直线的斜率大于e，即斜率的范围是(e, 正无穷)， 直线和曲线的右半部分有两个交点
        
        taolun4 = Tex(r"$k \in [0, e)$", tex_template=MyTexTemplate, color=WHITE).next_to(taolun3, DOWN).shift( LEFT*2.2222 ).scale(0.7777)
        taolun5 = Text("直线与f(x) (x>0) 没有交点", color=WHITE).next_to(taolun4, RIGHT).scale(0.4444).shift(LEFT*2.2222)
        self.play( k_tracker.animate.set_value(0), run_time = 1.1111, rate_func=rate_functions.ease_in_out_sine)
        self.play( k_tracker.animate.set_value(1.1111), run_time = 1.1111, rate_func=rate_functions.ease_in_out_sine )
        self.play( Write(taolun4) )
        self.play( Write(taolun5) )
        self.wait(2.2222)
        
        taolun6 = Tex(r"$k = e$", tex_template=MyTexTemplate, color=WHITE).next_to(taolun4, DOWN).shift( LEFT*0.2222+LEFT*0.07070707070707 ).scale(0.7777)
        taolun7 = Text("直线与f(x) (x>0) 有一个交点", color=WHITE).next_to(taolun6, RIGHT).scale(0.4444).shift(LEFT*2.2222)
        self.play( k_tracker.animate.set_value(math.e), run_time = 1.1111 )
        self.play( Write(taolun6) )
        self.play( Write(taolun7) )
        self.wait(2.2222)
        
        taolun8 = Tex(r"$k \in (e, \infty)$", tex_template=MyTexTemplate, color=WHITE).next_to(taolun6, DOWN).shift( RIGHT*0.2222+RIGHT*0.07070707070707 ).scale(0.7777)
        taolun9 = Text("直线与f(x) (x>0) 有两个交点", color=WHITE).next_to(taolun8, RIGHT).scale(0.4444).shift(LEFT*2.2222)
        self.play( k_tracker.animate.set_value(5), run_time = 1.1111, rate_func=rate_functions.ease_in_out_sine)
        self.play( Write(taolun8) )
        self.play( Write(taolun9) )
        self.wait(2.2222)
        
        vgroup_before_taolun = VGroup(
            taolun1,
            # taolun2,
            taolun3,
            taolun4,
            taolun5,
            taolun6,
            taolun7,
            taolun8,
            taolun9,
        )
        
        self.play(
            vgroup_before_taolun.animate.shift(UP*2.2222)
        )
        
        self.wait(2.2222)
        
        # 接下来再看一下k小于0的情况
        # 当k<0时：
        taolun10 = Text("②k<0", color=WHITE).next_to(taolun8, DOWN).shift( RIGHT*2.2222 ).scale(0.8888)
        self.play( k_tracker.animate.set_value(-2.2222), run_time = 1.1111, rate_func=rate_functions.ease_in_out_sine)
        self.play( Write(taolun10) )
        
        taolun11 = Text("直线与f(x) (x>0) 永远没有交点", color=WHITE).next_to(taolun10, DOWN).shift( RIGHT*0.2222 ).scale(0.4444)
        taolun12 = Text("直线与f(x) (x<0) 有且只有一个交点", color=WHITE).next_to(taolun11, DOWN).shift( RIGHT*0.2222 ).scale(0.4444)

        # 直线与函数的y轴右边部分没有交点
        self.play( ApplyWave(positive_graph) )
        self.play( Indicate(positive_graph) )
        self.play( Write(taolun11) )
        
        zuo_jiaodian = always_redraw(
            lambda: Dot().move_to( 
                axes.coords_to_point( 
                    func_k_to_x( k_tracker.get_value() ), 
                    func_k_to_x( k_tracker.get_value() )*k_tracker.get_value()
                ) 
            ).scale(2.2222)
        )
         # 直线与函数的y轴左边部分有且仅有一个交点
        self.play( ApplyWave(negative_graph) )
        self.play( Indicate(negative_graph) )
        self.play( FadeIn(zuo_jiaodian) )
        self.play( FocusOn(zuo_jiaodian) )
        self.play( Flash(zuo_jiaodian) )
        self.play( Write(taolun12) )
        
        # 综上所述 当k的范围是负无穷到e 开区间的时候， 直线与f(x)只有一个交点
        zongjie1 = Tex(r"$k \in (-\infty, e)$", tex_template=MyTexTemplate, color=WHITE).next_to(taolun12, DOWN).shift( LEFT*2.2222+LEFT*0.7777+DOWN*0.7777 ).scale(0.7777)
        zongjie2 = Text("直线与f(x)有一个交点", color=WHITE).next_to(zongjie1, RIGHT).shift( LEFT*2.2222+RIGHT*0.7777+LEFT*0.2222 ).scale(0.4444)
        
        # 当k刚好等于e时， 直线与f(x)有两个交点
        zongjie3 = Tex(r"$k = e$", tex_template=MyTexTemplate, color=WHITE).next_to(zongjie1, DOWN).shift( LEFT*0.2222+LEFT*0.2222 ).scale(0.7777)
        zongjie4 = Text("直线与f(x)有两个交点", color=WHITE).next_to(zongjie3, RIGHT).shift( LEFT*0.2222 ).scale(0.4444)
        
        # 当k的范围是e到正无穷时， 直线与f(x)有三个交点
        zongjie5 = Tex(r"$k \in (e, \infty)$", tex_template=MyTexTemplate, color=WHITE).next_to(zongjie3, DOWN).shift( RIGHT*0.2222 ).scale(0.7777)
        zongjie6 = Text("直线与f(x)有三个交点", color=WHITE).next_to(zongjie5, RIGHT).shift( LEFT*2.2222+RIGHT*0.2222 ).scale(0.4444)
        
        self.play( k_tracker.animate.set_value(-5.5555), run_time = 1.1111, rate_func=rate_functions.ease_in_out_sine)
        self.play( k_tracker.animate.set_value(-1.1111), run_time = 1.1111, rate_func=rate_functions.ease_in_out_sine)
        self.play( k_tracker.animate.set_value(-5.5555), run_time = 1.1111, rate_func=rate_functions.ease_in_out_sine)
        self.play( k_tracker.animate.set_value(0), run_time = 1.1111, rate_func=rate_functions.ease_in_out_sine)
        self.play( k_tracker.animate.set_value(1.1111), run_time = 1.1111, rate_func=rate_functions.ease_in_out_sine)
        self.play( k_tracker.animate.set_value(2.2222), run_time = 1.1111, rate_func=rate_functions.ease_in_out_sine)
        self.play( k_tracker.animate.set_value(1.1111), run_time = 1.1111, rate_func=rate_functions.ease_in_out_sine)
        self.play( Write(zongjie1) )
        self.play( Write(zongjie2) )
        self.wait(0.7777)
        
        self.play( k_tracker.animate.set_value( math.e ), run_time = 1.1111, rate_func=rate_functions.ease_in_out_sine)
        self.play( Write(zongjie3) )
        self.play( Write(zongjie4) )
        self.wait(2.2222)
        
        self.play( k_tracker.animate.set_value( 3.3333 ), run_time = 1.1111, rate_func=rate_functions.ease_in_out_sine)
        self.play( k_tracker.animate.set_value( 5.5555 ), run_time = 1.1111, rate_func=rate_functions.ease_in_out_sine)
        self.play( k_tracker.animate.set_value( 3.3333 ), run_time = 1.1111, rate_func=rate_functions.ease_in_out_sine)
        self.play( Write(zongjie5) )
        self.play( Write(zongjie6) )
        self.wait(0.7777)
        
        brace_zongjie = Brace( VGroup(zongjie1, zongjie3, zongjie5), direction=LEFT )
        self.play( 
            Write(brace_zongjie) ,
            Circumscribe( VGroup(zongjie1, zongjie3, zongjie5) )      
        ) 
        self.wait(2.2222)
        
        self.play( Circumscribe(text3) )
        self.play( Circumscribe(VGroup(zongjie3, zongjie4)) )
        
        self.wait(0.7777)
        
        self.play( Circumscribe(zongjie3) )
        
        self.wait(22.2222)
        


