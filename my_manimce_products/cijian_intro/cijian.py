from manim import *
from PIL import Image
import tempfile

class Cijian(MovingCameraScene):
    def construct(self):
        
        kuang_image_path = "album_kuang.png"
        kuang_image = Image.open(kuang_image_path)
        kuang_image = kuang_image.convert("RGBA")  # 将图像转换为RGBA模式
        
        # 对图像进行颜色处理，将某种颜色设为透明色
        r, g, b = 68, 247, 0  # 要设为透明的颜色
        data = kuang_image.getdata()
        new_data = []
        for item in data:
            if item[0] == r and item[1] == g and item[2] == b:
                new_data.append((r, g, b, 0))  # 将指定颜色设为透明
            else:
                new_data.append(item)
        kuang_image.putdata(new_data)
        
        # 创建一个临时文件并保存处理后的图像
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
            temp_image_path = tmp.name
            kuang_image.save(temp_image_path)
        
        # 创建一个ImageMobject对象，并使用临时文件的路径
        image = ImageMobject(temp_image_path)
        
        # 设置图片的位置和大小
        image.move_to(ORIGIN)
        image.scale(2)
        
        # 将图片添加到场景中
        self.add(image)
        
        # 显示场景
        self.wait()