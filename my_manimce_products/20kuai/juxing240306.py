from manim import *
import math
from typing import Sequence

class test(MovingCameraScene):
    def construct(self):
        
        BEISHU = 1.1111
        rect_abcd = Rectangle(width=8*BEISHU, height=3*BEISHU)
        self.play(Create(rect_abcd))
        
        point_a = rect_abcd.get_vertices()[1]
        point_b = rect_abcd.get_vertices()[2]
        point_c = rect_abcd.get_vertices()[3]
        point_d = rect_abcd.get_vertices()[0]
        
        label_a = Tex('A').move_to(point_a).shift(UP*0.2222)
        label_b = Tex('B').move_to(point_b).shift(DOWN*0.2222)
        label_c = Tex('C').move_to(point_c).shift(DOWN*0.2222)
        label_d = Tex('D').move_to(point_d).shift(UP*0.2222)
        
        self.play(Write(label_a), run_time = 0.4444)
        self.play(Write(label_b), run_time = 0.4444)
        self.play(Write(label_c), run_time = 0.4444)
        self.play(Write(label_d), run_time = 0.4444)
        
        k = ValueTracker(0) # ap/ad的比值
        # xP_disp = Tex( "xP = {:.2f}".format(xP.get_value()) ).to_edge(LEFT).shift(DOWN*2.2222+RIGHT*0.4444)

        
        
        dot_p = always_redraw( lambda:
            Dot(color=YELLOW_D).move_to(point_a + k.get_value() * (point_d - point_a))
        )
        
        label_p = always_redraw( lambda:
            Tex('P').next_to(dot_p, UP).shift(UP*0.1111)
        )

        velocity_p = always_redraw( lambda: 
            # Vector( Line ( dot_p.get_center()+LEFT*0.4444+UP*0.4444, dot_p.get_center()+RIGHT*0.4444+UP*0.4444 )  )
            Vector( [1+0.2222*k.get_value(),0] ).next_to(dot_p, UP).shift(UP*0.4444+LEFT*0.8888+RIGHT*0.2222*k.get_value())
        )
        
        label_vp = always_redraw( lambda:
            Text('1单位/s').next_to(velocity_p, UP)
        )
        

        self.play(Create(dot_p))
        self.play(Write(label_p))
        self.play(Flash(dot_p))
        self.play( Create( velocity_p ), Write(label_vp) )
        
        
        # self.play(xP.animate.set_value(1.8888), run_time=0.8888)
        self.play(
            k.animate(run_time=2.2222, rate_func=rate_functions.ease_in_out_sine).set_value(1),
        )
        self.play(
            k.animate(run_time=0.8888, rate_func=rate_functions.slow_into).set_value(0),
        )
        
        dot_q = always_redraw( lambda:
            Dot(color=YELLOW_D).move_to(point_b + 2 * k.get_value() * (point_c - point_b))
        )
        
        label_q = always_redraw( lambda:
            Tex('Q').next_to(dot_q, DOWN).shift(DOWN*0.1111)
        )
        
        velocity_q = always_redraw( lambda: 
            # Vector( Line ( dot_p.get_center()+LEFT*0.4444+UP*0.4444, dot_p.get_center()+RIGHT*0.4444+UP*0.4444 )  )
            Vector( [2+2*0.2222*k.get_value(),0] ).next_to(label_q, DOWN).shift(DOWN+0.8888+LEFT*0.8888+RIGHT*0.2222*k.get_value())
        )
        
        label_vq = always_redraw( lambda:
            Text('2单位/s').next_to(velocity_q, DOWN*2.2222).shift(UP*0.4444)
        )
        

        self.play(Create(dot_q))
        self.play(Write(label_q))
        self.play(Flash(dot_q))
        self.play( Create( velocity_q ), Write(label_vq) )
        
        print( self.camera.frame.get_width() )
        
        self.play( self.camera.frame.animate.set(width = self.camera.frame.get_width()+8.8888).shift(RIGHT*4.4444) )

        
        shexianbc = Line(point_b, point_b+2.2222*(point_c-point_b)).set_stroke(BLUE_D, 2.2222).set_z_index(-1)
        self.play(Create(shexianbc))
        
        self.play(
            k.animate(run_time=2.2222, rate_func=rate_functions.ease_in_out_sine).set_value(1),
        )
        
        self.wait(0.8888)
        
        self.play(
            k.animate(run_time=2.2222, rate_func=rate_functions.ease_in_out_sine).set_value(0),
        )
        
        self.wait(2.2222)
        
        self.play(
            k.animate(run_time=2.2222, rate_func=rate_functions.ease_in_out_sine).set_value(0.2222),
        )
        
        line_aq = always_redraw( lambda:
            Line(point_a, dot_q).set_stroke(YELLOW_D, 2.2222)    
        )
        line_pq = always_redraw( lambda:
            Line(dot_p, dot_q).set_stroke(YELLOW_D, 2.2222)    
        )
        line_dq = always_redraw( lambda:
            Line(point_d, dot_q).set_stroke(YELLOW_D, 2.2222)    
        )
        
        self.play( GrowFromPoint(line_aq, point_a) )
        self.play( GrowFromPoint(line_pq, dot_p) )
        self.play( GrowFromPoint(line_dq, point_d) )
        
        x_disp = always_redraw( lambda: 
            Text("x = {:.2f} 秒".format( 8 * k.get_value() )).next_to(rect_abcd, DOWN*4.4444).shift(DOWN*2.2222+LEFT*2.2222)
        )
        
        # x_disp.set_text("x = {:.2f} 秒".format( 8 * k.get_value() ))
        
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

        x_bg = get_background_pattern(x_disp)
        
        self.play(
            
            self.camera.frame.animate.shift(DOWN*0.8888),
            Write(x_disp),
            FadeIn(x_bg),
        )
        
        self.play(
            k.animate(run_time=0.8888, rate_func=rate_functions.slow_into).set_value(0),
        )
        
        self.play(
            k.animate(run_time=2.2222, rate_func=rate_functions.ease_in_out_sine).set_value(1),
        )
        
        self.wait(0.8888)
        self.play(
            k.animate(run_time=2.2222, rate_func=rate_functions.ease_in_out_sine).set_value(0.2222),
        )
        
        self.wait(2.2222)
        
        tri_apq = always_redraw(lambda:
            Polygon(point_a, dot_p.get_center(), dot_q.get_center(), ).set_opacity(0.4444).set_color(RED_D)
        )
        tri_dcq = always_redraw( lambda:
            Polygon(point_d, point_c, dot_q.get_center()).set_opacity(0.4444).set_color(GREEN_D)
        )

        
        # rtarrow0 = MathTex(r"\xrightarrow{x^6y^8}", font_size=96)
        tex_y1 = MathTex(r"y_{1} = S_{ \triangle APQ } ").next_to(rect_abcd, RIGHT*4.4444).shift(UP*2.2222+RIGHT*0.8888+DOWN*0.8888)
        tex_y2 = MathTex(r"y_{2} = S_{ \triangle DCQ } ").next_to(tex_y1, DOWN).shift(DOWN*0.8888)

        tex_y11 = MathTex(r" = \frac{1}{2} AP \cdot AB ").next_to(tex_y1, RIGHT)
        tex_y22 = MathTex(r" = \frac{1}{2} CQ \cdot CD ").next_to(tex_y2, RIGHT)
        
        tex_y111 = always_redraw( lambda:
            Tex(r" = {:.2f}".format( 0.5 * 8*k.get_value() * 3 )).next_to(tex_y1, RIGHT)    
        )
        tex_y222 = always_redraw( lambda:
            Tex(r" = {:.2f}".format( 0.5 * abs(8-8*2*k.get_value()) * 3 )).next_to(tex_y2, RIGHT)    
        )
        
        tex_y1111 = MathTex(r" = \frac{1}{2} x \cdot 3 ").next_to(tex_y11, RIGHT)
        tex_y2222 = MathTex(r" = \frac{1}{2} \lvert 8-2x \rvert \cdot 3 ").next_to(tex_y22, RIGHT)
        
        tex_y11111 = MathTex(r" = \frac{3x}{2}  ").next_to(tex_y1111, RIGHT)
        tex_y22222 = MathTex(r" = \lvert 12-3x \rvert").next_to(tex_y2222, RIGHT)
        
        self.play(Write(tri_apq))
        self.play(Write(tex_y1))
        self.play(Write(tex_y111))
        
        self.play(Write(tri_dcq))
        self.play(Write(tex_y2))
        self.play(Write(tex_y222))
        
        self.play(
            k.animate(run_time=0.8888, rate_func=rate_functions.slow_into).set_value(0),
        )
        
        self.play(
            k.animate(run_time=2.2222, rate_func=rate_functions.ease_in_out_sine).set_value(1),
        )
        
        self.wait(0.2222)
        self.play(
            k.animate(run_time=2.2222, rate_func=rate_functions.ease_in_out_sine).set_value(0.2222),
        )
        
        self.wait(2.2222)
        
        self.play( self.camera.frame.animate.shift(RIGHT*0.8888*2.2222), FadeOut(tex_y111) )
        self.play( Write(tex_y11)  )
        self.play( Write(tex_y1111)  )
        self.play( Write(tex_y11111)  )
        
        self.wait(0.8888)
        
        self.play( self.camera.frame.animate.shift(RIGHT*0.8888*2.2222), FadeOut(tex_y222) )
        self.play( Write(tex_y22)  )
        self.play( Write(tex_y2222)  )
        self.play( Write(tex_y22222)  )

        group_y1 = VGroup(tex_y1, tex_y11, tex_y1111, tex_y11111 )
        group_y2 = VGroup(tex_y2, tex_y22, tex_y2222, tex_y22222 )
        
        self.play( 
            self.camera.frame.animate.shift(RIGHT*2.2222 + DOWN*4.4444 + DOWN*2.2222 +RIGHT*0.4444 )
                                     .set(width =self.camera.frame.get_width()+4.4444 ) 
        )
        
        
        axes = Axes(
            x_range=(-2.2222, 8.8888*2.2222, 1),
            y_range=(-2.2222, 8.8888*2.2222, 1),
            x_length=8.8888*2.2222 - 4.4444,
            y_length=8.8888,
        ).next_to( tex_y22, DOWN ).shift(DOWN*4.4444+UP*0.8888+UP*0.2222)
        
        graph_y1 = axes.plot(lambda x: 3*x/2 , x_range=[-2.2222, 8.8888+2.2222], use_smoothing=True)
        gragh_y2 = axes.plot(lambda x: abs(12-3*x) , x_range=[-2.2222, 8.8888+2.2222-0.4444], use_smoothing=True)
        
        self.play( Create(axes) )
        
        self.play( group_y1.animate.shift(DOWN*4.4444 + DOWN*4.4444) )
        self.play( group_y1.animate.shift(RIGHT*4.4444) )
        self.play( Circumscribe(group_y1) )
        self.play( Create(graph_y1) )
        self.play( Indicate(graph_y1) )
        
        self.play( group_y2.animate.shift(DOWN*4.4444) )
        self.play( group_y2.animate.shift(RIGHT*4.4444) )
        self.play( Circumscribe(group_y2) )
        self.play( Create(gragh_y2) )
        self.play( Indicate(gragh_y2) )
        
        # dotd = Dot(axes.c2p(5/2, quadratic_function(5/2)))
        dot_x1 = Dot( axes.c2p(8/3, 4) ).set_color(YELLOW)
        dot_x2 = Dot( axes.c2p(8, 12) ).set_color(YELLOW)
        xuxian_x1 = DashedLine( axes.c2p(8/3, 4), axes.c2p(8/3, 0) )
        xuxian_x2 = DashedLine( axes.c2p(8, 12), axes.c2p(8, 0) )
        
        self.play( Create(dot_x1) )
        self.play( Create(xuxian_x1) )
        
        self.play( Create(dot_x2) )
        self.play( Create(xuxian_x2) )
        
        self.play( Circumscribe(group_y1) ,run_time=0.8888 )
        self.play( Circumscribe(group_y1) ,run_time=0.8888 )
        self.play( Indicate(graph_y1) ,run_time=0.8888 )
        self.play( Indicate(graph_y1) ,run_time=0.8888 )
        
        self.wait(0.8888)
        
        self.play( Circumscribe(group_y2) ,run_time=0.8888 )
        self.play( Circumscribe(group_y2) ,run_time=0.8888 )
        self.play( Indicate(gragh_y2) ,run_time=0.8888 )
        self.play( Indicate(gragh_y2) ,run_time=0.8888 )
        
        group_allax = VGroup(group_y1, group_y2, axes, graph_y1, gragh_y2)
        
        group_velo_and_label = VGroup( velocity_p, velocity_q, label_vp, label_vq )
        self.play( 
            self.camera.frame.animate.shift( LEFT*2.2222+UP*2.2222 )
                                     .set(width =self.camera.frame.get_width()+8.8888-2.2222 ),
                                
        )
        
        self.play( FadeOut( group_velo_and_label ))
        
        func_y1 = lambda x: 3*x/2
        func_y2 = lambda x: abs(12-3*x)
        
        dot_t1 = always_redraw( lambda:
            Dot(
                axes.c2p( 8*k.get_value(), func_y1(8*k.get_value()) )
            ).set_color(RED_D)
        )
        
        label_t1 = always_redraw( lambda:
            MathTex(r"( AP, S_{\triangle{APQ} } )" ).next_to(dot_t1, LEFT)
        )
        
        dot_t2 = always_redraw( lambda:
            Dot(
                axes.c2p( 8*k.get_value(), func_y2(8*k.get_value()) )
            ).set_color(RED_D)
        )
        
        label_t2 = always_redraw( lambda:
            MathTex(r"( BQ/2, S_{\triangle{DCQ} } )" ).next_to(dot_t2, RIGHT)
        )
        
        self.play(
            k.animate(run_time=2.2222, rate_func=rate_functions.slow_into).set_value(0),
        )
        

        # -----camera focus -----
        yuan_width = self.camera.frame.get_width()
        yuan_position = self.camera.frame.get_center()
        
        def camera_focus( obj ):
            self.play( 
                self.camera.frame.animate.move_to( obj.get_center() )
                                         .set(width = 8.8888 ) 
            )
            
        def camera_recover():
            self.play( 
                self.camera.frame.animate.move_to( yuan_position )
                                         .set(width = yuan_width ) 
            )
        
        self.play( Create(dot_t1) )
        self.play( Flash(dot_t1) )
        camera_focus(dot_t1)
        self.play( Write(label_t1) )
        self.play( FocusOn(dot_t1) )
        camera_recover()
        
        self.play(
            k.animate(run_time=2.2222, rate_func=rate_functions.ease_in_out_sine).set_value(1),
        )
        
        self.play(
            k.animate(run_time=2.2222, rate_func=rate_functions.slow_into).set_value(0.2222),
        )
        
        self.wait(0.4444)
        
        
        self.play( Create(dot_t2) )
        self.play( Flash(dot_t2) )
        camera_focus(dot_t2)
        self.play( Write(label_t2) )
        self.play( FocusOn(dot_t2) )
        camera_recover()
        
        self.play(
            k.animate(run_time=0.8888, rate_func=rate_functions.slow_into).set_value(0),
        )
        self.play(
            k.animate(run_time=2.2222, rate_func=rate_functions.ease_in_out_sine).set_value(1),
        )
        
        self.wait(4.4444)
        # manim -ql juxing240306.py
        