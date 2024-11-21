"""
cd /home/vincentzyu/Documents/github-repo/MyManimProjects/my_manimce_products/reproduce_2017_nn_from_3b1b
cd D:\MANIM\Projects\MyManimProjects\my_manimce_products\reproduce_2017_nn_from_3b1b

manim -pql part1.py 

"""

from manim import *

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
         