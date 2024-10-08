from manim import *
import os

class ComplexNumberScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        #tex_template
        # tex_template = TexTemplate.from_file(os.path.join("units", "template.tex"), tex_compiler="xelatex", output_format=".xdv")
        tex_template = TexTemplateFromFile(tex_compiler="xelatex", output_format=".xdv", tex_filename = "template.tex")
        SingleStringMathTex.set_default(tex_template = tex_template)
        MathTex.set_default(tex_template = tex_template)
        Tex.set_default(tex_template = tex_template)

        # Create LaTeX text
        text1 = MathTex(r"\text{已知复数 } z_1, z_2, \text{ 满足 } z_1 \neq z_2,").set_color(BLACK)
        text2 = MathTex(r"\text{若 } z_1, z_2 \text{ 同时满足 } |z| = 1,").set_color(BLACK)
        text3 = MathTex(r"\text{且 } |z-1| = |z-i|,").set_color(BLACK)
        text4 = MathTex(r"\text{则 } |z_1 - z_2| = \underline{\quad\quad\quad\quad\quad}").set_color(BLACK)

        # Arrange the texts in a vertical layout
        texts = VGroup(text1, text2, text3, text4).arrange(DOWN)

        # Add the texts to the scene
        for text in texts:
            self.add(text)
            # self.play(Write(text))
            # self.wait(1)

        # # Wait before ending the scene
        # self.wait(2)

if __name__ == "__main__":
    from manim import *
    config.media_width = "75%"
    config.verbosity = "WARNING"
    scene = ComplexNumberScene()
    scene.render()
