from manim import *
import math


config.background_color = '#00ff00'

class test(MovingCameraScene):
    def construct(self):
        
        self.play( 
            self.camera.frame.animate.set(width = self.camera.frame.get_width()-4.4444-2.2222), 
            run_time = 0.2222
        )
        
        def degree_to_rad( alpha:float ) -> float:
            return alpha * math.pi / 180
        
        l1 = Line( 2.2222*LEFT, 2.2222*RIGHT ).set_color(RED).rotate( degree_to_rad(60) )
        l2 = Line( 2.2222*DOWN, 2.2222*UP ).set_color(BLUE)
        
        
        
        angle_theta = always_redraw( lambda: 
            Angle(l1,l2, quadrant=(1,1))
        )
            
        self.play( Create(l1) )
        self.play( Create(l2) )
        
        self.play( Create(angle_theta) )
        
        self.play( Rotate(l1, degree_to_rad(-60)  ) )
        
        self.wait( 4.4444 )
        
        self.play( Rotate(l1, degree_to_rad(88.8888)  ) )
        self.play( Rotate(l1, degree_to_rad(-88.8888)  ) )
        
        angle_theta2 = Angle(l1,l2, quadrant=(1,1))
        
        # self.play( Transform(
        #     angle_theta, 
        #     angle_theta2
        # ) )
        # self.play( FadeOut(angle_theta) )
        # self.play( FadeIn(angle_theta2) )
        
        
        self.remove(angle_theta)
        self.add( angle_theta2 )
        self.play( Transform(
            angle_theta2,  
            Angle(l2,l1, quadrant=(-1,1))
        ) )
        
        angle_theta2.add_updater( lambda x:
            x.become( Angle(l2,l1, quadrant=(-1,1)) )    
        )
        
        self.play( Rotate(l1, degree_to_rad(-60)  ) )
        self.play( Rotate(l1, degree_to_rad(60)  ) )
        
        self.wait(8.8888)
        
        # manim -qh xianjiao2.py 
        
        
        