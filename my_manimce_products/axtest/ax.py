from manim import *
import sys

class AxesWithDifferentTips(MovingCameraScene):
    def construct(self):
        new_limit = 2222  # 设置新的递归层数限制
        sys.setrecursionlimit(new_limit)
        
        
        # 调整单位长度为0.2
        ax = Axes(
            axis_config={'tip_shape': StealthTip, 'unit_size': 0.2},
            x_range=[-2.2222, 16.6666, 0.8888],
            y_range=[-2.2222, 8.8888, 1.1111]
        )
        # self.add(ax)
        self.play( Create(ax) )   

        # 定义二次函数
        quadratic_function = lambda x: 1/22*(x+0.2222)**2 + 2
        derivative_quad_fun = lambda x: 1/11*(x+0.2222)

        quad_graph = ax.plot(quadratic_function, color=RED)  # 使用红色绘制二次函数
        self.play(Write(quad_graph))

        self.play(
            self.camera.frame.animate.set( width = 18 ),
        )

        # 创建ValueTracker来控制动点的x坐标
        xA_value = ValueTracker(2.22222)
        xB_value = ValueTracker(2.22222)  # 初始值为8

        # 添加固定坐标点
        fixed_point = Dot().move_to(ax.c2p(2.22222, quadratic_function(2.22222)))  # (1, f(1))为固定点的坐标
        fixed_point.add_updater(lambda d: d.move_to( ax.c2p( xA_value.get_value(), quadratic_function(xA_value.get_value() ))) )
        self.play(FadeIn(fixed_point))
        
        # 创建标签A和B
        label_A = Tex("A").next_to(fixed_point, UP)
        # 将标签与点的位置绑定
        label_A.add_updater(lambda l: l.next_to(fixed_point, UP))
        self.play( Create(label_A) )

        # 添加动点
        dynamic_point = Dot(color=YELLOW)
        dynamic_point.add_updater(lambda d: d.move_to(ax.c2p(xB_value.get_value(), quadratic_function(xB_value.get_value()))))
        self.play(FadeIn(dynamic_point))

        label_B = Tex("B").next_to(dynamic_point, UP)
        label_B.add_updater(lambda l: l.next_to(dynamic_point, UP))

        arc_ab = ax.plot( quadratic_function, color = YELLOW, 
                         x_range=[2.22222,xB_value.get_value(), 0.1] )
        arc_ab.add_updater(
            lambda f:
                f.become(
                    ax.plot( quadratic_function, color = YELLOW, 
                         x_range=[xA_value.get_value(), xB_value.get_value(), 0.1] )
                )
        )
        self.add(arc_ab)

        self.play(
            xB_value.animate.set_value(12.2222), 
            Create(label_B),
            run_time=1.1111
        )
        
        self.wait()
        
        self.play(xB_value.animate.set_value(14.4444))
        self.play(xB_value.animate.set_value(10.0000))
        self.play(xB_value.animate.set_value(12.2222))

        self.wait()

        # 添加连接两点的线段
        line = Line(fixed_point.get_center(), dynamic_point.get_center())
        self.play( Create(line) )
        # 更新线段的位置
        line.add_updater(lambda l: l.put_start_and_end_on(fixed_point.get_center(), dynamic_point.get_center()))

        # 添加水平线段
        horizontal_projection = Line(
            fixed_point.get_center(),  # 水平线段的起点在固定点的下方一定距离
            fixed_point.get_center() + RIGHT * (dynamic_point.get_center()[0] - fixed_point.get_center()[0]),  # 水平线段的终点在动点的x坐标在固定点x坐标上的投影
            stroke_width=2.2222,  # 设置线段的宽度为1
            color=GRAY  # 设置线段的颜色为灰色
        )
        self.play(Create(horizontal_projection))
        # 更新水平线段的位置
        horizontal_projection.add_updater(
            lambda h: h.put_start_and_end_on(
                fixed_point.get_center(),
                fixed_point.get_center() + RIGHT * (dynamic_point.get_center()[0] - fixed_point.get_center()[0])
            )
        )

        vertical_projection = Line(
            fixed_point.get_center() + RIGHT * (dynamic_point.get_center()[0] - fixed_point.get_center()[0]),
            dynamic_point.get_center(),
            stroke_width = 2.2222,
            color = GRAY,
        )
        self.play(Create(vertical_projection))
        vertical_projection.add_updater(
            lambda h: h.put_start_and_end_on(
                fixed_point.get_center() + RIGHT * (dynamic_point.get_center()[0] - fixed_point.get_center()[0]),
                dynamic_point.get_center(),
            )
        )
        
        horizontal_brace = Brace(horizontal_projection).shift( UP*0.2222 )
        self.play(Create(horizontal_brace))
        horizontal_label = horizontal_brace.get_tex(r"\Delta x")
        self.play(Write(horizontal_label))
        horizontal_label.add_updater(
            lambda l:
                l.match_x(horizontal_projection)
        )     
        horizontal_brace.add_updater(
            lambda b:
                b.match_x(horizontal_projection).set_width(horizontal_projection.get_width())
        )
        
        # vertical_brace = Brace(vertical_projection)
        vertical_brace = BraceBetweenPoints(fixed_point.get_center() + RIGHT * (dynamic_point.get_center()[0] - fixed_point.get_center()[0]),
                                                dynamic_point.get_center()).next_to(vertical_projection, RIGHT)
        self.play(Create(vertical_brace))
        vertical_label = vertical_brace.get_tex(r"\Delta y").next_to(vertical_brace, RIGHT)
        self.play(Write(vertical_label))
        vertical_label.add_updater(
            lambda l:
                l.match_y(vertical_projection).next_to(vertical_brace, RIGHT)
        )
        vertical_brace.add_updater(
            lambda b:
                b.match_y(vertical_projection).set_height(vertical_projection.get_height()).next_to(vertical_projection, RIGHT)
        )
        
        self.play(
            self.camera.frame.animate.set( width = 12.8888 ),
        )
        
        # 创建DecimalNumber对象来跟踪线段AB的长度
        # AB_length_tracker = DecimalNumber().next_to(ax.get_corner(UL), UP)  # 设置跟踪器初始位置在屏幕的左上角
        # Variable(start, 'x', num_decimal_places=3)
        AB_length_tracker = Variable(line.get_length(), r"\Delta s", num_decimal_places=4).next_to(ax.get_corner(UL), UP)
        AB_length_tracker.shift(RIGHT*4.4444 + DOWN*0.4444)
        # 更新函数，以便在动点B的位置变化时更新跟踪
        AB_length_tracker.add_updater(
            lambda obj: obj.tracker.set_value(line.get_length())
        )
        horizontal_length_tracker = Variable(horizontal_projection.get_length(), r"\Delta x", num_decimal_places=4).next_to(AB_length_tracker, DOWN)
        # 更新函数，以便在动点B的位置变化时更新跟踪
        horizontal_length_tracker.add_updater(
            lambda obj: obj.tracker.set_value(horizontal_projection.get_length())
        )
        
        vertical_length_tracker = Variable(vertical_projection.get_length(), r"\Delta y", num_decimal_places=4).next_to(horizontal_length_tracker, DOWN)
        vertical_length_tracker.add_updater(
            lambda obj: obj.tracker.set_value(vertical_projection.get_length())
        )
        
        self.play( Write(AB_length_tracker))
        self.play( Write(horizontal_length_tracker))
        self.play( Write(vertical_length_tracker))
        
        self.wait()
        
        # 播放动画，改变动点的x坐标
        self.play(
            xB_value.animate.set_value(4.4444), 
            run_time=2.2222,
        )  # 将动点的x坐标从8变化到2，持续2秒

        # manim -pql ax.py --disable_caching
        
        self.play(
            self.camera.frame.animate.set( width = 18 ).shift(DOWN*0.8888),
        )
        
        self.wait(0.4444)
        
        self.play(
            xB_value.animate.set_value(12.2222), 
            run_time=0.8888,
        )  # 将动点的x坐标从8变化到2，持续2秒
        
        tex_siml = Tex("When $\Delta$ x is infinitely small, we can nonrigorously assume that:")
        tex_siml.next_to(ax, DOWN)
        self.play(FadeIn(tex_siml))
        
        tex_deltaxys = MathTex(r"{(\Delta x)}^{2} \, + \, {(\Delta y)}^{2} \, = \, {(\Delta s)}^{2}")
        tex_deltaxys.next_to(tex_siml, DOWN)
        self.play(Write(tex_deltaxys))
        
        self.wait(0.4444)      

        self.play(
            FadeOut(tex_siml),
            FadeOut(tex_deltaxys),
        )
        
        self.play( self.camera.frame.animate.set(width = 22).shift( DOWN*0.22 ) )
        
        tex_but = Tex(r"but this is way too \textbf{nonrigorous},")
        tex_but.next_to(ax, DOWN)
        tex_to = Tex(r"to make it more rigorous, we introduce the concept of \textbf{\textit{ differential }}")
        tex_to.next_to(tex_but, DOWN)
        
        tex_wiki = MarkupText(
            "<span font_family='Cascadia Code Light'>The term differential is used nonrigorously in calculus to refer to an infinitesimal change in some varying quantity.  \n \u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0 ————WikiPedia</span>"
        ).next_to(tex_to, DOWN).scale(0.4444)
        tex_wiki.shift(UP * 0.4444)
        # text_wiki = MarkupText(
        #     "The term <b>differential<\b> is used nonrigorously in calculus \n to refer to an infinitesimal change in some varying quantity.",
        #     font='Cascadia Code',
        # ).next_to(tex_to, DOWN).scale(0.2222)
        background_rect_text_wiki = BackgroundRectangle(tex_wiki, color=GREY, fill_opacity=0.2)
        
        self.play( FadeIn( tex_but ) )
        self.play( FadeIn(tex_to) )
        self.play(
            Write(tex_wiki),
            Create(background_rect_text_wiki)
        )
        
        print(fixed_point.get_center())
        
        self.play(
            FadeOut(tex_wiki),
            FadeOut(background_rect_text_wiki)
        )
        self.play(
            FadeOut(tex_but),
            FadeOut(tex_to),
        )

        self.play(
            self.camera.frame.animate.set( width = 12 ).shift(UP*2.2222),
            xA_value.animate.set_value(3.333333),
            xB_value.animate.set_value(9.999999)
        )

        print( derivative_quad_fun( fixed_point.get_center()[0] - ax.get_origin()[0] ) )
        print( fixed_point.get_center()[0] - ax.get_origin()[0] )

        # 创建过点A的切线
        tangent_line = always_redraw(lambda: Line(
            fixed_point.get_center() + 22 * DOWN * derivative_quad_fun( xA_value.get_value() ) + 22 * LEFT, 
            fixed_point.get_center() + 22 * UP * derivative_quad_fun( xA_value.get_value() ) + 22 * RIGHT,  
            color=YELLOW  # 设置切线的颜色,
        ))
        self.play(Create(tangent_line), run_time = 2.2222)
        
        intersec_dy_point = Intersection( tangent_line, vertical_projection )
        
        # 将更新函数与交点对象关联
        intersec_dy_point.add_updater( lambda d: d.become( Intersection( tangent_line, vertical_projection ) ) )

        self.play( Create(intersec_dy_point) )

        self.play(
            self.camera.frame.animate.set( width = 22.2222 ).shift(DOWN*2.2222),
            # stroke_width = 2.2222,
        )
        
        tex_usingcalculus = MarkupText(
            "<span font_family='Cascadia Code Light'>Using calculus, it is possible \nto relate the infinitely small changes of various variables to each other mathematically using derivatives. </span>"
        ).next_to(ax, DOWN).scale(0.4444)    
        tex_usingcalculus.shift(UP*0.8888)
        # tex_usingcalculus.set_width(8.88888888)
        background_rect_tex_usingcalculus = BackgroundRectangle(tex_usingcalculus, color=GREY, fill_opacity=0.2)
        self.play(
            Write( tex_usingcalculus ),
            Create(background_rect_tex_usingcalculus)
        )
        
        self.wait( 0.8888 )
        self.play(
            VGroup(tex_usingcalculus, background_rect_tex_usingcalculus) .animate.shift(UP * 0.8888)
        )
        # If y is a function of x, then the differential dy of y is related to dx by the formula
        tex_if = MarkupText(
            "<span font_family='Cascadia Code Light'>If y is a function of x, then the differential dy of y is related to dx by the formula. </span>"
        ).next_to(tex_usingcalculus, DOWN).scale(0.4444) 
        tex_if.shift(UP*0.2222)   
        background_rect_tex_if = BackgroundRectangle(tex_if, color=GREY, fill_opacity=0.2)
        self.play(
            Write( tex_if ),
            Create(background_rect_tex_if)
        )
        
        # text=MathTex(
        #     "\\frac{d}{dx}f(x)g(x)=","f(x)\\frac{d}{dx}g(x)","+",
        #     "g(x)\\frac{d}{dx}f(x)"
        # )
        # tex_dydx = MathTex("dy = \\frac{dy}{dx} dx").next_to(tex_usingcalculus, DOWN)
        tex_dydx = Tex(
            r"$ dy = \frac{dy}{dx} dx $",
        ).next_to(tex_if, DOWN*2.2222)
        self.play(
            Write(tex_dydx)
        )
        
        tex_where = MarkupText(
            "<span font_family='Cascadia Code Light'>where dy/dx denotes the derivative of y with respect to x. </span>"
        ).next_to(tex_dydx, DOWN).scale(0.4444)
        background_rect_tex_where = BackgroundRectangle( tex_where, color=GREY, fill_opacity=0.2 ) 
        # self.play( 
        #     Write(tex_where),
        #     Create( background_rect_tex_where )
        # )
        self.play( Write( tex_where ))
        self.play( Create(background_rect_tex_where) )
        
        self.wait( 0.8888 )
        
        #  This formula summarizes the intuitive idea that the derivative of y with respect to x is the limit of the ratio of differences Δy/Δx as Δx becomes infinitesimal.
        self.play(
            VGroup(tex_usingcalculus, background_rect_tex_usingcalculus).animate.shift( UP*2.2222 ).fade( 1 ),
            VGroup(tex_if, background_rect_tex_if).animate.shift( UP*2.2222 ).fade( 1 ),
            VGroup(tex_where, background_rect_tex_where).animate.shift( UP*2.2222 ).fade( 1 ),
            tex_dydx.animate.shift( UP*2.2222 )
        )       

        rect_dydx = BackgroundRectangle( tex_dydx, color=BLUE_C, fill_opacity=0.2222 )               
        self.play( Create(rect_dydx) )

        self.play(
            self.camera.frame.animate.set( width = 18.88888888 ).shift( UP*0.8888 )
        )
        
        dy_dot = always_redraw(
            lambda: Dot( point = ( fixed_point.get_center() + [horizontal_projection.get_length(), horizontal_projection.get_length() * derivative_quad_fun( xA_value.get_value() ), 0] ), color=GOLD )
        )

        self.play( Create(dy_dot) )

        projection_dydx = Line( dy_dot.get_center(), 
                               dy_dot.get_center() - [0, horizontal_projection.get_length() * derivative_quad_fun( xA_value.get_value() ),0] )
        projection_dydx.add_updater(
            lambda obj: obj.put_start_and_end_on(
                dy_dot.get_center(), 
                dy_dot.get_center() - [0, horizontal_projection.get_length() * derivative_quad_fun( xA_value.get_value() ),0]
            )
        )

        dy_brace = BraceBetweenPoints( dy_dot.get_center(), dy_dot.get_center() - [0, horizontal_projection.get_length() * derivative_quad_fun( xA_value.get_value() ),0] )
        dy_brace.add_updater(
            lambda b:
                b.match_y( projection_dydx ).set_height( projection_dydx.get_length() ).next_to( projection_dydx, LEFT )
        )
        self.play( Create(dy_brace) )
        
        vertical_label = vertical_brace.get_tex(r"\Delta y").next_to(vertical_brace, RIGHT)
        dy_label = always_redraw(
            lambda: dy_brace.get_tex(r"dy")
        )
        self.play( Write(dy_label) )
        
        self.wait(2.2222)