from manim import *

class L13(MovingCameraScene):
    def construct(self):
                      #genetal_intro
        logo=   ImageMobject("logo.png")
        logo.to_edge(RIGHT)
        self.add(logo)
        intro= Text("Learn Physics \n with \n Farouk", t2w = {'Farouk':BOLD}, t2c = {'Farouk': YELLOW} ).scale(2)
        intro.to_edge(LEFT)
        self.play(Write(intro),  FadeIn(logo), run_time=5)
        self.wait(5)
                        #video_intro
        welcome = Text("Welcome back", color = RED)
        to = Text("to", color= YELLOW).next_to(welcome, DOWN)
        welcome_group = VGroup(welcome, to)
        qm = Text("Quantum Mechanics", color = GREEN)
        qm.next_to(welcome_group, DOWN)
        self.play(Transform(intro, welcome))
        self.play(Write(to))
        self.play(Write(qm))
        self.wait(3)
        lec= Text("Lecture 13", color= GRAY_A).to_edge(UP).scale(0.25)
        spin= Text("Spin 1/2 System", color= PINK).scale(0.5)
        spin.next_to(lec, DOWN)
        self.remove(welcome,to, intro)
        self.play(Transform(qm, lec))
        logo.scale(0.25).to_edge(UP)
        self.play(Write(spin), run_time= 3)
        self.wait(5)
        system = Text("Particle \n (electron)").next_to(spin, RIGHT + 0.2 * DOWN).scale(0.5)
        ssarrow = Arrow(spin.get_right(), system.get_left(), buff = 0.3)
        self.play(Create(ssarrow), run_time = 2)
        self.play(self.camera.frame.animate.scale(0.5).move_to(system))
        self.play(Write(system), run_time = 2)
        self.wait(5)
        self.play(self.camera.frame.animate.scale(2).move_to(ORIGIN))
        system_spin = MathTex(r"S = \frac{1}{2}, \ \frac{3}{2}, \ \frac{\hbar}{2}, \ \dots ").next_to(spin, LEFT + 0.2 * DOWN).scale(0.5)
        ssparrow = Arrow(spin.get_left(), system_spin.get_right(), buff = 0.3)

        self.play(Create(ssparrow), run_time = 2)
        self.play(self.camera.frame.animate.scale(0.5).move_to(system_spin))
        self.play(Write(system_spin), run_time = 5)
        self.wait(3)
        self.play(self.camera.frame.animate.scale(2).move_to(ORIGIN))
        self.remove(system, ssarrow, system_spin, ssparrow)
        self.wait()

        exp= Text("eg: S-G EXP", color = BLUE).move_to([-2, 2, 0]).scale(0.5)
        self.play(Write(exp), run_time = 3)
        self.wait()
                #oven
        e1 = Ellipse(width= 0.25, height= 0.5, fill_color= RED, fill_opacity = 0.5)
        e2 = e1.copy().move_to(2*LEFT)
        l1 = Line(e1.get_top(), e2.get_top(), color= RED)
        l2 = Line(e1.get_bottom(), e2.get_bottom(), color= RED)
        oven = VGroup(e1, e2, l1, l2).scale(0.5).to_edge(LEFT)
        self.add(oven)
        self.play(self.camera.frame.animate.scale(0.5).move_to(oven))
        oven_text = Text("Oven").scale(0.75).next_to(oven, DOWN)
        self.play(Write(oven_text, run_time= 2))
        self.wait(5)
        self.play(self.camera.frame.animate.scale(2).move_to(ORIGIN))
        self.wait()
         #screen
        vertices1 = [
            np.array([1, -1, 0]),
            np.array([-1.2, -1, 0]),
            np.array([-1, 1, 0]),
            np.array([1.2, 1, 0])
        ]
        screen = Polygon(*vertices1, color=GRAY_A, fill_opacity=0.5).to_edge(RIGHT)
        self.add(screen)
        self.play(self.camera.frame.animate.scale(0.5).move_to(screen))
        screen_text = Text("Screen").scale(0.75).next_to(screen, DOWN)
        self.play(Write(screen_text))
        self.wait(3)
        self.play(self.camera.frame.animate.scale(2).move_to(ORIGIN))
        self.wait()
        dash_line = DashedLine(oven.get_right(), screen.get_center())
        self.add(dash_line)
        blue_dot1 = Dot(radius = 0.1 , color = PURE_BLUE)
        blue_dot1.to_edge(LEFT)
        self.play(blue_dot1.animate.move_to(screen.get_center()), run_time=10, rate_func = linear)
        self.wait(2)

         #magnet
        vertices2 = [
            np.array([1, -0.2, 0]),
            np.array([ -1.5, -0.2, 0]),
            np.array([-1,0.2, 0 ]),
            np.array([1.5, 0.2, 0])

        ]
        mp1 = Polygon(*vertices2, fill_color = RED, fill_opacity= 1)
        mp2=mp1.copy().move_to(3*DOWN)
        vertices3= [
            np.array([1.5, 0.2, 0]),
            np.array([1, -0.2, 0]),
            np.array([1.25, -0.4, 0])
        ]
        mp3 = Polygon(*vertices3, fill_color = RED, fill_opacity= 0.5)
        vertices4= [
            np.array([-1.5, -0.2, 0]),
            np.array([-1, 0.2, 0]),
            np.array([-1.25, -0.4, 0])
        ]
        mp4 = Polygon(*vertices4, fill_color = RED, fill_opacity= 0.5)
        vertices5 = [
            np.array([1, -0.2, 0]), 
            np.array([-1.5, -0.2, 0]),
            np.array([-1.25, -0.4, 0]),
            np.array([1.25, -0.4, 0])
        ]
        mp5 = Polygon(*vertices5, fill_color = RED, fill_opacity= 1)
        uppermp = VGroup(mp1, mp3, mp4, mp5)
        #downmp
      
        vertices6 = [
            np.array([1.5, -2.3, 0]), 
            np.array([1.5, -2.8, 0]),
            np.array([-1, -2.8, 0]),
            np.array([-1, -2.3, 0])
            
        ]
        md1 = Polygon(*vertices6, fill_color = RED, fill_opacity= 0.5)
        vertices7 = [
            np.array([1.5, -2.3, 0]), 
            np.array([1.3, -2.5, 0]),
            np.array([-1.2, -2.5, 0]),
            np.array([-1, -2.3, 0])
            
        ]
        md2 = Polygon(*vertices7, fill_color = RED, fill_opacity= 1)

        vertices8 = [
            np.array([1.06, -3.2, 0]), 
            np.array([1.05, -2.85, 0]),
            np.array([-1.47, -2.85, 0]),
            np.array([-1.45, -3.2, 0])
            
        ]
        md3= Polygon(*vertices8, fill_color = RED, fill_opacity= 1)

        vertices9 = [
            np.array([1.3, -2.6, 0]), 
            np.array([1.05, -2.85, 0]),
            np.array([-1.47, -2.85, 0]),
            np.array([-1.3, -2.6, 0])
            
        ]
        md4= Polygon(*vertices9, fill_color = RED, fill_opacity= 1)
        downmp = VGroup(mp2, md1, md2, md3, md4)
        
        uppermp.move_to([-1.5, 0.7, 0])
        self.add(uppermp)
        self.play(self.camera.frame.animate.scale(0.5).move_to(uppermp))
        self.wait()
        uppermp_text = Text("N-pole", color = PURPLE).scale(0.3).next_to(uppermp, UP)
        self.play(Write(uppermp_text))
        self.wait()
        self.play(self.camera.frame.animate.scale(2).move_to(ORIGIN))
        downmp.move_to([-1.5, -0.7 , 0])
        self.add(downmp)
        self.wait()
        self.play(self.camera.frame.animate.scale(0.5).move_to(downmp))
        downmp_text = Text("S-pole", color = PURPLE).scale(0.3).next_to(downmp, DOWN)
        self.play(Write(downmp_text))
        self.wait(2)
        self.play(self.camera.frame.animate.scale(2).move_to(ORIGIN))
        self.wait(2)
        magnet_text = Text("Inhomogenious  \n    magnetic \n   field").scale(0.3)
        magnet_text.next_to(downmp_text, DOWN)
        self.play(Write(magnet_text))
        self.wait(2)

         #dots 
        red_dot1 = Dot(radius = 0.1 , color = PURE_RED)
        red_dot1.to_edge(LEFT)
        self.play(red_dot1.animate.move_to([-1.5, 0, 0]), run_time=4)
        self.play(red_dot1.animate.move_to(0.5*UP + 5.5*RIGHT), run_time = 4)
        self.wait(2)

        yellow_dot1 = Dot(radius = 0.1 , color = YELLOW)
        yellow_dot1.to_edge(LEFT)
        self.play(yellow_dot1.animate.move_to([-1.5, 0, 0]), run_time=4)
        self.play(yellow_dot1.animate.move_to(0.5*DOWN + 5.5*RIGHT), run_time = 4)
        self.wait(2)

        red_dot3 = Dot(radius = 0.1 , color = PURE_RED)
        red_dot3.to_edge(LEFT)
        self.play(red_dot3.animate.move_to([-1.5, 0, 0]), run_time=4)
        self.play(red_dot3.animate.move_to(0.5*UP + 5.5*RIGHT), run_time = 4)
        self.wait(2)

        yellow_dot3 = Dot(radius = 0.1 , color = YELLOW)
        yellow_dot3.to_edge(LEFT)
        self.play(yellow_dot3.animate.move_to([-1.5, 0, 0]), run_time=4)
        self.play(yellow_dot3.animate.move_to(0.5*DOWN + 5.5*RIGHT), run_time = 4)
        self.wait(2)

        red_dot2 = Dot(radius = 0.1 , color = PURE_RED)
        red_dot2.to_edge(LEFT)
        self.play(red_dot2.animate.move_to([-1.5, 0, 0]), run_time=4)
        self.play(red_dot2.animate.move_to(0.5*UP + 5.5*RIGHT), run_time = 4)
        self.wait(2)

        yellow_dot2 = Dot(radius = 0.1 , color = YELLOW)
        yellow_dot2.to_edge(LEFT)
        self.play(yellow_dot2.animate.move_to([-1.5, 0, 0]), run_time=4)
        self.play(yellow_dot2.animate.move_to(0.5*DOWN + 5.5*RIGHT), run_time = 4)
        self.wait(2)
        self.play(self.camera.frame.animate.scale(0.5).move_to(screen))
        spin_up_text = MathTex(r"S_+ = + \frac{\hbar}{2}", color = PURE_RED).scale(0.3).next_to(red_dot2, 0.5*RIGHT)
        self.play(Write(spin_up_text), run_time = 3)
        self.wait(6)
        spin_down_text = MathTex(r"S_- = - \frac{\hbar}{2}", color = YELLOW).scale(0.3).next_to(yellow_dot2, 0.5*RIGHT)
        self.play(Write(spin_down_text), run_time = 3)
        self.wait(6)
        self.play(self.camera.frame.animate.scale(2).move_to(ORIGIN))
        self.wait()
        S_G_exp = VGroup(oven, oven_text, screen, screen_text, uppermp, uppermp_text, downmp, downmp_text,
                         magnet_text, dash_line, blue_dot1, red_dot1, red_dot2, red_dot3,
                         yellow_dot1, yellow_dot2, yellow_dot3, spin_up_text, spin_down_text)
        self.play(FadeOut(lec, qm, spin, exp),S_G_exp.animate.scale(0.6).to_edge(UP))
        self.wait(2)

          #spin_half_eqss
        eigen_eq = Text("The Eigen Value Equation", color = GRAY).scale(0.75)
        eigen_eq.next_to(S_G_exp, DOWN)
        self.play(Write(eigen_eq), run_time = 2, rate_func = linear)
        self.wait(2)
        eigen_math = MathTex(r" A  \ | \grave{a} > =  \grave{a}  \ | \grave{a} >").scale(2).next_to(eigen_eq, DOWN)
        self.play(Transform(eigen_eq, eigen_math))
        self.wait(5)
        eigen_math1 = eigen_math.copy().scale(0.5).to_edge(LEFT)
        spin_up_eigen_eq = MathTex(r" S_Z  \ | + >", r"= + \frac{\hbar}{2} \ | + >", color = PURPLE_A).scale(1.5).move_to([0, -1, 0])
        spin_down_eigen_eq = MathTex(r" S_Z \ | - >", r"= - \frac{\hbar}{2} \ | - >", color = BLUE).scale(1.5).move_to([0, -3, 0])
        self.play(Transform(eigen_math, eigen_math1))
        self.play(Transform(eigen_eq,spin_up_eigen_eq), run_time=2)
        self.wait()
        self.play(Transform(spin_up_eigen_eq, spin_down_eigen_eq), run_time=2)
        self.wait(3)
        self.play(eigen_eq.animate.next_to(eigen_math1, DOWN).scale(0.5))
        self.wait()
        self.play(spin_up_eigen_eq.animate.next_to(eigen_eq, DOWN).scale(0.5))
        self.wait()
        identity_eq = Text("{Identity Equation}").move_to([0.5 , 0, 0])
        self.play(Write(identity_eq))
        self.wait(2)
        identity_math = MathTex(r"\sum_{\grave{a}} |\grave{a}><\grave{a}| \ = \ 1", color = YELLOW)
        self.play(Transform(identity_eq, identity_math))
        self.wait(2)
        self.play(identity_eq.animate.scale(0.75))
        self.wait()    
        identity_state = MathTex(r"\sum_{states} |state><state| \ = \ 1", color = YELLOW)
        self.play(Transform(identity_eq, identity_state))
        self.wait(3)
        self.play(identity_eq.animate.scale(0.75))
        plus_minus = MathTex(r"|+><+| \ + \ |-><-| \ = \ 1", color = YELLOW)
        self.play(Transform(identity_eq, plus_minus))
        self.play(identity_eq.animate.scale(0.75))
        self.wait(3)
        sz_plus_minus = MathTex(r"S_Z|+><+|",r"+",r"S_Z|-><-|", r"= S_Z", color = YELLOW).scale(0.75)
        sz_plus_minus.next_to(plus_minus, DOWN)
        self.play(Write(sz_plus_minus))
        self.wait()
        frame_box1 = SurroundingRectangle(sz_plus_minus[0], buff = 0.1, color = WHITE)
        frame_box2 = SurroundingRectangle(eigen_eq[0], buff = 0.1, color = WHITE)
        self.play(Create(frame_box1))
        self.play(Create(frame_box2))
        self.wait()
        frame_box3 = SurroundingRectangle(eigen_eq[1], buff = 0.1, color = WHITE)
        self.play(ReplacementTransform(frame_box2, frame_box3))
        self.wait()
        sz_eigen1 = MathTex(r"\frac{\hbar}{2} |+><+|", color = PINK).scale(0.75)
        sz_eigen1.move_to([-1, -2.25, 0])
        self.play(Write(sz_eigen1))
        frame_box4 = SurroundingRectangle(sz_eigen1, color = WHITE, buff = 0.1)
        arrow1 = Arrow(frame_box1.get_bottom(), frame_box4.get_top())
        arrow2 = Arrow(frame_box2.get_right(), frame_box4.get_left())
        self.play(Create(arrow1), Create(arrow2), Create(frame_box4))
        self.wait()
        sz_eigen2 = MathTex(r" + \ -\frac{\hbar}{2} |-><-|", color = PINK).scale(0.75)
        sz_eigen2.next_to(sz_eigen1, 0.5*RIGHT)
        self.play(Write(sz_eigen2))
        frame_box5 = SurroundingRectangle(sz_eigen2, color = WHITE, buff = 0.1)
        frame_box6 = SurroundingRectangle(spin_up_eigen_eq[1], color = WHITE, buff= 0.1)
        frame_box7 = SurroundingRectangle(sz_plus_minus[2], color= WHITE, buff = 0.1)
        self.play(ReplacementTransform(frame_box3, frame_box6))
        arrow3 = Arrow(frame_box7.get_bottom(), frame_box5.get_top())
        arrow4 = Arrow(frame_box6.get_right(), frame_box5.get_bottom())
        self.play(ReplacementTransform(frame_box4, frame_box5),ReplacementTransform(frame_box1, frame_box7),
                   Transform(arrow1, arrow3), Transform(arrow2, arrow4))
        self.wait(2)
        self.remove(logo, S_G_exp, sz_eigen1, sz_eigen2, sz_plus_minus, arrow1,
                          arrow2, arrow3, arrow4, frame_box1, frame_box2, frame_box3,
                          frame_box4, frame_box5, frame_box6, frame_box7, 
                          eigen_eq, eigen_math, eigen_math1, sz_eigen1, sz_eigen2, sz_plus_minus,
                          spin_up_eigen_eq, spin_down_eigen_eq, identity_eq, identity_math, identity_state)
        self.wait(3)
        self.play(FadeOut(S_G_exp))

        mstate1 = MathTex(r"|+> \ + \ |->")
        self.play(Write(mstate1))
        mstate2 = MathTex(r"| \pm >")
        self.wait()
        self.play(Transform(mstate1, mstate2))
        self.wait()
        msz = MathTex(r"S_Z").next_to(mstate1, LEFT)
        self.play(FadeIn(msz))
        self.wait()
        self.remove(mstate1)
        msz_group = VGroup(msz, mstate2).scale(0.5)
        self.play(msz_group.animate.to_edge(UP+LEFT))
        msz1 = MathTex(r"= \ S_Z|+> \ + \ S_Z|->").scale(0.5).next_to(msz_group, 0.5*RIGHT)
        self.play(Write(msz1))
        self.wait()

        msz_eigen0 = MathTex(r"\ = \frac{\hbar}{2} |+><+|+> \ + \ -\frac{\hbar}{2} |-><-|+>" ).scale(0.5).next_to(msz1,0.5* RIGHT)
        msz_eigen1 = MathTex(r"+" ).scale(0.5).next_to(msz_eigen0, RIGHT)
        msz_eigen2= MathTex(r"\frac{\hbar}{2} |+><+|-> \ + \ -\frac{\hbar}{2} |-><-|->" ).scale(0.5).next_to(msz_eigen1, RIGHT)
        msz_eigen3= MathTex(r"\ because <+|-> \ = \  <-|+> \ = \ 0", color = PURE_RED ).scale(0.5).next_to(msz_eigen0, DOWN)
        msz_eigen4= MathTex(r"\ because <+|+> \ = \  <-|-> \ = \ 1", color = PURE_GREEN ).scale(0.5).next_to(msz_eigen3, DOWN)
        msz_eigen5 = MathTex(r"S_Z | \pm > \ = \frac{\hbar}{2} |+>\ + \ - \frac{\hbar}{2}  |->" ).scale(0.5).next_to(msz_eigen4, DOWN + 1.5 * LEFT)
        msz_eigen6 = MathTex(r"S_Z |\pm > \ = \ (\pm \frac{\hbar}{2}) (|+>\ + \ |->)" ).scale(0.5).next_to(msz_eigen4, DOWN + 1.5*RIGHT)
        eq_arrow = Arrow (msz_eigen5.get_right(), msz_eigen6.get_left(), color = YELLOW)
        msz_eigen7 = MathTex(r"S_Z |\pm > \ = \ (\pm \frac{\hbar}{2})  |\pm >" ).scale(0.5).next_to(eq_arrow, DOWN)
        self.play(Write(msz_eigen0))
        self.play(Write(msz_eigen1))
        self.play(Write(msz_eigen2))
        self.wait()
        self.play(Write(msz_eigen3), Write(msz_eigen4))
        self.wait()
        self.play(Write(msz_eigen5))
        self.wait()
        self.play(Create(eq_arrow))
        self.play(Write(msz_eigen6))
        self.wait()
        self.play(Transform(msz_eigen6, msz_eigen7))
        self.play(msz_eigen6.animate.set_color(YELLOW).scale(3).move_to([0, -0.5, 0]))
        eq_surrounding1 = SurroundingRectangle(msz_eigen6, color = GRAY)
        self.play(Create(eq_surrounding1, run_time = 2))
        self.wait(2)
        self.remove(eq_surrounding1)
        self.play(msz_eigen6.animate.set_color(WHITE).scale(1/3).next_to(msz_eigen4, DOWN + 1.5*RIGHT))
        self.wait()

        S_G_exp1 = S_G_exp.copy().scale(0.8).next_to(eq_arrow, 2*DOWN)
        self.add((S_G_exp1))
        self.wait(3)
        spin_up_up= MathTex(r"S_+ \uparrow").scale(0.5).move_to([+5, 0.5, 0])
        spin_down_down= MathTex(r"S_- \downarrow").scale(0.5).move_to([+5, -0.7, 0])
        plus_arrow = Arrow([+5.4, 0.5, 0], [+3, 0.2, 0],buff = 0.7, color = RED)
        minus_arrow = Arrow([+5.4, -0.7, 0], [+3, -0.7, 0],buff = 0.7, color = YELLOW)
        self.play(Write(spin_up_up))
        self.play(Create(plus_arrow))
        self.play(Write(spin_down_down))
        self.play(Create(minus_arrow))

        self.play(self.camera.frame.animate.scale(0.5).move_to(screen))
        self.wait(2)
       
        what_happen = Text("What happen ?", color = YELLOW ).scale(0.4).next_to(screen, 0.05*RIGHT)
        plus_arrow_1 = Arrow(spin_up_up.get_right(), what_happen.get_left())
        minus_arrow_1 = Arrow(spin_down_down.get_right(), what_happen.get_left())

        self.play(Create(plus_arrow_1), Create(minus_arrow_1))
        self.play(Write(what_happen))
        self.wait(3)
        self.play(self.camera.frame.animate.move_to(what_happen, UP))
        logic_text= Text(r"المنطق بيقول لو أثرنا على الكترون في الحالة العلوية ب").next_to(what_happen, 2*DOWN ).scale(0.3)
        logic_text1= Text(r"فمش هايحصل اي تغيير بسب إن الالكترون اساسا في حالته العلوية").next_to(logic_text, DOWN ).scale(0.3)
        logic_text2= Text(r"و المنطق بيقول برضو لو أثرنا على الكترون في الحالة السفلية ب").next_to(logic_text1, DOWN ).scale(0.3)
        logic_text3= Text(r"فمش هايحصل اي تغيير برضو بسب إن الالكترون اساسا في حالته السفلية").next_to(logic_text2, DOWN ).scale(0.3)
        spin_up_up_1= spin_up_up.copy().set_color(RED).next_to(logic_text, LEFT)
        spin_down_down_1= spin_down_down.copy().set_color(YELLOW).next_to(logic_text2, LEFT)

        self.play(Write(logic_text), reverse = True, run_time = 4)
        self.play(Write(spin_up_up_1))
        self.play(Write(logic_text1), reverse = True, run_time = 4)
        self.wait(3)

        self.play(Write(logic_text2), reverse = True, run_time = 4)
        self.play(Write(spin_down_down_1))
        self.play(Write(logic_text3), reverse = True, run_time = 4)
        self.wait(3)
        self.play(self.camera.frame.animate.scale(1).move_to(screen, UP + RIGHT))
        self.wait(2)
        spin_up_operator= MathTex(r"S_+ = \hbar \ |+><-|", color = RED).scale(0.5).next_to(screen, 9*LEFT + 3*DOWN)
        self.play(Write(spin_up_operator))
        self.wait(2)
        spin_down_operator= MathTex(r"S_- = \hbar \ |-><+|", color = YELLOW).scale(0.5).next_to(spin_up_operator, DOWN)
        self.play(Write(spin_down_operator))
        self.wait()
        self.play(self.camera.frame.animate.scale(0.6).move_to(spin_up_operator, UP + 0.8 *LEFT))    
        self.wait(2)
        up = MathTex(r"S_+|+> = \hbar \ |+><-|+> = 0", color = RED).scale(0.3).next_to(spin_down_operator, DOWN)
        down = MathTex(r"S_- |-> = \hbar \ |-><+|-> = 0", color = YELLOW).scale(0.3).next_to(up, DOWN )
        self.play(Write(up))
        self.play(Write(down))
        self.wait(3)

        up_down = MathTex(r"S_+|-> = \hbar \ |+><-|-> = \hbar \ |+>", color = RED).scale(0.3).next_to(up, RIGHT)
        self.play(self.camera.frame.animate.scale(1).move_to(up_down, 0.5*LEFT))    

        down_up = MathTex(r"S_- |+> = \hbar \ |-><+|+>  = \hbar \ |->", color = YELLOW).scale(0.3).next_to(down, RIGHT )
        self.play(Write(up_down))
        self.play(Write(down_up))
        spin_group = VGroup(up_down, down_up)
        spsurrounding= SurroundingRectangle(spin_group, color = GREEN)
        self.play(Create(spsurrounding), run_time = 5)
        self.wait(3)
        self.play(self.camera.frame.animate.scale(4).move_to(ORIGIN))    
        self.wait(3)

