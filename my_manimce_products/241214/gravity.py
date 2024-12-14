from manim import *

"""
manim -pql gravity.py
manim -pqh gravity.py

"""

class GravityScene(MovingCameraScene):
    def construct(self):
        
        qiu = Circle(
            radius = 1, color = BLUE, fill_opacity = 1,
            stroke_color = DARK_BLUE, stroke_width = 5
        )
        self.play(
            Create(qiu), run_time=1.5
        )

        text_m = Text("m", font_size = 50)
        text_m.next_to(qiu, RIGHT)
        self.play(
            Write(text_m)
        )

        # 定义电场箭头的相关参数
        num_arrows = 15  # 箭头的数量
        spacing = 1.5    # 箭头之间的间距
        arrow_length = 5.5 # 箭头长度

        # 创建一组水平向左的箭头
        gravity_field_arrows = VGroup(*[
            # Arrow(
            #     start=RIGHT * arrow_length / 2, 
            #     end=LEFT * arrow_length / 2,
            #     color=YELLOW
            # ).shift(UP * (i - num_arrows // 2) * spacing)
            Arrow(
                start=UP * arrow_length / 2, 
                end=DOWN * arrow_length / 2,
                stroke_width = 4.5,
                color=YELLOW
            ).shift(LEFT * (i - num_arrows // 2) * spacing)
            for i in range(num_arrows)
        ])

        # 将电场箭头移动到场景合适的位置
        gravity_field_arrows.shift(RIGHT * 1)

        # 添加电场箭头到场景中，并且逐渐显示它们
        self.play(
            *[GrowArrow(arrow) for arrow in gravity_field_arrows],
            run_time=1.5
        )

        # self.wait()

        arrow_mg = Arrow(
            start = qiu.get_center_of_mass(),
            end = qiu.get_center()+DOWN*5,
            buff = 0,
            color = WHITE
        )

        self.play( 
            self.camera.frame.animate.set(width = 20).shift(DOWN*1.5),
            *[FadeOut(arrow, run_time=2.5) for arrow in gravity_field_arrows],
            Create(arrow_mg, run_time = 1.5)
        )

        label_arrow_mg = Text("mg")
        label_arrow_mg.next_to(arrow_mg, RIGHT)
        self.play(
            Write(label_arrow_mg)
        )

        self.wait()

        text_q = Text("+q", font_size=50)
        text_q.next_to(text_m, UP*1.5)
        self.play(
            Write(text_q),
            Flash(
                qiu,
                line_length=0.44444,
                num_lines=30, 
                color=YELLOW,
                flash_radius=1.11111,
                time_width=0.25, run_time=1,
                rate_func = rush_from
            )
        )

        # 定义电场箭头的相关参数
        num_arrows = 10  # 箭头的数量
        spacing = 1.5    # 箭头之间的间距
        arrow_length = 10 # 箭头长度

        # 创建一组水平向左的箭头
        electric_field_arrows = VGroup(*[
            Arrow(
                start=RIGHT * arrow_length / 2, 
                end=LEFT * arrow_length / 2,
                color=YELLOW
            ).shift(UP * (i - num_arrows // 2) * spacing)
            for i in range(num_arrows)
        ])

        # 将电场箭头移动到场景合适的位置
        electric_field_arrows.shift(DOWN * 1)

        # 添加电场箭头到场景中，并且逐渐显示它们
        self.play(
            *[GrowArrow(arrow) for arrow in electric_field_arrows],
            run_time=1.5
        )

        arrow_qE = Arrow(
            start = qiu.get_center_of_mass(), 
            end = qiu.get_center()+LEFT*5 /4*3,
            buff = 0,
            color = WHITE
        )

        self.play( 
            self.camera.frame.animate.set(width = 20).shift(LEFT*1),
            *[FadeOut(arrow, run_time=2.5) for arrow in electric_field_arrows],
            Create(arrow_qE, run_time = 1.5)
        )


        label_arrow_qE = Text("qE")
        label_arrow_qE.next_to(arrow_qE, UP)
        self.play(
            Write(label_arrow_qE)
        )


        self.wait()

        self.play(
            Indicate(arrow_mg),
            FocusOn(label_arrow_mg)
        )

        self.play(
            Indicate(arrow_qE),
            FocusOn(label_arrow_qE)
        )

        arrow_Fhe = Arrow(
            start = qiu.get_center_of_mass(),
            end = qiu.get_center() + DOWN*5 + LEFT*5/4*3,
            buff=0,
            color = WHITE
        )
        self.play(
            Create(arrow_Fhe)
        )

        
    

        self.wait()

        self.wait()

        self.wait()

        self.wait()
