from manim import *
import manimpango

class fontlist(MovingCameraScene):
    def construct(self):
        print(manimpango.list_fonts())
        text = Text(
            "得意黑",
            font='Smiley Sans Oblique',
        )
        self.add(text)

        MyTexTemplate = TexTemplate(
            tex_compiler="xelatex",
            output_format='.xdv',
        )
        MyTexTemplate.add_to_preamble(r"\usepackage{fontspec}\setmainfont{Smiley Sans Oblique}")

        tex = Tex(
            "得意黑",
            tex_template=MyTexTemplate,
            color = BLUE,
        ).next_to(text, DOWN)
        self.add(tex)
        
        # text_wiki = Text(
        #     "The term differential is used nonrigorously in calculus to refer to an infinitesimal change in some varying quantity.",
        #     font='Cascadia Code',
        # ).next_to(tex, DOWN).scale(0.2222)
        # background_rect_text_wiki = BackgroundRectangle(text_wiki, color=GREY, fill_opacity=0.2)
        # self.add(text_wiki)
        # self.add(background_rect_text_wiki)
        
        # self.camera.background_color = WHITE  # 设置相机的背景颜色为白色
        
        # self.camera.frame.shift(UP * 0.88888888).set(width=8)
        
        # MyTexTemplate = TexTemplate(
        #     tex_compiler="xelatex",
        #     output_format='.xdv',
        # )
        # MyTexTemplate.add_to_preamble(r"\usepackage{fontspec}\setmainfont{Smiley Sans Oblique}")

        # tex1 = Tex(
        #     "KEEP",
        #     # tex_template=MyTexTemplate,
        #     color = BLACK,
        # ).shift( UP * 2.22222222)
        
        # tex2 = Tex("THINGS", color = BLACK).next_to(tex1, DOWN)
        # tex3 = Tex("PURE", color = BLACK).next_to(tex2, DOWN)
        # tex4 = Tex("AND", color = BLACK).next_to(tex3, DOWN)
        # tex5 = Tex("JOYFUL", color = BLACK).next_to(tex4, DOWN)

        # self.add(tex1, tex2, tex3, tex4, tex5)