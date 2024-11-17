# 2022年7月， 破晓季到来，引入全新机制 碎石机制
# 在某些日期，碎片会定期从伊甸山爆发，降落在天空王国的某个位置
# 这个视频，将用四条规律， 讲清楚网易国服的碎片喷发规律

# 我先放个日历在这边

# 规律一， 碎片所降临的大地图，五天为一个周期，
# 如果碎片在1号降临，那么一定是在暮土，
# 如果碎片在2号降临，那么一定是在禁阁，
# 3号云野，4号雨林，5号霞谷
# 然后往后 一个新的周期，6，7，8，9，10， 暮土禁阁云野雨林霞谷
# 又一个新的周期，11,12,13,14,15， 暮土禁阁云野雨林霞谷
# 以此类推，往后都是五天一一个周期，


# 接下来是规律二，
# 在前半个月，只有周二周六周日才会有碎片，
# 周二黑色，周六周日红色
# 在后半个月，只有周三周五周日才会有碎片，
# 周三黑色，周五周日红色

# 规律三， 是一张表，
# “碎片事件，对应的小地图，以及烛火数目表格
# ，自行暂停观看、截图即可

# 规律四，也是一张表
# “每天 碎片喷发的具体时间（精确到分钟）” 表格，
# 自行暂停观看、截图即可

# 以上就是网易国服的碎片喷发规律，恭喜你已经学会自己计算碎片事件的降临时间了！


from manim import *

config.background_color = '#5ed4f8'

Color_DayPassed = '#55c3ff'
Color_MediumBlue = '#0000CD'
Color_BlackShard = '#847272'
Color_RedShard = '#ff1e14'

Color_Period_A = Color_DayPassed
Color_Period_B = ORANGE

# manim -ql shard2.py --disable_caching

class Calendar(MovingCameraScene):
    def construct(self):   
        
        # self.camera.frame_width = 576  # 9:16 aspect ratio
        # self.camera.frame_height = 1024
        
        
        MyTexTemplate = TexTemplate(
            tex_compiler="xelatex",
            output_format='.xdv',
            placeholders={
                "title": r"\centering",  # 设置所有文本居中对齐
            },
        )
        MyTexTemplate.add_to_preamble(r"\usepackage{fontspec}\setmainfont{Smiley Sans Oblique}")
        
        title = Tex(
            "四条规律讲清楚 网易国服碎片规律",
            tex_template=MyTexTemplate,
            color = WHITE,
            font_size = 72
        )
        
        self.wait(0.4444)
        self.play(Write(title), run_time=2.2222)
        
        self.wait(0.8888)
        
        # ----------------------------------------------------------------
        
        # 创建表格
        table = VGroup() #是square的集合
        daynums = VGroup()
        weekday_row = VGroup()
        num_rows = 5
        num_cols = 7
        cell_width = 1.2
        cell_height = 1.2
        start_x = -2 #左上顶点坐标
        start_y = 0

        
        for row in range(num_rows):
            for col in range(num_cols):
                cell = Square(side_length=cell_width, fill_color=WHITE, fill_opacity=0.8888, stroke_width=4.4444, stroke_color=GRAY_A)
                cell.move_to( (start_x + col * (cell_width+0.0808) * RIGHT) + (start_y + row * (cell_height+0.0808) * DOWN ) )
                table.add(cell)
                
        # table.shift(LEFT*2.2222+UP*2.2222)
        table.next_to(title, DOWN*4.4444)
        
        
        
        # 添加数字
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
    
        for num in enumerate(numbers):
            # print(num[0], num[1])
            idx = num[0]
            daynum = num[1]
            
            text = Text(
                str(daynum), font_size=48, color=BLACK
            ).move_to(table[idx+2])
            
            text.set_stroke(color=WHITE, width=0.8888)
            
            daynums.add(text)
            
        
        print("width", self.camera.frame.get_width())

        
        weekdays = ["一","二","三","四","五","六","日"]
        
        for weekday in enumerate(weekdays):
            idx = weekday[0]
            day = weekday[1]
            
            # tex = Tex(
            #     day,
            #     tex_template=MyTexTemplate,
            #     color = WHITE,
            # ).next_to(table[idx], UP)
            tex = Text(day, font="Microsoft JhengHei UI").next_to(table[idx], UP)
            # self.play(Write(tex), run_time = 0.4444)
            weekday_row.add(tex)
        
        self.play( Write(weekday_row), run_time = 0.8888 )
        
        # self.wait(0.8888)    
        
        def get_bianse_ani ( idx, color=Color_DayPassed, time=0.2222 ): #idx means table[idx]
            return Transform( 
                table[idx], 
                Square(side_length=cell_width, fill_color=color, fill_opacity=0.8888, stroke_width=4.4444, stroke_color=GRAY_A).move_to(table[idx]),
                run_time = time
            )
        
        # ----------------------------------------------------------------

        rule1 = Tex(
            "① 每个月当中，碎片所降临的大地图 5天为一个周期。",
            tex_template = MyTexTemplate,
            color = WHITE,
            font_size = 36,
        ).scale(0.8888).next_to(title, DOWN).shift(RIGHT*0.2222)
        
        rule2 = Tex(
            "② 前半个月(1<=日期<=15) 周二黑石、周六周日红石， \\\\ 后半个月(16<=日期) ~~~~ 周三黑石、周五周日红石",
            tex_template = MyTexTemplate,
            color = WHITE,
            font_size = 36,
        ).scale(0.8888).next_to(rule1, DOWN)
        
        rule3 = Tex(
            "③ ``碎片事件 对应的小地图和烛火数目`` 表格 ~~~~",
            tex_template = MyTexTemplate,
            color = WHITE,
            font_size = 36,
        ).scale(0.8888).next_to(rule2, DOWN).shift(LEFT*0.2222)
        
        rule4 = Tex(
            "④ ``每天 碎片喷发的具体时间`` 表格（精确到分钟） ",
            tex_template = MyTexTemplate,
            color = WHITE,
            font_size = 36,
        ).scale(0.8888).next_to(rule3, DOWN).shift(RIGHT*0.2222)
        
        rule_group = VGroup( rule1, rule2, rule3, rule4)
        rule_group.arrange(DOWN, aligned_edge=LEFT)
        rule_group.next_to(title, DOWN).shift(RIGHT*0.2222)
        
        self.play(Write(rule1), run_time = 2.2222)
        self.wait(2.2222)

        pic_paths = [
            r"D:\MANIM\Projects\MyManimProjects\my_products\shard\mutu_sq.png",
            r"D:\MANIM\Projects\MyManimProjects\my_products\shard\jinge_sq.png",
            r"D:\MANIM\Projects\MyManimProjects\my_products\shard\yunye_sq.png",
            r"D:\MANIM\Projects\MyManimProjects\my_products\shard\yulin_sq.png",
            r"D:\MANIM\Projects\MyManimProjects\my_products\shard\xiagu_sq.png",
            # "D:\MANIM\Projects\MyManimProjects\my_products\shard\mutu_sq.png"
        ]
        
        pics = []
        for path in pic_paths:
            pics.append(
                ImageMobject(path)
            )
        
        grid_bg = []
        
        for i in range(1,32):
            grid = table[i+1]
            daynum = daynums[i-1]
            
            bg = pics[(i-1)%5].copy().scale(0.4444-0.0808-0.0404).move_to(grid)
            grid_bg.append( bg )
            
            grid.set_z_index(1)
            bg.set_z_index(2)
            daynum.set_z_index(3)
        
        self.wait(0.2222)
        self.play( Indicate(daynums[0]) )
        self.wait(0.2222)
        self.play(FadeIn(grid_bg[0]))
        self.wait(0.2222)
        
        self.play( Indicate(daynums[1]) )
        self.wait(0.2222)
        self.play(FadeIn(grid_bg[1]))
        self.wait(0.2222)
        
        self.play( Indicate(daynums[2]), run_time=0.4444 )
        # self.wait(0.2222)
        self.play(FadeIn(grid_bg[2]), run_time=0.4444 )
        
        self.play( Indicate(daynums[3]), run_time=0.4444-0.2222 )
        # self.wait(0.2222)
        self.play(FadeIn(grid_bg[3]), run_time=0.4444-0.2222 )
        
        self.play( Indicate(daynums[4]), run_time=0.4444-0.2222 )
        # self.wait(0.8888)
        self.play(FadeIn(grid_bg[4]), run_time=0.4444-0.2222 )
        
        self.wait(2.2222+1.1111)

        self.play( Indicate(daynums[5]), run_time=0.2222 )
        self.play( Indicate(daynums[6]), run_time=0.2222 )
        self.play( Indicate(daynums[7]), run_time=0.2222 )
        self.play( Indicate(daynums[8]), run_time=0.2222 )
        self.play( Indicate(daynums[9]), run_time=0.2222 )
        
        self.wait(0.8888)
        
        self.play(FadeIn(grid_bg[5]), run_time=0.2222 )
        self.play(FadeIn(grid_bg[6]), run_time=0.2222 )
        self.play(FadeIn(grid_bg[7]), run_time=0.2222 )
        self.play(FadeIn(grid_bg[8]), run_time=0.2222 )
        self.play(FadeIn(grid_bg[9]), run_time=0.2222 )
        
        self.wait(2.2222)
        
        self.play( Indicate(daynums[10]), run_time=0.2222+0.1111 )
        self.play( Indicate(daynums[11]), run_time=0.2222+0.1111 )
        self.play( Indicate(daynums[12]), run_time=0.2222+0.1111 )
        self.play( Indicate(daynums[13]), run_time=0.2222+0.1111 )
        self.play( Indicate(daynums[14]), run_time=0.2222+0.1111 )
        
        self.wait(0.8888-0.2222)
        
        self.play(FadeIn(grid_bg[10]), run_time=0.2222+0.1111 )
        self.play(FadeIn(grid_bg[11]), run_time=0.2222+0.1111 )
        self.play(FadeIn(grid_bg[12]), run_time=0.2222+0.1111 )
        self.play(FadeIn(grid_bg[13]), run_time=0.2222+0.1111 )
        self.play(FadeIn(grid_bg[14]), run_time=0.2222+0.1111 )
        
        
        def get_bianse_ani ( idx, color=Color_DayPassed, time=0.2222 ): #idx means table[idx]
            return Transform( 
                table[idx], 
                Square(side_length=cell_width, fill_color=color, fill_opacity=0.8888, stroke_width=4.4444, stroke_color=GRAY_A).move_to(table[idx]),
                run_time = time
            )
            
            
        self.wait(0.8888)
        
        rule1_remain_ani = []
        
        for i in range(1,5+1):
            rule1_remain_ani.append( get_bianse_ani(i+1,Color_Period_A) )
        rule1_remain_ani.append( Wait(0.4444) )
        
        for i in range(6,10+1):
            rule1_remain_ani.append( get_bianse_ani(i+1,Color_Period_B) )
        rule1_remain_ani.append( Wait(0.4444) )
        
        for i in range(11,15+1):
            rule1_remain_ani.append( get_bianse_ani(i+1,Color_Period_A) )
        rule1_remain_ani.append( Wait(0.2222) )
        for i in range(11,15+1):
            rule1_remain_ani.append( FadeIn( grid_bg[i-1], run_time=0.2222 ) )
        rule1_remain_ani.append( Wait(0.2222) )
        
        for i in range(16,20+1):
            rule1_remain_ani.append( get_bianse_ani(i+1,Color_Period_B) )
        rule1_remain_ani.append( Wait(0.2222) )
        for i in range(16,20+1):
            rule1_remain_ani.append( FadeIn( grid_bg[i-1], run_time=0.2222 ) )
        rule1_remain_ani.append( Wait(0.2222) )
        
        for i in range(21,25+1):
            rule1_remain_ani.append( get_bianse_ani(i+1,Color_Period_A) )
        rule1_remain_ani.append( Wait(0.2222) )
        for i in range(21,25+1):
            rule1_remain_ani.append( FadeIn( grid_bg[i-1], run_time=0.2222 ) )
        rule1_remain_ani.append( Wait(0.2222) )
        
        for i in range(26,30+1):
            rule1_remain_ani.append( get_bianse_ani(i+1,Color_Period_B) )
        rule1_remain_ani.append( Wait(0.2222) )
        for i in range(26,30+1):
            rule1_remain_ani.append( FadeIn( grid_bg[i-1], run_time=0.2222 ) )
        rule1_remain_ani.append( Wait(0.2222) )
        
        rule1_remain_ani.append( get_bianse_ani(31+1,Color_Period_A) )
        rule1_remain_ani.append( FadeIn( grid_bg[31-1], run_time=0.2222 ) )
        
        # for ani in rule1_remain_ani:
        #     self.play( ani )
        self.play(
            AnimationGroup( *rule1_remain_ani, lag_ratio=0.2222 )
        )
        
        self.wait(4.4444) # 截图
        
        rule1_fadeout_ani = []
        for i in range(1,31+1):
            rule1_fadeout_ani.append( FadeOut( grid_bg[i-1], run_time=0.1111 ) )
            rule1_fadeout_ani.append( get_bianse_ani(i+1, WHITE, 0.1111) )
            
        self.play(
            AnimationGroup( *rule1_fadeout_ani, lag_ratio=0.1111 )
        )
        
        #_----------------------
        # rule 2
        cir_black = Circle(color = Color_BlackShard, fill_opacity=1, radius=0.4444).scale(1+0.2222)
        cir_red = Circle(color = Color_RedShard, fill_opacity=1, radius=0.4444).scale(1+0.2222)
        cir_black_cal = cir_black.copy().set_opacity(0.8888)
        cir_red_cal = cir_red.copy().set_opacity(0.8888)
        cirs = []
        for i in range(1,31+1):
            cir = None
            
            if i <=15:
                if i % 7 == 0:
                    cir = cir_black_cal.copy() 
                else:
                    cir = cir_red_cal.copy() 
            else:
                if i % 7 == 1:
                    cir = cir_black_cal.copy() 
                else:
                    cir = cir_red_cal.copy() 
            
            table[i+1].set_z_index(22)
            grid_bg[i-1].set_z_index(23)
            cir.set_z_index(24)
            daynums[i-1].set_z_index(25)
            
            cir.move_to(  table[i+1] )
            cirs.append(cir)
                

        qianban_a = []
        for i in range(1,15+1):
            qianban_a.append( get_bianse_ani(i+1, Color_Period_A) )
            
        houban_b = []
        for i in range(16,31+1):
            houban_b.append( get_bianse_ani(i+1, Color_Period_B) )
            
        def weekday_wiggle( i:int ): #i=1,2,3...
            return Wiggle(weekday_row[i-1], scale_value=2.2222, run_time=0.8888)
        
        def cir_wiggle( i:int):
            return Wiggle( cirs[i-1], run_time=0.2222 )
        
        def cir_fadein( i:int ): #i=1,2,3...
            return FadeIn( cirs[i-1], run_time=0.2222 )
            
        rule2_ani = [
            AnimationGroup( *qianban_a, lag_ratio=0.2222 ), Wait(0.2222),
            
            AnimationGroup( weekday_wiggle(2), cir_fadein(7), cir_fadein(14), lag_ratio=0.2222 ), Wait(0.1111),
            AnimationGroup( weekday_wiggle(6), cir_fadein(4), cir_fadein(11),weekday_wiggle(7), cir_fadein(5), cir_fadein(12), lag_ratio=0.2222 ), 
            Wait(0.2222),
            AnimationGroup( weekday_wiggle(2), cir_wiggle(7), cir_wiggle(14), lag_ratio=0.2222 ), Wait(0.2222),
            AnimationGroup( weekday_wiggle(6), cir_wiggle(4), cir_wiggle(11),weekday_wiggle(7), cir_wiggle(5), cir_wiggle(12), lag_ratio=0.2222 ), 
            
            Wait(0.8888),
            
            AnimationGroup( *houban_b, lag_ratio=0.2222 ), Wait(0.2222),
            
            AnimationGroup( weekday_wiggle(3), cir_fadein(22), cir_fadein(29), lag_ratio=0.2222 ), Wait(0.1111),
            AnimationGroup( weekday_wiggle(5), cir_fadein(17), cir_fadein(24), cir_fadein(31),weekday_wiggle(7), cir_fadein(19), cir_fadein(26),  lag_ratio=0.2222 ), 
            Wait(0.2222),
            AnimationGroup( weekday_wiggle(3), cir_wiggle(22), cir_wiggle(29), lag_ratio=0.2222 ), Wait(0.2222),
            AnimationGroup( weekday_wiggle(5), cir_wiggle(17), cir_wiggle(24), cir_wiggle(31),weekday_wiggle(7), cir_wiggle(19), cir_wiggle(26),  lag_ratio=0.2222 ), 
        ]
        
        self.play( Write(rule2), run_time = 2.2222 )
        
        for ani in rule2_ani:
            self.play( ani )
            
        #
        
        self.wait(4.4444)
        
        
        
        img_rule3 = ImageMobject(r"D:\MANIM\Projects\MyManimProjects\my_products\shard\rule3.png").scale(0.4444+0.1111)
        img_rule3.next_to(rule3, DOWN).shift(RIGHT*0.8888)
        img_rule4 = ImageMobject(r"D:\MANIM\Projects\MyManimProjects\my_products\shard\rule4.png").scale(0.2222*2.2222)
        img_rule4.next_to(rule4, DOWN).shift(RIGHT*0.8888)
        
        self.wait(2.2222)
        self.play( Write(rule3) )
        self.play( FadeIn(img_rule3) )
        
        self.play(
            self.camera.frame.animate.set( width = self.camera.frame.get_width()-4.4444 ).move_to(img_rule3)
        )
        self.play( ApplyWave(rule3), run_time = 2.2222 )
        self.play(
            self.camera.frame.animate.set( width = self.camera.frame.get_width()-2.2222 )
        )
        
        self.wait( 2.2222 )
        
        #-----------------------------
        
        self.play( 
            self.camera.frame.animate.set( width = self.camera.frame.get_width()+8.8888 ).shift(UP*2.2222+LEFT*4.4444+LEFT*0.2222),
            FadeOut(img_rule3)
        )
        
        
        self.play( Write(rule4) )
        self.play( FadeIn(img_rule4) )
        
        self.play(
            self.camera.frame.animate.set( width = self.camera.frame.get_width()-4.4444 ).move_to(img_rule4)
        )
        self.play( ApplyWave(rule4), run_time = 2.2222 )
        self.play(
            self.camera.frame.animate.set( width = self.camera.frame.get_width()-4.4444 )
        )
        
        self.wait(2.2222)
        
        self.play( 
            self.camera.frame.animate.set( width = self.camera.frame.get_width()+8.8888 ).shift(LEFT*4.4444+UP*2.2222),
            FadeOut(img_rule4)
        )
        
        self.wait(2.2222)
        
        self.play( 
            self.camera.frame.animate.set( width = self.camera.frame.get_width()-0.7777 ).shift(UP*0.7777)
        )
        
        
        star_icon = ImageMobject(r"D:\MANIM\Projects\MyManimProjects\my_products\shard\star.jpg").scale(2.2222)
        star_icon.next_to( table, UP ).shift(UP*0.7777+LEFT*0.7777+LEFT*0.7777+LEFT*0.7777)
        
        congrats_Tex = Tex(
            "恭喜你， 你已经成功掌握碎片规律，快去自己计算吧",
            tex_template = MyTexTemplate,
            color = WHITE,
            font_size = 36,
        ).scale(2.2222*0.7777)
        congrats_Tex.next_to(star_icon, RIGHT)
        
        self.play( 
            AnimationGroup(
                FadeIn(star_icon),
                Write( congrats_Tex ),
                VGroup( title, rule_group ).animate.shift( RIGHT*0.7777 ).scale(1.2222),
                lag_ratio=0.7777777
            )
        )
        
        self.wait(8.8888*8.8888*2.2222)  
        # manim -qh shard2.py --disable_caching

        