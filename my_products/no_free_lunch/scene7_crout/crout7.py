from manim import *

class MatrixExample(MovingCameraScene):
    def construct(self):
        
        equations = [
            MathTex(r"2x_1 + \;\: x_2 +  \;\: x_3 \qquad\quad\! = 4"),
            MathTex(r"4x_1 + 3x_2 + 3x_3 + \;\:x_4 = 11"),
            MathTex(r"8x_1 + 7x_2 + 9x_3 + 5x_4 = 29"),
            MathTex(r"6x_1 + 7x_2 + 9x_3 + 8x_4 = 30"),
        ]

        equation_4 = VGroup(*equations)

        equations[0].align_on_border(LEFT)
        equations[0].shift( RIGHT * 3.333 + UP * 1.234 )
        # self.play(FadeIn(equations[0]))
        equations[1].next_to(equations[0], DOWN, aligned_edge=LEFT)
        # self.play(FadeIn(equations[1]))
        equations[2].next_to(equations[1], DOWN, aligned_edge=LEFT)
        # self.play(FadeIn(equations[2]))
        equations[3].next_to(equations[2], DOWN, aligned_edge=LEFT)
        # self.play(FadeIn(equations[3]))
        self.play(FadeIn(equation_4))
        
        brace = Brace(equation_4, direction=LEFT)
        self.play(FadeIn(brace))
        
        gaussian_elimination = Tex(r"Gaussian Elimination:")
        gaussian_elimination.next_to(equations[0], UP*1.11)
        self.play(FadeIn(gaussian_elimination))
        
        self.wait(1)
        
        equations2 = [
            MathTex(r"2x_1 + \;\: x_2 +  \;\: x_3 \qquad\quad\! = 4"),
            MathTex(r"x_2 + \;\: x_3 + \;\: x_4 = 3"),
            MathTex(r"2x_3 + 2x_4 = 4"),
            MathTex(r"2x_4 = 2"),
        ]
        
        self.wait(1)
        
        equations2[1].next_to(equations2[0], DOWN, aligned_edge=RIGHT)
        equations2[2].next_to(equations2[1], DOWN, aligned_edge=RIGHT)
        equations2[3].next_to(equations2[2], DOWN, aligned_edge=RIGHT)
    
        equation_42 = VGroup(*equations2)
        equation_42.move_to(equation_4)
        self.play(Transform(equation_4, equation_42))
        
        arrow = Arrow([3, -2.22, 0], [3, -2, 0], buff=0)
        huidai = Tex(r"substitude back").next_to(equation_4, RIGHT*2.10).scale(0.8)
        self.add(arrow)

        self.play(FadeIn(arrow), 
                  ApplyMethod(arrow.shift, UP * 2.22), 
                  Transform(arrow, Arrow([3, -1.11, 0], [3, 1.11, 0], buff=0)),
                  FadeIn(huidai),
        )
        
        self.wait(3)
        
        # group_all = VGroup(brace,equation_4,arrow,huidai,gaussian_elimination)
        # self.play(
        #     FadeOut(group_all)
        # )
        
        
        matrix_representation = Tex(r"The process above can be described by matrices\\ as follows: ")
        matrix_representation.next_to(equations[3], DOWN*1.23456)
        matrix_representation.shift(LEFT*1.11)
        
        self.play(
            self.camera.frame.animate.shift(1.23456 * DOWN + 3*DOWN),
            run_time = 1.23456
        )
        self.play(FadeIn(matrix_representation))
        
        # self.play(
        #     self.camera.frame.animate.move_to( matrix_representation ).set( width = 12 )
        # )

        matrix_a = Matrix(
            [
                ["2", "1", "1", "0",],
                ["4", "3", "3", "1",],
                ["8", "7", "9", "5",],
                ["6", "7", "9", "8",],
            ]
        )
        
        matrix_b = Matrix(
            [
                ["x_{1}"],
                ["x_{2}"],
                ["x_{3}"],
                ["x_{4}"],
            ]
        )
        
        matrix_c = Matrix(
            [
                ["4"],
                ["11"],
                ["29"],
                ["30"],
            ]
        )
        
        # self.play(
        #     self.camera.frame.animate.move_to( matrix_representation )
        # )
        

        # 调整矩阵A的位置和大小
        matrix_a.next_to(matrix_representation, DOWN*1.23)
        matrix_a.to_edge(LEFT).shift(RIGHT*1.11)
        matrix_a.scale(0.8)
        
        # 调整矩阵B的位置和大小
        matrix_b.next_to(matrix_a, RIGHT, buff=0.2)
        matrix_b.scale(0.8)
        
        # 在矩阵B的右侧放置等号符号
        equal_sign = MathTex("=")
        equal_sign.next_to(matrix_b, RIGHT, buff=0.2)
        
        # 在等号符号的右侧放置矩阵C
        matrix_c.next_to(equal_sign, RIGHT, buff=0.2)
        matrix_c.scale(0.8)
        
        self.play(
            Write(matrix_a),
            Write(matrix_b),
        )
        
        self.play(
            Write(equal_sign),
            Write(matrix_c),
        )
        
        # 添加矩阵A的标识
        matrix_rect_a = SurroundingRectangle(matrix_a, color=RED, buff=SMALL_BUFF)
        matrix_label_a = Text("A", font_size=24)
        matrix_label_a.next_to(matrix_a, DOWN)
        self.play(
            Create(matrix_rect_a),
            FadeIn(matrix_label_a),
        )
            
        # 添加矩阵B的标识
        matrix_rect_b = SurroundingRectangle(matrix_b, color=RED, buff=SMALL_BUFF)
        matrix_label_b = Text("X", font_size=24)
        matrix_label_b.next_to(matrix_b, DOWN)
        self.play(
            Create(matrix_rect_b),
            FadeIn(matrix_label_b),
        )        
        
        # 添加矩阵C的标识
        matrix_rect_c = SurroundingRectangle(matrix_c, color=RED, buff=SMALL_BUFF)
        matrix_label_c = Text("B", font_size=24)
        matrix_label_c.next_to(matrix_c, DOWN)
        self.play(
            Create(matrix_rect_c),
            FadeIn(matrix_label_c),
        ) 
        
        eq = MathTex("   AX = B")
        eq.next_to( equal_sign, DOWN*7.7777777 )
        self.play(Write(eq))

        self.play(
            self.camera.frame.animate.shift(5.55555 * DOWN),
            run_time = 1
        )

        tex_zengguang = Tex(r"then concatenate matrix A and vector B \\ to form the augmented matrix (A\textbar{}B).")  
        tex_zengguang.next_to(eq, DOWN*1.23)
        self.play(FadeIn(tex_zengguang))
        
        matrix_ab = Matrix(
            [
                ["2", "1", "1", "0", "4"],
                ["4", "3", "3", "1", "11"],
                ["8", "7", "9", "5", "29"],
                ["6", "7", "9", "8", "30"],
            ]
        ).next_to(tex_zengguang, DOWN*1.23)
        
        top_left_ab = matrix_ab.get_corner(UL)
        bottom_right_ab = matrix_ab.get_corner(DR)
        height_ab = matrix_ab.get_height()
        width_ab = matrix_ab.get_width()          
        shuxian_up = top_left_ab + np.array([( 3/4 + 1/16 )*width_ab, 0, 0])
        shuxian_down = shuxian_up + np.array([0, -height_ab, 0])
        
        shuxian = Line(shuxian_up, shuxian_down, color = GRAY)
        shuxian.set_stroke(width=2, opacity=0.8)
        # self.play(Create(shuxian))
        self.play(
            Create(shuxian),
            Write(matrix_ab)
        )
        
        self.play(
            self.camera.frame.animate.shift(5.55555 * DOWN),
            run_time = 1
        )
        
        tex_for = Tex(r"Focus on matrix a:").next_to(matrix_ab, DOWN*2.222)
        self.play(FadeIn(tex_for))
        
        matrix_a_copy = matrix_a.copy()
        matrix_a_copy.next_to(tex_for, DOWN*2.222)
        matrix_label_a_copy = Tex("$A$", font_size = 48)
        matrix_label_a_copy.next_to(matrix_a_copy, DOWN)
        self.play(
            FadeIn(matrix_a_copy),
            FadeIn(matrix_label_a_copy),
        )
        # self.play(FadeIn(matrix_a_copy))
        
        tex_equal = Tex(r"The elimination process described above, \\if represented using matrices, is equivalent to:").next_to(matrix_label_a_copy, DOWN*2.222)
        self.play(FadeIn(tex_equal))
        
        tex_leftmul = Tex(r"left-multiply matrix A \\with several elementary lower triangular matrices").next_to(tex_equal, DOWN)
        self.play(FadeIn(tex_leftmul))
        
        # self.play(
        #     self.camera.frame.animate.shift(5.55555 * DOWN),
        #     run_time = 1
        # )
        self.play(
            self.camera.frame.animate.shift(0.123456789*DOWN),
            self.camera.frame.animate.set( width = 20 ),
        )
        
        matrix_l1 = Matrix(
            [
                ["1", "0", "0", "0"],
                ["-2", "1", "0", "0"],
                ["-4", "0", "1", "0"],
                ["-3", "0", "0", "1"],
            ]
        ).next_to(matrix_a_copy, LEFT).scale(0.8)
        # self.play(
        #     Create(matrix_l1)
        # )
        for i, row in enumerate(matrix_l1.get_entries()):
            for j, entry in enumerate(row):
                if matrix_l1.get_entries()[i][j].get_tex_string() == "0":
                    entry.set_opacity(0)  # 隐藏零元素
        # self.play(Write(matrix_l1))
        matrix_label_l1 = Tex("$L_1$", font_size = 48).next_to(matrix_l1, DOWN)
        
        self.play(
            Write(matrix_l1),
            FadeIn(matrix_label_l1),
        )
        
        # matrix_a_copy = matrix_a.copy()
        # matrix_a_copy.next_to(tex_for, DOWN*1.23456)
        # self.play(FadeIn(matrix_a_copy))
        
        equal_sign = Tex(r"=").next_to(matrix_a_copy, RIGHT)
        
        matrix_l1a = Matrix(
            [
                ["2", "1", "1", "0",],
                ["0", "1", "1", "1",],
                ["0", "3", "5", "5",],
                ["0", "4", "6", "8",],
            ]
        ).next_to(equal_sign, RIGHT).scale(0.8)
        
        eq1 = Tex(r"=").next_to(matrix_label_a_copy, RIGHT*7.7777777)
        tex_l1a = Tex("$L_1A$", font_size = 48).next_to(eq1, RIGHT*8.88888888)

        self.play(
            FadeIn(equal_sign),
            FadeIn(matrix_l1a),
            FadeIn(eq1),
            FadeIn(tex_l1a),
            ApplyMethod(matrix_label_l1.shift, RIGHT*4.444), run_time = 1.111,
        )
        
        self.play(
            ApplyMethod(
                VGroup(matrix_l1, matrix_a_copy, equal_sign, matrix_l1a, matrix_label_l1, matrix_label_a_copy, eq1, tex_l1a ).shift ,
                LEFT*5.55555
            ),
            run_time = 1.111
        )
        
        self.play(
            FadeOut(
                VGroup(matrix_l1, matrix_a_copy, equal_sign,matrix_label_l1, matrix_label_a_copy, eq1)   
            ),
            run_time = 0.888
        )
        
        matrix_l2 = Matrix(
            [
                ["1", "0", "0", "0"],
                ["0", "1", "0", "0"],
                ["0", "-3", "1", "0"],
                ["0", "-4", "0", "1"],
            ]
        ).next_to(matrix_l1a, LEFT).scale(0.8)
        for i, row in enumerate(matrix_l2.get_entries()):
            for j, entry in enumerate(row):
                if matrix_l2.get_entries()[i][j].get_tex_string() == "0":
                    entry.set_opacity(0)  # 隐藏零元素
        # self.play(Write(matrix_l1))
        matrix_label_l2 = Tex("$L_2$", font_size = 48).next_to(matrix_l2, DOWN)
        
        self.play(
            Write(matrix_l2),
            FadeIn(matrix_label_l2),
        )
        
        equal_sign_mx_2 = Tex(r"=").next_to(matrix_l1a, RIGHT)
        
        matrix_l2l1a = Matrix(
            [
                ["2", "1", "1", "0",],
                ["0", "1", "1", "1",],
                ["0", "0", "2", "2",],
                ["0", "0", "2", "4",],
            ]
        ).next_to(equal_sign_mx_2, RIGHT).scale(0.8)
        
        eq2 = Tex(r"=").next_to(tex_l1a, RIGHT*5.55555)
        tex_l2l1a = Tex("$L_2L_21A$", font_size = 48).next_to(eq2, RIGHT*9.999999999)

        self.play(
            FadeIn(equal_sign_mx_2),
            FadeIn(matrix_l2l1a),
            FadeIn(eq2),
            FadeIn(tex_l2l1a),
            ApplyMethod(matrix_label_l2.shift, RIGHT*3.333),
            run_time = 1.111,
        )
        
        self.play(
            ApplyMethod(
                VGroup(matrix_l2, matrix_l1a, equal_sign_mx_2, matrix_l2l1a, matrix_label_l2, tex_l1a, eq2, tex_l2l1a ).shift ,
                LEFT*5.55555
            ),
            run_time = 1.111
        )
        
        self.play(
            FadeOut(
                VGroup(matrix_l2, matrix_l1a, equal_sign_mx_2, matrix_label_l2, tex_l1a, eq2)   
            ),
            run_time = 0.888
        )

        matrix_l3 = Matrix(
            [
                ["1", "0", "0", "0"],
                ["0", "1", "0", "0"],
                ["0", "0", "1", "0"],
                ["0", "0", "-1", "1"],
            ]
        ).next_to(matrix_l2l1a, LEFT).scale(0.8)
        for i, row in enumerate(matrix_l3.get_entries()):
            for j, entry in enumerate(row):
                if matrix_l3.get_entries()[i][j].get_tex_string() == "0":
                    entry.set_opacity(0)  # 隐藏零元素
        # self.play(Write(matrix_l1))
        matrix_label_l3 = Tex("$L_3$", font_size = 48).next_to(matrix_l3, DOWN)

        self.play(
            Write(matrix_l3),
            FadeIn(matrix_label_l3),
        )
        
        equal_sign_mx_3 = Tex(r"=").next_to(matrix_l2l1a, RIGHT)
        
        matrix_u = Matrix(
            [
                ["2", "1", "1", "0",],
                ["0", "1", "1", "1",],
                ["0", "0", "2", "2",],
                ["0", "0", "0", "2",],
            ]
        ).next_to(equal_sign_mx_3, RIGHT).scale(0.8)
        
        matrix_u.shift(LEFT*0.088)

        eq3 = Tex(r"=").next_to(tex_l2l1a, RIGHT*6.666666)
        tex_u = Tex("$U$", font_size = 48).next_to(eq3, RIGHT*7.7777777)
        
        self.play(
            FadeIn(equal_sign_mx_3),
            FadeIn(matrix_u),
            FadeIn(eq3),
            FadeIn(tex_u),
            ApplyMethod(matrix_label_l3.shift, RIGHT*3.456789 + UP*0.03),
            run_time = 1.111,
        )

        self.play(
            ApplyMethod(
                VGroup(matrix_l3, matrix_l2l1a, equal_sign_mx_3, matrix_u, matrix_label_l3, tex_l2l1a, eq3, tex_u ).shift ,
                LEFT*4.4444
            ),
            run_time = 1.111
        )
        
        self.play(
            FadeOut(
                VGroup(matrix_l3, matrix_l2l1a, equal_sign_mx_3, matrix_label_l3, tex_l2l1a, eq3)   
            ),
            run_time = 0.888
        )

        self.play(
            self.camera.frame.animate.shift(RIGHT*12.2222),
            # self.camera.frame.animate.set( width = 24 ),
            run_time = 1.23456
        )
        
        tex_jilu = Tex(r"In the mean time, during the process of elementary row operations, \\ perform the same and synchronized operation \\ on the rightmost vector of the augmented matrix, \\by doing so, we obtain a new augmented matrix (U\textbar{}C).")
        tex_jilu.next_to(tex_equal, RIGHT*5.55555)
        tex_jilu.shift(DOWN*0.666666)
        self.play(
            FadeIn(tex_jilu)
        )

        matrix_uc = Matrix(
            [
                ["2", "1", "1", "0", "4"],
                ["0", "1", "1", "1", "3"],
                ["0", "0", "2", "2", "4"],
                ["0", "0", "0", "2", "2"],
            ]
        ).next_to(tex_jilu, UP*1.23456789)
        matrix_uc.shift(LEFT*3.333)
        
        top_left_uc = matrix_uc.get_corner(UL)
        bottom_right_uc = matrix_uc.get_corner(DR)
        height_uc = matrix_uc.get_height()
        width_uc = matrix_uc.get_width()          
        shuxian2_up = top_left_uc + np.array([( 3/4 + 1/16 )*width_uc, 0, 0])
        shuxian2_down = shuxian2_up + np.array([0, -height_uc, 0])
        
        shuxian2 = Line(shuxian2_up, shuxian2_down, color = GRAY)
        shuxian2.set_stroke(width=2, opacity=0.8)
        # self.play(Create(shuxian))
        self.play(
            self.camera.frame.animate.set( width = 24 ),
            Create(shuxian2),
            Write(matrix_uc)
        )
        
        arrow2 = Arrow(bottom_right_uc + [0.22, -2.22, 0], bottom_right_uc + [0.22, -2, 0], buff=0)
        huidai2 = Tex(r"substitude back").next_to(matrix_uc, RIGHT*2.10).scale(0.8)
        self.add(arrow2)

        self.play(FadeIn(arrow), 
                  ApplyMethod(arrow2.shift, UP * 2.22), 
                  Transform(arrow2, Arrow(bottom_right_uc + [0.22, 0, 0], bottom_right_uc + [0.22, 2.22, 0], buff=0)),
                  FadeIn(huidai2),
        )
        
        self.play(
            self.camera.frame.animate.shift( UP*14.4444 + LEFT*4.4444 ),
            ApplyMethod(
                VGroup(matrix_uc, shuxian2, arrow2, huidai2 ).shift ,
                UP*14.4444
            ),
            run_time = 1.888888
        )
        
        tex_same = Tex(r"They are the same.").next_to(matrix_uc, UP)
        self.play(
            self.camera.frame.animate.set( width = 20 ),
            Write(tex_same)
        )
        
        self.play(
            self.camera.frame.animate.shift( DOWN*18.8888 + LEFT*6.6666 ),
            run_time = 1.68
        )
        
        tex_notelu = Tex(r"Note that during the process of elimination, \\we have:").next_to(tex_leftmul, DOWN*2.2222)
        self.play( FadeIn(tex_notelu) )
        tex_l3l2l1au = MathTex(r"L_3L_2L_1A = U").next_to(tex_notelu, DOWN)
        self.play( FadeIn(tex_l3l2l1au) )
        
        tex_ie = MathTex(r"i.e., \: A = (L_{3}L_{2}L_{1})^{-1}U").next_to(tex_l3l2l1au, DOWN)
        self.play(FadeIn(tex_ie))
        
        tex_let = MathTex(r"Then \: we \: let \: (L_{3}L_{2}L_{1})^{-1} = L").next_to(tex_ie, DOWN)
        self.play( FadeIn(tex_let ) )
        
        self.play(
            self.camera.frame.animate.shift( DOWN*4.4444 ),
            run_time = 0.8888
        )
        
        tex_ieie = MathTex(r"i.e.: \: A = LU").next_to(tex_let, DOWN)
        self.play( FadeIn(tex_ieie ) )
        
        matrix_a_copy_2 = matrix_a.copy().next_to(tex_ieie, DOWN)
        matrix_a_copy_2.shift(LEFT*4.4444 + DOWN*0.4444)
        _a_ = Tex(r"A").next_to(matrix_a_copy_2, DOWN)
        
        equal_sign_alu = Tex(r"=").next_to(matrix_a_copy_2, RIGHT)

        matrix_l_copy = Matrix(
            [
                ["1", "0", "0", "0"],
                ["2", "1", "0", "0"],
                ["4", "3", "1", "0"],
                ["3", "4", "1", "1"],
            ]
        ).next_to(equal_sign_alu, RIGHT).scale(0.8)
        _l_ = Tex(r"L").next_to(matrix_l_copy, DOWN)
        
        matrix_u_copy = matrix_u.copy().next_to(matrix_l_copy, RIGHT)
        _u_ = Tex(r"U").next_to(matrix_u_copy, DOWN)
        
        self.play(
            FadeIn(matrix_a_copy_2), 
            FadeIn(equal_sign_alu),
            FadeIn(matrix_l_copy),
            FadeIn(matrix_u_copy),
            FadeIn(_a_),
            FadeIn(_l_),
            FadeIn(_u_),
        )
        
        self.play(
            self.camera.frame.animate.shift( DOWN*4.4444 ),
            run_time = 0.8888
        )

        tex_gen = Tex(r"More general, given a matrix, if and only if the matrix satisfy: ").next_to(equal_sign_alu, DOWN*2.2222)
        tex_gen.shift(RIGHT*3.333+DOWN*2.222)
        tex_gen1 = Tex(r"1.it is a square matrix, \\ i.e. the number of rows equals to numbers of columns. ").next_to(tex_gen, DOWN)
        tex_gen2 = Tex(r"2.it is an invertible matrix(aka non-singular matrix), \\ that is : All principal minors of matrix A \\ (i.e., determinants of any kxk submatrix starting from the top-left corner) \\ must be non-zero.").next_to(tex_gen1, DOWN)
        self.play(Write(tex_gen))
        self.play(Write(tex_gen1))
        self.play(Write(tex_gen2))
        
        tex_aluform = Tex(r"then this matrix can be decomposed into LU form \\ as A = LU").next_to(tex_gen2, DOWN*1.1111)
        self.play(Write(tex_aluform))
        
        self.play(
            self.camera.frame.animate.shift( DOWN*6.6666 ),
            run_time = 0.6666
        )
        
        tex_since = Tex(r"and since $L_1L_2L_3$... are elementary lower triangular matrices,").next_to(tex_aluform, DOWN*1.1111)
        self.play(FadeIn(tex_since))
        
        tex_then = Tex(r"hence L = $L_1L_2L_3$ is a lower triangular matrix").next_to(tex_since, DOWN)
        self.play(FadeIn(tex_then))
        
        tex_naturally = Tex(r"naturally, U is a upper triangular matrix").next_to(tex_then, DOWN)
        self.play(FadeIn(tex_naturally))
        
        _a_lu_ = MathTex(r'\mathbf{A} = \mathbf{LU}', font_size = 64).next_to(equal_sign_alu, DOWN*6.666666)
        _a_lu_.shift(RIGHT*3.333333 + DOWN*2.888888)
        
        texxxxx = VGroup(tex_gen, tex_gen1, tex_gen2, tex_aluform, tex_since, tex_then, tex_naturally )
        self.play(
            self.camera.frame.animate.shift( UP*6.666666 ),
        )
        
        self.play(
            self.camera.frame.animate.shift( DOWN* 2.3456 ),
            Transform(texxxxx, _a_lu_)
        )
        
        # text4 = Text("Hello world", t2w={'world':BOLD})
        tex_moreover = Tex("Moreover, \\\\ if L is \\textbf{unit} lower triangular matrix, \\\\ U is upper triangular matrix")
        tex_moreover.next_to(_a_lu_, DOWN*8.88888888)
        tex_moreover.shift(LEFT*4.8888 + DOWN*2.2222)
        self.play(
            self.camera.frame.animate.shift( DOWN*2.3456 ).set(width=20),
            FadeIn(tex_moreover)
        )
        
        matrix_a = Matrix(
            [
                ["a_11", "...", "a_1j", "...", "a_1n"], 
                ["...", "...", "...", "...", "..."], 
                ["a_i1", "...", "a_ij", "...", "a_in"], 
                ["...", "...", "...", "...", "..."],
                ["a_n1", "...", "a_nj", "...", "a_nn"], 
            ],
            h_buff = 1.0,
        ).next_to(tex_moreover, RIGHT)
        matrix_a.shift(LEFT*4.4444 + UP*2.2222 + RIGHT*0.4444 + DOWN*0.2222 )
        matrix_a.scale(0.5555)
        
        eqsign = Tex(r"=").next_to(matrix_a, RIGHT)
        eqsign.scale(0.8)
        
        matrix_l = Matrix(
            [
                ["1", "-1", "-1", "-1", "-1"], 
                ["...", "1", "-1", "-1", "-1"], 
                ["l_i1", "...", "1", "-1", "-1"], 
                ["...", "...", "...", "1", "-1"],
                ["a_n1", "...", "l_nj", "...", "1"], 
            ],
            h_buff = 1.0,
        ).next_to(eqsign, RIGHT)
        matrix_l.shift(LEFT*1.2222)
        matrix_l.scale(0.5555)
        for i, row in enumerate(matrix_l.get_entries()):
            for j, entry in enumerate(row):
                if matrix_l.get_entries()[i][j].get_tex_string() == "-1":
                    entry.set_opacity(0)  # 隐藏零元素
        
        matrix_u = Matrix(
            [
                ["u_{11}", "...", "u_{1j}", "...", "u_{1n}"], 
                ["-1", "...", "...", "...", "..."], 
                ["-1", "-1", "u_{ij}", "...", "u_{jn}"], 
                ["-1", "-1", "-1", "...", "..."],
                ["-1", "-1", "-1", "-1", "u_nn"], 
            ],
            h_buff = 1.0,
        ).next_to(matrix_l, RIGHT*0.2222)
        matrix_u.shift(LEFT*1.0000)
        matrix_u.scale(0.5555)
        for i, row in enumerate(matrix_u.get_entries()):
            for j, entry in enumerate(row):
                if matrix_u.get_entries()[i][j].get_tex_string() == "-1":
                    entry.set_opacity(0)  # 隐藏零元素
        
        self.play(
            # self.camera.frame.animate.shift(DOWN*4.4444),
            Write(matrix_a),
            FadeIn(eqsign),
            Write(matrix_l),
            Write(matrix_u),
        )
        
        top_left_l = matrix_l.get_corner(UL)
        bottom_left_l = matrix_l.get_corner(DL)
        bottom_right_l = matrix_l.get_corner(DR)
        triangle_l = Polygon(top_left_l, bottom_left_l, bottom_right_l)
        triangle_l.set_fill(color='#66CCFF', opacity=0.2)  # 设置填充颜色为红色，不透明度为0.5
        triangle_l.set_stroke(color='#00BFFF', width=2)  # 设置边框颜色为蓝色，宽度为2   
        
        top_left_u = matrix_u.get_corner(UL)
        top_right_u = matrix_u.get_corner(UR)
        bottom_right_u = matrix_u.get_corner(DR)
        triangle_u = Polygon(top_left_u, top_right_u, bottom_right_u)
        triangle_u.set_fill(color='#FFFF00', opacity=0.2)  # 设置填充颜色为红色，不透明度为0.5
        triangle_u.set_stroke(color='#FFD700', width=2)  # 设置边框颜色为蓝色，宽度为2  

        self.play(Create(triangle_l))
        self.play(Create(triangle_u))
        
        tex_doolittle = Tex(r"it is called \underline{\textbf{\textit{Doolittle Factorization}}}").next_to(tex_moreover, DOWN)
        self.play(
            FadeIn(tex_doolittle)
        )
        
        tex_alter = Tex("Alternatively, \\\\ if L is lowere triangular matrix, \\\\ U is \\textbf{unit} upper triangular matrix") 
        tex_alter.next_to(tex_doolittle, DOWN*8.8888)
        tex_alter.shift(DOWN*0.8888)
        self.play(self.camera.frame.animate.shift( DOWN*4.44 ),)
        self.play(FadeIn(tex_alter))
        
        matrix_a2 = matrix_a.copy().next_to(tex_alter, RIGHT)
        matrix_a2.shift(LEFT*2.2222+UP*2.2222)
        
        eqsign2 = Tex(r"=").next_to(matrix_a2, RIGHT)
        eqsign2.scale(0.8)
        
        matrix_l22 = Matrix(
            [
                ["l_11", "-1", "-1", "-1", "-1"], 
                ["...", "...", "-1", "-1", "-1"], 
                ["l_i1", "...", "l_ij", "-1", "-1"], 
                ["...", "...", "...", "...", "-1"],
                ["a_n1", "...", "l_nj", "...", "l_nn"], 
            ],
            h_buff = 1.0,
        ).next_to(eqsign2, RIGHT)
        matrix_l22.shift(LEFT*1.2222)
        matrix_l22.scale(0.5555)
        for i, row in enumerate(matrix_l22.get_entries()):
            for j, entry in enumerate(row):
                if matrix_l22.get_entries()[i][j].get_tex_string() == "-1":
                    entry.set_opacity(0)  # 隐藏零元素
        
        matrix_u2 = Matrix(
            [
                ["1", "...", "u_{1j}", "...", "u_{1n}"], 
                ["-1", "1", "...", "...", "..."], 
                ["-1", "-1", "1", "...", "u_{jn}"], 
                ["-1", "-1", "-1", "1", "..."],
                ["-1", "-1", "-1", "-1", "1"], 
            ],
            h_buff = 1.0,
        ).next_to(matrix_l22, RIGHT*0.2222)
        matrix_u2.shift(LEFT*1.0000)
        matrix_u2.scale(0.5555)
        for i, row in enumerate(matrix_u2.get_entries()):
            for j, entry in enumerate(row):
                if matrix_u2.get_entries()[i][j].get_tex_string() == "-1":
                    entry.set_opacity(0)  # 隐藏零元素
        
        self.play(
            # self.camera.frame.animate.shift(DOWN*4.4444),
            Write(matrix_a2),
            FadeIn(eqsign2),
            Write(matrix_l22),
            Write(matrix_u2),
        )

        top_left_l2 = matrix_l22.get_corner(UL)
        bottom_left_l2 = matrix_l22.get_corner(DL)
        bottom_right_l2 = matrix_l22.get_corner(DR)
        triangle_l2 = Polygon(top_left_l2, bottom_left_l2, bottom_right_l2)
        triangle_l2.set_fill(color='#66CCFF', opacity=0.2)  # 设置填充颜色为红色，不透明度为0.5
        triangle_l2.set_stroke(color='#00BFFF', width=2)  # 设置边框颜色为蓝色，宽度为2   
        
        top_left_u2 = matrix_u2.get_corner(UL)
        top_right_u2 = matrix_u2.get_corner(UR)
        bottom_right_u2 = matrix_u2.get_corner(DR)
        triangle_u2 = Polygon(top_left_u2, top_right_u2, bottom_right_u2)
        triangle_u2.set_fill(color='#FFFF00', opacity=0.2)  # 设置填充颜色为红色，不透明度为0.5
        triangle_u2.set_stroke(color='#FFD700', width=2)  # 设置边框颜色为蓝色，宽度为2  

        self.play(Create(triangle_l2))
        self.play(Create(triangle_u2))

        tex_crout = Tex(r"it is called \underline{\textbf{\textit{Crout Factorization}}}").next_to(tex_alter, DOWN)
        self.play(
            FadeIn(tex_crout)
        )

        self.wait(3)