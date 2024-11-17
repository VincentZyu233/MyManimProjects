from manim import *
import math
from typing import Sequence

class test(MovingCameraScene):
    def construct(self):
        
        axes = Axes(
            x_range=(-2.2222, 8.8888-1.1111, 1),
            y_range=(-1.1111, 11.1111, 1),
            x_length=8.8888,
            y_length=6,
            x_axis_config={"include_ticks": False},  # 隐藏 x 轴的刻度线
            y_axis_config={"include_ticks": False},  # 隐藏 y 轴的刻度线
        ).shift(RIGHT*0.8888+UP*0.4444)

        # 创建二次函数
        quadratic_function = lambda x: 1/2*x*x - 5/2*x + 2

        # 创建函数图形对象
        # graph = ParametricFunction(
        #     # lambda t: axes.c2p(t, quadratic_function(t), 0),
        #     quadratic_function,
        #     color=BLUE,
        #     t_range=(-4.4444, 8.8888+4.4444, 8.8888)
        # )
        graph = axes.plot(quadratic_function, x_range=[-2.2222, 8.8888-2.2222], use_smoothing=True)

        # 添加坐标轴和函数图形到场景
        # self.add(axes, graph)
        self.play( Create(axes) )
        self.play( Create(graph) )
        
        
        dota, dotb, dotc = Dot(axes.c2p(1, 0)), Dot(axes.c2p(4,0)), Dot(axes.c2p(0,2))
        labela, labelb, labelc = Tex('A').move_to(dota).shift(LEFT*0.4444+DOWN*0.2222), Tex('B').move_to(dotb).shift(RIGHT*0.4444+DOWN*0.2222), Tex('C').move_to(dotc).shift(LEFT*0.4444)
        
        dotd = Dot(axes.c2p(5/2, quadratic_function(5/2)))
        labeld = Tex('D').move_to(dotd).shift(DOWN*0.4444)
        
        
        self.play(Succession(
            Write(dota),
            FadeOut(dota),
            Write(labela),
            lag_ratio=0.8888
        ), run_time=0.8888)
        
        self.play(Succession(
            Write(dotb),
            FadeOut(dotb),
            Write(labelb),
            lag_ratio=0.8888
        ), run_time=0.8888)
        
        self.play(Succession(
            Write(dotc),
            FadeOut(dotc),
            Write(labelc),
            lag_ratio=0.8888
        ), run_time=0.8888)

        self.wait(2.2222)
        
        self.play(Succession(
            Write(dotd),
            # FadeOut(dotd),
            Flash(dotd, run_time=0.8888),
            Write(labeld),
            lag_ratio=0.8888
        ), run_time=0.8888)
        
        xP = ValueTracker(1.8888)
        
        xP_disp = Tex( "xP = {:.2f}".format(xP.get_value()) ).to_edge(LEFT).shift(DOWN*2.2222+RIGHT*0.4444)
        # xP_disp.add_updater(lambda m: m.set_value(xP.get_value())) 
        xP_disp.add_updater(lambda m: m.become(
            Tex( "xP = {:.2f}".format(xP.get_value()) ).to_edge(LEFT).shift(DOWN*2.2222+RIGHT*0.4444)
        ))

        
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

        xP_bg = get_background_pattern(xP_disp)
        
        self.play(FadeIn(xP_disp, xP_bg))
        
        dotp = Dot(axes.c2p(xP.get_value(), quadratic_function(xP.get_value()) ), color=YELLOW_D)
        
        dotp.add_updater( lambda mob:
            mob.become(
                Dot(axes.c2p(xP.get_value(), quadratic_function(xP.get_value()) ), color=YELLOW_D)
            )
        )
        
        # labeld = Tex('D').move_to(dotd).shift(DOWN*0.4444)
        labelp = always_redraw(
            lambda: Tex('P').move_to(dotp).shift(DOWN*0.2222)
        )
        
        print('---p laile ---')
        
        self.play(Succession(
            Write(dotp),
            # FadeOut(dotd),
            Write(labelp),
            lag_ratio=0.8888
        ), run_time=0.8888)
        self.play(Flash(dotp), run_time=0.8888)
        
        # xP.set_value(0.4444)
        # xP.set_value(2.2222)
        # xP.set_value(1.8888)
        
        self.play(xP.animate.set_value(0.4444), run_time=0.8888)
        self.play(xP.animate.set_value(2.2222), run_time=0.8888)
        self.play(xP.animate.set_value(1.8888), run_time=0.8888)
        
        self.wait(0.2222)
        self.play(xP.animate.set_value(1.8888-0.4444), run_time=0.8888)
        
        print(self.camera.frame.get_width())

        self.play( self.camera.frame.animate.set(width = 8.8888).shift(DOWN*1.2222+RIGHT*0.4444) )
        print(self.camera.frame.get_width())
        
        linecp = always_redraw( lambda:  Line(dotc, dotp).set_stroke(YELLOW,2.2222) )
        linedp = always_redraw( lambda:  Line(dotd, dotp).set_stroke(YELLOW,2.2222) )
        
        self.play(GrowFromPoint(linecp, dotc))
        self.play(GrowFromPoint(linedp, dotd))
        
        linebd = Line(dotb, dotd).set_stroke(YELLOW,2.2222)
        kbd = linebd.get_slope()
        
        pm1 = Dot([dotp.get_x()-4, dotp.get_y()-4*kbd, 0])
        pm2 = Dot([dotp.get_x()+8, dotp.get_y()+8*kbd, 0])
        # zhixianpm = Line( pm1, pm2 ).set_stroke(YELLOW,2.2222-0.4444)
        # zhixianpm = always_redraw( lambda:
        #     Line( dotp, (xP.get_value()+8, quadratic_function(xP.get_value())+8*kbd, 0)  )
        #     .set_stroke(YELLOW,2.2222-0.4444)
        # )
        
        zhixianpm = always_redraw( lambda:
            Line( (xP.get_value()-8, quadratic_function(xP.get_value())-8*kbd, 0), (xP.get_value()+8, quadratic_function(xP.get_value())+8*kbd, 0)  )
            .set_stroke(YELLOW,2.2222-0.4444)
        )
        
        self.play( Create(zhixianpm) )
        self.play( Create(linebd) )
        
        self.play( self.camera.frame.animate.set(width = 8.8888+4.4444).shift(UP*1.2222+LEFT*0.4444) )
        
        linebc = Line(dotb, dotc).set_stroke(YELLOW,2.2222)
        self.play(Create(linebc))
        
        def line_to_sequence(line: Line) -> Sequence[np.ndarray]:
            start_point = np.array([line.start[0], line.start[1], line.start[2]])
            end_point = np.array([line.end[0], line.end[1], line.end[2]])
            return [start_point, end_point]

        # dotm = Dot( line_intersection(line_to_sequence(linebc), line_to_sequence(zhixianpm))).set_color(ORANGE)
        # dotm = always_redraw( lambda: 
        #     Dot( 
        #         line_intersection([np.array([dotc.get_x(), dotc.get_y(),0]), np.array([dotb.get_x(), dotb.get_y(), 0])], [np.array([dotp.get_x(), dotp.get_y(), 0]), np.array([dotp.get_x()+8, dotp.get_y()+8*kbd, 0])])
        #     ).set_color(ORANGE).shift(LEFT*0.2222+UP*0.0404)
        # )
        dotm = always_redraw( lambda: 
            Dot( 
                line_intersection( linebc.get_start_and_end(), zhixianpm.get_start_and_end() )
            ).set_color(ORANGE)
            # .shift(LEFT*0.2222+UP*0.0404)
        )
        self.play(Create(dotm))
        
        labelm = Tex("M").move_to(dotm).shift(UP*0.4444)
        self.play(Write(labelm))
        
        bian_cp = always_redraw( lambda: Line(dotc, dotp).set_stroke(ORANGE,4.4444) )
        bian_pd = always_redraw( lambda: Line(dotp, dotd).set_stroke(ORANGE,4.4444) )
        bian_dm = always_redraw( lambda: Line(dotd, dotm).set_stroke(ORANGE,4.4444) )
        bian_mc = always_redraw( lambda: Line(dotm, dotc).set_stroke(ORANGE,4.4444) )
        
        self.play( GrowFromPoint(bian_cp, dotc), run_time=0.8888 )
        self.play( GrowFromPoint(bian_pd, dotp), run_time=0.8888 )
        self.play( GrowFromPoint(bian_dm, dotd), run_time=0.8888 )
        self.play( GrowFromPoint(bian_mc, dotm), run_time=0.8888 )
        
        self.play(xP.animate.set_value(0.4444), run_time=0.8888)
        self.play(xP.animate.set_value(2.2222), run_time=0.8888)
        self.play(xP.animate.set_value(1.8888), run_time=0.8888)
        
        
        self.wait(4.4444)
        
        # manim -pql erci240301.py
        