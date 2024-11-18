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
        
        three_image = ImageMobject("./resources/threes/three_1_rasterized.png").scale(10)

        three_rect = Rectangle(
            width = three_image.width + 0.5, height = three_image.height + 0.5,
            color = WHITE, stroke_width = 1
        )

        self.play(
            FadeIn(three_rect, run_time=2),
            FadeIn(three_image, run_time=2),
            lag_ratio=1
        )

        self.wait(2)
    
         