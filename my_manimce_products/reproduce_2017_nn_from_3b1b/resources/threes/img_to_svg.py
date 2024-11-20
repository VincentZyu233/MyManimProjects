"""
cd D:\MANIM\Projects\MyManimProjects\my_manimgl_products\_2017nn_from_3b1b\resources\threes
cd D:\MANIM\Projects\MyManimProjects\my_manimgl_products  

python img_to_svg.py
"""


"""
cd /home/vincentzyu/Documents/github-repo/MyManimProjects/my_manimce_products/reproduce_2017_nn_from_3b1b/resources/threes
cd /home/vincentzyu/Documents/github-repo/MyManimProjects/my_manimce_products

python img_to_svg.py
"""


import cv2
import numpy as np
import csv

def image_to_grayscale_svg_and_matrix(input_image_path, output_svg_path, output_matrix_path):
    # Step 1: 读取图片并转换为灰度图
    img = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)
    
    # Step 2: 调整图片大小为 28x28
    img_resized = cv2.resize(img, (28, 28), interpolation=cv2.INTER_AREA)
    
    # Step 3: 归一化灰度值到 [0, 1]
    grayscale_matrix = img_resized / 255.0

    # Step 4: 生成 SVG 文件
    with open(output_svg_path, 'w') as svg_file:
        svg_file.write('<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28">\n')

        # 每个像素点生成一个带透明边框的矩形
        for y in range(28):
            for x in range(28):
                gray_value = grayscale_matrix[y, x]
                # 将灰度值转为 RGB 格式
                color = f"rgb({int(gray_value * 255)}, {int(gray_value * 255)}, {int(gray_value * 255)})"
                svg_file.write(
                    f'<rect x="{x}" y="{y}" width="1" height="1" fill="{color}" '
                    'stroke="none" />\n'
                )

        svg_file.write('</svg>')

    # Step 5: 保存灰度矩阵到 CSV 文件
    with open(output_matrix_path, 'w', newline='') as matrix_file:
        writer = csv.writer(matrix_file)
        writer.writerows(grayscale_matrix)
    
    print(f"SVG image saved to {output_svg_path}")
    print(f"Grayscale matrix saved to {output_matrix_path}")
    return grayscale_matrix

# 使用示例
input_image = "three_4.png"  # 输入图片路径
output_svg = "three_4.svg"  # 输出 SVG 路径
output_matrix = "three_4.csv"  # 输出矩阵路径

# 转换并生成 SVG 和矩阵文件
matrix = image_to_grayscale_svg_and_matrix(input_image, output_svg, output_matrix)

# 打印灰度矩阵
print("Grayscale matrix:")
print(matrix)
