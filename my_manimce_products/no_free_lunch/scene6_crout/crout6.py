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
        
        gaussian_elimination = Tex(r"Gaussian elimination:")
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
        
        self.play(
            FadeIn(equal_sign),
            FadeIn(matrix_l1a),
            ApplyMethod(matrix_label_l1.shift, RIGHT*4.444), run_time = 1.111
        )
        
        eq1 = Tex(r"=").next_to(matrix_a_copy, RIGHT*3.333)
        tex_l1a = Tex(r"L_{1}A").next_to(eq1, RIGHT*3.333)
        
        self.play(
            ApplyMethod(
                VGroup(matrix_l1, matrix_a_copy, equal_sign, matrix_l1a, matrix_label_l1, matrix_label_a_copy, eq1, tex_l1a ) ,
                LEFT*8.88888888
            ),
            
            run_time = 1.111
        )
        
        
        