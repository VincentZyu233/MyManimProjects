from manim import *

config.background_color = '#00FF00'

class Calendar(MovingCameraScene):
    def construct(self):   
        
        self.play(
            self.camera.frame.animate.set( width = 8.8888 )
        )
        
        line = Line( LEFT*2.2222, RIGHT*2.2222, color=RED )
        
        self.play( Create(line), run_time = 2.2222 )
        
        self.wait(2.2222)
        
        # manim -qh red_line.py
        