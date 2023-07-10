from manim import *

class L13(MovingCameraScene):
    def construct(self):
                      #genetal_intro
        logo=   ImageMobject("logo.png")
        logo.to_edge(RIGHT)
        self.add(logo)
        intro= Text("Learn Physics \n with \n Farouk", t2w = {'Farouk':BOLD}, t2c = {'Farouk': YELLOW} ).scale(2)
        intro.to_edge(LEFT)
        self.play(Write(intro),  FadeIn(logo), run_time=3)
        self.wait(3)
                        #video_intro
        welcome = Text("Welcome back", color = RED)
        to = Text("to", color= YELLOW).next_to(welcome, DOWN)
        welcome_group = VGroup(welcome, to)
        qm = Text("Quantum Mechanics", color = GREEN)
        qm.next_to(welcome_group, DOWN)
        self.play(Transform(intro, welcome))
        self.play(Write(to))
        self.wait()
        self.play(Write(qm))
        self.wait(3)
        lec= Text("Lecture 13", color= GRAY_A).to_edge(UP).scale(0.25)
        spin= Text("Spin 1/2 System", color= PINK).scale(0.5)
        spin.next_to(lec, DOWN)
        self.remove(welcome,to, intro)
        self.play(Transform(qm, lec))
        logo.scale(0.25).to_edge(UP)
        self.play(Write(spin), run_time= 3)
        self.wait(3)
        exp= Text("eg: S-G EXP", color = BLUE).move_to([-2, 2, 0]).scale(0.5)
        self.play(Write(exp))
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
        self.play(Write(oven_text))
        self.wait()
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
        self.wait()
        self.play(self.camera.frame.animate.scale(2).move_to(ORIGIN))
        self.wait()
        dash_line = DashedLine(oven.get_right(), screen.get_center())
        self.add(dash_line)
        blue_dot1 = Dot(radius = 0.1 , color = PURE_BLUE)
        blue_dot1.to_edge(LEFT)
        self.play(blue_dot1.animate.move_to(screen.get_center()), run_time=4)
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
        uppermp_text = Text("N-pole", color = PURPLE).scale(0.3).next_to(uppermp, UP)
        self.play(Write(uppermp_text))
        self.wait()
        self.play(self.camera.frame.animate.scale(2).move_to(ORIGIN))
        downmp.move_to([-1.5, -0.7 , 0])
        self.add(downmp)
        self.play(self.camera.frame.animate.scale(0.5).move_to(downmp))
        downmp_text = Text("S-pole", color = PURPLE).scale(0.3).next_to(downmp, DOWN)
        self.play(Write(downmp_text))
        self.wait()
        self.play(self.camera.frame.animate.scale(2).move_to(ORIGIN))
        self.wait()
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
        spin_up_text = MathTex(r"S_+ = + \frac{\hbar}{2}", color = PURE_RED).scale(0.25).next_to(red_dot2, 0.5*RIGHT)
        self.play(Write(spin_up_text))
        self.wait()
        spin_down_text = MathTex(r"S_- = - \frac{\hbar}{2}", color = YELLOW).scale(0.25).next_to(yellow_dot2, 0.5*RIGHT)
        self.play(Write(spin_down_text))
        self.wait(2)
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



