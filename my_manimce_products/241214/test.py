from manim import *

class TextFadeInAndMoveDown(Scene):
    def construct(self):
        # 创建一个文本对象
        text = Text("Hello, Manim!")
        
        # 设置起始状态
        text.save_state()  # 保存原始状态以便复原
        
        # 设置目标状态
        target_text = text.copy()
        target_text.shift(DOWN * 2)  # 目标位置是向下移动2个单位
        target_text.set_opacity(1)   # 最终完全不透明
        
        # 动画：从透明到不透明并同时向下移动
        self.play(
            Restore(text),  # 恢复到保存的状态，即初始状态（如果需要）
            text.animate.set_opacity(0),  # 设置初始透明度为0
            text.animate.move_to(target_text.get_center()),  # 移动到目标位置
            run_time=2,  # 动画持续时间为2秒
            rate_func=linear  # 线性变化，也可以选择其他速率函数如 smooth
        )
        self.wait()