from manim import *

class Potato_cover(MovingCameraScene):
    def construct(self):
        self.camera.background_color = WHITE  # 设置相机的背景颜色为白色
        
        image_potato = ImageMobject(r"C:\Users\Administrator\Desktop\tmp\potato_pfp.jpg").scale(1.2222)
        
        tex_potato = Tex(r"WHITE POTATO", color = BLACK, font_size = 88).next_to(image_potato, UP)
        tex_potato.shift(DOWN*0.8888)

        tex_selected = ImageMobject(r"F:\potato作品集\_tex精选作品集.png").set_opacity(0.6666)
        tex_selected.next_to(image_potato, DOWN)
        tex_selected.shift(UP*0.8888)
    
    # manim -pqh potato_intro.py --disable_caching

        # self.add(tex_selected)
        self.add(image_potato)
        self.add(tex_potato)
        
        
if __name__ == "__main__":
    scene = Potato_cover(camera_config={"background_color": WHITE})
    scene.render()