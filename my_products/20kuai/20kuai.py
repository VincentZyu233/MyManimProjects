from manim import *


class test(MovingCameraScene):
    def construct(self):
    
        tri_abc = Polygon([0,0,0], [0,2,0], [2,0,0], 
                          fill_opacity=0.2222, fill_color='#66CCFF', stroke_width=2, stroke_color='#00BFFF' )
        tri_abc.shift(DOWN*0.4444 + RIGHT*2.2222).scale(1.2222)
        self.play( Create(tri_abc) )
        
        # print(tri_abc.get_vertices() )
        # print(tri_abc.get_vertices()[0] )
        
        point_a, point_b, point_c = tri_abc.get_vertices()[2], tri_abc.get_vertices()[0], tri_abc.get_vertices()[1]
        
        label_a = Tex('A').move_to( point_a )
        label_b = Tex('B').move_to( point_b )
        label_c = Tex('C').move_to( point_c )
    
        #  MathTex(r"2x_1 + \;\: x_2 +  \;\: x_3 \qquad\quad\! = 4"),
        tex1 = MathTex(r"in \: Rt\triangle ABC, \; \angle B = 90^\circ").next_to(tri_abc, LEFT).shift(LEFT*2.8888)
        
        self.play( 
            Write(tex1),
            Succession(
                Write(label_a),
                Write(label_b),
                Write(label_c),
                lag_ratio=0.4444
            )
        )
        
        zhijiao = Square(side_length=0.2222).move_to(point_b+UP*0.1111+RIGHT*0.1111)
        # zhijiao.set_stroke(about_edge = [0,1], opacity=0)
        self.play(Create(zhijiao))
        
        ab_brace = Brace( tri_abc, DOWN )
        bc_brace = Brace( tri_abc, LEFT )
        
        tex2 = MathTex(r"AB \; = \; BC \; = \; 2").next_to(tex1, DOWN).shift(LEFT*0.8888)
        
        self.play(
            Write(tex2),
            Succession(
                Create(ab_brace),
                Create(ab_brace.get_text('2')),
                Create(bc_brace),
                Create(bc_brace.get_text('2')),
                lag_ratio=0.4444
            )
        )
        
        tri_cnm = tri_abc.copy()
        self.play(Create(tri_cnm))
        
        cnm_roration = Rotate(tri_cnm, angle=PI/3, about_point=point_c)     
        
        tex3 = MathTex(r"\triangle ABC \xrightarrow{  \circlearrowleft \text{rotate } 60^\circ} \triangle CNM").next_to(tex2,DOWN)
        tex3.shift(RIGHT*1.1111)
        
        self.play( 
            Succession(
                Write(tex3),
                cnm_roration
            )
        )
        
        point_n, point_m = tri_cnm.get_vertices()[0], tri_cnm.get_vertices()[2]
        
        label_n = Tex('N').move_to( point_n )
        label_m = Tex('M').move_to( point_m )
        
        self.play( Succession(
            Write(label_n),
            Write(label_m),
            lag_ratio=0.4444
        ))
        
        line_bm = Line(point_b, point_m, color=YELLOW )
        tex4 = MathTex(r"connect \;\;\; BM").next_to(tex3, DOWN).shift(LEFT*2.2222+RIGHT*0.4444+RIGHT*0.2222)
        
        self.play(
            Succession(
                Create(line_bm),
                Write(tex4),
            )    
        )
        
        self.wait()