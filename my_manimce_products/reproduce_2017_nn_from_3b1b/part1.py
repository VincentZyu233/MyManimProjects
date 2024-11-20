"""
cd /home/vincentzyu/Documents/github-repo/MyManimProjects/my_manimce_products/reproduce_2017_nn_from_3b1b

manim -pql part1.py 

"""

from manim import *

class ExampleThree(MovingCameraScene):
    """
manim -pql part1.py ExampleThree
    """
    def construct(self):
        
        three_image = ImageMobject("./resources/threes/three_1_rasterized.png").scale(15)

        three_rect = Rectangle(
            width = three_image.width + 0.5, height = three_image.height + 0.5,
            color = WHITE, stroke_width = 1
        )

        three_group = Group(three_image, three_rect)

        brace_top = Brace(three_rect, direction=UP)
        brace_top_text = brace_top.get_text("28px")

        brace_left = Brace(three_rect, direction=LEFT)
        brace_left_text = brace_left.get_text("28px")

        brace_group = Group(brace_top, brace_top_text, brace_left, brace_left_text)
    
        self.play(
            FadeIn(three_rect, run_time=2),
            FadeIn(three_image, run_time=2),
            lag_ratio=1
        )
        self.wait()
        self.play(
            Succession(
                FadeIn(brace_top),
                FadeIn(brace_top_text),
                lag_ratio=0.5
            ), 
            Succession(
                FadeIn(brace_left),
                FadeIn(brace_left_text),
                lag_ratio=0.5
            )
        )

        self.play(
            FadeOut(brace_group),
            three_group.animate.shift(LEFT*2+UP).scale(0.45)
        )

        arrow_1 = Arrow(start=RIGHT, end=LEFT, color=GOLD)
        
        blue_arrow_right = Arrow(
            start=three_image.get_center()+RIGHT,
            end=three_image.get_center()+RIGHT*5,
            color=BLUE 
        )
        self.play(Create(blue_arrow_right))

        three_text = Text("3").next_to(blue_arrow_right, RIGHT*1.5).scale(2.5)
        self.play(FadeIn(three_text))

        self.wait(2)
    
         