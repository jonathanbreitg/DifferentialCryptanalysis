from manim import *
from pallete import *




class XorBox(VGroup):
    def __init__(self,topLabels=True,bottomLabels=True,offset=0,top_pfx='f"m"',bot_pfx='f"x"', **kwargs):
        super().__init__(**kwargs)
        n = 16
        width = 12
        height = 1

        # Box
        box = Rectangle(width=width, height=height).set_fill(SURFACE0,opacity=1).set_stroke(TEXT,3)
        box_text = MathTex(r"\oplus").set_color(TEXT).scale(1.5).move_to(box.get_center())

        # Input and output points at edges of box
        top_points = [
            box.get_top() + RIGHT * ((i + 0.5) * width / n - width/2)
            for i in range(n)
        ]
        bottom_points = [
            box.get_bottom() + RIGHT * ((i + 0.5) * width / n - width/2)
            for i in range(n)
        ]

        # Input labels above top points
        labels_top = VGroup(*[
            MathTex(rf"{eval(top_pfx)}",r"{{{'}}}",rf"_{{{i+offset}}}").next_to(top_points[i], UP, buff=0.3).set_color(TEAL).set_opacity_by_tex("'",0).set_opacity_by_tex(eval(top_pfx),1).scale(0.7)
            for i in range(n)
        ])
        top_lines = VGroup(*[
            Arrow(labels_top[i].get_bottom(), top_points[i]).set_color(TEAL)
            for i in range(n)
        ])


        # Output labels below bottom points
        labels_bottom = VGroup(*[
            MathTex(rf"{eval(bot_pfx)}",r"{{{'}}}",rf"_{{{i+offset}}}").next_to(bottom_points[i], DOWN, buff=0.3).set_opacity_by_tex("'",0).set_opacity_by_tex(eval(bot_pfx),1).set_color(PEACH).scale(0.7)
            for i in range(n)
        ])
        bottom_lines = VGroup(*[
            Arrow(bottom_points[i], labels_bottom[i].get_top()).set_color(PEACH)
            for i in range(n)
        ])


        # Group everything
        if topLabels:
            if bottomLabels:
                self.add(box, top_lines,bottom_lines, labels_top, labels_bottom,box_text)
            else:
                self.add(box, top_lines, labels_top,bottom_lines,box_text)
        else:
            if bottomLabels:
                self.add(box, bottom_lines, labels_bottom,top_lines,box_text)
            else:
                self.add(box, top_lines, bottom_lines,box_text)


class SBox(VGroup):
    def __init__(self,topLabels=True,bottomLabels=True,offset=0,bot_pfx='"y"',top_pfx='"x"', **kwargs):
        super().__init__(**kwargs)
        n = 4
        width = 3
        height = 1

        # Box
        box = Rectangle(width=width, height=height).set_fill(SURFACE0,opacity=1).set_stroke(TEXT,3)
        box_text = MathTex(r"S_{4}").set_color(TEXT).scale(1.5).move_to(box.get_center())

        # Input and output points at edges of box
        top_points = [
            box.get_top() + RIGHT * ((i + 0.5) * width / n - width/2)
            for i in range(n)
        ]
        bottom_points = [
            box.get_bottom() + RIGHT * ((i + 0.5) * width / n - width/2)
            for i in range(n)
        ]

        # Input labels above top points
        labels_top = VGroup(*[
            MathTex(f"{eval(top_pfx)}",r"{{{'}}}",rf"_{{{i}}}").next_to(top_points[i], UP, buff=0.3).set_color(TEAL).set_opacity_by_tex("'",0).set_opacity_by_tex(eval(top_pfx),1).scale(0.7)
            for i in range(n)
        ])
        top_lines = VGroup(*[
            Arrow(labels_top[i].get_bottom(), top_points[i]).set_color(TEAL)
            for i in range(n)
        ])

        # Output labels below bottom points
        labels_bottom = VGroup(*[
            MathTex(f"{eval(bot_pfx)}",r"{{{'}}}",rf"_{{{i}}}").next_to(bottom_points[i], DOWN, buff=0.3).set_color(PEACH).set_opacity_by_tex("'",0).set_opacity_by_tex(eval(bot_pfx),1).scale(0.7)
            for i in range(n)
        ])
        bottom_lines = VGroup(*[
            Arrow(bottom_points[i], labels_bottom[i].get_top()).set_color(PEACH)
            for i in range(n)
        ])


        # Group everything
        if topLabels:
            if bottomLabels:
                self.add(box, top_lines,bottom_lines, labels_top, labels_bottom,box_text)
            else:
                self.add(box, top_lines, labels_top,bottom_lines,box_text)
        else:
            if bottomLabels:
                self.add(box, bottom_lines, labels_bottom,top_lines,box_text)
            else:
                self.add(box, top_lines, bottom_lines,box_text)

class PBox(VGroup):
    def __init__(self, perm=[2,0,3,1], bit_labels=None,topLabels=True,bottomLabels=True,top_pfx='f"b"',bot_pfx='f"b"',height=2,txScale=1,width=12,permute=True, **kwargs):
        super().__init__(**kwargs)
        n = len(perm)


        # Box
        box = Rectangle(width=width, height=height).set_fill(SURFACE0,opacity=1).set_stroke(TEXT,3)

        # Input and output points at edges of box
        top_points = [
            box.get_top() + RIGHT * ((i + 0.5) * width / n - width/2)
            for i in range(n)
        ]
        bottom_points = [
            box.get_bottom() + RIGHT * ((i + 0.5) * width / n - width/2)
            for i in range(n)
        ]

        # Input labels above top points
        if bit_labels is None:
            bit_labels = [f"{eval(top_pfx)}"+r"{{{'}}}"+rf"_{{{i}}}" for i in range(n)]
        labels_top = VGroup(*[
            MathTex(label).next_to(top_points[i], UP, buff=0.3).set_color(TEAL).scale(0.7*txScale).set_opacity_by_tex("'",0).set_opacity_by_tex(eval(top_pfx),1)
            for i, label in enumerate(bit_labels)
        ])
        top_lines = VGroup(*[
            Arrow(labels_top[i].get_bottom(), top_points[i]).set_color(TEAL)
            for i in range(n)
        ])

        # Output labels below bottom points
        labels_bottom = VGroup(*[
            MathTex(f"{eval(bot_pfx)}",r"{{{'}}}",rf"_{{{i}}}").next_to(bottom_points[perm[i]] if permute else bottom_points[i], DOWN, buff=0.3).set_color(PEACH).scale(0.7*txScale).set_opacity_by_tex("'",0).set_opacity_by_tex(eval(bot_pfx),1)
            for i in range(n)
        ])
        bottom_lines = VGroup(*[
            Arrow(bottom_points[i], labels_bottom[perm[i]].get_top() if permute else labels_bottom[i].get_top()).set_color(PEACH)
            for i in range(n)
        ])

        perm_lines = VGroup(*[
            Line(top_points[i], bottom_points[perm[i]]).set_color([PEACH,TEAL] if bottom_points[perm[i]][0] >= top_points[i][0] else [TEAL,PEACH])
            for i in range(n)
        ])

        # Group everything
        if topLabels:
            if bottomLabels:
                self.add(box, top_lines,bottom_lines, labels_top, labels_bottom,perm_lines)
            else:
                self.add(box, top_lines, labels_top,bottom_lines,perm_lines)
        else:
            if bottomLabels:
                self.add(box, bottom_lines, labels_bottom,top_lines,perm_lines)
            else:
                self.add(box, top_lines, bottom_lines,perm_lines)

def colorize(line):
    line.set_color_by_tex(r"X",GREEN)
    line.set_color_by_tex(r"X'",YELLOW)
    line.set_color_by_tex(r"\Delta_x",TEAL)
    line.set_color_by_tex(r"\Delta_y",PEACH)
    line.set_color_by_tex(r"\Delta_p",PEACH)
    line.set_color_by_tex(r"P",[MAROON,PEACH])
    line.set_color_by_tex(r"K",BLUE)
    line.set_color_by_tex(r"M",PEACH)
    line.set_color_by_tex(r"A",MAUVE)
    line.set_color_by_tex(r"0",PINK)
    line.set_color_by_tex(r",",RED)
    line.set_color_by_tex(r"\oplus",RED)
    line.set_color_by_tex(r"AddKey",RED)


class OTPScene(Scene):
    def construct(self):
        title = Title("XOR | AddKey",font_size=50).set_color_by_gradient(BLUE,RED)
        self.play(Write(title))
        self.wait()

        eq1 = MathTex(r"{{X}} = {{M}} \oplus {{K}}")
        colorize(eq1)
        self.play(Write(eq1))
        self.wait()

        eq2 = MathTex(r"{{0}} = {{A}} \oplus {{A}}").next_to(eq1,DOWN,buff=0.5)
        colorize(eq2)
        self.play(Write(eq2))
        self.wait()

        eq3 = MathTex(r"{{A}} = {{0}} \oplus {{A}}").next_to(eq2,DOWN)
        colorize(eq3)
        self.play(Write(eq3))
        self.wait()

        self.play(VGroup(eq2,eq3).animate.to_edge(LEFT))

        eq4 = MathTex(r"{{M}} = {{X}} \oplus {{K}}").next_to(eq1,DOWN)
        colorize(eq4)
        self.play(Write(eq4))

        eq5 = MathTex(r"{{M}} = {{M}} \oplus {{K}} \oplus {{K}}").next_to(eq1,DOWN)
        colorize(eq5)
        self.play(Transform(eq4,eq5),Circumscribe(eq1))
        self.wait()

        eq6 = MathTex(r"{{M}} = {{M}} \oplus {{0}}").next_to(eq1,DOWN)
        colorize(eq6)
        self.play(Transform(eq4,eq6),Circumscribe(eq2))
        self.wait()

        eq7 = MathTex(r"{{M}} = {{M}}").next_to(eq1,DOWN)
        colorize(eq7)
        self.play(Transform(eq4,eq7),Circumscribe(eq3))
        self.wait()

        self.play(FadeOut(eq4))
        self.wait()

        eq8 = MathTex(r"{{AddKey}}_{{K}}(M) = {{M}} \oplus {{K}} = {{X}}").next_to(eq1,DOWN,buff=0.5)
        colorize(eq8)
        self.play(Write(eq8))
        self.wait()



class SubBox(Scene):
    def construct(self):
        title = Title(f"Substitution Boxes",font_size=50).set_color_by_gradient(BLUE,RED)
 
        self.play(Write(title))
        self.wait()

        sbox = Rectangle(width=2, height=2).set_fill(SURFACE0,opacity=1).set_stroke(TEXT,3)
        sbox_text = MathTex(r"S_{16}").set_color(TEXT).scale(2)
        sbox_group = VGroup(sbox,sbox_text)

        bitstring = Tex("1011 1100 0110 1001").set_color(TEAL).next_to(sbox_group,UP,buff=1)
        arrow1 = Arrow(start=bitstring.get_bottom(), end=sbox_group.get_top()-UP*0.1, buff=0.1, color=TEXT)
        bitstringOut = Tex("0110 1011 1000 0010").set_color(PEACH).next_to(sbox_group,DOWN,buff=1)
        arrow2 = Arrow(start=sbox_group.get_bottom()+DOWN*0.1, end=bitstringOut.get_top(), buff=0.1, color=TEXT)
        g = VGroup(bitstring, arrow1, sbox_group, arrow2, bitstringOut)
        self.play(Write(bitstring), GrowFromCenter(sbox_group), Write(arrow1))
        self.play(Wiggle(sbox_group,run_time=1.5))
        self.play(Write(arrow2), Write(bitstringOut))
        self.wait()

        bitstringHex = Tex("B C 6 3").set_color(TEAL).move_to(bitstring)
        bitstringOutHex = Tex("6 B 8 2").set_color(PEACH).move_to(bitstringOut)
        self.play(Transform(bitstring, bitstringHex), Transform(bitstringOut, bitstringOutHex))
        self.wait()

        bitstringHexModified = Tex("B C 6 4").set_color(TEAL).move_to(bitstringHex)
        bitstringOutHexModified = Tex("A 5 F B").set_color(PEACH).move_to(bitstringOutHex)
        self.play(Transform(bitstring, bitstringHexModified), Wiggle(sbox_group,run_time=1.5),Transform(bitstringOut, bitstringOutHexModified))
        self.wait()

        bitstringHexModified2 = Tex("B C 6 5").set_color(TEAL).move_to(bitstringHex)
        bitstringOutHexModified2 = Tex("2 C C 7").set_color(PEACH).move_to(bitstringOutHex)
        self.play(Transform(bitstring, bitstringHexModified2), Wiggle(sbox_group,run_time=1.5),Transform(bitstringOut, bitstringOutHexModified2))
        self.wait()

        self.play(g.animate.to_edge(LEFT))
        self.wait()

        #draw sbox table
        table_data = [
            ["B C 6 3", "6 B 8 2"],
            ["B C 6 4", "A 5 F B"],
            ["B C 6 5", "2 C C 7"],
        ]
        table = Table(table_data, 
                      include_outer_lines=True,
                      line_config={"stroke_color": TEXT, "stroke_width": 2}, #color input in peach and output in teal

                        
                        element_to_mobject=lambda x: Tex(x).set_color(TEXT),
                     ).scale(0.7)
        table.get_columns()[0].set_color(TEAL)
        table.get_columns()[1].set_color(PEACH)
        #Draw ellipsis before and after the table
        lookupText = Tex("S-Box Lookup Table").set_color(TEXT).next_to(table, UP, buff=0.7)
        ellipsis = Tex(r"\vdots").set_color(TEXT).next_to(table, UP, buff=0.2)
        ellipsis2 = Tex(r"\vdots").set_color(TEXT).next_to(table, DOWN, buff=0.2)
        self.play(Write(lookupText))
        self.wait()

        self.play(Write(ellipsis))
        self.play(Write(table))
        self.play(Write(ellipsis2))
        self.wait()

        self.play(FadeOut(VGroup(lookupText, ellipsis, ellipsis2, table)))
        self.wait()

        self.play(g.animate.move_to(ORIGIN))
        self.wait()

        self.play(FadeOut(VGroup(arrow1,arrow2,bitstring,bitstringOut)))
        sbox_text2  = MathTex("S_4").set_color(TEXT).scale(2)
        sbox_group2 = VGroup(sbox,sbox_text2)
        self.play(Transform(sbox_group,sbox_group2))
        self.wait()

        bitstr = Tex("1001").set_color(TEAL).next_to(sbox_group,UP,buff=1)
        arrow1b = Arrow(start=bitstr.get_bottom(), end=sbox_group.get_top()-UP*0.1, buff=0.1, color=TEXT)
        bitstrOut = Tex("1010").set_color(PEACH).next_to(sbox_group,DOWN,buff=1)
        arrow2b = Arrow(start=sbox_group.get_bottom()+DOWN*0.1, end=bitstrOut.get_top(), buff=0.1, color=TEXT)
        gb = VGroup(bitstr, arrow1b, sbox_group, arrow2b, bitstrOut)
        self.play(Write(bitstr),Write(arrow1b))
        self.play(Wiggle(sbox_group,run_time=1.5),Write(arrow2b), Write(bitstrOut))
        self.wait()

        bitstrhex = Tex("9").set_color(TEAL).move_to(bitstr)
        bitstrOuthex = Tex("A").set_color(PEACH).move_to(bitstrOut)
        self.play(Transform(bitstr, bitstrhex), Transform(bitstrOut, bitstrOuthex))
        self.wait()

        #4bit S-box table
        table_data2 = [
            ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"],
            ["E","4","D","1","2","F","B","8","3","A","6","C","5","9","0","7"],
        ]
        table2 = Table(table_data2, 
                      include_outer_lines=True,
                      line_config={"stroke_color": TEXT, "stroke_width": 2}, #color input in peach and output in teal
                        element_to_mobject=lambda x: Tex(x).set_color(TEXT),
                        ).scale(0.4)
        table2.get_rows()[0].set_color(TEAL)
        table2.get_rows()[1].set_color(PEACH)
        self.play(gb.animate.to_edge(LEFT))
        table2.next_to(gb, RIGHT, buff=0.1)
        lookupText2 = Tex("4-bit S-Box Lookup Table").set_color(ROSEWATER).next_to(table2, UP, buff=0.7)
        self.wait()

        self.play(Write(lookupText2))
        self.play(Write(table2))
        self.wait()

        self.play(Circumscribe(table2.get_columns()[9]))
        self.wait()

        self.play(FadeOut(gb))
        self.play( lookupText2.animate.move_to(ORIGIN+UP),table2.animate.scale(1.4))
        self.play(table2.animate.to_edge(LEFT,buff=0))
        self.wait()

        label = Tex("S-box of DES").set_color(ROSEWATER).move_to(lookupText2)
        self.play(Transform(lookupText2,label))
        self.wait()


class PboxScene(Scene):
    def construct(self):
        title = Title(f"Permutation Boxes",font_size=50).set_color_by_gradient(BLUE,RED)
 
        self.play(Write(title))
        self.wait()

        opaque_box = Rectangle(width=12, height=4).set_fill(SURFACE0,opacity=1).set_stroke(TEXT,3).shift(DOWN)
        opaque_text = MathTex(r"P_{16}").set_color(TEXT).scale(2).move_to(opaque_box.get_center())
        opaque_group = VGroup(opaque_box,opaque_text)
        self.play(Write(opaque_group))
        self.wait()

        input_bits = Tex("0110 1011 1000 0010").set_color(TEAL).next_to(opaque_group,UP,buff=0.3)
        arrow1 = Arrow(start=input_bits.get_bottom(), end=opaque_group.get_top(), buff=0.1, color=TEXT)
        output_bits = Tex("0110 1000 1101 0100").set_color(PEACH).next_to(opaque_group,DOWN,buff=0.3)
        arrow2 = Arrow(start=opaque_group.get_bottom(), end=output_bits.get_top(), buff=0.1, color=TEXT)
        g = VGroup(input_bits, arrow1, opaque_group, arrow2, output_bits)
        self.play(Write(input_bits), Write(arrow1))
        self.play(Wiggle(opaque_group,run_time=1.5))
        self.play(Write(arrow2), Write(output_bits))
        self.wait()

        pbox = PBox(perm=[0,4,8,12,1,5,9,13,2,6,10,14,3,7,11,15],width=12,height=4)
        self.play(FadeOut(VGroup(opaque_text,input_bits,output_bits,arrow1,arrow2)),Write(pbox))
        self.wait()

class SPNDiagram(Scene):
    def construct(self):
        title = Title(f"Substitution-Permutation Network",font_size=50).set_color_by_gradient(BLUE,RED)
 
        self.play(Write(title))
        self.wait()

        xorBox = XorBox(offset=0).move_to(ORIGIN+UP*1.5)

        leftLabel = MathTex(rf"K").next_to(xorBox.get_left(), LEFT, buff=0.25).set_color(BLUE)
        leftLine = Arrow(leftLabel.get_right(), xorBox.get_left(),buff=0).set_color(BLUE)

        sbox1 = SBox(offset=0,topLabels=False)
        sbox2 = SBox(offset=4,topLabels=False).next_to(sbox1, RIGHT, buff=0)
        sbox3 = SBox(offset=8,topLabels=False).next_to(sbox2, RIGHT, buff=0)
        sbox4 = SBox(offset=12,topLabels=False).next_to(sbox3, RIGHT, buff=0)

        sgroup = VGroup(sbox1,sbox2,sbox3,sbox4).next_to(xorBox, DOWN, buff=0)
        pbox = PBox(perm=[0,4,8,12,1,5,9,13,2,6,10,14,3,7,11,15],topLabels=False,bot_pfx='f"z"',top_pfx='f"y"',height=1.5,permute=False).next_to(sgroup, DOWN, buff=0)
        #totGroup = VGroup(sgroup,pbox).move_to(ORIGIN)
        self.play(Write(xorBox),Write(leftLabel),Write(leftLine))
        self.wait()

        self.play(Write(sgroup))
        self.wait()

        self.play(Write(pbox))
        self.wait()

        totGroup = VGroup(sgroup,pbox,xorBox,leftLabel,leftLine)
        #scale down totGroup duplicate totGroup to the right so they both fit on screen
        #totGroup.scale(0.6)
        #totGroup2 = totGroup.copy()
        #totGroup2.to_edge(RIGHT,buff=0)
        self.play(totGroup.animate.scale(0.55))
        self.wait()

        xorBoxB = XorBox(offset=0,top_pfx='f"m\'"',bot_pfx='f"x\'"').move_to(ORIGIN+UP*1.5)

        leftLabelB = MathTex(rf"K").next_to(xorBoxB.get_left(), LEFT, buff=0.25).set_color(BLUE)
        leftLineB = Arrow(leftLabelB.get_right(), xorBoxB.get_left(),buff=0).set_color(BLUE)

        sbox1B = SBox(offset=0  ,topLabels=False,bot_pfx='f"y\'"')
        sbox2B = SBox(offset=4  ,topLabels=False,bot_pfx='f"y\'"').next_to(sbox1B, RIGHT, buff=0)
        sbox3B = SBox(offset=8  ,topLabels=False,bot_pfx='f"y\'"').next_to(sbox2B, RIGHT, buff=0)
        sbox4B = SBox(offset=12 ,topLabels=False,bot_pfx='f"y\'"').next_to(sbox3B, RIGHT, buff=0)

        sgroupB = VGroup(sbox1B,sbox2B,sbox3B,sbox4B).next_to(xorBoxB, DOWN, buff=0)
        pboxB = PBox(perm=[0,4,8,12,1,5,9,13,2,6,10,14,3,7,11,15],topLabels=False,bot_pfx='f"z\'"',top_pfx='f"y"',height=1.5,permute=False).next_to(sgroupB, DOWN, buff=0)

        totGroup2 = VGroup(sgroupB,pboxB,xorBoxB,leftLabelB,leftLineB)#.shift(UP*0.1)
        totGroup2.scale(0.55)
        totGroup2.to_edge(RIGHT,buff=0)
        self.play(totGroup.animate.to_edge(LEFT,buff=0))
        dashed_line = DashedLine(start=ORIGIN+UP*2.5+RIGHT*0.03, end=ORIGIN+DOWN*3.5+RIGHT*0.03, stroke_color=TEXT)
        self.play(Write(totGroup2),Write(dashed_line))
        self.wait()

        lab1 = MathTex(r"m").scale(2).next_to(totGroup.get_top(), UP, buff=0.3).set_color(TEAL)
        lab2 = MathTex(r"m'").scale(2).next_to(totGroup2.get_top(), UP, buff=0.3).set_color(TEAL)
        self.play(Write(lab1),Write(lab2))
        self.wait()

        lab1Out = MathTex(r"z").scale(2).next_to(totGroup.get_bottom(), DOWN, buff=0.3).set_color(PEACH)
        lab2Out = MathTex(r"z'").scale(2).next_to(totGroup2.get_bottom(), DOWN, buff=0.3).set_color(PEACH)
        self.play(Transform(lab1,lab1Out),Transform(lab2,lab2Out))
        self.wait()

class permutationMath(Scene):
    def construct(self):
        # First line (stays on screen)
        title = Title(f"P-box Differential CryptAnalysis",font_size=50).set_color_by_gradient(BLUE,RED)
        self.play(Write(title))
        self.wait()

        line1 = MathTex(r"{{X}} \oplus {{X'}} = {{\Delta_x}}")
        colorize(line1)
        self.play(Write(line1))
        self.wait()


        aline2 = MathTex(r"{{\Delta_p}}={{P}}({{X}}) \oplus {{P}}({{X'}})")
        aline2.next_to(line1, DOWN)
        colorize(aline2)
        self.play(Write(aline2))
        self.wait()

        # Second line (transforms)
        line2 = MathTex(r"{{\Delta_p}}={{P}}({{X}}) \oplus {{P}}({{X'}}) = {{P}}({{X}} \oplus {{X'}})")
        line2.next_to(line1, DOWN)
        colorize(line2)
        self.play(Transform(aline2,line2))
        self.wait()

        self.play(FadeOut(line1))
        # Transform into PBox(Δ)
        step3 = MathTex(r"{{\Delta_p}}={{P}}({{\Delta_x}})")
        step3.move_to(aline2)
        colorize(step3)
        self.play(Transform(aline2,step3))
        self.wait()

        self.play(aline2.animate.to_edge(LEFT).shift(UP*3))
        self.wait()
        pbox = PBox(perm=[0,4,8,12,1,5,9,13,2,6,10,14,3,7,11,15],topLabels=True,top_pfx='"x"',bot_pfx='"x"',height=1.5,txScale = 0.6,width=14).move_to(ORIGIN)

        self.play(Write(pbox))
        self.wait()

        pbox2 = PBox(perm=[0,4,8,12,1,5,9,13,2,6,10,14,3,7,11,15],topLabels=True,top_pfx='"x"',bot_pfx='f"x\'_{{{i}}} \oplus x"',height=1.5,txScale = 0.6,width=14).move_to(ORIGIN)
        self.play(Transform(pbox,pbox2))
        self.wait()
        
        self.play(FadeOut(pbox))
        pbox3 = PBox(perm=[0,4,8,12,1,5,9,13,2,6,10,14,3,7,11,15],topLabels=True,top_pfx=r"'x\''",bot_pfx=r"'x\''",height=1.5,txScale = 0.6,width=14).move_to(ORIGIN)
        self.play(Write(pbox3))
        self.wait()

        self.play(FadeOut(pbox3))
        self.play(Write(pbox2))
        self.wait()

        self.play(FadeOut(pbox2))
        self.wait()

        pbox4 = PBox(perm=[0,4,8,12,1,5,9,13,2,6,10,14,3,7,11,15],topLabels=True,top_pfx='f"x\'_{{{i}}} \oplus x"',bot_pfx='f"x\'_{{{i}}} \oplus x"',height=1.5,txScale = 0.6,width=14).move_to(ORIGIN)
        self.play(Write(pbox4))
        self.wait()

        self.play(Circumscribe(aline2))
        self.wait()


        #print(pbox[0],pbox[1],pbox[2],pbox[3],pbox[4],pbox[5],pbox)

class DeltaMath(Scene):
    def construct(self):
        # First line (stays on screen)

        line1 = MathTex(r"{{X}} {{\oplus}} {{X'}} = {{\Delta_x}}")
        colorize(line1)
        self.play(Write(line1))
        self.wait()


        aline2 = MathTex(r"{{\Delta_y}}={{AddKey}}_{{K}}({{X}}) {{\oplus}} {{AddKey}}_{{K}}({{X'}})")
        aline2.next_to(line1, DOWN)
        colorize(aline2)
        self.play(Write(aline2))
        self.wait()

        # Second line (transforms)
        line2 = MathTex(r"{{\Delta_y}}={{AddKey}}_{{K}}({{X}}) {{\oplus}} {{AddKey}}_{{K}}({{X'}}) = ({{K}} {{\oplus}} {{X}}) {{\oplus}} ({{K}} {{\oplus}} {{X'}})")
        line2.next_to(line1, DOWN)
        colorize(line2)
        self.play(Transform(aline2,line2))
        self.wait()

        self.play(line1.animate.to_edge(UL))
        # Transform into K⊕X⊕K⊕X'
        step3 = MathTex(r"{{\Delta_y}}={{K}} {{\oplus}} {{X}} {{\oplus}} {{K}} {{\oplus}} {{X'}}")
        step3.move_to(aline2)
        colorize(step3)
        self.play(Transform(aline2,step3))
        self.wait()


        # Transform into X⊕X'
        step4 = MathTex(r"{{\Delta_y}}={{X}} {{\oplus}} {{X'}}")
        colorize(step4)
        step4.move_to(aline2)
        self.play(Transform(aline2,step4))
        self.wait()

        # Transform into Δ
        step5 = MathTex(r" = {{\Delta_x}}")
        colorize(step5)
        step5.next_to(aline2, RIGHT)
        self.play(Write(step5))
        self.wait()

        self.play(FadeOut(aline2,step5))
        self.wait()

"""def add_spanning_header(scene, table, start_col, num_cols, header_mobject, y_buff=0.06):
    
    #Position header_mobject so it is centered above columns [start_col .. start_col+num_cols-1]
    #scene: the Scene instance (used to add/play)
    #table: the Table mobject
    #header_mobject: Tex/MathTex to place
    
    cols = table.get_columns()
    assert 0 <= start_col < len(cols)
    assert start_col + num_cols - 1 < len(cols)
    left = cols[start_col].get_left()
    right = cols[start_col + num_cols - 1].get_right()
    x_center = (left[0] + right[0]) / 2
    # use the table top + a small buffer for y
    row_height = table.get_rows()[0].get_height()
    y = table.get_top()[1] + row_height/2 + y_buff
    header_mobject.move_to(np.array([x_center, y, 0]))
    return header_mobject"""

class SboxMath(Scene):
    def construct(self):
        title = Title(f"S-Box Differential CryptAnalysis",font_size=50).set_color_by_gradient(BLUE,RED)
        self.play(Write(title))
        self.wait()

        table_data2 = [
            ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"],
            ["E","4","D","1","2","F","B","8","3","A","6","C","5","9","0","7"],
        ]
        table2 = Table(table_data2, 
                      include_outer_lines=True,
                      line_config={"stroke_color": TEXT, "stroke_width": 2}, #color input in peach and output in teal
                        element_to_mobject=lambda x: Tex(x).set_color(TEXT),
                        ).scale(0.56)
        table2.get_rows()[0].set_color(TEAL)
        table2.get_rows()[1].set_color(PEACH)
        table2.to_edge(LEFT,buff=0).shift(UP*1.5)

        sbox = SBox(offset=0,topLabels=True,bottomLabels=True).to_edge(LEFT).shift(DOWN*1.5)
        sbox2 = SBox(offset=0,topLabels=True,bottomLabels=True,top_pfx='"x\'"',bot_pfx='"y\'"').next_to(sbox, RIGHT, buff=1)
        
        #print(sbox[0],sbox[1],sbox[2],sbox[3],sbox[4],sbox[5],sbox)

        self.play(Write(table2),Write(sbox),Write(sbox2))
        sbox2l = VGroup(sbox2[0],sbox2[-1])
        sboxl = VGroup(sbox[0],sbox[-1])
        self.wait()

        self.play(Transform(sbox,sboxl),Transform(sbox2,sbox2l))
        self.wait()

        lab1 = MathTex(r"0").scale(1.5).next_to(sbox.get_top(), UP, buff=0.6).set_color(TEAL)
        lab2 = MathTex(r"B").scale(1.5).next_to(sbox2.get_top(), UP, buff=0.6).set_color(TEAL)

        arrow1 = Arrow(start=lab1.get_bottom(), end=sbox.get_top()-UP*0.1, buff=0.1, color=TEAL)
        arrow2 = Arrow(start=lab2.get_bottom(), end=sbox2.get_top()-UP*0.1, buff=0.1, color=TEAL)
        #position xorLabel between lab1 and lab2
        xorLabel = MathTex(r" \oplus ").set_color(RED).scale(1.5).move_to((lab1.get_right() + lab2.get_left()) / 2)
        eqLabel = MathTex(r"= B" ).scale(1.5).next_to(lab2, RIGHT, buff=1).set_color(TEAL)

        self.play(Write(lab1), Write(lab2))
        self.wait()

        self.play(Write(xorLabel),Write(eqLabel))
        self.wait()

        self.play(Write(arrow1), Write(arrow2))

        lab1Out = MathTex(r"E").scale(1.5).next_to(sbox.get_bottom(), DOWN, buff=0.6).set_color(PEACH)
        lab2Out = MathTex(r"C").scale(1.5).next_to(sbox2.get_bottom(), DOWN, buff=0.6).set_color(PEACH)

        arrow1Out = Arrow(start=sbox.get_bottom()+UP*0.1, end=lab1Out.get_top(), buff=0.1, color=PEACH)
        arrow2Out = Arrow(start=sbox2.get_bottom()+UP*0.1, end=lab2Out.get_top(), buff=0.1, color=PEACH)

        self.play(Write(arrow1Out), Write(arrow2Out))
        self.wait()

        self.play(Write(lab1Out), Write(lab2Out),Circumscribe(table2.get_columns()[0]),Circumscribe(table2.get_columns()[11]))
        self.wait()

        labOutXor = MathTex(r" \oplus ").set_color(RED).scale(1.5).move_to((lab1Out.get_right() + lab2Out.get_left()) / 2)
        eqOutLabel = MathTex(r"= 2" ).scale(1.5).next_to(lab2Out, RIGHT, buff=1).set_color(PEACH)

        self.play(Write(labOutXor),Write(eqOutLabel))
        self.wait()

        lab3 = MathTex(r"4").scale(1.5).next_to(sbox.get_top(), UP, buff=0.6).set_color(TEAL)
        lab4 = MathTex(r"F").scale(1.5).next_to(sbox2.get_top(), UP, buff=0.6).set_color(TEAL)

        lab3Out = MathTex(r"2").scale(1.5).next_to(sbox.get_bottom(), DOWN, buff=0.6).set_color(PEACH)
        lab4Out = MathTex(r"7").scale(1.5).next_to(sbox2.get_bottom(), DOWN, buff=0.6).set_color(PEACH)

        eqOutLabel2 = MathTex(r"= 5" ).scale(1.5).next_to(lab4Out, RIGHT, buff=1).set_color(PEACH)
        self.play(Transform(lab1,lab3),Transform(lab2,lab4),Transform(lab1Out,lab3Out),Transform(lab2Out,lab4Out),Transform(eqOutLabel,eqOutLabel2),Circumscribe(table2.get_columns()[4]),Circumscribe(table2.get_columns()[15]))
        self.wait()

        formula1 = MathTex(r"{{\Delta_y}}=S({{X}}) {{\oplus}} S({{X'}})").next_to(eqLabel,RIGHT,buff=1)
        colorize(formula1)
        self.play(Write(formula1))

        disclaimer = MathTex(r"{{When}} \,\,{{\Delta_x = B}}").next_to(formula1,DOWN).set_color(TEAL)
        formula2 = MathTex(r"{{\Delta_y}} = 2 {{,}} 5 {{,}} 7 {{,}} D {{,}} F").next_to(disclaimer,DOWN).set_color(PEACH)
        colorize(formula2)
        colorize(disclaimer)
        self.play(Write(disclaimer))
        self.wait()

        self.play(Write(formula2))
        self.wait()

        self.play(FadeOut(VGroup(sbox,sbox2,lab1,lab2,lab1Out,lab2Out,arrow1,arrow2,arrow1Out,arrow2Out,xorLabel,eqLabel,labOutXor,eqOutLabel)))
        eqGroup = VGroup(formula1,disclaimer,formula2)
        self.play(eqGroup.animate.to_edge(LEFT))
        self.wait()

        #Create DDT
        ddt_data = [
            ["-","0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"],
            ["0","16","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
            ["1","0","0","0","2","0","0","0","2","0","2","4","0","4","2","0","0"],
            ["2","0","0","0","2","0","6","2","2","0","2","0","0","0","0","2","0"],
            ["3","0","0","2","0","2","0","0","0","0","4","2","0","2","0","0","4"],
            ["4","0","0","0","2","0","0","6","0","0","2","0","4","2","0","0","0"],
            ["5","0","4","0","0","0","2","2","0","0","0","4","0","2","0","0","2"],
            ["6","0","0","0","4","0","4","0","0","0","0","0","0","2","2","2","2"],
            ["7","0","0","2","2","2","0","2","0","0","2","2","0","0","0","0","4"],
            ["8","0","0","0","0","0","0","2","2","0","0","0","4","0","4","2","2"],
            ["9","0","2","0","0","2","0","0","4","2","0","2","2","2","0","0","0"],
            ["A","0","2","2","0","0","0","0","0","6","0","0","2","0","0","4","0"],
            ["B","0","0","8","0","0","2","0","2","0","0","0","0","0","2","0","2"],
            ["C","0","2","0","0","2","2","2","0","0","0","0","2","0","6","0","0"],
            ["D","0","4","0","0","0","0","0","4","2","0","2","0","2","0","2","0"],
            ["E","0","0","2","4","2","0","0","0","6","0","0","0","0","0","2","0"],
            ["F","0","2","0","0","6","0","0","0","0","4","0","2","0","0","2","0"]
        ]
        ddt = Table(ddt_data, 
                      include_outer_lines=False,
                      line_config={"stroke_color": TEXT, "stroke_width": 2}, #color input in peach and output in teal
                        element_to_mobject=lambda x: Tex(x).set_color(TEXT if x =="-" or x== "0" else RED).scale(4),
                        ).scale_to_fit_height(0.9*config.frame_height).to_edge(DOWN,buff=0.1/2)
        ddt.get_rows()[0].set_color(PEACH)
        ddt.get_columns()[0].set_color(TEAL)
        ddt.add(Line(ddt.get_corner(UR), ddt.get_corner(DR),stroke_color=TEXT,stroke_width=2))
        ddt.add(Line(ddt.get_corner(DL), ddt.get_corner(DR),stroke_color=TEXT,stroke_width=2))

        self.play(FadeOut(eqGroup),FadeOut(table2),FadeOut(title))
        self.play(Write(ddt))
        self.wait()

        brace = Brace(ddt.get_columns()[0], direction=LEFT, buff=0.3, stroke_color=TEAL).set_color(TEAL)
        braceText = MathTex(r"\Delta_x").set_color(TEAL).next_to(brace, LEFT, buff=0.1)
        brace2 = Brace(ddt.get_rows()[0], direction=UP, buff=0.2/4, stroke_color=PEACH).set_color(PEACH)
        braceText2 = MathTex(r"\#{{\Delta_y}}").set_color(PEACH).next_to(brace2, UP, buff=0.1/4)
        colorize(braceText)
        colorize(braceText2)
        self.play(Write(brace), Write(braceText))
        self.wait()

        self.play(Write(brace2), Write(braceText2))
        self.wait()

        self.play(FadeOut(VGroup(brace,braceText,brace2,braceText2)),ddt.animate.move_to(ORIGIN))
        self.wait()

        self.play(Circumscribe(ddt.get_rows()[12]))
        self.wait()

        self.play(Circumscribe(ddt.get_cell((13,4))))
        self.wait()

        self.play(Circumscribe(ddt.get_cell((2,2))))
        self.wait()

        self.play(ddt.animate.to_edge(RIGHT,buff=0))
        prob = MathTex(r"{{\mathbb{P}}}({{\Delta_y=2}} | {{\Delta_x=B}}) = \frac{8}{16} = \frac{1}{2}").to_edge(LEFT,buff=0).set_color(ROSEWATER).scale(0.9)
        colorize(prob)
        self.play(Write(prob))
        self.wait()

        self.play(Indicate(ddt.get_rows()[12]))
        self.wait()

class reversibility(Scene):
    def construct(self):
        buffy = 0.75
        xorBox = Rectangle(width=2, height=1).set_fill(SURFACE0,opacity=1).set_stroke(TEXT,3).shift(UP*2+LEFT*3)
        xorText = MathTex(r"\oplus").set_color(TEXT).scale(1.5).move_to(xorBox.get_center())
        colorize(xorText)
        xorBoxGroup = VGroup(xorBox,xorText)
        msg = MathTex(r"{{M}}").scale(1.5).next_to(xorBox, UP, buffy)
        colorize(msg)
        arr = Arrow(start=msg.get_bottom(), end=xorBox.get_top(), buff=0.1, color=TEAL)

        leftLabel = MathTex(rf"K").scale(1.5).next_to(xorBox.get_left(), LEFT, buff=buffy).set_color(BLUE)
        leftLine = Arrow(leftLabel.get_right(), xorBox.get_left(),buff=0.1).set_color(BLUE)

        sbox1 = Rectangle(width=2, height=1).set_fill(SURFACE0,opacity=1).set_stroke(TEXT,3)
        sbox_text = MathTex(r"S").set_color(TEXT).scale(1.5)
        colorize(sbox_text)
        sbox1 = VGroup(sbox1,sbox_text)
        sbox1.next_to(xorBox, DOWN, buff=buffy)

        arr2 = Arrow(start=xorBox.get_bottom(), end=sbox1.get_top(), buff=0.1, color=PEACH)

        opaque_box = Rectangle(width=2, height=1).set_fill(SURFACE0,opacity=1).set_stroke(TEXT,3).next_to(sbox1, DOWN, buff=buffy)
        opaque_text = MathTex(r"P").set_color(TEXT).scale(1.5).move_to(opaque_box.get_center()) 
        opaque_group = VGroup(opaque_box,opaque_text)
        arr3 = Arrow(start=sbox1.get_bottom(), end=opaque_box.get_top(), buff=0.1, color=YELLOW)

        out = MathTex(r"{{Z}}").scale(1.5).next_to(opaque_group, DOWN, buffy).set_color(RED)
        arr4 = Arrow(start=opaque_group.get_bottom(), end=out.get_top(), buff=0.1, color=RED)

        #totGroup = VGroup(sgroup,pbox).move_to(ORIGIN)
        self.play(Write(xorBoxGroup),Write(leftLabel),Write(leftLine),Write(sbox1),Write(msg),Write(arr),Write(arr2),Write(opaque_group),Write(arr3),Write(out),Write(arr4))
        self.wait()

        z_copy  = out.copy()
        dashed_line = DashedLine(start=ORIGIN+UP*2.5, end=ORIGIN+DOWN*3.5, stroke_color=TEXT)
        self.play(z_copy.animate.shift(RIGHT*6),Write(dashed_line))
        self.wait()

        pbox_inv = Rectangle(width=2, height=1).set_fill(SURFACE0,opacity=1).set_stroke(TEXT,3).next_to(z_copy, UP, buff=buffy)
        pbox_inv_text = MathTex(r"P^{-1}").set_color(TEXT).scale(1.5).move_to(pbox_inv.get_center()) 
        colorize(pbox_inv_text)
        pbox_inv_group = VGroup(pbox_inv,pbox_inv_text)
        arr5 = Arrow(start=z_copy.get_top(), end=pbox_inv.get_bottom(), buff=0.1, color=RED)
        sbox_inv = Rectangle(width=2, height=1).set_fill(SURFACE0,opacity=1).set_stroke(TEXT,3).next_to(pbox_inv_group, UP, buff=buffy)
        sbox_inv_text = MathTex(r"S^{-1}").set_color(TEXT).scale(1.5).move_to(sbox_inv.get_center())
        colorize(sbox_inv_text)
        sbox_inv_group = VGroup(sbox_inv,sbox_inv_text)
        sbox_inv_group.next_to(pbox_inv_group, UP, buff=buffy)
        arr6 = Arrow(start=pbox_inv_group.get_top(), end=sbox_inv_group.get_bottom(), buff=0.1, color=YELLOW)

        xorbox2 = Rectangle(width=2, height=1).set_fill(SURFACE0,opacity=1).set_stroke(TEXT,3).next_to(sbox_inv_group, UP, buff=buffy)
        xorbox2_text = MathTex(r"\oplus").set_color(TEXT).scale(1.5).move_to(xorbox2.get_center())
        colorize(xorbox2_text)
        xorbox2_group = VGroup(xorbox2,xorbox2_text)

        xor_leftLabel = MathTex(rf"K").scale(1.5).next_to(xorbox2.get_left(), LEFT, buff=buffy).set_color(BLUE)
        colorize(xor_leftLabel)
        xor_leftLine = Arrow(xor_leftLabel.get_right(), xorbox2.get_left(),buff=0.1).set_color(BLUE)

        arr8 = Arrow(start=sbox_inv_group.get_top(), end=xorbox2.get_bottom(), buff=0.1, color=PEACH)
        out2 = MathTex(r"{{M}}").scale(1.5).next_to(xorbox2, UP, buffy).set_color(TEAL)
        arr7 = Arrow(start=xorbox2.get_top(), end=out2.get_bottom(), buff=0.1, color=TEAL)

        self.play(Write(pbox_inv_group),Write(arr5))
        self.wait()

        self.play(Write(sbox_inv_group),Write(arr6))
        self.wait()

        self.play(Write(xorbox2_group),Write(xor_leftLabel),Write(xor_leftLine),Write(arr8))
        self.wait()

        self.play(Write(out2),Write(arr7))
        self.wait()

        self.play(xor_leftLabel.animate.set_opacity(0.3))
        outGroup = VGroup(arr7,out2,xorbox2_group,xor_leftLabel,xor_leftLine)
        labelXor = MathTex(r"{{M}} \oplus {{K}}").set_color(TEXT).scale(1.5).next_to(sbox_inv, UP, buff=buffy)
        colorize(labelXor)
        self.play(Write(labelXor),outGroup.animate.shift(UP*10))
        self.wait()

        self.play(Wiggle(labelXor,run_time=1.5))
        self.wait()

        self.play(labelXor.animate.shift(LEFT*1+UP*0.5))
        added = MathTex(r"\oplus {{M}}").scale(1.5).next_to(labelXor, RIGHT,buff=0.1)
        colorize(added)
        self.wait()

        self.play(Write(added))
        self.wait()

        final = MathTex(r"{{K}}").scale(1.5).move_to(labelXor)
        colorize(final)
        self.play(Transform(VGroup(labelXor,added),final))
        self.wait()

        self.play(FadeOut(VGroup(z_copy,dashed_line,pbox_inv_group,arr5,sbox_inv_group,arr6,xorbox2_group,xor_leftLabel,xor_leftLine,arr8,out2,arr7,labelXor)))
        self.wait()

        xorBox3 = Rectangle(width=2, height=1).set_fill(SURFACE0,opacity=1).set_stroke(TEXT,3)
        xorText3 = MathTex(r"\oplus").set_color(TEXT).scale(1.5).move_to(xorBox3.get_center())
        colorize(xorText3)
        xorBoxGroup3 = VGroup(xorBox3,xorText3).next_to(opaque_box,DOWN, buff=buffy)
        self.play(Write(xorBoxGroup3),FadeOut(out))

        leftLabel3 = MathTex(rf"K_2").scale(1.5).next_to(xorBox3.get_left(), LEFT, buff=buffy).set_color(BLUE)
        colorize(leftLabel3)
        leftLine3 = Arrow(leftLabel3.get_right(), xorBox3.get_left(),buff=0.1).set_color(BLUE)
        self.wait()

        leftLabel4 = MathTex(rf"K_1").scale(1.5).next_to(xorBox.get_left(), LEFT, buff=buffy).set_color(BLUE)
        colorize(leftLabel4)
        leftLine4 = Arrow(leftLabel4.get_right(), xorBox.get_left(),buff=0.1).set_color(BLUE)
        self.play(Write(leftLabel3),Write(leftLine3),Transform(leftLabel,leftLabel4),Transform(leftLine,leftLine4))
        self.wait()

        eq = MathTex(r"{{F}}({{X}}) = {{P}}({{S}}({{X}}))").set_color(RED).set_color_by_tex("S",TEAL).set_color_by_tex("Y",ORANGE).scale(1.25).to_edge(DOWN,buff=0.1).shift(RIGHT*2)
        colorize(eq)
        self.play(Write(eq))
        self.wait()

        eq2 = MathTex(r"{{F}}^{-1}({{Y}}) = {{S}}^{-1}({{P}}^{-1}({{Y}}))").set_color(RED).set_color_by_tex("S",TEAL).set_color_by_tex("Y",ORANGE).scale(1.25).next_to(eq, UP, buff=0.2)
        colorize(eq2)
        self.play(Write(eq2))
        self.wait()




class EvenMansourConstruction(Scene):
    def construct(self):
        M = MathTex(r"{{M}}").set_color(TEAL).scale(1.5).to_edge(LEFT,buff=0.5).shift(UP*1.5)
        self.play(Write(M))
        self.wait()
        xor1 = VGroup(Rectangle(width=2, height=1/1.5).set_fill(SURFACE0,opacity=1).set_stroke(TEXT,3),MathTex(r"\oplus {{K_1}}").set_color(TEXT).scale(1.25)).next_to(M, RIGHT, buff=1.5)
        colorize(xor1[1])
        arr1 = Arrow(start=M.get_right(), end=xor1.get_left(), buff=0.1/2, color=TEAL)
        self.play(Write(xor1),Write(arr1))
        self.wait()



        Fbox = Rectangle(width=2, height=1/1.5).set_fill(SURFACE0,opacity=1).set_stroke(TEXT,3).next_to(xor1, RIGHT, buff=1.5)
        Fbox_text = MathTex(r"F").set_color(TEXT).scale(1.5).move_to(Fbox.get_center()) 
        colorize(Fbox_text)
        Fbox_group = VGroup(Fbox,Fbox_text)
        arr2 = Arrow(start=xor1.get_right(), end=Fbox.get_left(), buff=0.1/2, color=GREEN)
        self.play(Write(Fbox_group),Write(arr2))
        self.wait()

        V = MathTex(r"{{V}}").set_color(GREEN).scale(1.5).next_to(arr2,UP,buff=0.1)
        self.play(Write(V))
        self.wait()



        xor2 = VGroup(Rectangle(width=2, height=1/1.5).set_fill(SURFACE0,opacity=1).set_stroke(TEXT,3),MathTex(r"\oplus {{K_2}}").set_color(TEXT).scale(1.25)).next_to(Fbox, RIGHT, buff=1.5)
        colorize(xor2[1])
        arr3 = Arrow(start=Fbox.get_right(), end=xor2.get_left(), buff=0.1/2, color=ORANGE)
        self.play(Write(xor2),Write(arr3))
        self.wait()

        W = MathTex(r"{{W}}").set_color(ORANGE).scale(1.5).next_to(arr3,UP,buff=0.1)
        self.play(Write(W))
        self.wait()

        arr4 = Arrow(start=xor2.get_right(), end=xor2.get_right()+RIGHT*1.5, buff=0.1/2, color=RED)
        self.play(Write(arr4))
        self.wait()

        Z = MathTex(r"{{Z}}").set_color(RED).scale(1.5).next_to(arr4,RIGHT,buff=0.1/2)
        self.play(Write(Z))
        self.wait()

        network = VGroup(M,arr1,xor1,arr2,Fbox_group,arr3,xor2,arr4,Z,V,W)
        
        pair1 = MathTex(r"({{M_1}},{{Z_1}})").set_color(ROSEWATER).set_color_by_tex("M",TEAL).set_color_by_tex("Z",RED).scale(1.5).to_edge(LEFT).shift(DOWN*1)
        pair2 = MathTex(r"({{M_2}},{{Z_2}})").set_color(ROSEWATER).set_color_by_tex("M",TEAL).set_color_by_tex("Z",RED).scale(1.5).next_to(pair1, DOWN, buff=0.25)
        rec= SurroundingRectangle(VGroup(pair1,pair2),color=MAUVE,stroke_width=3,buff=0.3)
        label = MathTex(r"Known:").set_color(MAUVE).next_to(rec, UP, buff=0.1)
        self.play(Write(pair1))
        self.wait()

        self.play(Write(pair2))
        self.wait()

        self.play(Write(rec))
        self.play(Write(label))
        self.wait()

        K1bitstring = MathTex(r"{{K_1}} =", "{{0101\ldots1010}}").set_color(ROSEWATER).set_color_by_tex("K",BLUE).scale(1.5).to_edge(RIGHT).shift(DOWN)
        brace = Brace(K1bitstring[2], direction=UP, buff=0.3, stroke_color=BLUE).set_color(BLUE)
        braceText = MathTex(r"{{n}}-bits").set_color(ROSEWATER).set_color_by_tex("n",BLUE).next_to(brace, UP, buff=0.1)
        self.play(Write(K1bitstring))
        self.wait()

        self.play(Write(brace), Write(braceText))
        self.wait()

        K2bitstring = MathTex(r"{{K_2}} =" ,"1010\ldots0101").set_color(ROSEWATER).set_color_by_tex("K",BLUE).scale(1.5).next_to(K1bitstring, DOWN, buff=0.25)
        self.play(Write(K2bitstring))
        self.wait()

        self.play(FadeOut(VGroup(K1bitstring,brace,braceText,K2bitstring)))
        self.wait()

        twoN = MathTex(r"\mathcal{O}(2^{2{{n}}})").set_color(ROSEWATER).set_color_by_tex("n",BLUE).scale(1.5).to_edge(UP).shift(LEFT*1)
        self.play(Write(twoN))
        self.wait()

        oneN = MathTex(r"\mathcal{O}(2^{{n}}})").set_color(ROSEWATER).set_color_by_tex("n",BLUE).scale(1.5).next_to(twoN, RIGHT,buff=2)
        arrow = Arrow(start=twoN.get_right(), end=oneN.get_left(), buff=0.1/2, color=RED)
        self.play(Write(arrow),Write(oneN))
        self.wait()

        self.play(FadeOut(VGroup(twoN,oneN,arrow)))
        self.wait()

        title = Title(f"Even-Mansour Construction Known-plaintext attack",font_size=50).set_color_by_gradient(BLUE,RED)
        self.play(Write(title))
        self.wait()

        self.play(FadeOut(title))
        self.wait()

        eq1 = MathTex(r"{{\Delta_M}}={{M_1}} {{\oplus}} {{M_2}}").set_color(ROSEWATER).set_color_by_tex("\oplus",RED).set_color_by_tex("M",TEAL).scale(1.5).to_edge(RIGHT,buff=0.5)
        self.play(Write(eq1))
        self.wait()

        eq2 = MathTex(r"{{\Delta_Z}}={{Z_1}} {{\oplus}} {{Z_2}}").set_color(ROSEWATER).set_color_by_tex("\oplus",RED).set_color_by_tex("Z",RED).scale(1.5).next_to(eq1, DOWN, buff=0.25)
        self.play(Write(eq2))
        self.wait()

        eq3 = MathTex(r"{{\Delta_Z}}={{\Delta_W}}").set_color(ROSEWATER).set_color_by_tex("Z",RED).set_color_by_tex("W",RED).set_color_by_tex("F",PEACH).set_color_by_tex("V",GREEN).set_color_by_tex("M",TEAL).scale(1.5).next_to(eq2, DOWN, buff=0.25)
        self.play(Write(eq3))
        self.wait()

        eq4  = MathTex(r"={{F}}({{V}} {{\oplus}} {{\Delta_M}}) {{\oplus}} {{F}}({{V}})").set_color(ROSEWATER).set_color_by_tex("Z",RED).set_color_by_tex("F",PEACH).set_color_by_tex("V",GREEN).set_color_by_tex("\oplus",RED).set_color_by_tex("M",TEAL).scale(1.5).next_to(eq3, DOWN, buff=0.25).to_edge(RIGHT,buff=0.5)
        self.play(Write(eq4))
        self.wait()

        known3 = MathTex(r"{{\Delta_M}},{{\Delta_Z}},{{\Delta_W}}").set_color(ROSEWATER).set_color_by_tex("M",TEAL).set_color_by_tex("Z",RED).set_color_by_tex("W",RED).scale(1.5).next_to(pair2,DOWN,buff=0.25).to_edge(LEFT)
        rec2 = SurroundingRectangle(VGroup(pair1,pair2,known3),color=MAUVE,stroke_width=3,buff=0.3)

        self.play(Write(known3),Transform(rec,rec2),label.animate.next_to(rec2, UP, buff=0.1))
        self.wait()

        self.play(FadeOut(VGroup(eq1,eq2)))
        self.wait()

        idea1 = MathTex(r"Generate \, all:({{V'}},{{V'}} {{\oplus}} {{\Delta_M}})").set_color(ROSEWATER).set_color_by_tex("V",GREEN).set_color_by_tex("M",TEAL).set_color_by_tex("\oplus",RED).scale(1.3).shift(UP*1.75+RIGHT*2.25)
        self.play(Write(idea1),network.animate.to_edge(UP,buff=0.2))
        self.wait()

        idea2 = MathTex(r"{{F}}({{V'}}) {{\oplus}} {{F}}({{V'}} {{\oplus}} {{\Delta_M}}) \stackrel{?}{=} {{\Delta_W}}").set_color(ROSEWATER).set_color_by_tex("F",PEACH).set_color_by_tex("V",GREEN).set_color_by_tex("M",TEAL).set_color_by_tex("W",RED).set_color_by_tex("\oplus",RED).scale(1.3).next_to(idea1, DOWN, buff=0.2)
        surr = SurroundingRectangle(VGroup(idea1,idea2),color=RED,stroke_width=3,buff=0.2)
        self.play(Write(idea2),Write(surr))
        self.wait()

        #/*SHOW CODE*/

        idea3 = MathTex(r"{{E}}_{{K}}({{M_2}}) \stackrel{?}{=} {{Z_2}} {{\land}} \ldots").set_color(ROSEWATER).set_color_by_tex("E",ORANGE).set_color_by_tex("M",TEAL).set_color_by_tex("Z",RED).set_color_by_tex("K",BLUE).scale(1.3).next_to(idea2, DOWN, buff=0.2)
        surr2 = SurroundingRectangle(VGroup(idea1,idea2,idea3),color=RED,stroke_width=3,buff=0.2)
        self.play(Write(idea3),Transform(surr,surr2))
        self.wait()









        



class differentialTrails(Scene):
    def construct(self):
        buffy = 0.6
        m1 = MathTex(r"4").set_color(TEAL).scale(1.25).to_edge(UP+LEFT,buff=1).shift(UP*0.85)
        m2 = MathTex(r"F").set_color(TEAL).scale(1.25).to_edge(UP+RIGHT,buff=1).shift(UP*0.85)
        self.play(Write(m1),Write(m2))
        self.wait()

        eq = MathTex(r"{{M}} {{\oplus}} {{M'}} = 4 {{\oplus}} F = B").set_color(TEAL).scale(1.5)
        colorize(eq)
        self.play(Write(eq))
        self.wait()

        self.play(FadeOut(eq))
        self.wait()
        
        xor1 = VGroup(Rectangle(width=2, height=1/1.5).set_fill(SURFACE0,opacity=1).set_stroke(TEXT,3),MathTex(r"\oplus {{K_1}}").set_color(TEXT).scale(1.25)).next_to(m1, DOWN, buff=buffy)
        colorize(xor1[1])
        arr1 = Arrow(start=m1.get_bottom(), end=xor1.get_top(), buff=0.1/2, color=TEAL)

        sbox1 = VGroup(Rectangle(width=2, height=1/1.5).set_fill(SURFACE0,opacity=1).set_stroke(TEXT,3),MathTex(r"S").set_color(TEXT).scale(1.5)).next_to(xor1, DOWN, buff=buffy)
        arr2 = Arrow(start=xor1.get_bottom(), end=sbox1.get_top(), buff=0.1/2, color=PEACH)

        xor2 = VGroup(Rectangle(width=2, height=1/1.5).set_fill(SURFACE0,opacity=1).set_stroke(TEXT,3),MathTex(r"\oplus {{K_2}}").set_color(TEXT).scale(1.25)).next_to(sbox1, DOWN, buff=buffy)
        colorize(xor2[1])
        arr3 = Arrow(start=sbox1.get_bottom(), end=xor2.get_top(), buff=0.1/2, color=YELLOW)

        sbox2 = VGroup(Rectangle(width=2, height=1/1.5).set_fill(SURFACE0,opacity=1).set_stroke(TEXT,3),MathTex(r"S").set_color(TEXT).scale(1.5)).next_to(xor2, DOWN, buff=buffy)
        arr4 = Arrow(start=xor2.get_bottom(), end=sbox2.get_top(), buff=0.1/2, color=PEACH)

        xor3 = VGroup(Rectangle(width=2, height=1/1.5).set_fill(SURFACE0,opacity=1).set_stroke(TEXT,3),MathTex(r"\oplus {{K_3}}").set_color(TEXT).scale(1.25)).next_to(sbox2, DOWN, buff=buffy)
        colorize(xor3[1])
        arr5 = Arrow(start=sbox2.get_bottom(), end=xor3.get_top(), buff=0.1/2, color=YELLOW)
        self.play(Write(xor1),Write(sbox1),Write(xor2),Write(sbox2),Write(xor3),Write(arr1),Write(arr2),Write(arr3),Write(arr4),Write(arr5))
        self.wait()
        aaaa =VGroup(xor1,sbox1,xor2,sbox2,xor3,arr2,arr3,arr4,arr5).copy().next_to(m2, DOWN, buff=buffy)
        arr1b = Arrow(start=m2.get_bottom(), end=aaaa.get_top(), buff=0.1/2, color=TEAL)
        aaaa.add(arr1b)
        self.play(Write(aaaa)) #Write(Line(aaaa,xor3.get_bottom()))
        self.wait()

        dm = MathTex(r"{{\Delta_m}} = B").set_color(RED).scale(1.5).move_to(m1.get_center()+(m2.get_center()-m1.get_center())/2)
        colorize(dm)
        self.play(Write(dm))
        self.wait()
        m3 = MathTex(r"B").set_color(RED).scale(1.5).move_to(m1.get_center()+(m2.get_center()-m1.get_center())/2)
        self.play(Transform(dm,m3))
        self.wait()

        xorb1 = VGroup(Rectangle(width=2, height=1/1.5).set_fill(SURFACE0,opacity=1).set_stroke(RED,4),MathTex(r"\oplus {{K_1}}").set_color(TEXT).scale(1.25)).next_to(m3, DOWN, buff=buffy)
        colorize(xorb1[1])
        arrb1 = Arrow(start=m3.get_bottom(), end=xorb1.get_top(), buff=0.1/2, color=TEAL)

        sboxb1 = VGroup(Rectangle(width=2, height=1/1.5).set_fill(SURFACE0,opacity=1).set_stroke(RED,4),MathTex(r"S").set_color(TEXT).scale(1.5)).next_to(xorb1, DOWN, buff=buffy)
        arrb2 = Arrow(start=xorb1.get_bottom(), end=sboxb1.get_top(), buff=0.1/2, color=PEACH)

        xorb2 = VGroup(Rectangle(width=2, height=1/1.5).set_fill(SURFACE0,opacity=1).set_stroke(RED,4),MathTex(r"\oplus {{K_2}}").set_color(TEXT).scale(1.25)).next_to(sboxb1, DOWN, buff=buffy)
        colorize(xorb2[1])
        arrb3 = Arrow(start=sboxb1.get_bottom(), end=xorb2.get_top(), buff=0.1/2, color=YELLOW)

        sboxb2 = VGroup(Rectangle(width=2, height=1/1.5).set_fill(SURFACE0,opacity=1).set_stroke(RED,4),MathTex(r"S").set_color(TEXT).scale(1.5)).next_to(xorb2, DOWN, buff=buffy)
        arrb4 = Arrow(start=xorb2.get_bottom(), end=sboxb2.get_top(), buff=0.1/2, color=PEACH)

        xorb3 = VGroup(Rectangle(width=2, height=1/1.5).set_fill(SURFACE0,opacity=1).set_stroke(RED,4),MathTex(r"\oplus {{K_3}}").set_color(TEXT).scale(1.25)).next_to(sboxb2, DOWN, buff=buffy)
        colorize(xorb3[1])
        arrb5 = Arrow(start=sboxb2.get_bottom(), end=xorb3.get_top(), buff=0.1/2, color=YELLOW)

        self.play(Write(xorb1),Write(sboxb1),Write(xorb2),Write(sboxb2),Write(xorb3),Write(arrb1),Write(arrb2),Write(arrb3),Write(arrb4),Write(arrb5))
        self.wait()

        temp =VGroup(sboxb1,xorb2,sboxb2,xorb3,arrb3,arrb4,arrb5)
        m3b = MathTex(r"B").set_color(RED).scale(1.5).move_to(sboxb1)
        self.play(FadeOut(temp))
        self.wait()

        self.play(Write(m3b))
        self.wait()

        self.play(Wiggle(arr2),Wiggle(aaaa[5]),Circumscribe(arr2),Circumscribe(aaaa[5]))
        self.wait()

        eq2 = MathTex(r"{{AddKey_K({{X}})}} {{\oplus}} {{AddKey_K({{X'}})}} {{=}} {{\Delta_x}}").set_color(MAUVE)
        colorize(eq2)
        self.play(Write(eq2),Wiggle(m3b,run_time=1.5))
        self.wait()

        self.play(FadeOut(eq2))

        self.play(FadeOut(m3b),FadeIn(temp))
        self.wait()

        m3b.scale(1/1.5).next_to(arrb2,LEFT,buff=0.5/2)
        self.play(Write(m3b))
        self.wait()

        self.play(Circumscribe(arrb3),Circumscribe(sboxb1))
        self.wait()

        #fade in editing later

        postS = MathTex(r"{{2}} {{,}} 5 {{,}} 7 {{,}} D {{,}} F").set_color(PEACH).set_opacity(0.8).set_opacity_by_tex("2",2).set_color_by_tex("2","#ff8031").next_to(arrb3,LEFT,buff=0.5/2)
        colorize(postS)
        self.play(Write(postS))
        self.wait()

        postSCopy = postS.copy()
        self.play(postSCopy.animate.next_to(arrb4,LEFT,buff=0.5/2))
        self.wait()

        #16 possible different inputs and 2**12 possible keys

        outA = MathTex(r"3").set_color(PEACH).next_to(aaaa,DOWN,buffy)
        arroutA = Arrow(start=aaaa.get_bottom(), end=outA.get_top(), buff=0.1/2, color=PEACH)
        self.play(Write(outA),Write(arroutA))
        self.wait()

        outB = MathTex(r"6").set_color(PEACH).next_to(xor3,DOWN,buffy)
        arroutB = Arrow(start=xor3.get_bottom(), end=outB.get_top(), buff=0.1/2, color=PEACH)
        self.play(Write(outB),Write(arroutB))
        self.wait()

        outC = MathTex(r"5").set_color(RED).next_to(xorb3,DOWN,buffy)
        arroutC = Arrow(start=xorb3.get_bottom(), end=outC.get_top(), buff=0.1/2, color=RED)
        self.play(Write(outC),Write(arroutC))
        self.wait()

        outCCopy = outC.copy()
        self.play(outCCopy.animate.next_to(arrb5,LEFT,0.5/2))
        self.wait()

        #/* Nerd digression: Feels very similar to quantum computers, the 2,5,7,d,f possible xor's are a superposition which will
        # collaps when 'meassuring' the real xor and collapsing the wave function, reminds me of shor's and grover's algorithm where you can
        # manipulate a wavefunction a by looking at the resulting probability distribution intuit information about the building mathmatical
        # information (k, or the DDT characteristics) *
        # /

        keyGuess = MathTex(r"{{K_3'}} = {{2}}").scale(1.5).set_color_by_tex("2",BLUE).move_to(m1.get_center()+(m3.get_center()-m1.get_center())/2 + DOWN*0.25)
        colorize(keyGuess)
        self.play(Write(keyGuess),Write(SurroundingRectangle(keyGuess,color=BLUE,stroke_width=3)))
        self.wait()

        xoredA = MathTex(r"{{6}} {{\oplus}} 2").set_color(BLUE).set_color_by_tex("6",PEACH).next_to(arr5,RIGHT,buff=0.5/2)
        colorize(xoredA)
        self.play(Write(xoredA))
        self.wait()
        xoredA2 = MathTex(r"4").set_color(PEACH).next_to(arr5,RIGHT,buff=0.5/2)
        self.play(Transform(xoredA,xoredA2))
        self.wait()

        xoredB = MathTex(r"{{3}} {{\oplus}} 2").set_color(BLUE).set_color_by_tex("3",PEACH).next_to(aaaa[-2],LEFT,buff=0.5/2)
        colorize(xoredB)
        self.play(Write(xoredB))
        self.wait()
        xoredB2 = MathTex(r"1").set_color(PEACH).next_to(aaaa[-2],LEFT,buff=0.5/2)
        self.play(Transform(xoredB,xoredB2))
        self.wait()

        #/SHOW SBOX TABLE AGAIN/

        sedA = MathTex(r"1").set_color(TEAL).next_to(arr4,RIGHT,buff=0.5/2)
        self.play(Write(sedA))
        self.wait()
        
        sedB = MathTex(r"3").set_color(TEAL).next_to(aaaa[-3],LEFT,buff=0.5/2)
        self.play(Write(sedB))
        self.wait()

        sedACopy = sedA.copy()
        sedBCopy = sedB.copy()
        self.play(sedACopy.animate.move_to(m3.get_center()+(m2.get_center()-m3.get_center())/2+DOWN*0.25))

        xorSymbol = MathTex(r"\oplus").set_color(RED).next_to(sedACopy, RIGHT, buff=0.1)
        self.play(Write(xorSymbol))
        self.wait()

        self.play(sedBCopy.animate.next_to(xorSymbol, RIGHT, buff=0.1))
        self.wait()

        eqs = MathTex(r"= {{2}}").set_color_by_tex("2","#ff8031").next_to(sedBCopy, RIGHT, buff=0.1)
        self.play(Write(eqs))
        self.wait()

        #/GENERAL CASE NOW/

        #Fadeout everything except dm,keyguess and the red center differential Trail
        self.play(FadeOut(VGroup(m1,m2,arr1,arr2,arr3,arr4,arr5,aaaa,arroutA,outA,xor1,sbox1,xor2,sbox2,xor3,arroutB,outB,outC,xoredA,xoredB,sedA,sedB,xorSymbol,eqs,sedACopy,sedBCopy)))
        self.wait()

        Ops1 = MathTex(r"{{16}} \cdot ").set_color_by_tex("16",BLUE).move_to(sedACopy)
        Ops2 = MathTex(r"{{16}}").set_color_by_tex("16",RED).next_to(Ops1, RIGHT, buff=0.1)
        Ops3 = MathTex(r"= {{256}}").set_color_by_tex("256",PEACH).next_to(Ops2, RIGHT, buff=0.1)

        self.play(Write(Ops1))
        self.wait()

        self.play(Write(Ops2))
        self.wait()

        self.play(Write(Ops3))
        self.wait()

        self.play(FadeOut(VGroup(Ops1,Ops2,Ops3)))
        self.wait()

        table = Table(
            [["Potential \\, {{K_3}}","\#"],
             ["{{K_3'}}=0","0"],
             ["{{K_3'}}=1","0"],
             ["{{K_3'}}=2","1"],
             ["{{K_3'}}=3","0"],
             ["{{K_3'}}=4","0"],
             ["{{K_3'}}=5","0"],
             ["{{K_3'}}=6","0"],
             ["{{K_3'}}=7","0"],
             ["{{K_3'}}=8","0"],
             ["{{K_3'}}=9","0"],
             ["{{K_3'}}=A","0"],
             ["{{K_3'}}=B","0"],
             ["{{K_3'}}=C","0"],
             ["{{K_3'}}=D","0"],
             ["{{K_3'}}=E","0"],
             ["{{K_3'}}=F","0"]],
            include_outer_lines=True,
            line_config={"stroke_color": TEXT, "stroke_width": 2},
            element_to_mobject=lambda x: MathTex(x).set_color_by_tex("K",BLUE).scale(3),
        ).scale_to_fit_height(0.95*config.frame_height).to_edge(RIGHT,buff=buffy)
        self.play(Write(table))
        self.wait()

        self.play(Circumscribe(table.get_rows()[3]))
        self.wait()

        #/*SHOW CODE SNIPPET*/

        table2 = Table(
            [["Potential \\, {{K_3}}","\#"],
             ["{{K_3'}}=0","2"],
             ["{{K_3'}}=1","2"],
             ["{{K_3'}}=2","8"],
             ["{{K_3'}}=3","4"],
             ["{{K_3'}}=4","4"],
             ["{{K_3'}}=5","2"],
             ["{{K_3'}}=6","4"],
             ["{{K_3'}}=7","4"],
             ["{{K_3'}}=8","0"],
             ["{{K_3'}}=9","0"],
             ["{{K_3'}}=A","0"],
             ["{{K_3'}}=B","2"],
             ["{{K_3'}}=C","0"],
             ["{{K_3'}}=D","0"],
             ["{{K_3'}}=E","0"],
             ["{{K_3'}}=F","0"]],
            include_outer_lines=True,
            line_config={"stroke_color": TEXT, "stroke_width": 2},
            element_to_mobject=lambda x: MathTex(x).set_color_by_tex("K",BLUE).scale(3),
        ).scale_to_fit_height(0.95*config.frame_height).move_to(table.get_center())
        table2.get_columns()[1].set_color(MAUVE)
        self.play(Transform(table,table2))
        self.wait()

        self.play(Circumscribe(table2.get_rows()[3]))
        self.wait()

        #/* flash Prob(2) again in the DDT*/
        prob = MathTex(r"{{\mathbb{P}}}({{\Delta_y=2}} | {{\Delta_x=B}})  = \frac{1}{2}").scale(0.9).to_edge(LEFT,buff=0.1).shift(UP*2).set_color(ROSEWATER)
        colorize(prob)
        self.play(Write(prob))
        self.wait()

        expected = MathTex(r"{{\mathbb{E}}}({{K_3'}}={{K_3}}) = 16 \cdot \frac{1}{2} = {{8}}").set_color(ROSEWATER).set_color_by_tex("8",MAUVE).scale(0.9).to_edge(LEFT,buff=0.1).shift(UP*0)
        colorize(expected)
        self.play(Write(expected))
        self.wait()

        self.play(Circumscribe(table2.get_rows()[3]))
        self.wait()

        expected2 = MathTex(r"{{\mathbb{E}}}({{K_3'}}{{\neq}}{{K_3}}) = {{2.125}}").set_color(ROSEWATER).set_color_by_tex("2.125",MAUVE).scale(0.9).to_edge(LEFT,buff=0.1).shift(UP*(-2))
        colorize(expected2)
        self.play(Write(expected2))
        self.wait()

class proofExpectedVal(Scene):
    def construct(self):
        ddt_data = [
            ["-","0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"],
            ["0","16","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
            ["1","0","0","0","2","0","0","0","2","0","2","4","0","4","2","0","0"],
            ["2","0","0","0","2","0","6","2","2","0","2","0","0","0","0","2","0"],
            ["3","0","0","2","0","2","0","0","0","0","4","2","0","2","0","0","4"],
            ["4","0","0","0","2","0","0","6","0","0","2","0","4","2","0","0","0"],
            ["5","0","4","0","0","0","2","2","0","0","0","4","0","2","0","0","2"],
            ["6","0","0","0","4","0","4","0","0","0","0","0","0","2","2","2","2"],
            ["7","0","0","2","2","2","0","2","0","0","2","2","0","0","0","0","4"],
            ["8","0","0","0","0","0","0","2","2","0","0","0","4","0","4","2","2"],
            ["9","0","2","0","0","2","0","0","4","2","0","2","2","2","0","0","0"],
            ["A","0","2","2","0","0","0","0","0","6","0","0","2","0","0","4","0"],
            ["B","0","0","8","0","0","2","0","2","0","0","0","0","0","2","0","2"],
            ["C","0","2","0","0","2","2","2","0","0","0","0","2","0","6","0","0"],
            ["D","0","4","0","0","0","0","0","4","2","0","2","0","2","0","2","0"],
            ["E","0","0","2","4","2","0","0","0","6","0","0","0","0","0","2","0"],
            ["F","0","2","0","0","6","0","0","0","0","4","0","2","0","0","2","0"]
        ]
        ddt = Table(ddt_data, 
                      include_outer_lines=False,
                      line_config={"stroke_color": TEXT, "stroke_width": 2}, #color input in peach and output in teal
                        element_to_mobject=lambda x: Tex(x).set_color(TEXT if x =="-" or x== "0" else RED).scale(4),
                        ).scale_to_fit_height(0.8*config.frame_height).to_edge(RIGHT,buff=0.1/2)
        ddt.get_rows()[0].set_color(PEACH)
        ddt.get_columns()[0].set_color(TEAL)
        ddt.add(Line(ddt.get_corner(UR), ddt.get_corner(DR),stroke_color=TEXT,stroke_width=2))
        ddt.add(Line(ddt.get_corner(DL), ddt.get_corner(DR),stroke_color=TEXT,stroke_width=2))
        self.play(Write(ddt))
        self.wait()

        expected = MathTex(r"{{\mathbb{E}}}({{K_3'}}{{\neq}}{{K_3}}) = ").set_color(ROSEWATER).scale(0.8).to_edge(LEFT,buff=0.1)
        colorize(expected)
        self.play(Write(expected))
        self.wait()

        eight = MathTex(r"{{8}}").set_color(RED).next_to(expected,RIGHT,buff=0.1)
        self.play(Write(eight))
        self.wait()
        
        self.play(Circumscribe(ddt.get_rows()[3]))
        self.wait()

        prob = MathTex(r"\cdot (\frac{6}{16}").set_color(PEACH).scale(0.8).next_to(eight,RIGHT,buff=0.1)
        colorize(prob)
        self.play(Write(prob))
        self.wait()
        
        self.play(Circumscribe(ddt.get_columns()[6]))
        self.wait()

        prob2 = MathTex(r"\cdot \frac{6}{16}").set_color(TEAL).scale(0.8).next_to(prob,RIGHT,buff=0.1)
        self.play(Write(prob2))
        self.wait()

        self.play(Circumscribe(ddt.get_rows()[3]),Circumscribe(ddt.get_columns()[4]),Circumscribe(ddt.get_columns()[7]),Circumscribe(ddt.get_columns()[8]),Circumscribe(ddt.get_columns()[10]),Circumscribe(ddt.get_columns()[15]))
        self.wait()
        prob3 = MathTex(r"+4\cdot {{(\frac{2}{16})}} ^2)").set_color(ROSEWATER).set_color_by_tex("16",MAUVE).scale(0.8).next_to(prob2,RIGHT,buff=0.1)
        self.play(Write(prob3))
        self.wait()

        formal = MathTex(r"{{8}} \cdot ( {{\mathbb{P}}}({{\Delta_y=5}} | {{\Delta_x=2}}) \cdot {{\mathbb{P}}}({{\Delta_x=2}} | {{\Delta_y=5}})").set_color(ROSEWATER).set_color_by_tex("8",RED).scale(0.65).to_edge(LEFT,buff=0.1).shift(DOWN*2)
        colorize(formal)
        self.play(Write(formal),Circumscribe(ddt.get_rows()[3]),Circumscribe(ddt.get_columns()[6]))
        self.wait()

        formal2 = MathTex(r"+ 4 \cdot {{\ldots}})").set_color(ROSEWATER).set_color_by_tex("ldots",MAUVE).scale(0.65).next_to(formal,RIGHT,buff=0.1)
        self.play(Write(formal2),Circumscribe(ddt.get_rows()[3]),Circumscribe(ddt.get_columns()[4]),Circumscribe(ddt.get_columns()[7]),Circumscribe(ddt.get_columns()[8]),Circumscribe(ddt.get_columns()[10]),Circumscribe(ddt.get_columns()[15]))
        self.wait()

        prob4 = MathTex(r"+ {{8}}\cdot {{\frac{1}{16}}").set_color(ROSEWATER).set_color_by_tex("8",RED).scale(0.8).to_edge(LEFT,buff=0.1).shift(DOWN*0.75)
        self.play(Write(prob4))
        self.wait()

        formal3 = MathTex(r" + {{8}} \cdot {{\mathbb{P}}}({{\Delta_x}}={{2}})").set_color(ROSEWATER).set_color_by_tex("8",RED).scale(0.65).to_edge(LEFT,buff=0.1).shift(DOWN*2.5)
        colorize(formal3)
        self.play(Write(formal3))
        self.wait()

        prob5 = MathTex(r"= 2.125").set_color(ROSEWATER).scale(0.8).next_to(prob4,RIGHT,buff=0.1)
        self.play(Write(prob5))
        self.wait()
        

        #/*NERD NOTE, you can actually calculate the probability of getting an input diff of 2 more exactly but i'll leave that as an exercise for the viewer*/
        








        









        






    











