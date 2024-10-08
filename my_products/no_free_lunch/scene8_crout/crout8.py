from manim import *

class MatrixExample(MovingCameraScene):
    def construct(self):
        
        tex_how = Tex(r"Then, how to calculate matrix L and U?")
        self.play(
            Write(tex_how)
        )
        
        self.play(
            self.camera.frame.animate.set( width = 22 ),
        )

        matrix_a = Matrix(
            [
                ["a_{11}", "...", "{a_1j}", "...", "{a_1n}"], 
                ["...", "...", "...", "...", "..."], 
                ["a_{i1}", "...", "a_{ij}", "...", "a_{in}"], 
                ["...", "...", "...", "...", "..."],
                ["a_{n1}", "...", "a_{nj}", "...", "a_{nn}"], 
            ],
            h_buff = 1.0,
        ).next_to(tex_how, DOWN)
        matrix_a.scale(0.8)
        matrix_a.shift(LEFT*6.666666)
        
        eqsign = Tex(r"=").next_to(matrix_a, RIGHT)
        
        matrix_l = Matrix(
            [
                ["l_{11}", "-1", "-1", "-1", "-1"], 
                ["...", "...", "-1", "-1", "-1"], 
                ["l_{i1}", "...", "l_{ij}", "-1", "-1"], 
                ["...", "...", "...", "...", "-1"],
                ["l_{n1}", "...", "l_{nj}", "...", "l_{nn}"], 
            ],
            h_buff = 1.0,
        ).next_to(eqsign, RIGHT)
        matrix_l.shift(LEFT*0.4444)
        matrix_l.scale(0.8)
        for i, row in enumerate(matrix_l.get_entries()):
            for j, entry in enumerate(row):
                if matrix_l.get_entries()[i][j].get_tex_string() == "-1":
                    entry.set_opacity(0)  # 隐藏零元素
        
        matrix_u = Matrix(
            [
                ["u_{11}", "...", "u_{1j}", "...", "u_{1n}"], 
                ["-1", "...", "...", "...", "..."], 
                ["-1", "-1", "u_{ij}", "...", "u_{jn}"], 
                ["-1", "-1", "-1", "...", "..."],
                ["-1", "-1", "-1", "-1", "u_{nn}"], 
            ],
            h_buff = 1.0,
        ).next_to(matrix_l, RIGHT)
        matrix_u.shift(LEFT*0.4444)
        matrix_u.scale(0.8)
        for i, row in enumerate(matrix_u.get_entries()):
            for j, entry in enumerate(row):
                if matrix_u.get_entries()[i][j].get_tex_string() == "-1":
                    entry.set_opacity(0)  # 隐藏零元素
        
        self.play(
            self.camera.frame.animate.shift(DOWN*4.4444),
            Write(matrix_a),
            FadeIn(eqsign),
            Write(matrix_l),
            Write(matrix_u),
        )
        
        tex_above = Tex(r"In the context above we've already referred to one method:").next_to(eqsign, DOWN*8.88888888)
        tex_above.shift(RIGHT*3.333333)
        self.play(
            FadeIn(tex_above)
        )
        
        # Tex(r"it is called \underline{\textbf{\textit{Doolittle Factorization}}}").next_to(tex_moreover, DOWN)
        tex_gaussian = Tex(r"\underline{\textbf{Gaussian Elimination}}").next_to(tex_above, DOWN)
        self.play(
            FadeIn(tex_gaussian)
        )
        
        _A_ = Tex("$A$").next_to(tex_gaussian, DOWN)
        self.play(FadeIn(_A_))

        tex_thatis = Tex(r"That is, \\ to construct several elementary lower triangular matrices, \\ which to be left-multiplied to matrix A, \\").next_to(tex_gaussian, DOWN*4.4444)
        self.play(
            FadeIn(tex_thatis)
        )
        
        tex_inorder = Tex(r"in order to eliminate on matrix A, column by column").next_to(tex_thatis, DOWN)
        self.play(
            FadeIn(tex_inorder)
        )
        
        _L1_ = Tex("$L_1$").next_to(_A_, LEFT)
        self.play(FadeIn(_L1_, shift = RIGHT), run_time = 0.333)

        _L2_ = Tex("$L_2$").next_to(_L1_, LEFT)
        self.play(FadeIn(_L2_, shift = RIGHT), run_time = 0.333)
        
        _L3_ = Tex("$L_3$").next_to(_L2_, LEFT)
        self.play(FadeIn(_L3_, shift = RIGHT), run_time = 0.333)
        
        self.play(
            FadeOut(tex_thatis),
            FadeOut(tex_inorder),
        )
        
        tex_eli_finish = Tex(r"when the elimination is finished, matrix A has turned into U").next_to(tex_gaussian, DOWN*4.4444)
        self.play(FadeIn(tex_eli_finish))
        
        _U_ = Tex("$=U$").next_to(_A_, RIGHT)
        self.play(FadeIn(_U_))
        
        self.play(FadeOut(tex_eli_finish))
        tex_thenlet = Tex("Then let $(L_1L_2L_3)^{-1} = L$").next_to(tex_gaussian, DOWN*4.4444)
        self.play(FadeIn(tex_thenlet))
        tex_thenwehave = Tex("finally we have: A = LU").next_to(tex_thenlet, DOWN)
        self.play(FadeIn(tex_thenwehave))
        
        self.play(
            self.camera.frame.animate.shift( DOWN*4.4444 ),
            run_time = 0.8888
        )
        
        tex_however = Tex(r"However, this method is too \textbf{indirective}, \\ cuz we need to calculate matrices $L_1L_2...L_n$ for n time, then find their inverse")
        tex_however.next_to(tex_thenwehave, DOWN*2.2222)
        self.play(FadeIn(tex_however))
        
        tex_thereis = Tex(r"There is a more directive way for computer to calculate L and U: ")
        tex_thereis.next_to(tex_however, DOWN)
        self.play(FadeIn(tex_thereis))
        self.play(
            self.camera.frame.animate.shift(4.4444*DOWN),
        )
        
        tex_takeex = Tex(r"Take Crout Factorization as an example: ").next_to(tex_thereis, DOWN*2.2222)
        tex_first = Tex(r"first, write down the result of factorization:").next_to(tex_takeex, DOWN*1.1111)
        self.play(FadeIn(tex_first))
        
        matrix_a = Matrix(
            [
                ["a_{11}", "...", "a_{1j}", "...", "a_{1n}"], 
                ["...", "...", "...", "...", "..."], 
                ["a_{i1}", "...", "a_{ij}", "...", "a_{in}"], 
                ["...", "...", "...", "...", "..."],
                ["a_{n1}", "...", "a_{nj}", "...", "a_{nn}"], 
            ],
            h_buff = 1.0,
        ).next_to(tex_first, DOWN)
        matrix_a.shift(LEFT*4.8888)
        matrix_a.scale(0.8888)
        
        eqsign = Tex(r"=").next_to(matrix_a, RIGHT)
        
        matrix_l = Matrix(
            [
                ["l_{11}", "-1", "-1", "-1", "-1"], 
                ["...", "...", "-1", "-1", "-1"], 
                ["l_{i1}", "...", "l_{ij}", "-1", "-1"], 
                ["...", "...", "...", "...", "..."],
                ["l_{n1}", "l_{n2}", "l_{n3}", "...", "l_{nn}"], 
            ],
            h_buff = 1.0,
        ).next_to(eqsign, RIGHT)
        matrix_l.scale(0.8888)
        matrix_l.shift(LEFT*0.0404)
        for i, row in enumerate(matrix_l.get_entries()):
            for j, entry in enumerate(row):
                if matrix_l.get_entries()[i][j].get_tex_string() == "-1":
                    entry.set_opacity(0)  # 隐藏零元素
        
        matrix_u = Matrix(
            [
                ["1", "u_{12}", "u_{13}", "...", "u_{1n}"], 
                ["-1", "1", "u_{23}", "...", "u_{2n}"], 
                ["-1", "-1", "1", "...", "u_{jn}"], 
                ["...", "...", "...", "...", "..."],
                ["-1", "-1", "-1", "-1", "1"], 
            ],
            h_buff = 1.0,
        ).next_to(matrix_l, RIGHT*0.2222)
        matrix_u.scale(0.8888)
        matrix_u.shift(LEFT*0.2222)
        for i, row in enumerate(matrix_u.get_entries()):
            for j, entry in enumerate(row):
                if matrix_u.get_entries()[i][j].get_tex_string() == "-1":
                    entry.set_opacity(0)  # 隐藏零元素
        
        self.play(
            # self.camera.frame.animate.shift(DOWN*4.4444),
            Write(matrix_a),
            FadeIn(eqsign),
            Write(matrix_l),
            Write(matrix_u),
        )

        top_left_a = matrix_a.get_corner(UL)
        top_right_a = matrix_a.get_corner(UR)
        bottom_left_a = matrix_a.get_corner(DL)
        bottom_right_a = matrix_a.get_corner(DR)

        top_left_l = matrix_l.get_corner(UL)
        bottom_left_l = matrix_l.get_corner(DL)
        bottom_right_l = matrix_l.get_corner(DR)
        width_l = matrix_l.get_width()
        height_l = matrix_l.get_height()
        
        triangle_l = Polygon(top_left_l, bottom_left_l, bottom_right_l)
        triangle_l.set_fill(color='#66CCFF', opacity=0.2)  # 设置填充颜色为红色，不透明度为0.5
        triangle_l.set_stroke(color='#00BFFF', width=2)  # 设置边框颜色为蓝色，宽度为2   
        
        top_left_u = matrix_u.get_corner(UL)
        top_right_u = matrix_u.get_corner(UR)
        bottom_right_u = matrix_u.get_corner(DR)
        width_u = matrix_u.get_width()
        height_u = matrix_u.get_height()
        
        triangle_u = Polygon(top_left_u, top_right_u, bottom_right_u)
        triangle_u.set_fill(color='#FFFF00', opacity=0.2)  # 设置填充颜色为红色，不透明度为0.5
        triangle_u.set_stroke(color='#FFD700', width=2)  # 设置边框颜色为蓝色，宽度为2  

        self.play(Create(triangle_l))
        self.play(Create(triangle_u))
                    
        tex_foreach = Tex(r"Consider each element $a_{ij}$ in matrix A:").next_to(tex_first, DOWN*6.666666)
        tex_foreach.shift(DOWN*3.333333)
        tex_according = Tex(r"According to the rules of matrix mutiplication, we have:").next_to(tex_foreach, DOWN)
        self.play(self.camera.frame.animate.shift(4.4444*DOWN),FadeIn(tex_foreach))
        self.play(FadeIn(tex_according))
        
        _aij_ = Tex(r"$a_{ij}$ = ").next_to(tex_according, DOWN*4.4444)
        _aij_.shift(LEFT*4.8888 + DOWN*2.8888)
        matrix_li = Matrix(
            [
                ["l_{i1},", "l_{i2},", "...,", "l_{ii},", "0,", "...,", "0" ], 
            ],
            h_buff = 0.9
        ).next_to(_aij_, RIGHT)
        
        matrix_uj = Matrix(
            [
                ["u_{1j}"],
                ["u_{2j}"],
                ["..."],
                ["u_{_{j-1,j}}"],
                ["1"],
                ["0"],
                ["..."],
                ["0"],
            ],
            bracket_h_buff = 0.02
        ).next_to(matrix_li, RIGHT)
        
        self.play(
            self.camera.frame.animate.shift(4.4444*DOWN),
            Write(_aij_),
        )
        self.play(Write(matrix_li))
        self.play(Write(matrix_uj))
        
        self.play(
            self.camera.frame.animate.shift(4.4444*UP),
            FadeOut(triangle_l),
            FadeOut(triangle_u),
        )

        rectl_center = top_left_l + np.array( [1/2*width_l, -1/2*height_l, 0] )
        rectl = Rectangle(width = width_l, height = 1/5*height_l, 
                           fill_opacity=0.1, fill_color='#66CCFF', stroke_width=2, stroke_color='#00BFFF')
        rectl.move_to(rectl_center)
        self.play( Create(rectl) )
        
        rectu_center = top_left_u + np.array( [1/2*width_u, -1/2*height_u, 0] )
        rectu = Rectangle(width = 1/5*width_u, height = height_u, 
                           fill_opacity=0.1, fill_color='#FFFF00', stroke_width=2, stroke_color='#FFD700')
        rectu.move_to(rectu_center)
        self.play( Create(rectu) )
        
        DL_li = matrix_li.get_corner(DL)
        DR_li = matrix_li.get_corner(DR) 
        width_li = matrix_li.get_width()

        self.play(
            self.camera.frame.animate.shift(4.4444*DOWN),
        )

        liline = Line( DL_li, DR_li + np.array( [-5/14*width_li, 0, 0] ) )
        brace_li = Brace(liline)
        self.play(Write(brace_li))
        # b1text = b1.get_text("Horizontal distance")
        litext = brace_li.get_text("i none-zero elements")
        self.play(FadeIn(litext))

        UR_uj = matrix_uj.get_corner(UR)
        DR_uj = matrix_uj.get_corner(DR)
        height_uj = matrix_uj.get_height()

        brace_uj = BraceBetweenPoints( UR_uj, DR_uj + np.array( [ 0, 3/8*height_uj, 0 ] ), np.array([1, 0, 0]) )
        self.play(Write(brace_uj))
        ujtext = brace_uj.get_text("j none-zero elements")
        self.play(FadeIn(ujtext))
        
        self.play(
            self.camera.frame.animate.shift(8.8888 * UP),
        )        
        self.play(
            self.camera.frame.animate.shift(18.88888888 * RIGHT).set(width = 22),
        )
        tex_when1 = Tex("When i $\leq$ j, that is, ").next_to(matrix_u, RIGHT)
        tex_when1.shift(UP*6.6666 + RIGHT*6.6666)
        self.play( FadeIn(tex_when1) )
        
        triangle_a1 = Polygon(top_left_a, bottom_left_a, bottom_right_a)
        triangle_a1.set_fill(color='#FF4500', opacity=0.2)  # 设置填充颜色为红色，不透明度为0.5
        triangle_a1.set_stroke(color='#FFFF00', width=2)  # 设置边框颜色为蓝色，宽度为2
        
        self.play(
            self.camera.frame.animate.shift(LEFT * 16.88888888),
        )
        self.play(Create(triangle_a1),)
        self.play(
            self.camera.frame.animate.shift(RIGHT * 16.88888888),
            FadeOut(triangle_a1),
        )
        
        tex_aijdown = Tex(r"for each element in lower triangular potion, we have:").next_to(tex_when1, DOWN)
        self.play( FadeIn(tex_aijdown) )
        
        tex_aij1 = Tex("$ a_{ij} = \sum_{k=1}^{j} l_{ik}u_{kj} = \sum_{k=1}^{j-1} l_{ik}u_{kj} + l_{ij}  $").next_to(tex_aijdown, DOWN)
        self.play( Write(tex_aij1) )
        _1_ = Tex(r"(1)").next_to(tex_aij1, RIGHT)
        self.play( Write(_1_) )
        
        tex_thus1 = Tex(r"thus").next_to(tex_aij1, DOWN)
        self.play(FadeIn(tex_thus1))
        tex_aij2 = MathTex(r" l_{ij} = a_{ij} - \sum_{k=1}^{j-1} l_{ik}u_{kj}. \quad (i=i,2,...,n, \, j=1,2,...,i) ").next_to(tex_thus1, DOWN)
        self.play(FadeIn(tex_aij2))
        _2_ = Tex(r"(2)").next_to(tex_aij2, RIGHT)
        self.play(Write(_2_))
        
        self.wait(1)
        
        tex_when2 = Tex("When i $>$ j, that is, ").next_to(tex_aij2, DOWN*2.22222222)
        self.play(
            FadeIn(tex_when2),
        )
        
        triangle_a2 = Polygon(top_left_a, top_right_a, bottom_right_a)
        triangle_a2.set_fill(color='#FF4500', opacity=0.2)  # 设置填充颜色为红色，不透明度为0.5
        triangle_a2.set_stroke(color='#FFFF00', width=2)  # 设置边框颜色为蓝色，宽度为2
        
        self.play(self.camera.frame.animate.shift(LEFT * 8.88888888),)
        self.play(Create(triangle_a2),)
        self.play(
            self.camera.frame.animate.shift(RIGHT * 8.88888888),
            FadeOut(triangle_a2),
        )
        
        tex_aijup = Tex(r"for each element in upper triangular potion, we have:").next_to(tex_when2, DOWN)
        self.play( FadeIn(tex_aijup) )
        
        tex_aij3 = Tex("$ a_{ij} = \sum_{k=1}^{i} l_{ik}u_{kj} = \sum_{k=1}^{i-1} l_{ik}u_{kj} + l_{ii}u_{ij}  $").next_to(tex_aijup, DOWN)
        self.play( Write(tex_aij3) )
        _3_ = Tex(r"(3)").next_to(tex_aij3, RIGHT)
        self.play( Write(_3_) ) 
        
        tex_thus2 = Tex(r"thus").next_to(tex_aij3, DOWN)
        self.play(FadeIn(tex_thus2))
        
        tex_aij4 = MathTex(r" u_{ij} = \frac{ a_{ij} - \sum_{k=1}^{i-1} l_{ik}u_{kj} } { l_{ii} }. \quad (i=i,2,...,n-1, \, j=i+1,i+2,...,n) ").next_to(tex_thus2, DOWN)
        self.play(FadeIn(tex_aij4))
        _4_ = Tex(r"(4)").next_to(tex_aij4, RIGHT)
        self.play( Write(_4_) )
        
        rect_2 = SurroundingRectangle(tex_aij2, color=ORANGE, buff=SMALL_BUFF)
        self.play( Create(rect_2) )
        rect_4 = SurroundingRectangle(tex_aij4, color=ORANGE, buff=SMALL_BUFF)
        self.play( Create(rect_4) )
        
        tex_croutsum = Tex(r"above all, equation (2) and (4) are called \textbf{Formula of Crout Factorization}").next_to(tex_aij4, DOWN*1.1111)
        tex_fornn = Tex(r"for nxn invertible matrix A").next_to(tex_croutsum, DOWN)
        self.play( Write(tex_croutsum) )
        self.play( Write(tex_fornn) )
        
        crout_formula_move_move = 18.88888888
        self.play(
            ApplyMethod(tex_aij2.shift, RIGHT * crout_formula_move_move + DOWN*0.2222), 
            ApplyMethod(_2_.shift, RIGHT * crout_formula_move_move + DOWN*0.2222), 
            ApplyMethod(tex_aij4.shift, RIGHT * crout_formula_move_move + UP*2.2222), 
            ApplyMethod(_4_.shift, RIGHT * crout_formula_move_move + UP*2.2222), 
            ApplyMethod(tex_croutsum.shift, RIGHT * crout_formula_move_move + UP*2.2222), 
            self.camera.frame.animate.shift(RIGHT * crout_formula_move_move + LEFT * 2.2222).set( width = 18 ),
        )

        self.wait(3)
        
        tex_similarly = Tex(r"Similarly, we can obtain \textbf{Formula of Doolittle Factorization}").next_to(tex_croutsum, RIGHT*4.4444)
        tex_similarly.shift(RIGHT*2.2222)
        self.play(
            self.camera.frame.animate.shift( RIGHT*16.88888888 ),
            Write(tex_similarly),
        )
        
        tex_doolittle1 = MathTex(r" u_{ij} = a_{ij} - \sum_{k=1}^{i-1} l_{ik}u_{kj}. \quad (i=i,2,...,n, \, j=1,2,...,n) ").next_to(tex_similarly, UP)
        tex_doolittle1.shift(UP*2.2222)
        self.play( Write(tex_doolittle1) )
        
        tex_doolittle2 = MathTex(r" l_ {ij} = \frac{ a_{ij} - \sum_{k=1}^{i-1} l_{ik}u_{kj} } { l_{jj} }. \quad (i=2,...,n-1, \, j=1,2,...,i-1) ").next_to(tex_doolittle1, DOWN)
        self.play( Write(tex_doolittle2) )
        
        self.play(
            self.camera.frame.animate.shift( LEFT*16.88888888 ),
        )

        self.play(
            ApplyMethod(tex_aij2.shift, UP*2.2222), 
            ApplyMethod(_2_.shift, UP*2.2222), 
            ApplyMethod(tex_aij4.shift, DOWN*2.2222), 
            ApplyMethod(_4_.shift, DOWN*2.2222), 
            ApplyMethod(tex_croutsum.shift, DOWN*2.2222), 
            self.camera.frame.animate.set( width = 22 ),
        )

        # _group_alu_ = VGroup(matrix_a, eqsign, matrix_l, matrix_u)
        matrix_a2 = matrix_a.copy()
        eqsign2 = eqsign.copy().next_to(matrix_a2, RIGHT)
        matrix_l2 = matrix_l.copy().next_to(eqsign2, RIGHT)
        matrix_u2 = matrix_u.copy().next_to(matrix_l2, RIGHT)
   
        _group_alu_2 = VGroup(matrix_a2, eqsign2, matrix_l2, matrix_u2)
        _group_alu_2.next_to(tex_aij2, DOWN*2.22222222)
        self.play( Write(_group_alu_2) )

        ent_l = matrix_l2.get_entries()
        ent_u = matrix_u2.get_entries()

        rect_l_12 = SurroundingRectangle(ent_l[12], color=BLUE)
        self.play( Create( rect_l_12 ) )
        self.wait(1)
        
        rect_l_11 = SurroundingRectangle(ent_l[11])
        self.play( Create( rect_l_11 ), run_time = 0.4444)
        rect_l_10 = SurroundingRectangle(ent_l[10])
        self.play( Create( rect_l_10 ), run_time = 0.4444 )
        rect_u_2 = SurroundingRectangle(ent_u[2])
        self.play( Create( rect_u_2 ), run_time = 0.4444 )
        rect_u_7 = SurroundingRectangle(ent_u[7])
        self.play( Create( rect_u_7 ), run_time = 0.4444 )

        self.play(
            FadeOut(rect_l_11),
            FadeOut(rect_l_10),
            FadeOut(rect_u_2),
            FadeOut(rect_u_7),
        )
        self.play( FadeOut(rect_l_12) )
        
        matrix_l3 = Matrix(
            [
                ["l_{11}", "-1", "-1", "-1", "-1"], 
                ["l_{21}", "l_{22}", "-1", "-1", "-1"], 
                ["l_{31}", "l_{32}", "l_{33}", "-1", "-1"], 
                ["...", "...", "...", "...", "..."],
                ["l_{n1}", "l_{n2}", "l_{n3}", "...", "l_{nn}"], 
            ],
            h_buff = 1.0,
        ).next_to(eqsign2, RIGHT)
        matrix_l3.shift(LEFT*0.0404)
        matrix_l3.scale(0.8888)
        for i, row in enumerate(matrix_l3.get_entries()):
            for j, entry in enumerate(row):
                if matrix_l3.get_entries()[i][j].get_tex_string() == "-1":
                    entry.set_opacity(0)  # 隐藏零元素
        
        matrix_u3 = Matrix(
            [
                ["1", "u_{12}", "u_{13}", "...", "u_{1n}"], 
                ["-1", "1", "u_{23}", "...", "u_{2n}"], 
                ["-1", "-1", "1", "...", "u_{jn}"], 
                ["...", "...", "...", "...", "..."],
                ["-1", "-1", "-1", "-1", "1"], 
            ],
            h_buff = 1.0,
        ).next_to(matrix_l3, RIGHT*0.2222)
        matrix_u3.scale(0.8888)
        for i, row in enumerate(matrix_u3.get_entries()):
            for j, entry in enumerate(row):
                if matrix_u3.get_entries()[i][j].get_tex_string() == "-1":
                    entry.set_opacity(0)  # 隐藏零元素

        self.play(
            Transform(
                VGroup(matrix_l2, matrix_u2),
                VGroup(matrix_l3, matrix_u3)
            ),
        )

        ent_l3 = matrix_l3.get_entries()
        ent_u3 = matrix_u3.get_entries()
        
        ent_crout_seq = []
        ent_crout_seq.append( ent_l3[0] )
        ent_crout_seq.append( ent_u3[1] )
        ent_crout_seq.append( ent_u3[2] )
        ent_crout_seq.append( ent_u3[3] )
        ent_crout_seq.append( ent_u3[4] )
        
        ent_crout_seq.append( ent_l3[5] )
        ent_crout_seq.append( ent_l3[6] )
        ent_crout_seq.append( ent_u3[7] )
        ent_crout_seq.append( ent_u3[8] )
        ent_crout_seq.append( ent_u3[9] )
        
        ent_crout_seq.append( ent_l3[10] )
        ent_crout_seq.append( ent_l3[11] )
        ent_crout_seq.append( ent_l3[12] )
        ent_crout_seq.append( ent_u3[13] )
        ent_crout_seq.append( ent_u3[14] )
        
        ent_crout_seq.append( ent_l3[20] )
        ent_crout_seq.append( ent_l3[21] )
        ent_crout_seq.append( ent_l3[22] )
        ent_crout_seq.append( ent_l3[23] )
        ent_crout_seq.append( ent_l3[24] )

        for i in range(0,20):
            self.play(Create( SurroundingRectangle(ent_crout_seq[i]) ), runtime = 0.02020202)
            if i%5 == 0:
                self.wait(0.02020202)
                print('next line')
        
        self.wait(3)