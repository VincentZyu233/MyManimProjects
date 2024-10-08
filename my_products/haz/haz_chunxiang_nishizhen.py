from manim import *
import math

config.background_color = '#ffffff'


class haz(MovingCameraScene):
    def construct(self):
        
        # 设置图片路径
        image_path = r"C:\Users\Administrator\Desktop\haz\body.png"  # 替换为你的图片路径

        # 创建图像对象
        image = ImageMobject(image_path)

        # 调整图片大小（可选）
        image.scale(1)  # 将图片放大两倍

        # 添加图片到场景中
        # self.add(image)
        # self.play( FadeIn(image) )
        self.add(image)
        
        position = DOWN*1.1111+LEFT*1.1111+DOWN*0.2222
        position2 = UP*2.2222+UP*0.8888+LEFT*0.8888
        image_arm = ImageMobject(r"C:\Users\Administrator\Desktop\haz\arm_touming.png").shift(LEFT*2.2222)
        image_cake = ImageMobject( r"C:\Users\Administrator\Desktop\haz\cake_touming.png" ).scale(0.1).shift(position2)
        
        # self.play( FadeIn(image_arm),run_time = 0.2222 )
        # self.play( FadeIn(image_cake),run_time = 0.2222 )
        
        # self.wait(0.8888)
        self.add(image_arm, image_cake)
        
        dot = Dot(color=YELLOW).scale(2).shift(position)
        # self.play(FadeIn(dot))
        
        for i in range (100):
             
            self.play(
                Rotate(
                    image_arm,
                    angle=2*PI,
                    about_point=position,
                    rate_func=rate_functions.linear,
                    run_time = 0.2222
                ),
                Rotate(
                    image_cake,
                    angle=2*PI,
                    about_point=position2,
                    rate_func=rate_functions.linear,
                    run_time = 0.2222
                ),
            )
        
        # self.wait(2.2222)
        
        
        
        
