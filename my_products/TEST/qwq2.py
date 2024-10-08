from manim import *

class MathEquation(Scene):
    def construct(self):
        # 定义矩阵 B 和向量 C
        B = r'B'
        C = r'C'

        # 定义向量 XT 和数字 x_n
        XT = r'\begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_{n-1} \end{bmatrix}'
        xn = r'x_n'

        # 定义完整的公式
        equation = f'{B}({XT}) + {C}{xn}'

        # 创建 Tex 对象并显示公式
        tex = Tex(equation)
        self.play(Write(tex))
        self.wait()