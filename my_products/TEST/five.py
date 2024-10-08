from manim import *

class Five(MovingCameraScene):
    def construct(self):
        fuzhuyuan = Circle(radius = 2.2222) #辅助圆

        p1 = Dot().move_to( fuzhuyuan.point_at_angle( np.pi/2 - np.pi*2/5 ) )
        p2 = Dot().move_to( fuzhuyuan.point_at_angle( np.pi/2 ) )
        p3 = Dot().move_to( fuzhuyuan.point_at_angle( np.pi/2 + np.pi*2/5 ) )
        p4 = Dot().move_to( fuzhuyuan.point_at_angle( np.pi/2 + np.pi*4/5 ) )
        p5 = Dot().move_to( fuzhuyuan.point_at_angle( np.pi/2 - np.pi*4/5 ) )
        
        dot1 = Dot().move_to(p1)
        dot2 = Dot().move_to(p2)
        dot3 = Dot().move_to(p3)
        dot4 = Dot().move_to(p4)
        dot5 = Dot().move_to(p5)
        
        self.play(
            Succession(
                FadeIn(dot1),
                FadeIn(dot2),
                FadeIn(dot3),
                FadeIn(dot4),
                FadeIn(dot5),
                lag_ratio=0.4444
            )
        )
        
        line1 = always_redraw( lambda: Line(dot1, dot2) )
        line2 = always_redraw( lambda: Line(dot2, dot3) )
        line3 = always_redraw( lambda: Line(dot3, dot4) )
        line4 = always_redraw( lambda: Line(dot4, dot5) )
        line5 = always_redraw( lambda: Line(dot5, dot1) )
        
        self.play(
            GrowFromPoint(line1, dot1),
            GrowFromPoint(line2, dot2),
            GrowFromPoint(line3, dot3),
            GrowFromPoint(line4, dot4),
            GrowFromPoint(line5, dot5),
        )
        
        self.play(
            self.camera.frame.animate.set(width=12.2222)
        )
        
        self.play(
            dot2.animate.shift( p1.get_center() - p2.get_center() ),
            dot1.animate.shift( (p1.get_center() - p2.get_center()) / 5 ),
        )
        self.play(
            dot1.animate.shift( p4.get_center() - dot1.get_center() ),
            dot4.animate.shift( (p4.get_center() - p1.get_center()) / 5 ),
        )
        self.play(
            dot5.animate.shift( p2.get_center() - dot5.get_center() )
        )
        self.play(
            dot4.animate.shift( p5.get_center() - dot4.get_center() )
        )
        
        self.wait(0.8888)

        self.play(
            dot1.animate.shift( p1.get_center() - dot1.get_center() ),
            dot2.animate.shift( p2.get_center() - dot2.get_center() ),
            dot3.animate.shift( p3.get_center() - dot3.get_center() ),
            dot4.animate.shift( p4.get_center() - dot4.get_center() ),
            dot5.animate.shift( p5.get_center() - dot5.get_center() ),
        )
        
        self.wait(0.4444)
        
        self.play(
            dot2.animate.shift( p1.get_center() - dot2.get_center() ),
            dot1.animate.shift( p4.get_center() - dot1.get_center() ),
            dot5.animate.shift( p2.get_center() - dot5.get_center() ),
            dot4.animate.shift( p5.get_center() - dot4.get_center() ),
        )
        
        self.wait(0.4444)
        
        self.play(
            dot1.animate.shift( p1.get_center() - dot1.get_center() ),
            dot2.animate.shift( p2.get_center() - dot2.get_center() ),
            dot3.animate.shift( p3.get_center() - dot3.get_center() ),
            dot4.animate.shift( p4.get_center() - dot4.get_center() ),
            dot5.animate.shift( p5.get_center() - dot5.get_center() ),
        )
        
        self.wait(0.4444)
        
        self.play(
            dot2.animate.shift( p1.get_center() - dot2.get_center() ),
            dot1.animate.shift( p4.get_center() - dot1.get_center() ),
            dot5.animate.shift( p2.get_center() - dot5.get_center() ),
            dot4.animate.shift( p5.get_center() - dot4.get_center() ),
        )
        
        self.wait(0.8888)
        
        