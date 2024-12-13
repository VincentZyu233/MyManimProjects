"""
cd /home/vincentzyu/Documents/github-repo/MyManimProjects/my_manimce_products/reproduce_2017_nn_from_3b1b
cd D:\MANIM\Projects\MyManimProjects\my_manimce_products\reproduce_2017_nn_from_3b1b

manim -pql part1.py 

"""

from manim import *
import random

class ExampleThree(MovingCameraScene):
    """
manim -pql part1.py ExampleThree
manim -pqh part1.py ExampleThree

    """
    def construct(self):
        
        # three_image = ImageMobject("./resources/threes/three_1_rasterized.png").scale(15)
        three_image = SVGMobject("./resources/threes/three_1.svg").scale(2).set_z_index(0)

        RECT_EDGE_LEN = max(three_image.width - 0.5, three_image.height - 0.5 )
        three_rect = Rectangle(
            width = RECT_EDGE_LEN, height = RECT_EDGE_LEN,
            color = WHITE, stroke_width = 1
        ).set_z_index(100)

        three_group = Group(three_image, three_rect)

        brace_top = Brace(three_rect, direction=UP)
        brace_top_text = brace_top.get_text("28px")

        brace_left = Brace(three_rect, direction=LEFT)
        brace_left_text = brace_left.get_text("28px")

        brace_group = Group(brace_top, brace_top_text, brace_left, brace_left_text)
    
        self.play(
            FadeIn(three_rect, run_time=2),
            Write(three_image, run_time=2),
            lag_ratio=1
        )
        self.wait()
        self.play(
            Succession(
                FadeIn(brace_top, run_time=2),
                FadeIn(brace_top_text, run_time=2),
                lag_ratio=0.1
            ), 
            Succession(
                FadeIn(brace_left, run_time=2),
                FadeIn(brace_left_text, run_time=2),
                lag_ratio=0.1
            )
        )

        self.wait()

        self.play(
            FadeOut(brace_group),
            three_group.animate.shift(LEFT*3+UP).scale(0.45)
        )

        arrow_1 = Arrow(start=RIGHT, end=LEFT, color=GOLD)
        
        blue_arrow_right = Arrow(
            start=three_image.get_center()+RIGHT,
            end=three_image.get_center()+RIGHT*5,
            color=BLUE 
        )
        self.play(Create(blue_arrow_right))

        three_text = Text("3").next_to(blue_arrow_right, RIGHT*2).scale(2.5)
        self.play(FadeIn(three_text))

        self.wait()

        brain = SVGMobject("./resources/brain/brain-svgrepo-com.svg")
        brain.next_to(blue_arrow_right, DOWN*2)
        self.play(Create(brain), run_time=2)

        how_text = Text("how?!?")
        how_text.next_to(brain, DOWN)
        self.play(Write(how_text))

        self.wait(2)

        self.play(
            FadeOut(brain),
            FadeOut(how_text),
            lag_ratio = 0.5
        )

        self.wait(2)

        three_image_2 = SVGMobject("./resources/threes/three_2.svg")
        three_image_2.next_to(three_text, RIGHT+UP).scale(0.75)
        three_rect_2 = SurroundingRectangle(three_image_2, color=WHITE).set_z_index(100)
        
        three_image_3 = SVGMobject("./resources/threes/three_3.svg")
        three_image_3.next_to(three_image_2, DOWN*2).scale(0.75)
        three_rect_3 = SurroundingRectangle(three_image_3, color=WHITE).set_z_index(100)
        
        three_image_4 = SVGMobject("./resources/threes/three_4.svg")
        three_image_4.next_to(three_image_3, DOWN*2).scale(0.75)
        three_rect_4 = SurroundingRectangle(three_image_4, color=WHITE).set_z_index(100)

        # self.play(Write(three_image_2))
        # self.play(FadeIn(three_rect_2))

        self.play(
            Succession(
                FadeIn(three_rect_2),
                Write(three_image_2),
                lag_ratio=0.5
            )
        )
        
        self.play(
            Succession(
                FadeIn(three_rect_3),
                Write(three_image_3),
                lag_ratio=0.5
            )
        )
        
        self.play(
            Succession(
                FadeIn(three_rect_4),
                Write(three_image_4),
                lag_ratio=0.5
            )
        )

        self.wait(2)

        self.play(
            FadeOut(blue_arrow_right),
            FadeOut(three_text),
            lag_ratio=0.5
        )

        self.wait()

        three_group.set_z_index(101).set_opacity(0.5)
        
        self.play(
            three_group.animate.move_to(three_image_2.get_center())
        )

        self.wait()

        self.play(
            three_group.animate.move_to(three_image_3.get_center())
        )

        self.play(
            three_image.animate.shift(LEFT*5),
            three_rect.animate.set_opacity(0).shift(LEFT*5)
        )

        self.play(
            three_image.animate.set_opacity(0).shift(LEFT*5)
        )

        self.wait(2)

class WriteAProgram(MovingCameraScene):
    """
    manim -pql part1.py WriteAProgram
    manim -pqh part1.py WriteAProgram
    """
    def construct(self):
        
        three_image = SVGMobject("./resources/threes/three_1.svg").scale(2.5).set_z_index(0).shift(LEFT*2.5)

        RECT_EDGE_LEN = max(three_image.width - 0.5, three_image.height - 0.5 )
        three_rect = Rectangle(
            width = RECT_EDGE_LEN, height = RECT_EDGE_LEN,
            color = WHITE, stroke_width = 1
        ).set_z_index(100).move_to(three_image.get_center())

        self.play(
            # Create(three_image),
            DrawBorderThenFill(three_image),
            Create(three_rect),
            lag_ratio=0.5
        )

        self.wait()

        arrow_right = Arrow(
            start = three_image.get_center()+RIGHT*2.5, 
            end = three_image.get_center()+RIGHT*5
        )        
        self.play(
            Create(arrow_right)
        )

        numbers = VGroup(*[Text(str(i)).scale(0.75) for i in range(10)])
        
        # Arrange them vertically with a buffer between each number
        numbers.arrange(DOWN, buff=0.25).shift(RIGHT*2.5)
        
        # Add numbers to the scene
        self.add(numbers)
        
        # Optionally, you can animate them
        self.play(FadeIn(numbers))

        yellow_rect = SurroundingRectangle(numbers[0], color=YELLOW)
        self.play(
            Create(yellow_rect)
        )

        self.wait()
        question_mark = Text("?").next_to(yellow_rect, RIGHT)
        self.play(Write(question_mark))
        group_rect_question = VGroup(yellow_rect, question_mark)

        self.play(
            group_rect_question.animate.move_to(numbers[8].get_center()+RIGHT*0.22)
        )
        self.wait(0.5)
        self.play(
            group_rect_question.animate.move_to(numbers[4].get_center()+RIGHT*0.22)
        )
        self.wait(0.5)
        self.play(
            group_rect_question.animate.move_to(numbers[0].get_center()+RIGHT*0.22)
        )
        self.wait(0.5)
        self.play(
            group_rect_question.animate.move_to(numbers[2].get_center()+RIGHT*0.22)
        )
        self.wait(0.5)
        

        self.wait(5)
        
class LayoutPlan(MovingCameraScene):
    """
    manim -pql part1.py LayoutPlan
    manim -pqh part1.py LayoutPlan
    """
    def construct(self):
        text_1 = Text("Machine learning", color=GREEN)
        text_2 = Text("Neural Network", color=BLUE).next_to(text_1, DOWN)
        
        self.play(
            Write(text_1),
            Write(text_2),
            lag_ratio = 0.5
        )
        
        self.wait()
        
        self.play(
            text_1.animate.shift(UP*2+RIGHT*4).scale(5/6),
            text_2.animate.shift(UP*2+RIGHT*4).scale(5/6),
        )
        
        self.wait()
        
        column_counts = [8, 6, 6, 4] # 每列的水平间距
        column_spacing = 1 # 每个点的垂直间距
        row_spacing = 0.7
        
        dots_group = VGroup()  # 创建所有点
        for i, count in enumerate(column_counts):
            column_dots = VGroup(
                *[
                    Circle(stroke_color = BLUE, radius = 0.2, fill_color=BLACK, fill_opacity=1, z_index=10).shift(UP * (row_spacing * (count / 2 - j - 0.5)))
                    for j in range(count)
                ]
            )
            column_dots.shift(RIGHT * (i * column_spacing)) # 移动列的位置
            dots_group.add(column_dots)
        
        dots_group.center().shift(LEFT*4+UP*1) # 居中并添加到场景
        # self.play(Create(dots_group))
        
        self.play(
            Transform(
                text_2.copy(),
                dots_group
            )
        )
        
        self.wait(2)
        # 创建所有连接线
        lines_group = VGroup()
        for i in range(len(column_counts) - 1):
            for j in range(column_counts[i]):
                for k in range(column_counts[i + 1]):
                    start_dot = dots_group[i][j]
                    end_dot = dots_group[i + 1][k]
                    line = Line(
                        start=start_dot.get_center(),
                        end=end_dot.get_center(),
                        stroke_width = 2,
                        color=WHITE,
                        z_index=9  # 确保线条在圆之下
                    )
                    lines_group.add(line)

        # 添加线条到场景，并创建动画
        self.play(
            Create(lines_group),
            Create(dots_group),
            run_time=5
        )
        
        self.wait()
        
        formula = MathTex(r"a_{l+1} = \rho(W_l a_l + b_l)")  # 插入神经网络公式
        formula.next_to(text_2, DOWN).shift(LEFT)
        self.play(Write(formula))
        self.wait()

        bubble = SVGMobject("./resources/bubble/bubble_white.svg").scale(1.5).shift(RIGHT*2+DOWN*2)
        self.play(Write(bubble))
        self.wait()
        
        why_text = Text("为什么分层？")
        why_text.move_to(bubble).shift(UP*0.5)
        self.play(Write(why_text))
        
        self.wait()
        
        learning_text = Text("Learning 学习", color=YELLOW)
        learning_text.next_to(dots_group, DOWN*1.5)
        
        self.play(Write(learning_text) )
        
        self.wait()
        
         # 在这里再次遍历所有的直线，给每个直线都设置成黄色，并设置随机透明度
        yellow_lines_group = VGroup()
        for line in lines_group:
            print("line: ", line)
            new_line = line.copy()  # 复制原线条以便保留原始状态 [ty-reference](7)
            new_line.set_color(YELLOW)  # 设置颜色为黄色
            new_line.set_opacity(random.uniform(0.3, 1))  # 设置随机透明度 [ty-reference](8)
            yellow_lines_group.add(new_line)

        # 使用 Transform 动画将原来的线条转换为新样式的线条
        self.play(Transform(lines_group, yellow_lines_group), run_time=2)  # [ty-reference](9)
        
        self.wait(5)