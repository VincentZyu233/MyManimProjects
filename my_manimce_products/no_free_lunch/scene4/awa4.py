from manim import *

class MatrixExample(Scene):
    def construct(self):
        # 定义矩阵
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
        
        
        # 调整矩阵A的位置和大小
        matrix_a.to_edge(LEFT)
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

        self.wait(5)