



from manim import *

from manim.typing import Vector3

# manim -pql liji.py --disable_caching

class Test_camera(ThreeDScene):

    def construct(self):

        axes = ThreeDAxes( x_length=8.888, x_range=[-4,4,0.5], y_length=8.8888, y_range=[-4,4,0.5], z_length=8.8888-2.2222, z_range=[-4,4,0.5] )
        # axes.shift(DOWN*2.2222)
        # cube_yellow = Cube(fill_color=YELLOW, stroke_width=2, stroke_color=WHITE)
        # sphere_blue = Sphere(fill_color=BLUE, checkerboard_colors=None).shift(OUT * 2)
        # cube_green = Cube(fill_color=GREEN).scale([2, 0.5, 0.5]).shift(RIGHT * 3.25)

        phi_0, theta_0 = 0, 0 # 起始角度
        phi, theta = 60 * DEGREES, -120 * DEGREES # 目标角度

        self.set_camera_orientation(phi=phi_0, theta=theta_0)
        # self.add(cube_yellow, sphere_blue, cube_green)
    
        
        FANGDA = 2
        rect_abcd = Rectangle(width=2*FANGDA, height=1*FANGDA, fill_opacity=0.4444, fill_color='#66CCFF', stroke_width=2, stroke_color='#00BFFF')
        rect_abcd.move_to(axes.center())
        point_a = rect_abcd.get_corner(UL)
        point_b = rect_abcd.get_corner(UR)
        point_c = rect_abcd.get_corner(DR)
        point_d = rect_abcd.get_corner(DL)

        toumingdu = ValueTracker(0.4444)
        
        tri_abd = Polygon(point_a, point_b, point_d, 
                          fill_opacity=toumingdu.get_value(), fill_color='#66CCFF', stroke_width=2, stroke_color='#00BFFF')
        
        tri_bcd = Polygon(point_d, point_b, point_c, 
                          fill_opacity=toumingdu.get_value(), fill_color='#66CCFF', stroke_width=2, stroke_color='#00BFFF')
        
        a1, b1, d1 = np.array(tri_abd.get_vertices()[0]), np.array(tri_abd.get_vertices()[1]), np.array(tri_abd.get_vertices()[2])
        d2, b2, c2 = np.array(tri_bcd.get_vertices()[0]), np.array(tri_bcd.get_vertices()[1]), np.array(tri_bcd.get_vertices()[2])
        # c2.add_updater( lambda mob: mob.become( np.array(tri_bcd.get_vertices()[2]) ) )
        
        # print( np.array(tri_bcd.get_vertices()[2]) )

        # self.play(FadeIn(rect_abcd))
        self.play(Create(axes))
        self.wait(0.2222)
        self.play(Write(rect_abcd))
        self.wait(0.4444)
        self.move_camera(zoom=1.2222,run_time=0.8888)

        # self.wait()
        # dt = 1/15
        # delta_phi, delta_theta = (phi - phi_0) / 30, (theta - theta_0) / 60
        # for i in range(30):
        #     phi_0 += delta_phi
        #     self.set_camera_orientation(phi=phi_0, theta=theta_0)
        #     self.wait(dt)
        # for i in range(60):
        #     theta_0 += delta_theta
        #     self.set_camera_orientation(phi=phi_0, theta=theta_0)
        #     self.wait(dt)
        # self.wait(2)
        
        
        self.set_camera_orientation(phi=0* DEGREES,theta=0*DEGREES,distance=8)
        self.begin_ambient_camera_rotation(rate=0.0404)
        # self.move_camera(zoom=1.4444,run_time=0.8888)
        
        print(tri_bcd.get_vertices())
        print("qaq?")
        print(tri_bcd.get_vertices()[0])
        print(tri_bcd.get_vertices()[1])
        print(tri_bcd.get_vertices()[2])
        
        label_a = MathTex('A').move_to(point_a)
        # label_a.rotate(PI/2, axis=OUT)
        
        label_b = MathTex('B').move_to(point_b)
        
        ################################################ manim -ql liji.py --disable_caching
        print("c is here: ", tri_bcd.get_vertices()[0])
        label_c = MathTex('C').move_to(point_c)
        # label_c = VMobject()
        # label_c.add_updater( lambda x: x.become(
        #     MathTex('C').move_to(
        #         tri_bcd.get_vertices()[0]
        #     )
        # ))
        
        label_d = MathTex('D').move_to(point_d)
        
        self.add_fixed_orientation_mobjects(label_a, label_b, label_c, label_d)
        
        self.play(Write(label_a), run_time=0.8888)
        self.wait(0.0808)
        self.play(Write(label_b), run_time=0.8888)
        self.wait(0.0808)
        self.play(Write(label_c), run_time=0.8888)
        self.wait(0.0808)
        self.play(Write(label_d), run_time=0.8888)
        self.wait(0.0808)
        
        self.move_camera(theta=45*DEGREES,phi=45*DEGREES,run_time=2.8888,distance=4)
        self.wait(0.8888)
        # self.move_camera(theta=0*DEGREES,phi=0*DEGREES,run_time=2.8888,distance=4)
        
        # self.play( Flash(a1) )
        # self.play( Flash(b1) )
        # self.play( Flash(d1) )
        # self.play( Flash(b2) )
        # self.play( Flash(c2) )
        # self.play( Flash(d2) )

        # return -(np.cos(np.pi * t) - 1) / 2

        brace_ab = Brace(rect_abcd, UP )
        len_ab = brace_ab.get_text('2').rotate(180*DEGREES)
        brace_bc = Brace(rect_abcd, RIGHT )
        len_bc = brace_bc.get_text('1').rotate(180*DEGREES)
        self.play(Write(brace_ab), Write(len_ab))
        self.play(Write(brace_bc), Write(len_bc))
        
        self.wait(0.8888)
        self.play(
            FadeOut(brace_ab),
            FadeOut(len_ab),
            FadeOut(brace_bc),
            FadeOut(len_bc)
        )
        
        self.wait(0.8888)
        
        # self.move_camera(theta=45*DEGREES,phi=45*DEGREES,run_time=2.8888,distance=4)
        self.play(
            FadeOut(rect_abcd),
            Create(tri_abd),
            Create(tri_bcd),
        )
        
        bcd_zhuandong = 0
        def bcd_rotate(angle, runtime=1.4444): #angle danwei is degrees not rad
            global bcd_zhuandong
            bcd_zhuandong += angle
            
            bcd_rotate_animation = Rotate( VGroup(tri_bcd, label_c),
                                  angle= (-angle)*DEGREES, 
                                #   about_edge=Line(point_b, point_d),
                                    about_point=ORIGIN, 
                                  axis=[2,1,0],
                                  
                                  )

            self.play(bcd_rotate_animation, run_time = runtime)
 
        
        
        # self.begin_ambient_camera_rotation(rate=0.22)
        
        plane = Surface(
            lambda u, v: np.array([u, 0.5, v]),
            u_range=(-2.2222, 2.2222),
            v_range=(-2.2222, 2.2222),
            stroke_width=0.8888
        )
        # 设置平面颜色和透明度
        plane.set_color(YELLOW)
        plane.set_fill(opacity=0.2222)
        # 将平面添加到场景中
        # self.play( Create(plane) )
        # self.play(FadeOut(plane))
        
        # manim -ql liji.py --disable_caching
        
        self.move_camera(phi=(44.4444+8.8888)*DEGREES,run_time=2.8888,distance=4)
        self.move_camera(zoom=1.8888,run_time=2.2222, rate_func = rate_functions.ease_in_out_quint)
        self.wait(0.2222)
        bcd_rotate(120, 0.8888)
        # self.wait(0.1111)
        bcd_rotate(-60, 0.8888+0.2222)
        # self.wait(0.4444)
        bcd_rotate(30, 0.8888+0.2222)
        bcd_rotate(-30+8.8888, 0.8888)

        self.move_camera(phi=(44.4444+22.2222)*DEGREES,run_time=0.8888,distance=4)

        self.play( Indicate(label_c, scale_factor=2.2222), run_time=2.2222-0.8888 )
        self.wait(0.2222)
        self.play( Wiggle(label_c))        
        self.wait(0.8888)
        
        self.wait(0.8888)
        linecb = always_redraw( lambda: 
            Line(np.array(tri_bcd.get_vertices()[2]),b2)
        )
        linead = Line(a1,d1)
        self.play( Create(linecb), run_time = 0.4444 )
        self.play( Indicate(linecb), run_time = 0.4444 )
        self.wait(0.4444)
        self.play( Create(linead), run_time = 0.4444 )
        self.play( Indicate(linead), run_time = 0.4444 )
        self.wait(0.8888)
        self.play(
            FadeOut(linecb),
            FadeOut(linead)
        )
        
        
        # apie, dpie, bpie, cpie = tri_bcd.get_vertices()[0], tri_bcd.get_vertices()[1], tri_bcd.get_vertices()[2], tri_abd.get_vertices()[0]
        apie, dpie, bpie, cpie = np.array(tri_bcd.get_vertices()[0]), np.array(tri_bcd.get_vertices()[1]), np.array(tri_bcd.get_vertices()[2]), np.array(tri_abd.get_vertices()[0])
         
        # tri_cpieab = Polygon(cpie, apie, bpie,
        #                       fill_opacity=0.2222, fill_color='#66CCFF', stroke_width=2, stroke_color='#00BFFF' )
        # tri_cpiead = Polygon(cpie, apie, dpie,
        #                       fill_opacity=0.2222, fill_color='#66CCFF', stroke_width=2, stroke_color='#00BFFF' )
        
        tri_cpieab = always_redraw(
            lambda: 
                Polygon(np.array(tri_abd.get_vertices()[0]), np.array(tri_bcd.get_vertices()[0]), np.array(tri_bcd.get_vertices()[2]), 
                              fill_opacity=0.2222, fill_color='#66CCFF', stroke_width=2, stroke_color='#00BFFF', sheen_factor=0.44444,  )
        )
        
        tri_cpiead = always_redraw(
            lambda: 
                Polygon(np.array(tri_abd.get_vertices()[0]), np.array(tri_bcd.get_vertices()[0]), np.array(tri_bcd.get_vertices()[1]), 
                              fill_opacity=0.2222, fill_color='#66CCFF', stroke_width=2, stroke_color='#00BFFF', sheen_factor=0.44444,   )
        )
        
        
        # self.play(Succession(
        #     Flash(cpie),
        #     Flash(apie),
        #     Flash(bpie),
        #     Flash(dpie),
        #     lag_ratio=0.2222
        # ))
        
        
        # self.move_camera(phi=45*DEGREES,run_time=2.2222,distance=8.8888, 
        #                 #  added_anims=[bcd_rotate(-180)]  
        # )
        self.move_camera(zoom=1.1111+0.2222,run_time=0.8888)
        
        self.play(
            FadeIn(tri_cpieab),
            FadeIn(tri_cpiead),
        )
        
        self.wait(8.8888-2.2222)
        
        bcd_rotate(-8.8888)
        bcd_rotate(22.2222*2.2222)
        self.wait(0.2222)
        bcd_rotate(-22.2222*2.2222)
        self.wait(0.2222)
        bcd_rotate(22.2222*2.2222)
        
        
        self.wait(8.8888)
        # 1:11
        # 我先说结论，由于空间中 任意两条直线所成角的最大值就是90度，
        self.wait(8.8888)
        
        # 而在而且三角形旋转的过程中，确实存在某个位置， 使得C‘B与AD所成角是90度，
        
        self.wait(4.4444)
        self.play(
            FadeOut(tri_cpieab),
            FadeOut(tri_cpiead),
        )
        self.wait(0.8888)
        
        bcd_rotate(40, 0.4444)
        bcd_rotate(-120, 0.7777)
        bcd_rotate(120, 0.7777)
        
        
        # self.move_camera(zoom=2.2222,run_time=0.8888)
        self.move_camera(
            zoom=1.1, theta=260*DEGREES,phi=0*DEGREES,run_time=2.2222,distance=8.8888, 
            # added_anims=[bcd_rotate(-180)]  
        )
        
        self.play( Create(linecb), run_time = 0.4444 )
        self.play( Indicate(linecb), run_time = 0.4444 )
        self.wait(0.4444)
        self.play( Create(linead), run_time = 0.4444 )
        self.play( Indicate(linead), run_time = 0.4444 )
        self.wait(0.8888)
        self.play(
            FadeOut(linecb),
            FadeOut(linead)
        )
        
        # self.move_camera(theta=270*DEGREES,phi=0*DEGREES,run_time=2.8888,distance=8.8888, 
        #                 #  added_anims=[bcd_rotate(-180)]  
        #                  )
        bcd_rotate(-120, 0.7777)
        bcd_rotate(120, 0.7777)
        bcd_rotate(-120, 0.7777)
        
        #改角度
        # bcd_rotate(77.77777-7.7777)
        bcd_rotate( 180-bcd_zhuandong )
        
        self.wait(2.2222-0.8888)
        
        ### 1:30###
        self.play( Create(linecb), run_time = 0.4444 )
        self.play( Indicate(linecb), run_time = 0.4444 )
        self.wait(0.4444)
        self.play( Create(linead), run_time = 0.4444 )
        self.play( Indicate(linead), run_time = 0.4444 )
        self.wait(0.8888)
        self.play(
            FadeOut(linecb),
            FadeOut(linead)
        )
        
        self.wait(8.8888-2.2222)
        self.move_camera(
            phi=44.4444*DEGREES,run_time=2.2222-0.8888,distance=8.8888, 
        )
        self.play(
            FadeIn(tri_cpieab),
            FadeIn(tri_cpiead),
        )
        
        # 1:45
        self.play( Indicate( VGroup( tri_abd,tri_bcd, tri_cpieab, tri_cpiead ) ) )
        
        
        self.wait(60*2.2222)
        
        # manim -ql liji.py --disable_caching