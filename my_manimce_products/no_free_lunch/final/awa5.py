from manim import *
# manim -pql awa5.py --disable_caching

class MatrixExample(MovingCameraScene):
    def construct(self):
        matrix_a = Matrix(
            [
                ["2", "0.5", "0", "...", "0", "0", "0.5"], 
                ["0.5", "2", "0.5", "...", "0", "0", "0"],
                ["...", "...", "...", "...", "...", "...", "..." ],
                ["...", "...", "...", "...", "...", "...", "..." ],
                ["...", "...", "...", "...", "...", "...", "..." ],
                ["0", "0", "0", "...", "0.5", "2", "0.5"],
                ["0.5", "0", "0", "...", "0", "0.5", "2"]
            ]
        )
        matrix_a.to_edge(LEFT)
        
        matrix_b = Matrix(
            [
                ["x_{1}"],
                ["x_{2}"],
                ["x_{3}"],
                ["..."],
                ["..."],
                ["..."],
                ["x_{n}"],
            ]
        )
        
        matrix_c = Matrix(
            [
                ["p_{1}"],
                ["p_{2}"],
                ["p_{3}"],
                ["..."],
                ["..."],
                ["..."],
                ["p_{n}"],
            ]
        )
        
        self.play(
            self.camera.frame.animate.shift( UP*8.88888888 )
        )
        
        vector_p = Matrix([[ "p_1,", "p_2,", "p_3,", "...,", "p_{_{n-2}},", "p_{_{n-1}},", "p_n", ], ], left_bracket="[", right_bracket="]").next_to( matrix_a, UP*8.88888888 ).shift( RIGHT*2.2222 + UP*4.4444 )
        vector_c = Matrix([[ "c_1,", "c_2,", "c_3,", "...,", "c_{_{n-2}},", "c_{_{n-1}},", "c_n", ], ], left_bracket="[", right_bracket="]").next_to(vector_p, DOWN * 2.2222)
        label_p = Tex(r"p = ").next_to( vector_p, LEFT )
        label_c = Tex(r"c = ").next_to( vector_c, LEFT )
        self.play(Write(label_p))
        self.play(Write(vector_p))
        self.play(Write(label_c)) 
        self.play(Write(vector_c))
        
        def point_from_to(a, b):
            line = Line(a, b)
            return line
        
        entries_p = vector_p.get_entries()
        entries_c = vector_c.get_entries()
        
        def draw3( idx, time1, time2 ): 
            x = (idx-1) % 7
            y = idx % 7
            z = (idx+1)%7

            line1 = point_from_to(entries_p[idx].get_center(), entries_c[x].get_center()).set_color( RED_A )
            line2 = point_from_to(entries_p[idx].get_center(), entries_c[y].get_center()).set_color( BLUE_A )
            line3 = point_from_to(entries_p[idx].get_center(), entries_c[z].get_center()).set_color( RED_A )
            
            line1_label = Tex(r"0.5").move_to(line1).set_color( RED_C ).scale(0.4444)
            line2_label = Tex(r"2").move_to(line2).set_color( BLUE_C ).scale(0.4444)
            line3_label = Tex(r"0.5").move_to(line3).set_color( RED_C ).scale(0.4444)
            
            self.play( 
                Create(line1),
                Create(line2),
                Create(line3),
                run_time = time1
            )
            self.play( Write(line1_label), run_time=time2 )
            self.play( Write(line2_label), run_time=time2 )
            self.play( Write(line3_label), run_time=time2 )
            
            self.wait( time2 )
            self.play(
                FadeOut(line1),
                FadeOut(line2),
                FadeOut(line3),
                FadeOut(line1_label),
                FadeOut(line2_label),
                FadeOut(line3_label),
                run_time = time2
            )
        
        draw3(0, 0.8888, 0.2222)
        draw3(1, 0.8888, 0.2222)
        draw3(2, 0.0808, 0.0101)
        draw3(3, 0.0808, 0.0101)
        draw3(4, 0.0808, 0.0101)
        draw3(5, 0.0808, 0.0101)
        draw3(6, 0.8888, 0.2222)

        self.wait( 0.4444 )
        self.play(
            self.camera.frame.animate.shift( DOWN*4.4444 )
        )
        
        equations = [
            MathTex(r"p_1 = 2c_1 + 0.5c_n + 0.5c_2"),
            MathTex(r"p_2 = 2c_2 + 0.5c_1 + 0.5c_3"),
            MathTex(r"\quad \quad......"),
            MathTex(r"p_{n-1} = 2c_{n-1} + 0.5c_{n-2} + 0.5c_n"),
            MathTex(r"p_n = 2c_n + 0.5c_{n-1} + 0.5c_1"),
        ]  
        
        group_equations = VGroup( *equations )
        group_equations.arrange( DOWN, aligned_edge = LEFT, buff = 0.2222 )
        group_equations.next_to( vector_c, DOWN*4.4444 )
        
        for i in range( len(equations) ):
            e = equations[i]
            self.play( Write(e), rum_time = 0.8888 - 0.1111*i )
        
        equations_brace = Brace(group_equations, LEFT, buff=SMALL_BUFF)
        self.play( Create(equations_brace) )
        
        self.play( self.camera.frame.animate.shift( DOWN*4.4444 ).set(width = 18.8888 ) )
        # 定义矩阵   
        
        # 调整矩阵A的位置和大小
        matrix_a.scale(0.8)
        self.play(Write(matrix_a))
        
        # 调整矩阵B的位置和大小
        matrix_b.next_to(matrix_a, RIGHT, buff=0.2)
        matrix_b.scale(0.8)
        self.play(Write(matrix_b))
        
        # 在矩阵B的右侧放置等号符号
        equal_sign = MathTex("=")
        equal_sign.next_to(matrix_b, RIGHT, buff=0.2)
        self.play(Write(equal_sign))
        
        # 在等号符号的右侧放置矩阵C
        matrix_c.next_to(equal_sign, RIGHT, buff=0.2)
        matrix_c.scale(0.8)
        self.play(Write(matrix_c))
        
        # 添加矩阵A的标识
        matrix_rect_a = SurroundingRectangle(matrix_a, color=RED, buff=SMALL_BUFF)
        self.play(Create(matrix_rect_a))
        matrix_label_a = Text("A", font_size=24)
        matrix_label_a.next_to(matrix_a, DOWN)
        self.play(FadeIn(matrix_label_a))
                
        # 显示主对角线
        top_left = matrix_a.get_corner(UL)
        bottom_right = matrix_a.get_corner(DR)
        diagonal_line = Line(top_left, bottom_right, color=YELLOW)
        diagonal_line.set_stroke(width=4, opacity=0.8)
        self.play(Create(diagonal_line))
        
        # 添加矩阵B的标识
        matrix_rect_b = SurroundingRectangle(matrix_b, color=RED, buff=SMALL_BUFF)
        self.play(Create(matrix_rect_b))
        matrix_label_b = Text("X", font_size=24)
        matrix_label_b.next_to(matrix_b, DOWN)
        self.play(FadeIn(matrix_label_b))
        
        # 添加矩阵C的标识
        matrix_rect_c = SurroundingRectangle(matrix_c, color=RED, buff=SMALL_BUFF)
        self.play(Create(matrix_rect_c))
        matrix_label_c = Text("P", font_size=24)
        matrix_label_c.next_to(matrix_c, DOWN)
        self.play(FadeIn(matrix_label_c))
        
        eq = MathTex("   AX = P")
        eq.move_to( DOWN*3.5 )
        self.play(Write(eq))
        
        self.wait(3)

        group1 = VGroup(matrix_b, matrix_rect_b, matrix_label_b, matrix_c, matrix_rect_c, matrix_label_c, equal_sign, diagonal_line, eq )
        self.play(FadeOut(group1))

        self.wait(1)
        
        group2 = VGroup( matrix_rect_a, matrix_label_a )
        self.play(FadeOut(group2))
        
        self.wait(1)
        
        # 获取矩阵的宽度和高度
        matrix_width = matrix_a.get_width()
        matrix_height = matrix_a.get_height()

        # 获取矩阵左上角的坐标
        top_left = matrix_a.get_corner(UL)

        # 计算矩形宽度和高度
        rect_width1 = 6 / 7 * matrix_width - 0.16
        rect_height1 = 6 / 7 * matrix_height - 0.09
        
        rect_width2 = 1 / 7 * matrix_width - 0.16
        rect_height2 = 1 / 7 * matrix_height - 0.09

        # 计算矩形中心位置
        rect_center_11 = top_left + np.array([3 / 7 * matrix_width, -3 / 7 * matrix_height, 0])
        # 创建矩形
        rect11 = Rectangle(width=rect_width1, height=rect_height1, 
                         fill_opacity=0.2, fill_color='#66CCFF',
                         stroke_width=2, stroke_color='#00BFFF' )
        rect11.move_to(rect_center_11)
        self.play(Create(rect11))

        matrix_label_a11 = Tex("$B$", font_size = 48)
        matrix_label_a11.next_to(rect11, UP)
        self.play(FadeIn(matrix_label_a11))

        rect_center_17 = top_left + np.array([6.5 / 7 * matrix_width, -3 / 7 * matrix_height, 0])
        
        rect17 = Rectangle(width=rect_width2, height=rect_height1, 
                         fill_opacity=0.2, fill_color='#66CCFF',
                         stroke_width=2, stroke_color='#00BFFF' )
        rect17.move_to(rect_center_17)
        self.play(Create(rect17))

        matrix_label_a17 = Tex("$C$", font_size = 48)
        matrix_label_a17.next_to(rect17, UP)
        self.play(FadeIn(matrix_label_a17))

        rect_center_71 = top_left + np.array([3 / 7 * matrix_width, -6.5 / 7 * matrix_height, 0])
        # 创建矩形
        rect71 = Rectangle(width=rect_width1, height=rect_height2, 
                         fill_opacity=0.2, fill_color='#66CCFF',
                         stroke_width=2, stroke_color='#00BFFF' )
        rect71.move_to(rect_center_71)
        self.play(Create(rect71))

        matrix_label_a71 = Tex("$C^{T}$", font_size = 48)
        matrix_label_a71.next_to(rect71, DOWN)
        self.play(FadeIn(matrix_label_a71))
        
        rect_center_77 = top_left + np.array([6.5 / 7 * matrix_width, -6.5 / 7 * matrix_height, 0])
        # 创建矩形
        rect77 = Rectangle(width=rect_width2, height=rect_height2, 
                         fill_opacity=0.2, fill_color='#66CCFF',
                         stroke_width=2, stroke_color='#00BFFF' )
        rect77.move_to(rect_center_77)
        self.play(Create(rect77))
        
        # self.play(Write(matrix_b))
            
        top_left_b = matrix_b.get_corner(UL)
        
        rect_center_b1 = top_left_b + np.array([0.5 / 7 * matrix_width, -3 / 7 * matrix_height, 0])
        # 创建矩形
        rectb1 = Rectangle(width=rect_width2, height=rect_height1, 
                         fill_opacity=0.2, fill_color='#66CCFF',
                         stroke_width=2, stroke_color='#00BFFF' )
        rectb1.move_to(rect_center_b1)
        # self.play(Create(rectb1))
        
        rect_center_b7 = top_left_b + np.array([0.5 / 7 * matrix_width, -6.5 / 7 * matrix_height, 0])
        # 创建矩形
        rectb7 = Rectangle(width=rect_width2, height=rect_height2, 
                         fill_opacity=0.2, fill_color='#66CCFF',
                         stroke_width=2, stroke_color='#00BFFF' )
        rectb7.move_to(rect_center_b7)
        # self.play(Create(rectb7))

        self.play(
            Write(matrix_b),
            Create(rectb1)
        )
        self.play( Create(rectb7) )

        top_left_p = matrix_c.get_corner(UL)

        rect_center_p1 = top_left_p + np.array([0.5 / 7 * matrix_width, -3 / 7 * matrix_height, 0])
        # 创建矩形
        rectp1 = Rectangle(width=rect_width2, height=rect_height1, 
                         fill_opacity=0.2, fill_color='#66CCFF',
                         stroke_width=2, stroke_color='#00BFFF' )
        rectp1.move_to(rect_center_p1)
        # self.play(Create(rectb1))
        
        rect_center_p7 = top_left_p + np.array([0.5 / 7 * matrix_width, -6.5 / 7 * matrix_height, 0])
        # 创建矩形
        rectp7 = Rectangle(width=rect_width2, height=rect_height2, 
                         fill_opacity=0.2, fill_color='#66CCFF',
                         stroke_width=2, stroke_color='#00BFFF' )
        rectp7.move_to(rect_center_p7)
        # self.play(Create(rectb7))

        self.play(Write(equal_sign))
        self.play(
            Write(matrix_c),
            Create(rectp1)
        )
        self.play( Create(rectp7) )

        group = VGroup( equal_sign, matrix_c, rectp1, rectp7)
        # self.play(FadeOut(group))
        
        group_ayuan = VGroup(matrix_a, rect11, rect17, rect71, rect77, matrix_label_a11, matrix_label_a17, matrix_label_a71 )
        matrix_akuai = Matrix(
            [
                ["B","C"],
                ["C^{T}","2"]
            ]
        )
        matrix_akuai.shift( LEFT*0.8 )
        
        # self.play(Transform(group_ayuan, matrix_akuai))
        
        matrix_x1 = Matrix(
            [
                ["x_{1}"],
                ["x_{2}"],
                ["..."],
                ["x_{_{n-1}}"],
            ],
            bracket_h_buff = 0.10,
        )
        
        matrix_x2 = Matrix(
            [
                ["x_{n}"]
            ],
            bracket_h_buff = 0.36,
        )
        
        matrix_xkuai = MobjectMatrix(
            [
                [matrix_x1], 
                [matrix_x2]
            ],
            h_buff = 1.5
        )
        matrix_xkuai.next_to(matrix_akuai, RIGHT)
        
        group_byuan = VGroup(matrix_b, rectb1, rectb7 )
        
        # self.play(Transform(group_byuan, matrix_xkuai))
        self.play(
            Transform(group_ayuan, matrix_akuai),
            Transform(group_byuan, matrix_xkuai)
        )
        self.wait(0.4444)
        
        matrix_p1 = Matrix(
            [
                ["p_{1}"],
                ["p_{2}"],
                ["..."],
                ["p_{_{n-1}}"],
            ],
            bracket_h_buff = 0.10,
        )
        
        matrix_p2 = Matrix(
            [
                ["p_{n}"]
            ],
            bracket_h_buff = 0.36,
        )
        
        matrix_pkuai = MobjectMatrix(
            [
                [matrix_p1], 
                [matrix_p2]
            ],
            h_buff = 1.5
        )
        matrix_pkuai.next_to(equal_sign, RIGHT)
        
        group_cyuan = VGroup(matrix_c, rectp1, rectp7 )
        
        self.play(Transform(group_cyuan, matrix_pkuai))
        self.wait(0.8888)
        
        # matrix_x1_qwq1 = Matrix(
        #     [
        #         ["x_{1}"],
        #         ["x_{2}"],
        #         ["..."],
        #         ["x_{_{n-1}}"],
        #     ],
        #     bracket_h_buff = 0.10,
        # )
        
        # matrix_x1_qwq2 = Matrix(
        #     [
        #         ["x_{1}"],
        #         ["x_{2}"],
        #         ["..."],
        #         ["x_{_{n-1}}"],
        #     ],
        #     bracket_h_buff = 0.10,
        # )
        
        x1_text = MathTex(r"\begin{pmatrix} x\textsubscript{1} \\ x\textsubscript{2} \\ \vdots \\ x\textsubscript{n-1} \end{pmatrix}", font_size=20)
        x1_text2 = MathTex(r"\begin{pmatrix} x\textsubscript{1} \\ x\textsubscript{2} \\ \vdots \\ x\textsubscript{n-1} \end{pmatrix}", font_size=20)
        
        matrix_ab = MobjectMatrix(
            [
                [MathTex("B"),x1_text,MathTex("+"),MathTex("Cx_{n}")],
                [MathTex("C^{T}"),x1_text2,MathTex("+"),MathTex("2x_{n}")],
            ],
            v_buff = 2.4
        )

        # matrix_ab.move_to(equal_sign, LEFT)
        group_a_b = VGroup(group_ayuan, group_byuan)
        
        self.play(
            Transform(group_a_b, matrix_ab),
            # Write(matrix_ab)
        )
        self.wait(0.4444)

        p1_text = MathTex(r"\begin{pmatrix} p\textsubscript{1} \\ p\textsubscript{2} \\ \vdots \\ p\textsubscript{n-1} \end{pmatrix}", font_size=20)
        matrix_pp = MobjectMatrix(
            [
                [p1_text],
                [MathTex("p_{n}")],
            ],
            v_buff = 2.4
        )
        matrix_pp.next_to(equal_sign, RIGHT)
        
        self.play(
            Transform(group_cyuan, matrix_pp)
        )
        self.wait(0.8888)

        matrix_width_ab = matrix_ab.get_width()
        matrix_height_ab = matrix_ab.get_height()

        # 获取矩阵左上角的坐标
        top_left_ab = matrix_ab.get_corner(UL)

        # 计算矩形宽度和高度
        rect_width_ab = 1 / 1 * matrix_width_ab - 0.16
        rect_height_ab = 1 / 2 * matrix_height_ab - 0.09

        # 计算矩形中心位置
        rect_center_ab = top_left_ab + np.array([1 / 2 * matrix_width_ab, -1 / 4 * matrix_height_ab, 0])
        # 创建矩形
        rect_ab = Rectangle(width=rect_width_ab, height=rect_height_ab, 
                         fill_opacity=0.1, fill_color='#FFFF00',
                         stroke_width=2, stroke_color='#FFD700' )
        rect_ab.move_to(rect_center_ab)
        self.play(Create(rect_ab))
        
        matrix_width_pp = matrix_pp.get_width()
        matrix_height_pp = matrix_pp.get_height()

        # 获取矩阵左上角的坐标
        top_left_pp = matrix_pp.get_corner(UL)

        # 计算矩形宽度和高度
        rect_width_pp = 1 / 1 * matrix_width_pp - 0.16
        rect_height_pp = 1 / 2 * matrix_height_pp - 0.09

        # 计算矩形中心位置
        rect_center_pp = top_left_pp + np.array([1 / 2 * matrix_width_pp, -1 / 4 * matrix_height_pp, 0])
        # 创建矩形
        rect_pp = Rectangle(width=rect_width_pp, height=rect_height_pp, 
                         fill_opacity=0.1, fill_color='#FFFF00',
                         stroke_width=2, stroke_color='#FFD700' )
        rect_pp.move_to(rect_center_pp)
        self.play(Create(rect_pp))
        
        group_2mx = VGroup( group_a_b, group_cyuan, equal_sign, rect_ab, rect_pp )
        
        self.wait(0.8888)
        # group_shifted = group.copy().shift(UP)  # 拷贝一份group并上移一个单位长度
        # self.play(group_2mx.animate.shift(UP*1.5), run_time=1)
        self.play(self.camera.frame.animate.shift(DOWN*1.5) )
        
        note_text = Tex(r"note that we have n unknowns,").next_to(group_2mx, DOWN)
        so_we_can = Tex(r"so we can express ").next_to(note_text, DOWN)
        so_we_can.shift(LEFT*4.44)
        x123_n_1 = MathTex(r"x_1, x_2, \ldots, x_{n-1}").next_to(so_we_can, RIGHT)
        linearly_in_terms_of = Tex(r" linearly in terms of ").next_to(x123_n_1, RIGHT)
        x_n = MathTex(r"x_n").next_to(linearly_in_terms_of, RIGHT)
        group_note = VGroup(note_text,so_we_can,x123_n_1,linearly_in_terms_of,x_n).next_to(group_2mx, DOWN)
        group_note.shift( LEFT * 1.88 )
        self.play(FadeIn(group_note))
        self.wait(0.8888)
        
        text_assume = Tex(r"Let's assume that   ")
        text_assume_xin = MathTex(r"x_i = u_ix_n + v_i,\quad (i=1,2,3,\ldots,n-1)").next_to(text_assume, RIGHT)
        group_assume = VGroup( text_assume, text_assume_xin )
        group_assume.next_to( group_note, DOWN )
        self.play(FadeIn(group_assume))
        self.wait(0.8888)
        
        self.play(self.camera.frame.animate.shift(DOWN*5.55) )
        
        text_assume_ie = Tex(r"i.e.,  ")
        text_assume_x1 = MathTex(r"x_1 = u_1x_n + v_1").next_to(text_assume_ie, RIGHT)
        text_assume_x2 = MathTex(r"x_2 = u_2x_n + v_2").next_to(text_assume_x1, DOWN)
        text_assume_xdot = MathTex(r"\ldots\ldots\ldots").next_to(text_assume_x2, DOWN)
        text_assume_xn_1 = MathTex(r" x_{n-1} = u_{n-1}x_n + v_{n-1}").next_to(text_assume_xdot, DOWN)
        group_xxx = VGroup( text_assume_ie, text_assume_x1, text_assume_x2, text_assume_xdot, text_assume_xn_1 ).next_to(group_assume, DOWN)
        self.play(FadeIn(group_xxx))
        self.wait(0.8888)
        
        sooo = MathTex(r"so: ")
        xlie = MathTex(r"\begin{pmatrix} x\textsubscript{1} \\ x\textsubscript{2} \\ \vdots \\ x\textsubscript{n-1} \end{pmatrix}", font_size=36).next_to(sooo, RIGHT)
        dengyu = MathTex(r" = ", font_size=36).next_to(xlie, RIGHT)
        ulie = MathTex(r"\begin{pmatrix} u\textsubscript{1} \\ u\textsubscript{2} \\ \vdots \\ u\textsubscript{n-1} \end{pmatrix}", font_size=36).next_to(dengyu, RIGHT)
        shuchengxn_jia = MathTex(r"x_n + ").next_to(ulie, RIGHT)
        vlie = MathTex(r"\begin{pmatrix} v\textsubscript{1} \\ v\textsubscript{2} \\ \vdots \\ v\textsubscript{n-1} \end{pmatrix}", font_size=36).next_to(shuchengxn_jia,RIGHT)
        group_sooo = VGroup(sooo,xlie,dengyu,ulie,shuchengxn_jia,vlie).next_to(group_xxx, DOWN*1.1)
        self.play(FadeIn(group_sooo))
        self.wait(0.8888)
        
        # self.play(group_sooo.animate.shift(UP*5.5), runtime = 1.5)
        self.play(self.camera.frame.animate.shift(DOWN*3.33) )
        
        and_since = MathTex(r"and \quad hence: \quad B")
        xlielie = MathTex(r"\begin{pmatrix} x\textsubscript{1} \\ x\textsubscript{2} \\ \vdots \\ x\textsubscript{n-1} \end{pmatrix}", font_size=36).next_to(and_since, RIGHT)
        jia_cxn = MathTex(r" + \quad Cx_n = ").next_to(xlielie, RIGHT)
        plielie = MathTex(r"\begin{pmatrix} p\textsubscript{1} \\ p\textsubscript{2} \\ \vdots \\ p\textsubscript{n-1} \end{pmatrix}", font_size=36).next_to(jia_cxn,RIGHT)
        # text_assume_so = MathTex( "so: ", x1_text, " = x_n", u1_text, " + ", v1_text ).next_to(group_heti, DOWN)
        # self.play(FadeIn(text_assume_so))
        group_and_since = VGroup(and_since,xlielie,jia_cxn,plielie).next_to(group_sooo, DOWN)
        self.play(FadeIn(group_and_since))
        self.wait(0.8888)
        
        then_dai = Tex(r"then substitude: \quad B(")
        yaodairude = VGroup(ulie,shuchengxn_jia,vlie).copy()
        yaodairude.next_to(then_dai, RIGHT)
        jia_cxn2 = MathTex(r") + \quad Cx_n = \quad ").next_to(yaodairude, RIGHT)
        plielie2 = MathTex(r"\begin{pmatrix} p\textsubscript{1} \\ p\textsubscript{2} \\ \vdots \\ p\textsubscript{n-1} \end{pmatrix}", font_size=36).next_to(jia_cxn2,RIGHT)
        # text_assume_so = MathTex( "so: ", x1_text, " = x_n", u1_text, " + ", v1_text ).next_to(group_heti, DOWN)
        # self.play(FadeIn(text_assume_so))
        group_then_dai = VGroup(then_dai,yaodairude,jia_cxn2,plielie2).next_to(and_since, DOWN)
        group_then_dai.shift( DOWN * 0.88 + RIGHT * 2.88 )
        self.play(FadeIn(group_then_dai))
        self.wait(0.8888)
        
        and_ie = MathTex(r"i.e.: \quad B ")
        ulielie = ulie.copy()
        ulielie.next_to(and_ie, RIGHT)
        xn_jia_b = MathTex(r"x_n \quad + \quad B").next_to(ulielie, RIGHT)
        vlielie = vlie.copy()
        vlielie.next_to(xn_jia_b, RIGHT)
        jia_cxn_dengyu = MathTex(r"\quad + \quad Cx_n \quad = \quad ").next_to(vlielie, RIGHT*1.11)
        plielielie = plielie.copy()
        plielielie.next_to(jia_cxn_dengyu, RIGHT*1.11)
        
        group_and_ie = VGroup(and_ie,ulielie,xn_jia_b,vlielie,jia_cxn_dengyu,plielielie).next_to(group_then_dai, DOWN)
        # group_and_ie.shift( DOWN * 0.88 + RIGHT * 2.88 )
        
        self.play(self.camera.frame.animate.shift(DOWN*4.44) )
        self.wait(0.8888)
        self.play(FadeIn(group_and_ie))
        
        and_u_youxuanji = Tex(r"and what's more, when we consider u and v, we let:")
        bv_xuanji = MathTex(r"B").next_to(and_u_youxuanji, DOWN)
        bv_xuanji.shift(DOWN*0.88 + LEFT*2.88)
        vlielielie = vlielie.copy().next_to(bv_xuanji, RIGHT)
        dengyu_p = MathTex(r"\quad = \quad").next_to(vlielielie, RIGHT)
        p_xuanji = MathTex(r"\begin{pmatrix} p\textsubscript{1} \\ p\textsubscript{2} \\ \vdots \\ p\textsubscript{n-1} \end{pmatrix}", font_size=36).next_to(dengyu_p,RIGHT)
        andandand = Tex(r"and").next_to(dengyu_p, DOWN)
        andandand.shift(DOWN * 0.88 )
        bujiac_xuanji = MathTex(r"B").next_to(andandand, DOWN)
        bujiac_xuanji.shift( DOWN*0.88 + LEFT * 2.88 )
        ulielielie = ulielie.copy().next_to(bujiac_xuanji, RIGHT)
        jiac_dengyu_0 = MathTex(r"\quad + \quad C \quad = \quad 0").next_to(ulielielie, RIGHT)
        
        group_youxuanji = VGroup(bv_xuanji,vlielielie,dengyu_p,p_xuanji,andandand,bujiac_xuanji,ulielielie,jiac_dengyu_0).next_to(group_and_ie, DOWN)
        # group_youxuanji.shift( DOWN * 0.88, RIGHT * 2.88 )
        
        self.play(self.camera.frame.animate.shift(DOWN*3.45) )
        self.play( FadeIn(and_u_youxuanji) )
        self.play(FadeIn(group_youxuanji))
        
        # self.play(self.camera.frame.animate.set(width=36))
        
        then_tran = Tex(r"Then we transform the original problem into solving these two equations").next_to(group_youxuanji, DOWN*1.1)
        coffi_mx = Tex(r"whose cofficient matrices are both tridiagonal:").next_to(then_tran, DOWN)
        
        self.play(
            self.camera.frame.animate.shift( DOWN ),
            self.camera.frame.animate.set(width=20),
            FadeIn(then_tran),
            FadeIn(coffi_mx),
        )
        
        # self.play(self.camera.frame.animate.scale(0.8))
        
        matrix_bb = Matrix(
            [
                ["2", "0.5", "0", "...", "0", "0", "0"], 
                ["0.5", "2", "0.5", "...", "0", "0", "0"],
                ["...", "...", "...", "...", "...", "...", "..." ],
                ["...", "...", "0.5", "2", "0.5", "...", "..." ],
                ["...", "...", "...", "...", "...", "...", "..." ],
                ["0", "0", "0", "...", "0.5", "2", "0.5"],
                ["0", "0", "0", "...", "0", "0.5", "2"]
            ],
            h_buff=0.8
        )
        
        matrix_uu = Matrix(
            [
                ["u_1"],
                ["u_2"],
                ["u_3"],
                ["..."],
                ["..."],
                ["..."],
                ["u_{n-1}"],
            ],
            h_buff=0.8,
            bracket_h_buff=0.02
        ).next_to(matrix_bb, RIGHT)
        
        equal_uu = Tex(r"=").next_to(matrix_uu, RIGHT)
        
        matrix_cc = Matrix(
            [
                ["-0.5"],
                ["0"],
                ["0"],
                ["..."],
                ["..."],
                ["0"],
                ["-0.5"],
            ],
            h_buff=0.8,
            bracket_h_buff=0.02
        ).next_to(equal_uu, RIGHT)
        
        equation_uu = VGroup(matrix_bb,matrix_uu,equal_uu,matrix_cc).next_to(and_u_youxuanji, DOWN)
        equation_uu.scale(0.88)
        equation_uu.shift(UP*1.11)
        equation_vv_yuan = VGroup(bv_xuanji,vlielielie,dengyu_p)
        
        # self.play(Transform(equation_uu_yuan, equation_uu))
        
        matrix_bbbb = Matrix(
            [
                ["2", "0.5", "0", "...", "0", "0", "0"], 
                ["0.5", "2", "0.5", "...", "0", "0", "0"],
                ["...", "...", "...", "...", "...", "...", "..." ],
                ["...", "...", "0.5", "2", "0.5", "...", "..." ],
                ["...", "...", "...", "...", "...", "...", "..." ],
                ["0", "0", "0", "...", "0.5", "2", "0.5"],
                ["0", "0", "0", "...", "0", "0.5", "2"]
            ],
            h_buff=0.8
        )
        
        matrix_vv = Matrix(
            [
                ["v_1"],
                ["v_2"],
                ["v_3"],
                ["..."],
                ["..."],
                ["..."],
                ["v_{n-1}"],
            ],
            h_buff=0.8,
            bracket_h_buff=0.02
        ).next_to(matrix_bbbb, RIGHT)
        
        equal_vv = Tex(r"=").next_to(matrix_vv, RIGHT)
        
        matrix_pp = Matrix(
            [
                ["p_1"],
                ["p_2"],
                ["p_3"],
                ["..."],
                ["..."],
                ["..."],
                ["p_{n-1}"],
            ],
            h_buff=0.8,
            bracket_h_buff=0.02
        ).next_to(equal_vv, RIGHT)
        
        equation_vv = VGroup(matrix_bbbb,matrix_vv,equal_vv,matrix_pp).next_to(andandand, DOWN)
        equation_vv.scale(0.88)
        # equation_vv.shift(UP*1.66)
        equation_uu_yuan = VGroup(bujiac_xuanji,ulielielie,jiac_dengyu_0)
        
        u_and_v = Tex(r"and").next_to(equation_uu, RIGHT)
        equation_vv.next_to(u_and_v, RIGHT)
        
        group_uv_yuan = VGroup(equation_vv_yuan, equation_uu_yuan, andandand )
        uv = VGroup(equation_uu, equation_vv, u_and_v).next_to(and_u_youxuanji,DOWN )
        uv.shift( RIGHT * 0.69 )
        
        self.play(
            # Transform(equation_vv_yuan, equation_uu),
            # Transform(equation_uu_yuan, equation_vv),
            # self.camera.frame.animate.set(width=24),
            Transform(group_uv_yuan, uv)
        )
        
        so_far = MathTex(r"we \quad went \quad so \quad far").next_to(uv, RIGHT * 16.666666 )
        so_far.shift( UP * 3.666666 )
        so_far.shift( DOWN * 1.23456 )
        now_have = MathTex(r"now \quad we \quad have \quad these: ").next_to(so_far, DOWN)
        
        self.play(
            FadeIn(so_far),
            FadeIn(now_have),
            self.camera.frame.animate.move_to(now_have).set(width = now_have.width*1.2)
        )
        
        self.play(
            self.camera.frame.animate.set( width = 36 ),
            # self.camera.frame.animate.shift( UP*26.66 ),
            # self.camera.frame.animate.set(width = 36.66 ),
            self.camera.frame.animate.move_to(and_since).set(width = 44.44),
            run_time = 1.66
        )
        
        # text_assume_ie = Tex(r"i.e.,  ")
        text_assume_x1_ = MathTex(r"x_1 = u_1x_n + v_1").next_to(text_assume_ie, RIGHT)
        text_assume_x2_ = MathTex(r"x_2 = u_2x_n + v_2").next_to(text_assume_x1, DOWN)
        text_assume_xdot_ = MathTex(r"\ldots\ldots\ldots").next_to(text_assume_x2, DOWN)
        text_assume_xn_1_ = MathTex(r" x_{n-1} = u_{n-1}x_n + v_{n-1}").next_to(text_assume_xdot, DOWN)
        group_xxxxxx = VGroup( text_assume_x1_, text_assume_x2_, text_assume_xdot_, text_assume_xn_1_ )

        # group_xxxxxx = group_xxx.copy()
        group_xxxxxx.next_to(now_have, DOWN*1.6)
        
        andandand_andandand = Tex(r"and").next_to(group_xxxxxx, DOWN*1.6)
        
        self.play(
            FadeIn(group_xxxxxx),
            self.camera.frame.animate.move_to(andandand_andandand).set(width = 16)
        )
        
        _x_1 = MathTex(r"2x_n + 0.5x_1 + 0.5x_{n-1} = p_n").next_to(andandand_andandand, DOWN*1.6)
        _x_2 = MathTex(r"2x_n + 0.5(u_1 x_n + v_1) + 0.5(u_{n-1} x_n + v_{n-1}) = p_n").next_to(andandand_andandand, DOWN*1.6)
        _x_3 = MathTex(r"(2 + 0.5u_1 + 0.5u_{n-1}) x_n = p_n - 0.5v_1 - 0.5v_{n-1}").next_to(andandand_andandand, DOWN*1.6)
        _x_4 = MathTex(r"x_n = \frac{ p_n - 0.5v_1 - 0.5v_{n-1} }{ 2 + 0.5u_1 + 0.5u_{n-1} }").next_to(andandand_andandand, DOWN*1.6)
        
        self.play(FadeIn(andandand_andandand))
        
        self.play(FadeIn(_x_1))
        
        self.play(Transform(_x_1,_x_2))
        self.play(Transform(_x_1,_x_3))
        self.play(Transform(_x_1,_x_4))
        
        then_how = Tex(r"then the question is: how to find u and v?").next_to(_x_1, DOWN)
        self.play(FadeIn(then_how))
        
        rect_uu = SurroundingRectangle(equation_uu, color=ORANGE, buff=SMALL_BUFF)
        rect_vv = SurroundingRectangle(equation_vv, color=ORANGE, buff=SMALL_BUFF)
        self.play(self.camera.frame.animate.move_to(uv).set(width = 20))
        self.play(FadeIn(rect_uu))
        self.play(FadeIn(rect_vv))
        
        _to_ = Tex(r"to solve tridiagonal linear systems:").next_to(coffi_mx, DOWN * 1.23456)
        _solve_ = MarkupText("<u>Crout Factorization</u>").next_to(_to_, DOWN * 2.22)
        
        self.play(
            self.camera.frame.animate.move_to(_solve_).set(width = 12.34)
        )
        self.play(FadeIn(_to_))
        self.play(FadeIn(_solve_))

        self.play(
            self.camera.frame.animate.shift(DOWN*8.8888).set(width = 22.22222222)
        )

        self.wait(5)