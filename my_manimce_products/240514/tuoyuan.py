from manim import *
import math

class EllipseScene(MovingCameraScene):
    def construct(self):
        # 设置背景为白色
        self.camera.background_color = WHITE
        self.play( self.camera.frame.animate.set(width = 22.2222) )
        
        timu = ImageMobject(r"D:\MANIM\Projects\MyManimProjects\my_products\240514\timu-removebg-preview.png").shift(LEFT*6.6666+UP*4.4444).scale(2.2222)
        self.play( FadeIn(timu) )
        
        a = 2
        b = math.sqrt( 2*math.sqrt(5) - 2 )
        c = math.sqrt( 6-2*math.sqrt(5) )
        
        abc = [a, b, c]
        # 循环遍历列表，对每个元素乘以 2
        for i in range(len(abc)):
            abc[i] *= 2.2222
        
        a,b,c = abc
        
        # 创建坐标轴
        axes = Axes(
            x_range=(-1.1111*a*1.5, 1.1111*a*1.5),
            y_range=(-1.1111*b*1.5, 1.1111*b*1.5),
            x_length=2.2222*a*1.5,
            y_length=2.2222*b*1.5,
            axis_config={"color": BLUE},
        )    
        self.play(Create(axes))
        
        # 创建椭圆
        ellipse = ParametricFunction(
            lambda t: np.array([a*np.cos(t), b*np.sin(t), 0]),
            color=BLACK,
            t_range=[0, TAU],
            stroke_width=2,
        )
        self.play(Create(ellipse))

        # 创建椭圆上的点
        A = Dot(point=[a, 0, 0], color=RED)
        B = Dot(point=[0, b, 0], color=RED)
        F = Dot(point=[c, 0, 0], color=RED) 
        label_A = Text("A", color=BLACK).next_to(A, UP)
        label_B = Text("B", color=BLACK).next_to(B, LEFT)
        label_F = Text("F", color=BLACK).next_to(F, UP)
        # self.play(Create(A), Create(B), Create(F))
        self.play( Create(A), Write(label_A) )
        self.play( Create(B), Write(label_B) )
        self.play( Create(F), Write(label_F) )

        # 创建过ABF的圆
        circle_center = [(a+c) / 2, b, 0]  # 圆心为((a+c)/2, b)
        circle_radius = (a+c) / 2  # 半径为(a+c)/2
        circle = Circle(radius=circle_radius, color=GREEN).move_to(circle_center)
        self.play(Create(circle))

        # 点出圆心的点D
        D = Dot(point=circle_center, color=RED)
        self.play(Create(D))

        self.wait(2)
        
        print("a,b,c: ", a,b,c)
        # a,b,c:  4.4444 3.4939711833050917 2.7467902596000324
