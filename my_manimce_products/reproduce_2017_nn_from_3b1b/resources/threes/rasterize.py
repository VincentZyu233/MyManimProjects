"""
cd D:\MANIM\Projects\MyManimProjects\my_manimgl_products\_2017nn_from_3b1b\resources\threes
cd D:\MANIM\Projects\MyManimProjects\my_manimgl_products  

.\myenv-1.7.1\Scripts\Activate.ps1

python rasterize.py
"""

import cv2


def rasterize_image(input_path, output_path, size=(28, 28)):
    """
    将输入图片光栅化为指定大小，并保存结果。
    
    Args:
        input_path (str): 输入图片路径。
        output_path (str): 输出图片路径。
        size (tuple): 输出图片尺寸 (宽, 高)。
    """
    # 读取图像为灰度模式
    image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print(f"无法找到文件: {input_path}")
        return

    # 调整图像尺寸
    resized_image = cv2.resize(image, size, interpolation=cv2.INTER_AREA)

    # 保存光栅化结果
    cv2.imwrite(output_path, resized_image)

    print(f"光栅化完成，已保存到: {output_path}")


if __name__ == "__main__":
    

    input_filename = "three_1.png"
    output_filename = "three_1_rasterized.png"
    rasterize_image(input_filename, output_filename)
