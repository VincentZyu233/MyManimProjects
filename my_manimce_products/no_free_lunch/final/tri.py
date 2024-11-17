from manim import *

class qwqMatrix(Matrix):
    def __init__(self, data, **kwargs):
        # Call the parent class constructor
        super().__init__(data, **kwargs)
        
        # Iterate over matrix elements
        for i, row in enumerate(self.mob_matrix):
            for j, element in enumerate(row):
                # Check if element is -1
                if element.get_tex_string() == "-1":
                    # Set element to be transparent
                    element.set_opacity(0)

class Tridiagonal(MovingCameraScene):
    def construct(self):
        
        def get_DiagonalLine ( mx ) :
            top_left = mx.get_corner(UL)
            bottom_right = mx.get_corner(DR)
            diagonal_line = Line(top_left, bottom_right, color=YELLOW)
            diagonal_line.set_stroke(width=4, opacity=0.8)
            # self.play(Create(diagonal_line))
            return diagonal_line
        
        #对于三对焦矩阵 crout分解可以有更简单的计算方式：
        #以下是伪代码：
        tex_spec = Tex(r"More specifically,").scale(2.2222)
        self.play( FadeIn(tex_spec) )
        tex_given = Tex(r"Given a tridiagonal linear system").next_to(tex_spec, DOWN*2.2222)
        self.play( Create(tex_given) )
        
        self.play(
            self.camera.frame.animate.shift( DOWN * 2.2222 ),
        )
        tex_thatis = Tex(r"that is, coefficient matrix A is a tridiagonal matrix").next_to(tex_given, DOWN).scale(0.7777)
        self.play( Create(tex_thatis) )
        
        matrix_a = Matrix(
            [
                ["a_{11}", "a_{12}", "-1", "-1", "-1", "-1", "-1"], 
                ["a_{21}", "a_{22}", "a_{23}", "-1", "-1", "-1", "-1"], 
                ["-1", "-1", "...", "-1", "-1", "-1", "-1"], 
                ["-1", "-1", "-1", "...", "-1", "-1", "-1"], 
                ["-1", "-1", "-1", "-1", "...", "-1", "-1"], 
                ["-1", "-1", "-1", "-1", "a_{_{n-1,n-2}}", "a_{_{n-1,n-1}}", "a_{_{n-1,n}}"], 
                ["-1", "-1", "-1", "-1", "-1", "a_{a,n-1}", "a_{nn}"], 
            ],
            h_buff = 1.6,
        ).next_to(tex_given, DOWN*2.2222)
        matrix_a.shift(LEFT*2.8888)
        matrix_a.scale(0.8888)
        for i, row in enumerate(matrix_a.get_entries()):
            for j, entry in enumerate(row):
                if matrix_a.get_entries()[i][j].get_tex_string() == "-1":
                    entry.set_opacity(0)  # 隐藏零元素
        diagonalLine_mxa = get_DiagonalLine( matrix_a )
        
        matrix_x = Matrix(
            [
                ["x_{1}"],
                ["x_{2}"],
                ["x_{3}"],
                ["..."],
                ["..."],
                ["..."],
                ["x_{n}"],
            ]
        ).next_to(matrix_a, RIGHT)
        matrix_x.scale(0.8888)
        
        eq = MathTex("=").next_to(matrix_x, RIGHT)
        
        matrix_b = Matrix(
            [
                ["b_{1}"],
                ["b_{2}"],
                ["b_{3}"],
                ["..."],
                ["..."],
                ["..."],
                ["b_{n}"],
            ]
        ).next_to(eq, RIGHT)
        matrix_b.scale(0.8888)
                    
        self.play(
            self.camera.frame.animate.shift( DOWN * 2.2222 ).set( width = 22),
        )
        self.play( Write(matrix_a), Create(diagonalLine_mxa) )
        self.play( Write(matrix_x) )
        self.play( Write(eq), Write(matrix_b) )
        
        tex_which = Tex(r"which is assumed to have a unique solution").next_to(tex_thatis, DOWN*4.4444)
        tex_which.shift( DOWN*4.4444 )
        tex_which.scale(0.7777)
        self.play( Create(tex_which) )
        
        self.play(
            self.camera.frame.animate.shift( DOWN * 2.2222 )
        )
        tex_wecan = Tex(r"we can disign a more convenient algorithm \\ for computer to calculate the solution").next_to(tex_which, DOWN)
        self.play( Create(tex_wecan) )
        
        self.play(
            self.camera.frame.animate.shift( DOWN * 4.4444 ).set( width = 14 )
        )
        tex_likebelow = Tex(r"assume we have a program like below:").next_to( tex_wecan, DOWN*2.2222 )
        self.play( Create(tex_likebelow) )
        
        # text4 = Text("Hello world", t2w={'world':BOLD})
        # text1 = Text(
        #     'Google',
        #     t2c={'[:1]': '#3174f0', '[1:2]': '#e53125',
        #          '[2:3]': '#fbb003', '[3:4]': '#3174f0',
        #          '[4:5]': '#269a43', '[5:]': '#e53125'}, font_size=58).scale(3)
        text_input = Text(
            "INPUT:    the dimension n; the entries of A.",
            t2c = { '[:5]': BLUE },
            t2w = { ' n': BOLD, ' A':BOLD },
        )
        text_input.next_to( tex_likebelow, DOWN*4.4444)
        self.play(
            self.camera.frame.animate.shift( DOWN * 2.2222 ).set( width = 16 )
        )
        self.play( Write(text_input) )
        
        text_output = Text(
            "OUTPUT:    the solution ",
            t2c = { '[:6]': BLUE },
        ).next_to(text_input, DOWN*2.2222)
        text_output.shift( LEFT * 2.8888 ) 
        text_output.shift( LEFT * 0.2023 )
        # tex_x123dotn = Tex(
        #     "$x_1, \, x_2, \, ..., \, x_n$"
        # ).next_to(text_output)
        tex_x123dotn = Tex(
            "$\mathbf{x}_1, \, \mathbf{x}_2, \, ..., \, \mathbf{x}_n$"
        ).scale(1.6666).next_to(text_output, RIGHT)
        tex_x123dotn.shift( DOWN*0.1111 )
        
        self.play( Write(text_output) )
        self.play( Write(tex_x123dotn) )
        
        self.play(
            self.camera.frame.animate.shift( DOWN * 4.4444 ).set( width = 22 )
        )
        # self.play(
        #     self.camera.frame.animate.shift( LEFT * 4.4444 ).set( width = 24.4444 )
        # )
        
        tex_ax_equals_b = Tex(r"AX \, = \, b").next_to(text_input, DOWN*8.8888888).scale(1.1111)
        self.play( Write(tex_ax_equals_b) )
        tex_hint_axb = Tex(r"Remember our aim is to solve: \,").next_to(tex_ax_equals_b, LEFT).scale(0.8888)
        self.play( FadeIn(tex_hint_axb ) )
        
        tex_a_equals_lu = Tex(r"A \, = \, LU").scale(1.1111)
        tex_a_equals_lu.next_to( tex_ax_equals_b, DOWN )
        self.play(
            Write(tex_a_equals_lu)
        )
        tex_hint_alu = Tex(r"And we decompose A into: \,").next_to(tex_a_equals_lu, LEFT).scale(0.8888)
        self.play( FadeIn(tex_hint_alu) )
        
        self.wait(0.2222)
        self.play(
            tex_a_equals_lu.animate.shift(DOWN*2.2222),
            tex_hint_alu.animate.shift(DOWN*2.2222)
        )

        tex_column_alu = Tex(r"\, : \,").next_to(tex_a_equals_lu, RIGHT)
        self.play( FadeIn(tex_column_alu) )
        
        matrix_a = Matrix(
            [
                ["a_{11}", "...", "{a_1j}", "...", "{a_1n}"], 
                ["...", "...", "...", "...", "..."], 
                ["a_{i1}", "...", "a_{ij}", "...", "a_{in}"], 
                ["...", "...", "...", "...", "..."],
                ["a_{n1}", "...", "a_{nj}", "...", "a_{nn}"], 
            ],
            h_buff = 0.8888,
        ).next_to(tex_column_alu, RIGHT*2.2222)
        # matrix_a.shift( DOWN * 2.2222 )
        matrix_a.scale(0.6666)
        
        eqsign = Tex(r"=").next_to(matrix_a, RIGHT)
        
        matrix_l = Matrix(
            [
                ["l_{11}", "-1", "-1", "-1", "-1"], 
                ["...", "...", "-1", "-1", "-1"], 
                ["l_{i1}", "...", "l_{ij}", "-1", "-1"], 
                ["...", "...", "...", "...", "-1"],
                ["l_{n1}", "...", "l_{nj}", "...", "l_{nn}"], 
            ],
            h_buff = 0.8888,
        ).next_to(eqsign, RIGHT)
        matrix_l.shift(LEFT*0.8888)
        matrix_l.scale(0.6666)
        for i, row in enumerate(matrix_l.get_entries()):
            for j, entry in enumerate(row):
                if matrix_l.get_entries()[i][j].get_tex_string() == "-1":
                    entry.set_opacity(0)  # 隐藏零元素
        
        matrix_u = Matrix(
            [
                ["u_{11}", "...", "u_{1j}", "...", "u_{1n}"], 
                ["-1", "...", "...", "...", "..."], 
                ["-1", "-1", "u_{ij}", "...", "u_{jn}"], 
                ["-1", "-1", "-1", "1", "..."],
                ["-1", "-1", "-1", "-1", "u_{nn}"], 
            ],
            h_buff = 0.8888,
        ).next_to(matrix_l, RIGHT)
        matrix_u.shift(LEFT*0.8888)
        matrix_u.scale(0.6666)
        for i, row in enumerate(matrix_u.get_entries()):
            for j, entry in enumerate(row):
                if matrix_u.get_entries()[i][j].get_tex_string() == "-1":
                    entry.set_opacity(0)  # 隐藏零元素
        
        _matrix_alu_ = VGroup( matrix_a, eqsign, matrix_l, matrix_u )
        _matrix_alu_.next_to( tex_a_equals_lu, RIGHT*2.2222 )
        
        self.play( 
            Create( _matrix_alu_ ), run_time = 2.2222
        )
        
        # self.play(
        #     Create(matrix_a),
        #     Create(eqsign),
        #     Create(matrix_l), 
        #     Create(matrix_u),
        # )
        
        tex_lux_equals_b = Tex(r"LUx \, = \, b").next_to(tex_a_equals_lu, DOWN).scale(1.1111)
        tex_lux_equals_b.shift( DOWN * 2.2222 )
        self.play( Write(tex_lux_equals_b) )
        tex_hint_luxb = Tex(r"substitute into the original equation: \,").next_to(tex_lux_equals_b, LEFT).scale(0.8888)
        self.play( FadeIn(tex_hint_luxb) ) 
        
        self.play(
            self.camera.frame.animate.shift( DOWN*4.4444 )
        )
        
        tex_ux_equals_z = Tex(r"Ux \, = \, z").next_to(tex_lux_equals_b, DOWN).scale(1.1111)
        self.play( Write(tex_ux_equals_z) )
        tex_hint_uxz = Tex(r"Then we create a new denotion: \,").next_to(tex_ux_equals_z, LEFT).scale(0.8888)
        self.play(FadeIn(tex_hint_uxz))
        
        self.play( 
            tex_ux_equals_z.animate.shift(DOWN*2.2222),
            tex_hint_uxz.animate.shift( DOWN*2.2222 )
        )
        
        tex_column_uxz = Tex(r"\, : \,").next_to(tex_ux_equals_z, RIGHT)
        self.play( FadeIn(tex_column_uxz) )
        
        matrix_u__ = matrix_u.copy().next_to(tex_column_uxz, RIGHT*2.2222)
        # matrix_u__.shift(DOWN*2.2222)
        matrix_x__ = Matrix(
            [
                ["x_{1}"],
                ["x_{2}"],
                ["x_{3}"],
                ["..."],
                ["x_{n}"],
            ],
        ).scale(0.6666).next_to(matrix_u__, RIGHT)
        
        eq__ = Tex(r"=").next_to( matrix_x__, RIGHT ) 
        matrix_z__ = Matrix(
            [
                ["z_{1}"],
                ["z_{2}"],
                ["z_{3}"],
                ["..."],
                ["z_{n}"],
            ],
        ).scale(0.6666).next_to(eq__, RIGHT)
        
        _matrix_uxz__ = VGroup(matrix_u__, matrix_x__, eq__, matrix_z__)
        self.play(
            Create(_matrix_uxz__)
        )
        
        tex_lz_equals_b = Tex(r"Lz \, = \, b").next_to(tex_ux_equals_z, DOWN*4.4444).scale(1.1111)
        # tex_lz_equals_b.shift(DOWN * 2.2222)
        self.play( Write(tex_lz_equals_b) )
        self.play(
            tex_lz_equals_b.animate.shift( DOWN*2.2222 )
        )
        
        self.play(
            self.camera.frame.animate.shift( DOWN*4.4444 )
        )
        
        tex_hint_lzb = Tex(r"Consequently we convert the original problem into: \,").next_to(tex_lz_equals_b, LEFT).scale(0.8888)
        self.play( FadeIn(tex_hint_lzb) )
        tex_column_lzb = Tex(r"\, : \,").next_to(tex_lz_equals_b, RIGHT)
        self.play( FadeIn(tex_column_lzb) )
        
        matrix_l____ = matrix_l.copy().next_to(tex_column_lzb, RIGHT)
        matrix_l____.shift(LEFT*0.2222)
        matrix_z____ = matrix_z__.copy().next_to(matrix_l____, RIGHT)
        eq____ = Tex(r"=").next_to(matrix_z____, RIGHT)
        matrix_b____ = Matrix(
            [
                ["b_{1}"],
                ["b_{2}"],
                ["b_{3}"],
                ["..."],
                ["b_{n}"],
            ],
        ).scale(0.6666).next_to( eq____, RIGHT )
        _matrix_lzb_ = VGroup( matrix_l____, matrix_z____, eq____, matrix_b____ ).shift( RIGHT * 0.4444 )
        self.play(
            Create(_matrix_lzb_), run_time = 2.2222
        )

        group_analyse = VGroup(tex_ax_equals_b, tex_a_equals_lu, _matrix_alu_, tex_lux_equals_b, tex_ux_equals_z, tex_lz_equals_b, _matrix_lzb_, tex_hint_lzb )
        rect_ga = SurroundingRectangle(group_analyse, color = GRAY, buff = SMALL_BUFF )
        self.play(
            self.camera.frame.animate.shift( UP*6.6666 ).set( width = 44.4444 )
        )
        self.play( Create(rect_ga) )
        
        group_tobeFadeOut = VGroup( tex_ax_equals_b, tex_hint_axb, tex_lux_equals_b, tex_hint_luxb, rect_ga, tex_hint_alu, tex_hint_uxz, tex_hint_lzb )
        self.play( FadeOut(group_tobeFadeOut) )
        
        self.play(
            VGroup(tex_a_equals_lu, tex_column_alu, _matrix_alu_).animate.shift(UP*2.2222 + LEFT*4.4444),
            VGroup(tex_ux_equals_z, tex_column_uxz, _matrix_uxz__).animate.shift(UP*4.4444 + LEFT*4.4444 + DOWN*2.2222 + DOWN*0.8888 ),
            VGroup(tex_lz_equals_b, tex_column_lzb, _matrix_lzb_ ).animate.shift(UP*4.4444 + LEFT*4.4444 + UP*4.4444 * UP*0.8888 ),
        )
        
        self.play(
            self.camera.frame.animate.shift( DOWN*0.2424 ).set( width = 24.2424 )
        )
        
        self.wait(0.2222)
        self.play(
            self.camera.frame.animate.shift( UP*2.2222 ).set( width = 18.1818 )
        )
        
        matrix_a_tri = qwqMatrix(
            [
                ["a_{11}", "a_{12}", "-1", "-1", "-1"], 
                ["a_{21}", "a_{22}", "a_{23}", "-1", "-1"], 
                ["-1", "a_{32}", "a_{33}", "a_{34}", "-1"], 
                ["-1", "-1", "...", "...", "..."],
                ["-1", "-1", "-1", "a_{n,n-1}", "a_{nn}"], 
            ],
            h_buff = 0.8888,
        ).scale(0.6666).move_to(matrix_a)
        
        matrix_l_tri = qwqMatrix(
            [
                ["l_{11}", "-1", "-1", "-1", "-1"], 
                ["l_{21}", "l_{22}", "-1", "-1", "-1"], 
                ["-1", "l_{32}", "l_{33}", "-1", "-1"], 
                ["-1", "-1", "-1", "...", "..."],
                ["-1", "-1", "-1", "l_{n,n-1}", "l_{nn}"], 
            ],
            h_buff = 0.8888,
        ).scale(0.6666).move_to(matrix_l)
        
        matrix_u_tri = qwqMatrix(
            [
                ["1", "u_{12}", "-1", "-1", "-1"], 
                ["-1", "1", "u_{23}", "-1", "-1"], 
                ["-1", "-1", "1", "u_{34}", "-1"], 
                ["-1", "-1", "-1", "...", "..."],
                ["-1", "-1", "-1", "-1", "1"], 
            ],
            h_buff = 0.8888,
        ).scale(0.6666).move_to(matrix_u)

        diaLine_a = get_DiagonalLine( matrix_a )
        diaLine_l = get_DiagonalLine( matrix_l )
        diaLine_u = get_DiagonalLine( matrix_u )
        self.play(Create(diaLine_a), Transform(matrix_a, matrix_a_tri) )
        self.play(Create(diaLine_l), Transform(matrix_l, matrix_l_tri) )
        self.play(Create(diaLine_u), Transform(matrix_u, matrix_u_tri) )
        
        self.wait(0.2222)
        
        group_3matrices = VGroup( tex_a_equals_lu, tex_column_alu, _matrix_alu_, tex_ux_equals_z, tex_column_uxz, _matrix_uxz__, tex_lz_equals_b, tex_column_lzb, _matrix_lzb_,
                                 diaLine_a, diaLine_l, diaLine_u )
        
        self.play(
            self.camera.frame.animate.set(width = 33.333333).shift( DOWN*3.333 ),
            group_3matrices.animate.scale( 0.8888 )
        )
        
        # self.play(
        #     self.camera.frame.animate.set(width = 24.2424).shift( DOWN*2.2222 + LEFT*4.4444 )
        # )
        
        # self.play(
        #     self.camera.frame.animate.set(width = 22.2222).shift( DOWN*6.666 )
        # )
        
        tex_aij2 = MathTex(r" l_{ij} = a_{ij} - \sum_{k=1}^{j-1} l_{ik}u_{kj}. \quad (i=i,2,...,n, \, j=1,2,...,i) ").next_to(_matrix_uxz__, DOWN*4.4444)
        self.play(FadeIn(tex_aij2))
        _2_ = Tex(r"(2)").next_to(tex_aij2, RIGHT)
        self.play(Write(_2_))
        
        tex_aij4 = MathTex(r" u_{ij} = \frac{ a_{ij} - \sum_{k=1}^{i-1} l_{ik}u_{kj} } { l_{ii} }. \quad (i=i,2,...,n-1, \, j=i+1,i+2,...,n) ").next_to(tex_aij2, DOWN*2.2222)
        self.play(FadeIn(tex_aij4))
        _4_ = Tex(r"(4)").next_to(tex_aij4, RIGHT)
        self.play( Write(_4_) )
        
        self.play(
            self.camera.frame.animate.set(width = 33.333333).shift( UP*3.333 + DOWN*0.666666 )
        )
        
        group_qwq = VGroup( group_3matrices, tex_aij2, _2_, tex_aij4, _4_ )
        self.play( group_qwq.animate.shift(LEFT*8.88888888) )
        
        rect_qwq = SurroundingRectangle(group_qwq)
        rect_qwq.set_stroke(color=GRAY_D, width=4.4444)
        self.play( Create(rect_qwq)) 
        
        # self.play(
        #     self.camera.frame.animate.set(width = 22.2222 ).shift( RIGHT*2.22 + UP*2.22 + RIGHT*0.4444 )
        # )
        
        ent_l = matrix_l.get_entries()
        ent_u = matrix_u.get_entries()
        ent_z = matrix_z____.get_entries()
        ent_x = matrix_x__.get_entries()
        littleRectTime = 0.02020202
        littleRectTime_short = 0.02020202 / 4.4444
        
        rect_seq = []
        rect_seq.append( SurroundingRectangle(ent_l[0], color=GOLD ) )
        rect_seq.append( SurroundingRectangle(ent_u[1], color=GOLD ) )
        rect_seq.append( SurroundingRectangle(ent_z[0], color=GOLD ) ) 
        
        rect_seq.append( SurroundingRectangle(ent_l[5], color=GOLD ) )
        rect_seq.append( SurroundingRectangle(ent_l[6], color=GOLD ) )
        rect_seq.append( SurroundingRectangle(ent_u[7], color=GOLD ) )  
        rect_seq.append( SurroundingRectangle(ent_z[1], color=GOLD ) )
        
        rect_seq.append( SurroundingRectangle(ent_l[11], color=GOLD ) )
        rect_seq.append( SurroundingRectangle(ent_l[12], color=GOLD ) )  
        rect_seq.append( SurroundingRectangle(ent_u[13], color=GOLD ) )
        rect_seq.append( SurroundingRectangle(ent_z[2], color=GOLD ) )
        
        rect_seq.append( SurroundingRectangle(ent_l[23], color=GOLD ) )  
        rect_seq.append( SurroundingRectangle(ent_l[24], color=GOLD ) )
        rect_seq.append( SurroundingRectangle(ent_z[4], color=GOLD ) ) 
        
        rect_seq.append( SurroundingRectangle(ent_x[4], color=RED ) )
        
        rect_seq.append( SurroundingRectangle(ent_x[2], color=RED ) )
        rect_seq.append( SurroundingRectangle(ent_x[1], color=RED ) )
        rect_seq.append( SurroundingRectangle(ent_x[0], color=RED ) )
        
        def draw_rect( idx ):
            self.play( Create( rect_seq[idx] ) , runtime = littleRectTime_short )
                   
        tex_tip_step123 = Tex(r"(Steps 1-3 set up and solve Lz=b.)").next_to( tex_x123dotn, DOWN )
        tex_tip_step123.shift( DOWN*2.2222 + RIGHT*2.2222 + UP*0.8888 )
        
        text_pseudocode = Text(
            "PROGRAM: the pseudocode is like below: ",
            t2c = { '[:7]': BLUE }
        ).next_to( tex_tip_step123, UP*2.2222 )
        
        self.play( Write(text_pseudocode) )
        self.play( FadeIn(tex_tip_step123) )
        
        _step1_ = Tex(r"\textit{step} \  \textit{1}")
        tex_step1_1 = Tex("Set $l_{11}$ = $a_{11}$ ;")
        tex_step1_2 = Tex("Set $u_{12}$ = $a_{12}$ / $l_{11}$ ;")
        tex_step1_3 = Tex("Set $z_{1}$ = $b_{1}$ / $l_{11}$ ;")
        
        _step1_.next_to(tex_tip_step123, LEFT*4.4444)
        _step1_.shift( DOWN*1.1111 + RIGHT*1.1111 + UP*0.4444 )
        group_step1 = VGroup( tex_step1_1, tex_step1_2, tex_step1_3)
        group_step1.arrange(DOWN, aligned_edge=LEFT, buff=0.2222)
        group_step1.next_to(_step1_, RIGHT*2.2222).shift(DOWN*0.8888 + UP*0.2222 + DOWN*0.1111)
       
        self.play( Create(_step1_) )
        self.play( Write(group_step1) )
        
        draw_rect(0)
        draw_rect(1)
        draw_rect(2)

        _step2_ = Tex(r"\textit{step} \, \textit{2}")
        tex_step2_for = Tex(r"For i=2, ..., n-1 ")
        tex_step2_1 = Tex("Set $l_{i,i-1}$ = $a_{i,i-1}$")
        tex_step2_2 = Tex("Set $l_{ii}$ = $a_{ii}$ - $l_{i,i-1}u_{i-1,i}$")
        tex_step2_3 = Tex("Set $u_{i,i+1}$ = $b_{i}$ / $l_{ii}$")
        tex_step2_4 = Tex("Set $z_{i} = ( b_{i}-l_{ii-1}z_{i-1} ) / l_{ii}$")
        
        _step2_.next_to( _step1_, DOWN*8.8888 )
        tex_step2_for.next_to(_step2_, RIGHT*2.2222)
        _shabi_ = VGroup(tex_step2_1, tex_step2_2, tex_step2_3, tex_step2_4,)
        _shabi_.arrange(DOWN, aligned_edge=LEFT, buff=0.2222)
        _shabi_.next_to( tex_step2_for, RIGHT*2.2222).shift(DOWN*2.2222 + UP*0.8888 + UP*0.2222 )
        
        group_step2 = VGroup( tex_step2_for, _shabi_ )
        
        self.play( Create(_step2_) )
        self.play( Write(group_step2) )
        
        draw_rect(3)
        draw_rect(4)
        draw_rect(5)
        draw_rect(6)
        self.wait(0.2222)
        draw_rect(7)
        draw_rect(8)
        draw_rect(9)
        draw_rect(10)
        
        _step3_ = Tex(r"\textit{step} \  \textit{3}")
        tex_step3_1 = Tex("Set $l_{n,n-1}$ = $a_{n,n-1}$")
        tex_step3_2 = Tex("Set $l_{nn} = a_{nn} - l_{n,n-1}z{n-1} / l_{nn}$")
        tex_step3_3 = Tex("Set $z_{n} = ( b_{n} - l_{n,n-1}z_{n-1} ) / l_{nn}$")
        
        _step3_.next_to( _step2_, DOWN*8.8888 + DOWN*2.2222 )
        _step3_.shift( UP*0.2222 )
        group_step3 = VGroup( tex_step3_1, tex_step3_2, tex_step3_3 )
        group_step3.arrange(DOWN, aligned_edge=LEFT, buff = 0.2222)
        group_step3.next_to( _step3_, RIGHT*2.2222 ).shift( DOWN*0.8888 + UP*0.1111 )
        
        self.play( Create(_step3_) )
        self.play( Write(group_step3) )
        
        draw_rect(11)
        draw_rect(12)
        draw_rect(13)
        
        # self.play(
        #     self.camera.frame.animate.shift( DOWN*8.8888 )
        # )
        
        tex_tip_step45 = Tex(r"(Steps 4-5 solve Ux = z.)").next_to( tex_tip_step123, DOWN*8.8888 + DOWN*0.2222 )
        tex_tip_step45.shift( DOWN*4.4444 + DOWN*2.2222 + UP*0.8888 )
        self.play( FadeIn(tex_tip_step45) )
        
        _step4_ = Tex(r"\textit{step} \;\! \textit{4}")
        tex_step4_1 = Tex("Set $x_n = z_n$")
        
        _step4_.next_to(_step3_, DOWN*2.2222)
        _step4_.shift( DOWN*2.2222 + UP*0.2222 )
        tex_step4_1.next_to( _step4_, RIGHT )
        
        self.play( Create(_step4_) )
        self.play( Write(tex_step4_1) )
        
        draw_rect(14)
        
        _step5_ = Tex(r"\textit{step} \  \textit{5}")
        tex_step5_1 = Tex("For i = n-1, ..., 1 Set $x_{i} = z_{i} - u_{i,i+1}x_{i+1} $")
        
        _step5_.next_to( _step4_, DOWN*2.2222 )
        tex_step5_1.next_to(_step5_, RIGHT)
        
        self.play( Create(_step5_) )
        self.play( Write(tex_step5_1) )
        
        draw_rect(15)
        draw_rect(16)
        draw_rect(17)
        
        _step6_ = Tex(r"(Output result and stop)").next_to( tex_step5_1, DOWN*2.2222 )
        self.play( FadeIn(_step6_) )
        
        self.play(
            self.camera.frame.animate.shift( DOWN*0.666666 ).set(width = 33.333333 )
        )
        
        group_program = VGroup( text_pseudocode, tex_tip_step123, _step1_, _step2_, _step3_, _step4_, _step5_, group_step1, tex_step2_for, _shabi_, group_step3, tex_step4_1, tex_step5_1, tex_tip_step45, _step6_ )
        group_qwq.add( *rect_seq )
        
        self.play(
            VGroup( group_qwq, rect_qwq ).animate.shift( LEFT*8.88888888 ),
            group_program.animate.shift( LEFT*8.88888888 + RIGHT*2.22 + RIGHT*0.4444 )
        )
        
        self.play(
            self.camera.frame.animate.set(width = 33.333333-6.666666+3.333333 )
        )

        self.wait(2.2222)
        # manim -pql tri.py --disable_caching
