# 2022年7月，光遇迎来新的季节 破晓季，同时带来了新的机制-碎片机制
# 在某些日期，碎片会定期从伊甸山爆发，降落在天空王国的某个位置
# 而且至今为止 已经有不少玩家摸索出碎石喷发的日期规律了
# 今天这个视频 将用四句话 总结网易国服的碎片喷发规律 


from manim import *
import datetime

config.background_color = '#5ed4f8'
Color_DayPassed = '#55c3ff'
Color_MediumBlue = '#0000CD'
Color_BlackShard = '#847272'
Color_RedShard = '#ff1e14'

Color_Period_A = Color_DayPassed
Color_Period_B = ORANGE


class Calendar(MovingCameraScene):
    def construct(self):     
        
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
        
        self.wait(2.2222-0.8888-0.8888)
        self.play(Write(title))
        
        self.wait(2.2222)
        
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
        self.play(
            Create(table, run_time = 2.2222), 
            Create(daynums, run_time = 4.4444-0.8888-0.8888-0.8888),
            self.camera.frame.animate.set(width = self.camera.frame.get_width()+2.2222).shift(DOWN*2.2222+UP*0.4444+RIGHT*2.2222+RIGHT*0.8888+DOWN*2.2222),
            title.animate.shift(RIGHT*4.4444+DOWN*2.2222+RIGHT*2.2222+UP*0.4444+RIGHT*0.8888).scale(0.4444+0.2222)
        )
        
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
        
        self.play( Write(weekday_row), run_time = 2.2222 )
        
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
        # rule1[2].shift(UP*0.2222) #cuowu de
        self.play(Write(rule1), run_time = 3.3333+0.8888)
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
        
        
        
        self.play( Indicate(daynums[0]) )
        self.wait(0.8888)
        self.play(FadeIn(grid_bg[0]))
        self.wait(2.2222-0.4444-0.4444-0.4444)
        self.play( Indicate(daynums[1]) )
        self.wait(0.8888)
        self.play(FadeIn(grid_bg[1]))
        self.wait(2.2222-0.4444-0.4444-0.4444)
        self.play( Indicate(daynums[2]) )
        self.wait(0.8888)
        self.play(FadeIn(grid_bg[2]))
        self.wait(2.2222-0.4444-0.4444-0.4444)
        self.play( Indicate(daynums[3]) )
        self.wait(0.8888)
        self.play(FadeIn(grid_bg[3]))
        self.wait(2.2222-0.4444-0.4444-0.4444)
        self.play( Indicate(daynums[4]) )
        self.wait(0.8888)
        self.play(FadeIn(grid_bg[4]))
        self.wait(2.2222-0.4444-0.4444-0.4444-0.4444)
        self.play( Indicate(daynums[5]) )
        self.wait(0.8888)
        self.play(FadeIn(grid_bg[5]))
        
        
        self.wait(2.2222)
        
        # manim -ql shard.py --disable_caching

        qianwu_rect = SurroundingRectangle(VGroup(daynums[0], daynums[1], daynums[2], daynums[3], daynums[4] ))
        qianwu_rect.set_z_index(4)
        self.play( 
            Create(qianwu_rect),
            Succession(
                get_bianse_ani(2),
                get_bianse_ani(3),
                get_bianse_ani(4),
                get_bianse_ani(5),
                get_bianse_ani(6),
                lag_ratio=0.8888
            )
            
        )
        # self.play( get_bianse_ani(3), run_time=0.2222)
        # self.play( get_bianse_ani(4), run_time=0.2222)
        # self.play( get_bianse_ani(5), run_time=0.2222)
        # self.play( get_bianse_ani(6), run_time=0.2222)
        
        self.wait(0.8888)
        self.play( FadeOut(qianwu_rect))
        
        # self.wait(2.2222)
        # self.play( Circumscribe(grid_bg[5]) )
        self.wait(0.2222)
        self.play( Indicate(daynums[5]),run_time=0.8888 )
        self.wait(0.8888)
        self.play( Indicate(daynums[6]),run_time=0.8888 )
        self.play( FadeIn(grid_bg[6]),run_time=0.8888 )

        self.play( Indicate(daynums[7]),run_time=0.8888 )
        self.play( FadeIn(grid_bg[7]),run_time=0.8888 )
  
        self.play( Indicate(daynums[8]),run_time=0.8888 )
        self.play( FadeIn(grid_bg[8]),run_time=0.8888 )

        self.play( Indicate(daynums[9]),run_time=0.8888 )
        self.play( FadeIn(grid_bg[9]),run_time=0.8888 )
        
        
        rect_678910 = SurroundingRectangle(VGroup(daynums[5], daynums[6], daynums[7], daynums[8], daynums[9]))
        rect_678910.set_z_index(4)
        
        self.play(
            Create(rect_678910, run_time=0.8888), 
            Succession(
                get_bianse_ani(7, Color_Period_B),
                get_bianse_ani(8, Color_Period_B),
                get_bianse_ani(9, Color_Period_B),
                get_bianse_ani(10, Color_Period_B),
                get_bianse_ani(11, Color_Period_B),
                lag_ratio=0.8888
            )
            
        )
        # self.wait(0.8888)
        self.play(FadeOut(rect_678910))
        
        # self.wait(0.8888)
        self.play( Indicate(daynums[10]), run_time=0.4444 )
        self.play( Indicate(daynums[11]), run_time=0.4444 )
        self.play( Indicate(daynums[12]), run_time=0.4444 )
        self.play( Indicate(daynums[13]), run_time=0.4444 )
        self.play( Indicate(daynums[14]), run_time=0.4444 )
        
        self.wait(0.2222)
        self.play( FadeIn(grid_bg[10]), run_time=0.4444 )
        self.play( FadeIn(grid_bg[11]), run_time=0.4444 )
        self.play( FadeIn(grid_bg[12]), run_time=0.4444 )
        self.play( FadeIn(grid_bg[13]), run_time=0.4444 )
        self.play( FadeIn(grid_bg[14]), run_time=0.4444 )
        
        self.wait(0.2222)
        
        self.play(
            Succession(
                get_bianse_ani(12),
                get_bianse_ani(13),
                get_bianse_ani(14),
                get_bianse_ani(15),
                get_bianse_ani(16),
                lag_ratio=0.8888
            )
        )
        # self.wait(0.8888)
        
        # rect
        
        self.wait(0.8888-0.2222-0.2222)
        self.play( Indicate(daynums[15]), run_time=0.4444 )
        self.play( Indicate(daynums[16]), run_time=0.4444 )
        self.play( Indicate(daynums[17]), run_time=0.4444 )
        self.play( Indicate(daynums[18]), run_time=0.4444 )
        self.play( Indicate(daynums[19]), run_time=0.4444 )
        
        self.wait(0.2222+0.2222)
        self.play( FadeIn(grid_bg[15]), run_time=0.4444 )
        self.play( FadeIn(grid_bg[16]), run_time=0.4444 )
        self.play( FadeIn(grid_bg[17]), run_time=0.4444 )
        self.play( FadeIn(grid_bg[18]), run_time=0.4444 )
        self.play( FadeIn(grid_bg[19]), run_time=0.4444 )
        self.wait(0.2222)
        
        self.play(
            Succession(
                get_bianse_ani(17, Color_Period_B),
                get_bianse_ani(18, Color_Period_B),
                get_bianse_ani(19, Color_Period_B),
                get_bianse_ani(20, Color_Period_B),
                get_bianse_ani(21, Color_Period_B),
                lag_ratio=0.8888
            )
        )
        
        self.wait(0.8888)
        # 往后都是每五天一个周期
        
        # 再总结一下 如果碎片降临在...

        
        self.play(
            Succession(
                get_bianse_ani(22),
                get_bianse_ani(23),
                get_bianse_ani(24),
                get_bianse_ani(25),
                get_bianse_ani(26),
                lag_ratio=0.8888
            ),
        )
        
        self.play(
            Succession(
                FadeIn(grid_bg[20], run_time=0.2222),
                FadeIn(grid_bg[21], run_time=0.2222),
                FadeIn(grid_bg[22], run_time=0.2222),
                FadeIn(grid_bg[23], run_time=0.2222),
                FadeIn(grid_bg[24], run_time=0.2222),
                lag_ratio=0.8888
            )
        )
        
        self.play(
            Succession(
                get_bianse_ani(27, Color_Period_B),
                get_bianse_ani(28, Color_Period_B),
                get_bianse_ani(29, Color_Period_B),
                get_bianse_ani(30, Color_Period_B),
                get_bianse_ani(31, Color_Period_B),
                lag_ratio=0.8888
            )
        )
        
        self.play(
            Succession(
                FadeIn(grid_bg[25], run_time=0.2222),
                FadeIn(grid_bg[26], run_time=0.2222),
                FadeIn(grid_bg[27], run_time=0.2222),
                FadeIn(grid_bg[28], run_time=0.2222),
                FadeIn(grid_bg[29], run_time=0.2222),
                lag_ratio=0.8888
            )
        )
        
        self.play( get_bianse_ani(32) )
        self.wait(0.2222)
        self.play( FadeIn(grid_bg[30]) )
        
        # for i in range(20, 31):
        #     self.play( FadeIn(grid_bg[i]), run_time = 0.2222 )
        
        # 我先放个日历在这边
        # 
        # 规律一：每个月当中，碎片所降临的大地图 5天为一个周期，
        # 什么意思呢？ 是这样的：
        # 如果碎片在1号降临，那么一定是在墓土
        # 如果碎片在2号降临，那么一定是在禁阁
        # 如果碎片在3号降临，那么一定是在云野
        # 如果碎片在4号降临，那么一定是在雨林
        # 如果碎片在5号降临，那么一定是在霞谷
        # 如果碎片在6号降临，那么一定是在墓土
        
        # 到这里就可以发现规律了， 每五天为一个周期
        # 所以可以接着以此类推， 6号一定是墓土，7号一定是禁阁，八号一定是云野，九号一定是雨林，十号一定是霞谷，
        # 11，12,13,14,15， 墓土禁阁云野雨林霞谷
        # 16 17 18 19 20 墓土禁阁云野雨林霞谷
        # 依次类推，每五天是一个周期
        
        # 所以再总结一下，如果碎片降临在1号，6号，11号... 那么必定是在墓土， 即 如果碎片降临在(5n+1)天，一定是在墓土
        # 如果碎片降临在2号，7号，12号... 那么必定是在墓土， 即 如果碎片降临在(5n+2)天，一定是在禁阁
        # (5n+3) 云野
        # (5n+4) 雨林
        # (5n+5) 霞谷
        
        self.wait(0.2222)
        
        fadeout_anims = []
        for i in range(32, 2-1, -1):
            fadeout_anims.append(
                get_bianse_ani(i, WHITE)
            )
        for i in range(30, 0-1, -1):
            fadeout_anims.append(
                FadeOut( grid_bg[i], run_time=0.2222 )
            )
        
        fadeout_anim_group = AnimationGroup(*fadeout_anims, lag_ratio=0.0202)
        self.play( fadeout_anim_group )
        
        self.play( Indicate(daynums[0]), FadeIn(grid_bg[0]), run_time = 0.4444 )
        self.wait(0.2222)
        self.play( Indicate(daynums[5]), FadeIn(grid_bg[5]), run_time = 0.4444 )
        self.wait(0.2222)
        self.play( Indicate(daynums[10]), FadeIn(grid_bg[10]), run_time = 0.4444 )
        self.play( Indicate(daynums[15]), FadeIn(grid_bg[15]), run_time = 0.2222 )
        self.play( Indicate(daynums[20]), FadeIn(grid_bg[20]), run_time = 0.2222 )
        self.play( Indicate(daynums[25]), FadeIn(grid_bg[25]), run_time = 0.2222 )
        self.play( Indicate(daynums[30]), FadeIn(grid_bg[30]), run_time = 0.2222 )
        
        self.play( 
            Succession(
                Wiggle(grid_bg[0], scale_value=2.2222-0.8888, run_time=0.8888),
                Wiggle(grid_bg[5], scale_value=2.2222-0.8888, run_time=0.8888),
                Wiggle(grid_bg[10], scale_value=2.2222-0.8888, run_time=0.8888),
                Wiggle(grid_bg[15], scale_value=2.2222-0.8888, run_time=0.8888),
                Wiggle(grid_bg[20], scale_value=2.2222-0.8888, run_time=0.8888),
                Wiggle(grid_bg[25], scale_value=2.2222-0.8888, run_time=0.8888),
                Wiggle(grid_bg[30], scale_value=2.2222-0.8888, run_time=0.8888),
                lag_ratio=0.4444
            )
        )
        
        self.wait(2.2222+0.8888)
        
        self.play( Indicate(daynums[1]), FadeIn(grid_bg[1]), run_time = 0.4444 )
        self.wait(0.2222)
        self.play( Indicate(daynums[6]), FadeIn(grid_bg[6]), run_time = 0.4444 )
        self.wait(0.2222)
        self.play( Indicate(daynums[11]), FadeIn(grid_bg[11]), run_time = 0.4444 )
        self.play( Indicate(daynums[16]), FadeIn(grid_bg[16]), run_time = 0.2222 )
        self.play( Indicate(daynums[21]), FadeIn(grid_bg[21]), run_time = 0.2222 )
        self.play( Indicate(daynums[26]), FadeIn(grid_bg[26]), run_time = 0.2222 )
        
        self.play( 
            Succession(
                Wiggle(grid_bg[0+1], scale_value=2.2222-0.8888, run_time=0.8888),
                Wiggle(grid_bg[5+1], scale_value=2.2222-0.8888, run_time=0.8888),
                Wiggle(grid_bg[10+1], scale_value=2.2222-0.8888, run_time=0.8888),
                Wiggle(grid_bg[15+1], scale_value=2.2222-0.8888, run_time=0.8888),
                Wiggle(grid_bg[20+1], scale_value=2.2222-0.8888, run_time=0.8888),
                Wiggle(grid_bg[25+1], scale_value=2.2222-0.8888, run_time=0.8888),
                lag_ratio=0.4444
            )
        )
        
        self.wait(0.8888+0.8888)
        self.play(
            AnimationGroup(
                AnimationGroup( Indicate(daynums[0+2]), FadeIn(grid_bg[0+2]), run_time = 0.2222),
                AnimationGroup( Indicate(daynums[5+2]), FadeIn(grid_bg[5+2]), run_time = 0.2222),
                AnimationGroup( Indicate(daynums[10+2]), FadeIn(grid_bg[10+2]), run_time = 0.2222),
                AnimationGroup( Indicate(daynums[15+2]), FadeIn(grid_bg[15+2]), run_time = 0.2222),
                AnimationGroup( Indicate(daynums[20+2]), FadeIn(grid_bg[20+2]), run_time = 0.2222),
                AnimationGroup( Indicate(daynums[25+2]), FadeIn(grid_bg[25+2]), run_time = 0.2222),
                lag_ratio=0.8888
            )
        )
        
        self.wait(0.8888)
        self.play(
            AnimationGroup(
                AnimationGroup( Indicate(daynums[0+3]), FadeIn(grid_bg[0+3]), run_time = 0.2222),
                AnimationGroup( Indicate(daynums[5+3]), FadeIn(grid_bg[5+3]), run_time = 0.2222),
                AnimationGroup( Indicate(daynums[10+3]), FadeIn(grid_bg[10+3]), run_time = 0.2222),
                AnimationGroup( Indicate(daynums[15+3]), FadeIn(grid_bg[15+3]), run_time = 0.2222),
                AnimationGroup( Indicate(daynums[20+3]), FadeIn(grid_bg[20+3]), run_time = 0.2222),
                AnimationGroup( Indicate(daynums[25+3]), FadeIn(grid_bg[25+3]), run_time = 0.2222),
                lag_ratio=0.8888
            )
        )
        
        self.wait(0.8888)
        self.play(
            AnimationGroup(
                AnimationGroup( Indicate(daynums[0+4]), FadeIn(grid_bg[0+4]), run_time = 0.2222),
                AnimationGroup( Indicate(daynums[5+4]), FadeIn(grid_bg[5+4]), run_time = 0.2222),
                AnimationGroup( Indicate(daynums[10+4]), FadeIn(grid_bg[10+4]), run_time = 0.2222),
                AnimationGroup( Indicate(daynums[15+4]), FadeIn(grid_bg[15+4]), run_time = 0.2222),
                AnimationGroup( Indicate(daynums[20+4]), FadeIn(grid_bg[20+4]), run_time = 0.2222),
                AnimationGroup( Indicate(daynums[25+4]), FadeIn(grid_bg[25+4]), run_time = 0.2222),
                lag_ratio=0.8888
            )
        )

        self.wait(0.8888+2.2222+0.8888)
        self.play( ApplyWave(rule1, run_time=8.8888) )
        
        self.wait(0.2222)
        
        # ----------------------------------------------------------
        
        # 然后接下来是规律二， 前半个月 周二黑、周六周日红，后半个月周三黑、周五周日红
        # 什么意思呢？是这样的：
        
        # 首先我们知道 碎片有两种， 
        # 如果伊甸山普通喷发，将会落下黑色石头，玩家可以获得普通烛火
        # 如果伊甸山猛烈爆发,将会落下红色石头, 玩家可以获得升华蜡烛
        # 我先放一个图示在这边
        
        # 而且众所周知，碎片肯定不会是一个月当中的每一天 都会降临
        # 所以实际上，在一个月当中，只有周二 周三 周五 周六 周日 才会有碎石
        
        # 更加具体一点，是这样的：
        # 前半个月，也就是日期大于等于1 小于等于15，  将会在周二 喷发黑色碎石, 周六周日喷发红色碎石
        # 后半个月，也就是日期大于等于16             将会在周三 喷发黑色碎石, 周五周日喷发红色碎石
        
        # 2:02
        rule2 = Tex(
            "② 前半个月(1<=日期<=15) 周二黑石、周六周日红石， \\\\ 后半个月(16<=日期) ~~~~ 周三黑石、周五周日红石",
            tex_template = MyTexTemplate,
            color = WHITE,
            font_size = 36,
        ).scale(0.8888).next_to(rule1, DOWN).shift(LEFT*0.2222+RIGHT*0.0808)
        self.play(Write(rule2), run_time = 8.8888)
        
        # self.wait(12.2222)
        self.wait(2.2222)
        
        cir_black = Circle(color = Color_BlackShard, fill_opacity=1, radius=0.4444).scale(1+0.2222)
        cir_black.next_to(rule2, DOWN).shift(LEFT*0.8888+LEFT*0.2222)
        self.play( Write(cir_black) )
        self.wait(0.8888)
        
        img_wc = ImageMobject(r"D:\MANIM\Projects\MyManimProjects\my_products\shard\white_candle.jpg").scale(2.2222)
        img_wc.next_to(cir_black, RIGHT).shift(RIGHT*0.8888+RIGHT*0.2222)
        self.play( FadeIn(img_wc) )
        self.wait(1.8888)
        
        
        cir_red = Circle(color = Color_RedShard, fill_opacity=1, radius=0.4444).scale(1+0.2222)
        cir_red.next_to(cir_black, DOWN)
        self.play( Write(cir_red) )
        self.wait(0.8888+0.8888)
        
        img_ac = ImageMobject(r"D:\MANIM\Projects\MyManimProjects\my_products\shard\ascended_candle.jpg").scale(0.2222*0.8888)
        img_ac.next_to(cir_red, RIGHT).shift(RIGHT*0.8888+RIGHT*0.8888+LEFT*0.2222)
        self.play( FadeIn(img_ac) )
        
        cir_black_cal = cir_black.copy().set_opacity(0.8888)
        cir_red_cal = cir_red.copy().set_opacity(0.8888)
        
        cirs = []
        for i in range(1,31+1):
            if i <=15:
                if i % 7 == 0:
                    cirs.append( cir_black_cal.copy() )
                else:
                    cirs.append( cir_red_cal.copy() )
            else:
                if i % 7 == 1:
                    cirs.append( cir_black_cal.copy() )
                else:
                    cirs.append( cir_red_cal.copy() )
        
        
        self.wait(8.8888)
        fd1 = AnimationGroup(
            FadeOut( grid_bg[5], run_time=0.2222),
            FadeOut( grid_bg[12], run_time=0.2222),
            FadeOut( grid_bg[19], run_time=0.2222),
            FadeOut( grid_bg[26], run_time=0.2222),
        )
        fd2 = AnimationGroup(
            FadeOut( grid_bg[1], grid_bg[8], grid_bg[15], grid_bg[22], grid_bg[29], run_time=0.8888 )
        )
        
        # self.play( fd1 )
        kuang_zhouer = SurroundingRectangle( VGroup(weekday_row[1], table[29]), color = BLACK )
        kuang_zhouer.set_z_index(5)
        self.play( 
            AnimationGroup(
                fd1,
                Create(kuang_zhouer, run_time=0.4444),
                lag_ratio=0.8888
            )
        )
        kuang_zhousan = SurroundingRectangle( VGroup(weekday_row[2], table[30]), color = BLACK )
        kuang_zhousan.set_z_index(5)
        self.play( Create(kuang_zhousan, run_time=0.4444) )
        
        kuang_zhouwu = SurroundingRectangle( VGroup(weekday_row[4], table[32]), color = RED )
        kuang_zhouwu.set_z_index(5)
        self.play( 
            AnimationGroup(
                fd2,
                Create(kuang_zhouwu, run_time=0.4444),
                lag_ratio=0.2222
            )
        )
        
        kuang_zhouliu = SurroundingRectangle( VGroup(weekday_row[5], table[33]), color = RED )
        kuang_zhouliu.set_z_index(5)
        self.play( Create(kuang_zhouliu, run_time=0.4444) )
        
        kuang_zhouri = SurroundingRectangle( VGroup(weekday_row[6], table[34]), color = RED )
        kuang_zhouri.set_z_index(5)
        self.play( Create(kuang_zhouri, run_time=0.4444) )
        
        self.wait(2.2222)
        self.play(
            FadeOut(
                VGroup(kuang_zhouer,kuang_zhousan,kuang_zhouwu,kuang_zhouliu,kuang_zhouri)
            )
        )
        
        # self.wait(8.8888)
        
        ''' bisanse '''
        # def get_bianse_ani ( idx, color=Color_DayPassed ): #idx means table[idx]
        #     return Transform( 
        #         table[idx], 
        #         Square(side_length=cell_width, fill_color=color, fill_opacity=0.8888, stroke_width=4.4444, stroke_color=GRAY_A).move_to(table[idx]),
        #         run_time = 0.2222
        #     )
        
        qianbanyue_hint = []
        for i in range (2,16+1):
            qianbanyue_hint.append( get_bianse_ani(i) )
            
        qianbanyue_hint_anis = AnimationGroup(*qianbanyue_hint, lag_ratio=0.2222+0.2222)
        self.play( qianbanyue_hint_anis )
                
        
        def shard_tip_anim( idx:int, color:str ):
            cir = cirs[idx-2]
            
            cir.move_to(table[idx])
            
            table[idx].set_z_index(22)
            cir.set_z_index(23)
            grid_bg[idx-2].set_z_index(24)
            daynums[idx-2].set_z_index(25)
            
            return AnimationGroup(
                FadeOut( grid_bg[idx-2], run_time=0.2222 ),
                Create( cir, run_time = 0.4444 ),
                lag_ratio=0.2222
            ) 
        

        def bg_fadeout( idx:int ):
            return FadeOut( grid_bg[idx-2], run_time=0.2222 )
        
        qian_kuang_zhouer = SurroundingRectangle( VGroup(weekday_row[1], table[15]) , color=BLACK ).set_z_index(30)
        qian_kuang_zhouliu = SurroundingRectangle( VGroup(weekday_row[5], table[12]), color=RED_D ).set_z_index(30)
        qian_kuang_zhouri = SurroundingRectangle( VGroup(weekday_row[6], table[13]), color=RED_D ).set_z_index(30)
        
        self.wait(2.2222)
        
        qian_honghei = [
            AnimationGroup( shard_tip_anim(8, "black"),shard_tip_anim(8+7, "black") , lag_ratio=0.4444),
            AnimationGroup( bg_fadeout(2), bg_fadeout(2+7), bg_fadeout(2+7+7), lag_ratio=0.4444),
            AnimationGroup( bg_fadeout(4), bg_fadeout(4+7),                    lag_ratio=0.4444),
            AnimationGroup( shard_tip_anim(5, "red"),shard_tip_anim(5+7, "red") , lag_ratio=0.4444),
            AnimationGroup( shard_tip_anim(6, "red"),shard_tip_anim(6+7, "red") , lag_ratio=0.4444),
        ]
        
        self.play( Create(qian_kuang_zhouer, run_time=0.4444)  )
        self.play( qian_honghei[1] )
        self.play( Create(qian_kuang_zhouliu, run_time=0.4444-0.0808) )
        self.play( qian_honghei[2])
        self.play( Create(qian_kuang_zhouri), run_time=0.4444 )
        
        
        self.wait(0.8888+0.2222)
        self.play( qian_honghei[0] )
        self.wait(0.2222)
        self.play( qian_honghei[3] )
        self.play( qian_honghei[4] )
        self.wait(0.8888)
        
        qianbanyue_hint_disap = []
        for i in range (2,16+1):
            qianbanyue_hint_disap.append( get_bianse_ani(i, WHITE) )
            
        qianbanyue_hint_disp_anis = AnimationGroup(*qianbanyue_hint_disap, lag_ratio=0.2222+0.2222)
        
        self.play( 
            qianbanyue_hint_disp_anis,
            FadeOut(qian_kuang_zhouer),
            FadeOut(qian_kuang_zhouliu),
            FadeOut(qian_kuang_zhouri),
        )
        
        houbanyue_hint = []
        for i in range (17, 32+1):
            houbanyue_hint.append( get_bianse_ani(i, Color_Period_B) )
        houbanyue_hint_anis = AnimationGroup(*houbanyue_hint, lag_ratio=0.4444)
        
        self.play(
            houbanyue_hint_anis
        )
        
        
        
        self.wait(0.8888)
        
        hou_kuang_zhousan = SurroundingRectangle( VGroup(table[23], table[30]), color=BLACK ).set_z_index(30)
        hou_kuang_zhouwu = SurroundingRectangle( VGroup(table[18], table[32]), color=RED_D ).set_z_index(30)
        hou_kuang_zhouri = SurroundingRectangle( VGroup(table[20], table[27]), color=RED_D ).set_z_index(30)
        
        
        
        hou_honghei = [
            AnimationGroup( bg_fadeout(22), bg_fadeout(29),  lag_ratio=0.4444),
            AnimationGroup( shard_tip_anim(23, "black"), shard_tip_anim(30, "black"), lag_ratio=0.4444 ),
            AnimationGroup( bg_fadeout(19), bg_fadeout(26),  lag_ratio=0.4444-0.0808),
            AnimationGroup( shard_tip_anim(18, "red"), shard_tip_anim(25, "red"), shard_tip_anim(32, "red"), lag_ratio=0.4444-0.0909 ),
            AnimationGroup( shard_tip_anim(20, "red"), shard_tip_anim(27, "red"), lag_ratio=0.4444 ),
        ]
        
        self.play( hou_honghei[0] )
        self.play( Create(hou_kuang_zhousan, run_time=0.4444-0.0808 ) )
        self.play( Create(hou_kuang_zhouwu, run_time=0.4444 ) )
        self.play( hou_honghei[2] ) 
        self.play( Create(hou_kuang_zhouri, run_time=0.4444 ) )
        
        self.wait(0.8888)
        
        self.wait(0.2222)
        self.play( hou_honghei[1] )
        self.wait(0.2222)
        self.play( hou_honghei[3] ) 
        self.play( hou_honghei[4] ) 
    
        houbanyue_hint_disap = []
        for i in range(17,32+1):
            houbanyue_hint_disap.append( get_bianse_ani(i, WHITE) )
        
        houbanyue_hint_disap_ani = AnimationGroup(*houbanyue_hint_disap, lag_ratio=0.4444)
        
        self.play(
            houbanyue_hint_disap_ani,
            FadeOut(hou_kuang_zhousan),
            FadeOut(hou_kuang_zhouwu),
            FadeOut(hou_kuang_zhouri),
        )
        
        self.wait(0.8888)
        
        self.play(
            FadeOut(img_wc),
            FadeOut(cir_black),
            FadeOut(img_ac),
            FadeOut(cir_red),
        )
        
        # self.wait(0.2222)
        
        self.play( ApplyWave(rule2), run_time = 0.8888 )
        
        
        def cir_wiggle( idx:int ): # 正数是日期idx号，复数是负的星期idx
            if idx >= 1:
                return Wiggle( cirs[idx-1], scale_value=2.2222-0.8888,  run_time=0.8888-0.2222 )
            else:
                idx = - idx
                return Wiggle( weekday_row[idx-1] , scale_value=2.2222-0.8888,  run_time=0.8888-0.2222 )
        
        self.play( qianbanyue_hint_anis )
        # self.wait(0.8888)
        
        self.play( AnimationGroup(
            cir_wiggle(-2),
            cir_wiggle(7),
            cir_wiggle(14),
            lag_ratio=0.2222
        ) )
        self.play( AnimationGroup(
            cir_wiggle(-6),
            cir_wiggle(4),
            cir_wiggle(11),
            lag_ratio=0.2222
        ) )
        self.play( AnimationGroup(
            cir_wiggle(-7),
            cir_wiggle(5),
            cir_wiggle(12),
            lag_ratio=0.2222
        ) )
        
        self.play( qianbanyue_hint_disp_anis )
        
        
        self.play( houbanyue_hint_anis )
        self.wait(0.8888)
        
        self.play( AnimationGroup(
            cir_wiggle(-3),
            cir_wiggle(22),
            cir_wiggle(29),
            lag_ratio=0.2222
        ) )
        self.play( AnimationGroup(
            cir_wiggle(-5),
            cir_wiggle(17),
            cir_wiggle(24),
            cir_wiggle(31),
            lag_ratio=0.2222
        ) )
        self.play( AnimationGroup(
            cir_wiggle(-7),
            cir_wiggle(19),
            cir_wiggle(26),
            lag_ratio=0.2222
        ) )
        
        self.play( houbanyue_hint_disap_ani )
        
        self.play( ApplyWave(rule2), run_time = 0.8888 )
        
        # 以上就是规律2， 前半个月(1-15号) 二黑六日红
        # 后半个月（16号及以后）三黑五日红
        #---------------------------------------------------------------------
        
        # 接下来是规律三，规律三是一张表， 这个 暂停自己查看即可，
        # 这个表格是 “碎片时间 对应的小地图和烛火数目”表
        # 带大家稍微看一下
        
        # 一行是一个大地图
        # 一列是一个weekday
        # 如果在周二有碎片在云野，那么地点是蝴蝶平原，给200白蜡烛烛火
        # 如果在周三有碎片在玉林，那么地点是大树屋， 给3.5个升华蜡烛的烛火
        
        rule3 = Tex(
            "③ ``碎片事件 对应的小地图和烛火数目`` 表格 ~~~~",
            tex_template = MyTexTemplate,
            color = WHITE,
            font_size = 36,
        ).scale(0.8888).next_to(rule2, DOWN).shift(LEFT*0.0202+LEFT*0.0202)
        
        self.wait(0.8888)
        self.play( Write(rule3), run_time = 2.2222-0.8888 )
        
        img_rule3 = ImageMobject(r"D:\MANIM\Projects\MyManimProjects\my_products\shard\rule3.png")
        img_rule3.next_to(rule2, DOWN).shift(RIGHT*0.2222+UP*0.8888+UP*0.2222).scale(0.2222*2.2222)
        self.play( FadeIn(img_rule3) )
        
        
        print("frame width:  ", )
        self.play( self.camera.frame.animate.set(width = self.camera.frame.get_width()-2.2222).move_to(img_rule3) )
        self.play( self.camera.frame.animate.set(width = self.camera.frame.get_width()-4.4444-0.8888-0.2222).shift(UP*0.2222), rate_func = rate_functions.ease_in_out_quint  )
        print("frame width:  ", self.camera.frame.get_width())
        
        self.wait(2.2222)
        self.play( ApplyWave(rule3), run_time=2.2222+2.2222 )
        
        self.wait(0.2222)
        
        rect_rule3 = Rectangle(width=4.4444+2.2222-0.8888, height=0.4444).move_to(img_rule3).shift(UP*0.4444+UP*0.2222+UP*0.2222+UP*0.0808+UP*0.0202+UP*0.0202)
        self.play( Create(rect_rule3) )
        self.wait(0.2222)
        
        imgr3_s_down = 0.8888-0.2222-0.0808
        imgr3_s_right = 0.8888+0.2222-0.0808-0.0202+0.0202
        
        for i in range (4):
            self.play( rect_rule3.animate.shift(DOWN*imgr3_s_down), rate_func = rate_functions.ease_in_out_quint, run_time=0.4444 )

        
        self.wait(0.8888)
        self.play( 
            Transform(
                rect_rule3,
                Rectangle(width=0.8888, height=4.4444-0.8888).move_to(img_rule3).shift(LEFT*2.2222+RIGHT*0.2222+RIGHT*0.0404+RIGHT*0.0202+RIGHT*0.0202)
            )
        )
        for i in range (4):
            self.play( rect_rule3.animate.shift(RIGHT*imgr3_s_right), rate_func = rate_functions.ease_in_out_quint, run_time=0.4444 )
            
        self.wait(0.8888)
        
        self.play( FadeOut(rect_rule3) )  
        
        tip_ellipse = Ellipse(width=2.2222, height=1.1111, color=Color_BlackShard).scale(0.4444).move_to(img_rule3).shift(LEFT*2.2222+UP*1.1111+RIGHT*0.2222+RIGHT*0.0202)
        self.play( Create(tip_ellipse) )
        self.wait(4.4444)
        self.play( FadeOut(tip_ellipse) )
        self.wait(0.8888)
        
        tip_ellipse = Ellipse(width=2.2222, height=1.1111, color=Color_RedShard).scale(0.4444).move_to(img_rule3).shift(UP*0.4444+RIGHT*0.0202)
        self.play( Create(tip_ellipse) )
        self.wait(4.4444)
        self.play( FadeOut(tip_ellipse) )
        
        self.wait(0.8888)
        self.play( self.camera.frame.animate.set(width = self.camera.frame.get_width()+4.4444).shift(UP*0.8888), run_time = 4.4444, rate_func = rate_functions.ease_in_out_quint )
        
        self.play( ApplyWave(rule1), run_time = 2.2222 )
        self.play( ApplyWave(rule2), run_time = 2.2222 ) 
        
        self.play( self.camera.frame.animate.set(width = self.camera.frame.get_width()-2.2222).shift(DOWN*0.8888+UP*0.01010101), run_time = 4.4444-0.8888, rate_func = rate_functions.ease_in_out_quint )
        
        self.wait( 4.4444-0.8888 )
        self.play( self.camera.frame.animate.set(width = self.camera.frame.get_width()-2.2222), run_time = 4.4444-0.8888, rate_func = rate_functions.ease_in_out_quint )

        # 这个图可以暂停观看， 或者截图留下来备用
        # 这个表就是规律三，   接下来讲规律四
        
        # -----------------------------------------------------------------------------------------
        
        # 规律四也是一张表， 这个表是“在一周当中， 每天的碎片喷发的具体时间”， 精确到分钟
        # 同样 暂停观看即可
        ####
        # 如果在碎片在某个周二降临，那么只会在9:08-10:00, 14:08-15:00, 19:08-20:00 这三个时间段，有碎片
        # 后面同理
        
        # 可以暂停观看 以及自行截图备用
        
        
        rule4 = Tex(
            "④ ``每天 碎片喷发的具体时间`` 表格（精确到分钟） ",
            tex_template = MyTexTemplate,
            color = WHITE,
            font_size = 36,
        ).scale(0.8888).next_to(rule3, DOWN).shift(RIGHT*0.2222+RIGHT*0.0202)
        
        img_rule4 = ImageMobject(r"D:\MANIM\Projects\MyManimProjects\my_products\shard\rule4.png").scale(0.2222*2.2222)
        img_rule4.next_to(rule4, DOWN).shift(RIGHT*0.2222)
        
        self.wait(2.2222)
        self.play( 
            self.camera.frame.animate.set(width = self.camera.frame.get_width()+4.4444+2.2222).shift(UP*0.8888+UP*0.44444), run_time = 2.2222, rate_func = rate_functions.ease_in_out_quint 
        )
        
        self.play( FadeOut(img_rule3), run_time = 0.8888 )
        # self.wait(0.2222)
        self.play( Write(rule4) )
        # self.wait(0.2222)
        self.play( FadeIn(img_rule4), run_time = 0.8888 )
        # self.wait(0.2222)
        self.play( 
            self.camera.frame.animate.set(width = self.camera.frame.get_width()-4.4444-2.2222).move_to(img_rule4), run_time = 2.2222-0.8888, rate_func = rate_functions.ease_in_out_quint 
        )
        
        # self.wait(2.2222)
        self.play( ApplyWave(rule4), run_time = 4.4444-0.8888 )
        self.wait(2.2222-0.8888)
        
        self.play( self.camera.frame.animate.set(width = self.camera.frame.get_width()-0.8888).move_to(img_rule4) )

        rule1_tip_ellipse = Ellipse(width=1.1111+0.2222, height=1.1111, color=Color_BlackShard).move_to(img_rule4).shift(LEFT*2.2222+LEFT*0.2222+LEFT*0.0808+LEFT*0.0202)
        self.wait(2.2222-0.8888)
        self.play( Create(rule1_tip_ellipse) )
        self.wait(8.8888)
        self.play( FadeOut(rule1_tip_ellipse, shift = RIGHT*2.2222) )
        
        self.wait(4.4444)
        
        
        self.play( 
            self.camera.frame.animate.set(width = self.camera.frame.get_width()+8.8888).shift(UP*2.2222+LEFT*4.4444+LEFT*0.2222), run_time = 2.2222
        )
        self.play( FadeOut(img_rule4) )
                            
        
        '''
        def bg_fadeout( idx:int ):
            return FadeOut( grid_bg[idx-2], run_time=0.2222 )

        '''
        def cir_fadeout( idx:int ): #idx is day
            return FadeOut( cirs[idx-1], run_time = 0.2222 )
        
        self.play( 
            cir_fadeout(4), cir_fadeout(5),
            cir_fadeout(7), cir_fadeout(11),cir_fadeout(12), 
            cir_fadeout(14), cir_fadeout(17),cir_fadeout(19), 
            cir_fadeout(22), cir_fadeout(24),cir_fadeout(26),
            cir_fadeout(29), cir_fadeout(31),
        )
                
        # -----------------------------------------------------------
        # 再总结一下， 网易 国服的碎片规律可以被概括成这四条规律。
        # 掌握这四条规律，就可以实现自己推算碎片时间
        # 接下来我将给大家再用图示回顾一下这四个规律，然后会提示大家截四张图
        
        # 规律1： 碎片所降临的大地图，五天为一个周期
        # 这里可以自行截图
        # 规律2：前半个月（1号到15号） 周二黑石 周六周日红石， 后半个月（16号及以后） 周三黑石 周五周日红石
        # 这里可以自行截图
        # 规律3： 是 碎片事件对应的小地图和烛火数目 表格
        # 这里可以自行截图
        # 规律4： 是 每天碎片喷发的具体时间 表格（精确到分钟）
        # 这里可以自行截图 
        
        # 恭喜你，理解了这四条规律，以后你就可以自行推算网易国服的碎片时间啦（包括官服以及其他渠道服）
        
        conclu_rule1_anis = []
        
        for i in range( 1,7+1 ):
            
            for j in range( 1, 5+1 ):
                if (i-1)*5+j > 31 : continue
                if (i%2)==1:
                    conclu_rule1_anis.append( get_bianse_ani( (i-1)*5+j + 1, Color_Period_A) )
                else :
                    conclu_rule1_anis.append( get_bianse_ani( (i-1)*5+j + 1, Color_Period_B) )
                    
            conclu_rule1_anis.append( Wait(0.4444) )
            
            for j in range( 1, 5+1 ):
                if (i-1)*5+j > 31 : continue
                conclu_rule1_anis.append(  FadeIn(grid_bg[(i-1)*5+j - 1], run_time = 0.2222) ) 
                
            conclu_rule1_anis.append( Wait(0.4444) )
        
        self.wait(2.2222)
        self.play( ApplyWave(rule1), run_time = 0.8888 )
        self.play( ApplyWave(rule2), run_time = 0.8888 )
        self.play( ApplyWave(rule3), run_time = 0.8888 )
        self.play( ApplyWave(rule4), run_time = 0.8888 )

        self.wait(8.8888-0.8888)
        self.play( 
            AnimationGroup( *conclu_rule1_anis, lag_ratio=0.4444 ),
            ApplyWave(rule1, run_time = 2.2222),
            FadeOut(rule2),
            FadeOut(rule3),
            FadeOut(rule4),
        )
        
        conclu_rule1_pass_anis = []
        for i in range (1,31+1):
            conclu_rule1_pass_anis.append( FadeOut(grid_bg[i-1], run_time=0.1111) )
            conclu_rule1_pass_anis.append( get_bianse_ani(i+1, WHITE, 0.1111) )
            
        
        self.wait(4.4444-2.2222)
        self.play(
            AnimationGroup(*conclu_rule1_pass_anis, lag_ratio=0.1111)
        )
        
        
        #-------------------
        # self.wait(4.4444)
        self.play( FadeIn(rule2) )
        
        qianban_a = []
        for i in range(1,15+1):
            qianban_a.append( get_bianse_ani(i+1, Color_Period_A) )
            
        houban_b = []
        for i in range(15,31+1):
            houban_b.append( get_bianse_ani(i+1, Color_Period_B) )
        
        def weekday_wiggle( i:int ): #i=1,2,3...
            return Wiggle(weekday_row[i-1], scale_value=2.2222, run_time=0.8888)
        
        def cir_fadein( i:int ): #i=1,2,3...
            return FadeIn( cirs[i-1], run_time=0.2222 )
        
        conclu_rule2_anis = [
            AnimationGroup( *qianban_a, lag_ratio=0.2222 ), Wait(0.2222),
            
            AnimationGroup( weekday_wiggle(2), cir_fadein(7), cir_fadein(14), lag_ratio=0.2222 ), Wait(0.2222),
            AnimationGroup( weekday_wiggle(6), cir_fadein(4), cir_fadein(11),weekday_wiggle(7), cir_fadein(5), cir_fadein(12), lag_ratio=0.2222 ), 
            
            Wait(0.8888),
            
            AnimationGroup( *houban_b, lag_ratio=0.2222 ), Wait(0.2222),
            
            AnimationGroup( weekday_wiggle(3), cir_fadein(22), cir_fadein(29), lag_ratio=0.2222 ), Wait(0.2222),
            AnimationGroup( weekday_wiggle(5), cir_fadein(17), cir_fadein(24), cir_fadein(31),weekday_wiggle(7), cir_fadein(19), cir_fadein(26),  lag_ratio=0.2222 ), 
        ]
        
        for ani in conclu_rule2_anis:
            self.play( ani )

        self.wait(4.4444)
        
        # -------------------------------------------
        
        self.play( Write(rule3) )
        self.play( 
            self.camera.frame.animate.set(width = self.camera.frame.get_width()-4.4444).move_to(img_rule3), run_time = 2.2222, rate_func = rate_functions.ease_in_out_quint 
        )
        self.play( 
            FadeIn(img_rule3),
            ApplyWave(rule3, run_time=2.2222)
        )
        self.play( 
            self.camera.frame.animate.set(width = self.camera.frame.get_width()-4.4444+0.2222).shift(UP*0.2222)
        )
        
        
        self.wait(2.2222) #暂停截图
        
        self.play( 
            self.camera.frame.animate.set(width = self.camera.frame.get_width()+8.8888).shift(LEFT*4.4444+UP*0.8888+UP*0.7777), run_time = 2.2222, rate_func = rate_functions.ease_in_out_quint 
        )
        self.play( FadeOut(img_rule3) ) 
        
        #------------------------------------------------
        
        self.play( Write(rule4) )
        self.play( 
            self.camera.frame.animate.set(width = self.camera.frame.get_width()-4.4444).move_to(img_rule4), run_time = 2.2222, rate_func = rate_functions.ease_in_out_quint 
        )
        self.play( 
            FadeIn(img_rule4),
            ApplyWave(rule4, run_time=2.2222)
        )
        self.play( 
            self.camera.frame.animate.set(width = self.camera.frame.get_width()-4.4444)
        )
        
        self.wait(4.4444-0.8888) #暂停截图
        
        self.play( 
            self.camera.frame.animate.set(width = self.camera.frame.get_width()+8.8888).shift(LEFT*4.4444+UP*2.2222), run_time = 2.2222, rate_func = rate_functions.ease_in_out_quint 
        )
        self.play( FadeOut(img_rule4) ) 
        
        # -------------------
        
        self.play( 
            self.camera.frame.animate.shift(UP*0.7777+DOWN*0.07070707070707).set(width = self.camera.frame.get_width()+0.7777+0.07070707070707 )
        )
        
        star_icon = ImageMobject(r"D:\MANIM\Projects\MyManimProjects\my_products\shard\star.jpg").scale(2.2222)
        star_icon.next_to( table, UP ).shift(UP*0.7777+LEFT*0.7777+LEFT*0.7777)
        
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
                Write( congrats_Tex )
            ),
            lag_ratio = 0.8888
        )
        
        self.wait(8.8888*8.8888)
        # manim -ql shard.py --disable_caching
        # manim -qh shard.py --disable_caching

