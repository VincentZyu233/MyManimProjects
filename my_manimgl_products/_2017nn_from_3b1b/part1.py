"""
cd D:\MANIM\Projects\MyManimProjects\my_manimgl_products\_2017nn_from_3b1b\resources\threes
cd D:\MANIM\Projects\MyManimProjects\my_manimgl_products\_2017nn_from_3b1b 
cd D:\MANIM\Projects\MyManimProjects\my_manimgl_products

.\myenv-1.7.1\Scripts\Activate.ps1


manimgl part1.py SquareToCircle -ow
"""


import sys
import os.path
import cv2

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from manimlib import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)

        self.add(circle)