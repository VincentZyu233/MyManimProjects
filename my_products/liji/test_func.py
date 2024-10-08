from manim import *

class test(ThreeDScene):
    def construct(self):
        
        func = rate_functions.ease_in_out_quart

        for i in range(1, 101):  # 循环从1到100，包括1和100
            k = round(i / 100, 2) 
            print(func(k))
            
            # manim -ql test_func.py