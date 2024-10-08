from manim import *

class MatrixExample(MovingCameraScene):
    def construct(self):   
        tex1 = Tex(r"qwq", color=RED_A).shift( LEFT*2.2222 + UP*2.2222 + LEFT*4.4444 )
        tex2 = Tex(r"qwq", color=RED_B).next_to( tex1, DOWN )
        tex3 = Tex(r"qwq", color=RED_C).next_to( tex2, DOWN )
        tex4 = Tex(r"qwq", color=RED_D).next_to( tex3, DOWN )
        tex5 = Tex(r"qwq", color=RED_E).next_to( tex4, DOWN )
        tex6 = Tex(r"qwq", color=RED).next_to( tex5, DOWN )
        
        self.add(tex1, tex2, tex3, tex4, tex5, tex6 )
        
        tex7 = Tex(r"qwq", color=BLUE).next_to( tex1, RIGHT*4.4444 )
        tex8 = Tex(r"qwq", color=BLUE_A).next_to( tex7, DOWN )
        tex9 = Tex(r"qwq", color=BLUE_B).next_to( tex8, DOWN )
        tex10 = Tex(r"qwq", color=BLUE_C).next_to( tex9, DOWN )
        tex11 = Tex(r"qwq", color=BLUE_D).next_to( tex10, DOWN )
        tex12 = Tex(r"qwq", color=BLUE_E).next_to( tex11, DOWN )
        
        self.add(tex7, tex8, tex9, tex10, tex11, tex12 )
        
        dot = Dot( point = [1,1,4] )
        self.add(dot)
        
        gray_ = Tex(r"qwq", color=GRAY).next_to( tex7, RIGHT*4.4444)
        gray_1 = Tex(r"qwq", color=GRAY_A).next_to( gray_, DOWN )
        gray_2 = Tex(r"qwq", color=GRAY_B).next_to( gray_1, DOWN )
        gray_3 = Tex(r"qwq", color=GRAY_C).next_to( gray_2, DOWN )
        gray_4 = Tex(r"qwq", color=GRAY_D).next_to( gray_3, DOWN )
        gray_5 = Tex(r"qwq", color=GRAY_E).next_to( gray_4, DOWN )
        gray_6 = Tex(r"qwq", color=GRAY_BROWN).next_to( gray_5, DOWN )
        
        self.add( gray_, gray_1, gray_2, gray_3, gray_4, gray_5, gray_6)
        