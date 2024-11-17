from manim import *

class SVGWriteAnimation(Scene):
    def construct(self):
        
        text = Text("qwq")
        self.play(Write(text))
        
        # 加载 SVG 文件
        logo = SVGMobject("jianglin_logo.svg").scale(10)
        self.play(Create(logo))

        logo_rect = SurroundingRectangle(logo, color=WHITE)
        self.play(Create(logo_rect))

        # 等待一段时间以便观看动画
        self.wait(2)

# 在命令行中运行以下命令以渲染动画：
# manim -pql jiangllin.py SVGWriteAnimation