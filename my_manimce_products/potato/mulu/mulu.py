from manim import *
import manimpango

class mulu(MovingCameraScene):
    def construct(self):
        # print(manimpango.list_fonts())
        # text = Text(
        #     "得意黑",
        #     font='Smiley Sans Oblique',
        # )
        # self.add(text)

        self.camera.background_color = "#ffffff"
        
        MyTexTemplate = TexTemplate(
            tex_compiler="xelatex",
            output_format='.xdv',
        )
        MyTexTemplate.add_to_preamble(r"\usepackage{fontspec}\setmainfont{Smiley Sans Oblique}")

        self.play(
            self.camera.frame.animate.set( width = 6 ),
        )

        tex_mulu = Tex(
            "目录",
            tex_template=MyTexTemplate,
            color = BLACK,
        )
        # self.add(tex)
        self.play(
            Write(tex_mulu)
        )
        
        self.play(
            self.camera.frame.animate.set( width = 18 )
        )
        self.play(
            self.camera.frame.animate.shift( DOWN*4.44444444 )
        )

        title_list = [
            Tex("这是一个标题1", tex_template=MyTexTemplate,  color = BLACK),
            Tex("这是一个标题2", tex_template=MyTexTemplate,  color = BLACK),
            Tex("这是一个标题3", tex_template=MyTexTemplate,  color = BLACK),
            Tex("这是一个标题4", tex_template=MyTexTemplate,  color = BLACK),
            Tex("这是一个标题5", tex_template=MyTexTemplate,  color = BLACK),
            Tex("这是一个标题6", tex_template=MyTexTemplate,  color = BLACK),
            Tex("这是一个标题7", tex_template=MyTexTemplate,  color = BLACK),
            Tex("这是一个标题8", tex_template=MyTexTemplate,  color = BLACK),
        ]
        
        title_list[0].next_to(tex_mulu, DOWN*2.22222222)
        for i in range(1, len(title_list)):
            title_list[i].next_to(title_list[i-1], DOWN*1.11111111)
            
        horizen_height = title_list[0].get_height()
        for i in range(0,len(title_list)):
            self.play( FadeIn(title_list[i], shift=UP) )
        
        # manim -pql mulu.py --disable_caching
        
        self.wait(3)