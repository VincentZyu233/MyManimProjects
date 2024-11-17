from __future__ import annotations

from manimlib import *
import numpy as np

def quad(axis: np.ndarray, angle: float):
    vec = unit(angle/2)
    return np.array([axis[0]*vec[1], axis[1]*vec[1], axis[2]*vec[1], vec[0]])

#################################################################### 

def perspective(camera: CameraFrame, return_ratio: bool = False):
    position = camera.get_center()  # 获取相机的位置
    distance = camera.get_focal_distance()  # 获取相机的焦距
    orientation = camera.get_orientation().as_matrix()  # 获取相机的方向矩阵
    coordinate = [np.dot(orientation.T, base) for base in [RIGHT, UP, OUT]]  # 计算相机坐标系的基向量
    def util_0(point: np.ndarray):
        return np.dot(orientation, point) + position  # 坐标转换函数，将点从世界坐标系转换到相机坐标系
    def util(point: np.ndarray):
        point -= position  # 将点减去相机位置的偏移量
        return np.dot(orientation.T, point)  # 坐标转换函数，将点从相机坐标系转换到世界坐标系
    def util_2(point: np.ndarray):
        raw = np.dot(orientation.T, point - position) - distance*OUT  # 将点从世界坐标系转换到相机坐标系，并考虑焦距
        if math.isclose(raw[2], 0):  # 如果点的Z坐标接近于0（避免除以零错误）
            ratio = 0
            point = np.array([10000*raw[0], 10000*raw[1], 0])  # 将点设置为一个大的值，避免除以零错误
            return 
        else:
            ratio = -distance/raw[2]  # 计算透视投影的比率
            point = raw*ratio + distance*OUT  # 应用透视投影到点
        if return_ratio:
            return point, ratio  # 返回透视投影后的点和比率
        else:
            return point  # 只返回透视投影后的点
    return util_2  # 返回用于透视变换的函数

class Test_1(FrameScene):
    def construct(self):
        notice = FixedNotice("示例文本", "请　模仿")
        # notice = VMobject(stroke_width = 0, fill_opacity = 1, is_fixed_in_frame = True)
        # note = Notice("示例文本", "请　模仿")
        # notice.set_points(note.get_all_points())

        dots = [Dot(0.5*(i*RIGHT + j*UP), color = GREY).scale(1.5) for i in range(-20, 21) for j in range(-20, 21)]
        self.add(*dots)
        camera = self.camera.frame
        quadternion = quaternion_mult(quad(RIGHT, PI/4)) #, quad(UP, PI/8)
        camera.set_orientation(Rotation(quadternion)).shift(2*OUT)
        # func = perspective(camera)
        def pers_updater(reference: Dot):
            def util(mob: VMobject):
                func = perspective(camera)
                mob.set_points(reference.copy().apply_function(func).scale(2/3).get_points())
            return util
        dots_2 = [VMobject(is_fixed_in_frame = True, color = RED, stroke_width = 0, fill_opacity = 1).add_updater(pers_updater(dot)) for dot in dots]
        self.add(*dots_2, notice)
        self.wait(1)
        self.play(camera.animate.set_orientation(Rotation(quaternion_mult(quad(RIGHT, PI/4), quad(UP, -PI/4)))).shift(IN), run_time = 3)
        self.wait(1)

class Test_2(FrameScene): 
    def construct(self):
        matrix = np.array([[1, 0, 0], [0, np.cos(PI/4), -np.sin(PI/4)], [0, np.sin(PI/4), np.cos(PI/4)]])
        # func = lambda t: np.dot(matrix, t)
        # dots = [Dot(0.5*(i*RIGHT + j*UP)).apply_function(func).fix_in_frame() for i in range(-5, 6) for j in range(-3, 4)]
        # self.add(*dots)

        distance = self.camera.frame.get_focal_distance()
        def func(p: np.ndarray):
            raw = np.dot(matrix, p) - distance*OUT
            if math.isclose(raw[2], 0):
                return np.array([10000*raw[0], 10000*raw[1], 0])
            else:
                return -raw*distance/raw[2] + distance*OUT
        dots = [Dot(0.8*(i*RIGHT + j*UP)).apply_function(func).fix_in_frame() for i in range(-20, 21) for j in range(-20, 21)]
        self.add(*dots)
        
class Test_3(FrameScene):
    def construct(self):
        dots = [Dot(color = RED).shift(2*(i*RIGHT + j*UP)) for i in range(-2, 3) for j in range(-2, 3)]
        camera = self.camera.frame
        quadternion = quaternion_mult(quad(RIGHT, PI/4))
        camera.set_orientation(Rotation(quadternion)).shift(2*OUT)
        icons = [ImageMobject("cane.png", height = 0.5).fix_in_frame().shift(2*(i*RIGHT + j*UP)) for i in range(-2, 3) for j in range(-2, 3)]
        
        # func = perspective(camera)
        # for dot, icon in zip(dots, icons):
        #     position = func(dot.get_center())
        #     icon.move_to(position)

        def pers_updater(reference: Dot):
            def util(mob: VMobject):
                func = perspective(camera)
                mob.move_to(func(reference.get_center()))
            return util
        for dot, icon in zip(dots, icons):
            icon.add_updater(pers_updater(dot))
            
        self.add(*dots, *icons)
        self.wait(1)
        self.play(camera.animate.set_orientation(Rotation(quaternion_mult(quad(RIGHT, PI/4), quad(UP, -PI/4)))).shift(IN), run_time = 3)
        self.wait(1)

class Test_4(FrameScene):
    def construct(self):
        dots = [Dot(color = RED).shift(2*(i*RIGHT + j*UP)) for i in range(-2, 3) for j in range(-2, 3)]
        camera = self.camera.frame
        quadternion = quaternion_mult(quad(RIGHT, PI/4))
        camera.set_orientation(Rotation(quadternion)).shift(2*OUT)
        icons = [ImageMobject("cane.png", height = 0.5).fix_in_frame().shift(2*(i*RIGHT + j*UP)) for i in range(-2, 3) for j in range(-2, 3)]

        def pers_updater(reference: Dot):
            def util(mob: VMobject):
                func = perspective(camera, return_ratio = True)
                position, ratio = func(reference.get_center())
                mob.restore().move_to(position).scale(ratio)
            return util
        for dot, icon in zip(dots, icons):
            icon.save_state().add_updater(pers_updater(dot))
            
        self.add(*dots, *icons)
        self.wait(1)
        self.play(camera.animate.set_orientation(Rotation(quaternion_mult(quad(RIGHT, PI/4), quad(UP, -PI/4)))).shift(IN), run_time = 3)
        self.wait(1)

class Test_5(FrameScene):
    def construct(self):
        dots = [Dot(color = RED).shift(2*(i*RIGHT + j*UP)) for i in range(-2, 3) for j in range(-2, 3)]
        camera = self.camera.frame
        quadternion = quaternion_mult(quad(RIGHT, PI/4))
        camera.set_orientation(Rotation(quadternion)).shift(2*OUT)
        icons = [ImageMobject("cane.png", height = 0.5).shift(2*(i*RIGHT + j*UP)).save_state() for i in range(-2, 3) for j in range(-2, 3)]

        def icon_updater(mob: VMobject):
            position = mob.get_center()
            orientation = camera.get_orientation().as_matrix()
            mob.restore().apply_function(lambda t: np.dot(orientation, t), about_point = mob.get_center())
            mob.move_to(position)
        for icon in icons:
            icon.save_state().add_updater(icon_updater)
            
        self.add(*dots, *icons)
        self.wait(1)
        self.play(camera.animate.set_orientation(Rotation(quaternion_mult(quad(RIGHT, PI/4), quad(UP, -PI/4)))).shift(IN), run_time = 3)
        self.wait(1)

#################################################################### 

class Apple(TexturedSurface):
    def __init__(self, **kwargs):

        def func(u: float, v: float):
            position_raw = (-np.sin(3*v)+3*np.sin(v))/4*unit(u) + (-np.cos(3*v)+3*np.cos(v))/np.sqrt(8)*OUT
            position_raw[0] *= 1.05 + position_raw[2]*0.1
            position_raw[1] *= 1.05 + position_raw[2]*0.1
            position_raw[1] *= interpolate(1, position_raw[0], 0.03)
            position_raw[2] *= interpolate(1, position_raw[0], 0.03)
            return position_raw
        vanilla = ParametricSurface(func, u_range = (0, TAU), v_range = (0, PI))
        super().__init__(vanilla, "apple_texture.jpg", **kwargs)

class Test_6(FrameScene):
    def construct(self):
        def func(u: float, v: float):
            position_raw = (-np.sin(3*v)+3*np.sin(v))/4*unit(u) + (-np.cos(3*v)+3*np.cos(v))/np.sqrt(8)*OUT
            # position_raw = np.array([np.cos(u) * np.sin(v), np.sin(u) * np.sin(v), -7/6*np.cos(v) + 1/3*np.cos(v)**5])
            position_raw[0] *= 1.05 + position_raw[2]*0.1
            position_raw[1] *= 1.05 + position_raw[2]*0.1
            position_raw[1] *= interpolate(1, position_raw[0], 0.03)
            position_raw[2] *= interpolate(1, position_raw[0], 0.03)
            return position_raw
        vanilla_apple = ParametricSurface(func, u_range = (0, TAU), v_range = (0, PI)).shift(2*LEFT)
        # apple = TexturedSurface(vanilla_apple, "apple_texture.jpg").shift(4*RIGHT)
        apple = Apple().shift(2*RIGHT)
        camera = self.camera.frame
        quadternion = quaternion_mult(quad(RIGHT, PI/2))
        camera.set_orientation(Rotation(quadternion)).shift(OUT)
        alpha = ValueTracker(0.0)
        beta = ValueTracker(0.0)
        def float_updater(t: ValueTracker):
            def util(mob: Surface):
                angle = t.get_value()
                mob.restore().shift(0.05*np.sin(5*angle)*OUT).rotate(angle)
            return util
        vanilla_apple.save_state().add_updater(float_updater(alpha))
        apple.save_state().add_updater(float_updater(beta))
        self.add(vanilla_apple, apple).play(alpha.animate.set_value(TAU), beta.animate.set_value(-TAU), run_time = 20, rate_func = linear)

#################################################################### 

class Template(FrameScene):
    def construct(self):
        self.notices = [Notice("示例文本", "请　模仿")]
        self.notice = self.notices[0]