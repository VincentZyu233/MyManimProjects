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
        equal_sign = Tex("=")
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

        # group = VGroup( matrix_label_a, matrix_rect_a, matrix_rect_b, matrix_label_b, matrix_rect_c, matrix_label_c, diagonal_line )
        # self.play(FadeOut(group))
        
        eq = MathTex("   AX = P")
        eq.move_to( DOWN*3.5 )
        self.play(Write(eq))
        
        self.wait(5)