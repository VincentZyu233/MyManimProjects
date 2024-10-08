from manim import *
import math

class test(MovingCameraScene):
    def construct(self):
        
        sqrt3 = math.sqrt(3)
        pointa, pointb, pointc, pointd = [0,2,0], [-2*sqrt3,0,0], [0,-2,0], [2*sqrt3,0,0]
        lingxing = Polygon(pointa, pointb, pointc, pointd)
        
        self.play(self.camera.frame.animate.set(width=lingxing.width * 2.2222))
        
        self.play(Write(lingxing))
        
        labela = Tex('A').move_to(pointa).shift(UP*0.2222)
        labelb = Tex('B').move_to(pointb).shift(LEFT*0.2222)
        labelc = Tex('C').move_to(pointc).shift(DOWN*0.2222)
        labeld = Tex('D').move_to(pointd).shift(RIGHT*0.2222)
        
        # self.play(Write(labela), run_time=0.4444)
        # self.play(Write(labelb), run_time=0.4444)
        # self.play(Write(labelc), run_time=0.4444)
        # self.play(Write(labeld), run_time=0.4444)
        self.play(Succession(
           Write(labela, run_time=0.4444),
           Write(labelb, run_time=0.4444),
           Write(labelc, run_time=0.4444),
           Write(labeld, run_time=0.4444),
           lag_ratio=0.8888
        ))
        
        linebc = Line(pointb, pointc)
        lineab = Line(pointa, pointb)
        linebd = Line(pointb, pointd)
        lineac = Line(pointa, pointc)
        
        jiao_bac = Angle(lineab, linebc, quadrant=(1,-1))
        print('qwq')
        self.play(Create(jiao_bac))
        self.add(jiao_bac)
        self.play(Flash(pointb))
        
        
        self.play(Write(lineac), run_time=0.8888)
        self.play(Write(linebd), run_time=0.8888)
        
        pointo = [0,0,0]
        doto = Dot(pointo).move_to(pointo).scale(0.8888)
        labelo = Tex('O').move_to(pointo).shift(LEFT*0.2222+DOWN*0.2222)
        self.play(Write(labelo))

        
        banyuan = Arc(radius=linebc.get_length()/2, 
                      angle=PI, 
                      start_angle=-PI/6,
                      arc_center=linebc.get_center())
        
        dashed_banyuan = DashedVMobject(
            Arc(radius=linebc.get_length()/2, 
                      angle=PI, 
                      start_angle=PI*5/6,
                      arc_center=linebc.get_center())
        ) 
        
        pointe = [-sqrt3,1,0]
        dote = Dot(pointe, color=YELLOW).scale(0.8888)
        labele = Tex('E').move_to(pointe).shift(LEFT*0.2222+UP*0.2222)

        # self.play(Write(banyuan), run_time=0.8888)
        # self.play(Write(dashed_banyuan), run_time=0.8888-0.2222)
        self.play(Succession(
            Write(banyuan),
            Write(dashed_banyuan, run_time=0.4444),
            Create(dote),
            lag_ratio=0.8888
        ))
        # self.wait(0.2222)
        self.play(
            FadeOut(dashed_banyuan),
            Flash(dote)
        )
        self.play(Write(labele))
        
        arc_ac = Arc(radius=lineab.get_length(),
                     arc_center=pointb,
                     angle=PI/3,
                     start_angle=-PI/6)
        
        self.play(Write(arc_ac))
        
        lingxing = Polygon(pointa, pointb, pointc, pointd)
        
        dayuan = Circle(radius=lineab.get_length()).move_to(pointb)
        xiaoyuan = Circle(radius=linebc.get_length()/2).move_to(linebc.get_center())
        diffyuan = Difference(dayuan, xiaoyuan,color=RED, fill_opacity=0.5)
        
        yinying = Intersection(diffyuan, lingxing, color=PINK, fill_opacity=0.5)
        
        # self.play(
        #     FadeIn(
        #         Difference(dayuan, xiaoyuan,color=RED, fill_opacity=0.5)
        #     )
        # )
        self.play(
            
            FadeIn(yinying)
        )
        
        self.play( Indicate(yinying) )

        self.wait(4.4444)
        # manim -pql lingxing240229.py