from manim import *

color_BlueBack = '#2f2e33'
color_CoolGray = '#d5d6d2'
color_White    = '#ffffff'
color_Cobalt   = '#3a5199'
color_Orange   = '#ff8d3f'
color_Charcoal = '#353c3f'
color_Pumpkin  = '#d55448'
color_FadedRed = '#e05858'
color_RubyRed  = '#a01d26'
config.background_color = color_White

class LineToArc(MovingCameraScene):
    def construct(self):
        
        
        grid = NumberPlane(x_range=(-5, 5, 1), y_range=(-5, 5, 1)).set_opacity(0.2222)
        self.play(FadeIn(grid))

        # 创建圆
        circle = Circle(radius=1, color=color_Cobalt, stroke_width=2.2222)
        circle.set_fill(color_Cobalt, opacity=0.8888)
        self.play(FadeIn(circle))

        fuzhuyuan = Circle(radius = 1 + 0.2222) #辅助圆 放数字的

        self.play(
            self.camera.frame.animate.set(width=8.88888888 - 2.2222)
        )

        radius_line = Line( start=ORIGIN, end=np.array([1,0,0]), color=color_Orange )
        radius_line2 = Line( end=ORIGIN, start=np.array([1,0,0]), color=color_Orange )
        self.play( GrowFromPoint(radius_line, ORIGIN) )
        self.wait(0.2222)
        
        tex_r = Tex(r"r=1").set_color(color_BlueBack).next_to(radius_line, UP).scale(0.4444).shift(DOWN*0.2222)
        self.play( Write(tex_r) )
        self.wait(0.8888)
        
        p1 = np.array([1, 0, 0])
        dot_p1 = Dot(p1, color=color_Charcoal).set_stroke(color_BlueBack)
        self.play( Create(dot_p1) )

        # 1--------------------
        # 定义起始点和终点
        
        p2 = circle.point_at_angle(1)
        t1 = np.array([1, 1, 0])
        
        dot_p2 = Dot(p2, color=color_Charcoal).set_stroke(color_BlueBack)

        # 创建弧线
        line1 = Line(p1, t1, color=color_Orange)
        arc1 = ArcBetweenPoints(p1, p2, radius=1, color=color_Orange)

        # 绘制动画
        # self.play(GrowFromPoint(line1, p1))
        _1_ = radius_line.copy()
        self.play( Transform(_1_, line1),  )
        self.wait(0.2222)

        self.play( 
            Succession( 
                Transform(_1_, arc1), Create(dot_p2),
                lag_ratio = 0.8888
            )
        )
        self.wait(0.2222)

        label_acr1 = Tex(r"1", color=color_BlueBack ).scale(0.4444).move_to(fuzhuyuan.point_at_angle(0.5))
        quan1 = Circle(color=color_BlueBack, stroke_width=1.1111).surround(label_acr1)
        self.play(FadeIn(label_acr1), Create(quan1))
        self.wait(0.2222)
        # 1--------------------
        
        # 2--------------------
        t3 = p2 + np.array([-np.cos(1), np.sin(1), 0])  # 沿着切线方向移动
        p3 = circle.point_at_angle(2)
        dot_p3 = Dot(p3, color=color_Charcoal).set_stroke(color_BlueBack)
        
        line2 = Line(p2, t3, color=color_Orange)
        arc2 = ArcBetweenPoints(p2, p3, radius=1, color=color_Orange)

        _2_ = radius_line2.copy()
        self.play( Transform(_2_, line2) )
        # self.play(GrowFromPoint(line2, p2))
        self.wait(0.2222)

        self.play( 
            Succession( 
                Transform(_2_, arc2), Create(dot_p3),
                lag_ratio = 0.8888
            )
        )
        self.wait(0.2222)
        
        label_arc2 = Tex(r"2", color=color_BlueBack).scale(0.4444).move_to(fuzhuyuan.point_at_angle(1.5))
        quan2 = Circle(color=color_BlueBack, stroke_width=1.1111).surround(label_arc2)
        self.play(FadeIn(label_arc2), Create(quan2))
        self.wait(0.2222)
        
        # 2--------------------
        
        # 3--------------------
        theta3 = 2 - np.pi/2
        t4 = p3 + np.array( [-np.cos( theta3 ), -np.sin( theta3 ), 0] )
        p4 = circle.point_at_angle(3)
        dot_p4 = Dot(p4, color=color_Charcoal).set_stroke(color_BlueBack)
        
        line3 = Line(p3, t4, color=color_Orange)
        arc3 = ArcBetweenPoints(p3, p4, radius=1, color=color_Orange)
        
        _3_ = radius_line2.copy()
        self.play( Transform(_3_, line3) )
        # self.play( GrowFromPoint(line3,p3) )
        self.wait(0.2222)
        
        # self.play( Transform(_3_, arc3), Create(dot_p4) )
        self.play(
            Succession( 
                Transform(_3_, arc3), Create(dot_p4),
                lag_ratio = 0.8888
            ) 
        )
        self.wait(0.2222)
        
        label_arc3 = Tex(r"3", color=color_BlueBack).scale(0.4444).move_to(fuzhuyuan.point_at_angle(2.5))
        quan3 = Circle(color=color_BlueBack, stroke_width=1.1111).surround(label_arc3)
        self.play(FadeIn(label_arc3), Create(quan3))
        self.wait(0.2222)
        # 3--------------------
        
        # 4--------------------
        theta4 = np.pi - 3
        t5 = p4 + np.array( [-np.sin(theta4), -np.cos(theta4), 0] )
        p5 = circle.point_at_angle(4)
        dot_p5 = Dot(p5, color=color_Charcoal).set_stroke(color_BlueBack)
        
        line4 = Line(p4, t5, color=color_Orange)
        arc4 = ArcBetweenPoints(p4, p5, radius=1, color=color_Orange)
        
        _4_ = radius_line.copy()
        self.play( Transform(_4_, line4) )
        self.wait(0.2222)
        
        self.play(
            Succession( 
                Transform(_4_, arc4), Create(dot_p5),
                lag_ratio = 0.8888
            ) 
        )
        self.wait(0.2222)
        
        label_arc4 = Tex(r"4", color=color_BlueBack).scale(0.4444).move_to(fuzhuyuan.point_at_angle(3.5))
        quan4 = Circle(color=color_BlueBack, stroke_width=1.1111).surround(label_arc4)
        self.play(FadeIn(label_arc4), Create(quan4))
        self.wait(0.2222)
        # 4--------------------
        
        # 5--------------------
        theta5 = 3/2*np.pi - 4
        t6 = p5 + np.array( [np.cos(theta5), -np.sin(theta5), 0] )
        p6 = circle.point_at_angle(5)
        dot_p6 = Dot(p6, color=color_Charcoal).set_stroke(color_BlueBack)
        
        line5 = Line(p5, t6, color=color_Orange)
        arc5 = ArcBetweenPoints(p5, p6, radius=1, color=color_Orange)
        
        _5_ = radius_line.copy()
        self.play( Transform(_5_, line5) )
        self.wait(0.2222)
        
        self.play(
            Succession( 
                Transform(_5_, arc5), Create(dot_p6),
                lag_ratio = 0.8888
            ) 
        )
        self.wait(0.2222)
        
        label_arc5 = Tex(r"5", color=color_BlueBack).scale(0.4444).move_to(fuzhuyuan.point_at_angle(4.5))
        quan5 = Circle(color=color_BlueBack, stroke_width=1.1111).surround(label_arc5)
        self.play(FadeIn(label_arc5), Create(quan5))
        self.wait(0.2222)
        # 5--------------------
         
        # 6--------------------
        theta6 = np.pi/2 - 1
        p7 = circle.point_at_angle(-1)
        p8 = p1
        t8 = p7 + np.array( [np.cos(theta6), np.sin(theta6), 0] )
        t9 = p8 + np.array( [0, -1, 0] )
        dot_p7 = Dot(p7, color=color_Charcoal).set_stroke(color_BlueBack)
        
        line6 = Line(t9, p8, color=color_Orange)
        arc6 = ArcBetweenPoints(p7, p8, radius=1, color=color_Orange)
        
        _6_ = radius_line.copy()
        self.play( Transform(_6_, line6) )
        self.wait(0.2222)
        
        self.play(
            Succession( 
                Transform(_6_, arc6), Create(dot_p7),
                lag_ratio = 0.8888
            ) 
        )
        # self.play( GrowFromPoint(line6, p7) )
        self.wait(0.2222)
        
        label_acr6 = Tex(r"6", color=color_BlueBack).scale(0.4444).move_to(fuzhuyuan.point_at_angle(-0.5))
        quan6 = Circle(color=color_BlueBack, stroke_width=1.1111).surround(label_acr6)
        self.play( FadeIn(label_acr6), Create(quan6) )
        self.wait(0.2222)
        # 6--------------------
        
        # 0.28-------------------
        self.play(
            self.camera.frame.animate.set(width=2.2222).shift( DOWN*0.8888 + RIGHT*0.4444 )
        )
        
        end_028 = circle.point_at_angle( -1.1111 ) + np.array( [0.0202, -0.0404, 0] )
        start_028 = end_028 + np.array( [0.2222, -0.4444, 0.0000] )
        arrow_028 = Arrow( start_028, end_028, color=color_Pumpkin )
        
        arc_028 = ArcBetweenPoints(p6, p7, radius=1, color = color_RubyRed, stroke_width = 2.2222)
        self.play( Create(arc_028) )  
        
        arrow_028.shift( RIGHT*0.2222 + DOWN*0.4444 )
        self.play(
            FadeIn(arrow_028),
            arrow_028.animate.shift(LEFT * 0.2222 + UP * 0.4444),
        )
        for i in range (2):
            self.play( Flash(arc_028, color=color_FadedRed, line_stroke_width = 0.4444+0.2222 ) )
            self.wait(0.2222)
        
        self.play(
            self.camera.frame.animate.set(width=8.8888-2.2222).shift( UP*0.8888 + LEFT*0.4444 )
        )
        
        label_028 = Tex(r"$\mathbf{0.28}$").set_color( color_Pumpkin )
        label_028.next_to( arrow_028, RIGHT ).shift(LEFT*0.2222)
        self.play( Write(label_028), run_time = 2.2222 )
        
        for i in range(4): 
            self.play( Flash(arc_028, color=color_FadedRed, rate_func = rush_from, line_length=0.2222, line_stroke_width=0.88888888 ), run_time = 0.8888 )
            self.wait(0.2222)
        # 0.28-------------------
        
        self.play(
            self.camera.frame.animate.set(width=8.8888 - 0.8888).shift( RIGHT*0.4444 ),
            Flash(arc_028, color=color_FadedRed, rate_func = rush_from, line_length=0.2222, line_stroke_width=0.88888888 ) 
        )
        
        tex_cc = Tex(r"$ 2 \pi \approx 6.28 $").next_to(circle, RIGHT*2.2222).set_color( color_Pumpkin )
        self.play( Write(tex_cc), run_time = 2.2222 )
        
        for i in range(8): 
            self.play( Flash(arc_028, color=color_FadedRed, rate_func = rush_from, line_length=0.2222, line_stroke_width=0.88888888 ), run_time = 0.8888 )
            self.wait(0.2222)
        
        self.wait(2.2222)