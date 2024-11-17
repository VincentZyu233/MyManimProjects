from manim import *

class FadeOutMatrixElements(Scene):
    def construct(self):
        # 创建一个初始矩阵
        matrix = [
            ["a_{11}", "a_{12}", "-1", "-1", "-1", "-1", "-1"], 
            ["a_{21}", "a_{22}", "a_{23}", "-1", "-1", "-1", "-1"], 
            ["-1", "-1", "...", "-1", "-1", "-1", "-1"], 
            ["-1", "-1", "-1", "...", "-1", "-1", "-1"], 
            ["-1", "-1", "-1", "-1", "...", "-1", "-1"], 
            ["-1", "-1", "-1", "-1", "a_{_{n-1,n-2}}", "a_{_{n-1,n-1}}", "a_{_{n-1,n}}"], 
            ["-1", "-1", "-1", "-1", "-1", "a_{a,n-1}", "a_{nn}"], 
        ]

        # 创建一个VGroup对象，用于容纳矩阵中的元素
        matrix_elements = VGroup()

        # 创建矩阵对象并添加到VGroup中
        for i, row in enumerate(matrix):
            row_elements = VGroup()
            for j, element in enumerate(row):
                if i == j:  # 保留对角线上的元素
                    element_obj = MathTex(element)
                else:  # 非对角线上的元素执行fadeout动画
                    element_obj = MathTex(element).fade(1)
                row_elements.add(element_obj)
            matrix_elements.add(row_elements)

        # 设置矩阵的位置
        matrix_elements.arrange(buff=1.6)

        # 将矩阵添加到场景中
        self.add(matrix_elements)

        # 对非对角线上的元素执行fadeout动画
        self.play(FadeOut(matrix_elements[0][1:]))
        self.play(FadeOut(matrix_elements[1][0], matrix_elements[1][2:]))
        self.play(FadeOut(matrix_elements[2][0:2], matrix_elements[2][3:]))
        self.play(FadeOut(matrix_elements[3][0:3], matrix_elements[3][4:]))
        self.play(FadeOut(matrix_elements[4][0:4], matrix_elements[4][5:]))
        self.play(FadeOut(matrix_elements[5][0:5], matrix_elements[5][6]))
        self.play(FadeOut(matrix_elements[6][0:6]))

        self.wait(1)  # 等待一秒钟