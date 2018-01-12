from tkinter import *
from PIL import Image ,ImageTk
class ManualWindow:

    def create(window,x1,y1,x,y,z,b,u,l):

        window1 = Frame(window, width=800, height=600 ).place(x=x1, y=y1)

        toolb = Frame(window1, width=800, height=80, bg="#eee", bd=2, relief=GROOVE).place(x=x1, y=y1)

        Label(toolb, text="Current Position:", font=("Arial", 10, "bold italic")).place(x=x1, y=y1 + 1)
        Label(toolb, text="X:", font=("Forte", 30, "bold ")).place(x=x1, y=y1 + 20)
        Label(toolb, text=str(x), font=("OCR A Extended", 30, "")).place(x=x1 + 50, y=y1 + 20)
        Label(toolb, text="Y:", font=("Forte", 30, "bold ")).place(x=x1 + 200, y=y1 + 20)
        Label(toolb, text=str(y), font=("OCR A Extended", 30, "")).place(x=x1 + 250, y=y1 + 20)
        Label(toolb, text="Z:", font=("Forte", 30, "bold ")).place(x=x1 + 400, y=y1 + 20)
        Label(toolb, text=str(z), font=("OCR A Extended", 30, "")).place(x=x1 + 450, y=y1 + 20)
        Label(toolb, text="Angles:", font=("Arial", 10, "bold italic")).place(x=x1 + 600, y=y1 + 5)
        Label(toolb, text="-Base:", font=("Arial", 9, "bold italic")).place(x=x1 + 660, y=y1 + 10)
        Label(toolb, text="-Upper:", font=("Arial", 9, "bold italic")).place(x=x1 + 660, y=y1 + 30)
        Label(toolb, text="-Lower:", font=("Arial", 9, "bold italic")).place(x=x1 + 660, y=y1 + 50)

        Label(toolb, text=str(b), font=("Arial", 9, "bold italic")).place(x=x1 + 730, y=y1 + 10)
        Label(toolb, text=str(u), font=("Arial", 9, "bold italic")).place(x=x1 + 730, y=y1 + 30)
        Label(toolb, text=str(l), font=("Arial", 9, "bold italic")).place(x=x1 + 730, y=y1 + 50)

        # corrdinate panel
        coordinate = Frame(window1, width=799, height=665, bg="#0a1a46", bd=5, relief=RAISED).place(x=x1, y=y1 + 80)
        Label(coordinate, text="Hint: Define the size of the step for each command button and  then  press the button", font=("Arial", 13, ""),fg="#bfd0fe",bg="#0a1a46").place(x=x1 + 5, y=y1 + 85)

        bup = Button(coordinate, width=10 ,text="UP", font=("Arial", 14, ""),bg="#6ad0ea").place(x=x1 + 200, y=y1 + 150)
        bdown= Button(coordinate,width=10, text="DOWN", font=("Arial", 14, ""),bg="#6ad0ea").place(x=x1 + 200, y=y1 + 350)
        bright = Button(coordinate, width=10, text="RIGHT", font=("Arial", 14, ""),bg="#6ad0ea").place(x=x1 + 300, y=y1 + 250)
        bright = Button(coordinate, width=10, text="LEFT", font=("Arial", 14, ""),bg="#6ad0ea").place(x=x1 + 100, y=y1 + 250)
        bforward = Button(coordinate, width=10, text="FORWARD", font=("Arial", 14, ""),bg="#6ad0ea").place(x=x1 + 100, y=y1 + 450)
        bbackward = Button(coordinate, width=10, text="BACKWARD", font=("Arial", 14, ""),bg="#6ad0ea").place(x=x1 + 300, y=y1 + 450)
        stepvaluec = StringVar()
        stepc = Entry(coordinate, textvariable=stepvaluec, font=("OCR A Std", 14, ""), width=10).place(x=x1 + 230, y=y1 + 530)
        Label(coordinate, text="Coordinate step value:", font=("Arial", 16, ""),bg="#0a1a46",fg="#bfd0fe").place(x=x1 , y=y1 + 530)

        bb = Button(coordinate, width=10, text="Rotate Base", font=("Arial", 14, ""),bg="#6ad0ea").place(x=x1 + 600, y=y1 + 150)
        bu= Button(coordinate, width=10, text="Rotate Upper", font=("Arial", 14, ""),bg="#6ad0ea").place(x=x1 + 600, y=y1 + 250)
        bl = Button(coordinate, width=10, text="Rotate Lower", font=("Arial", 14, ""),bg="#6ad0ea").place(x=x1 + 600, y=y1 + 350)
        rvaluec = StringVar()
        rc = Entry(coordinate, textvariable=rvaluec, font=("OCR A Std", 14, ""), width=10).place(x=x1 + 640,y=y1 + 530)
        Label(coordinate, text="Rotation step value:", font=("Arial", 16, ""),bg="#0a1a46",fg="#bfd0fe").place(x=x1+440, y=y1 + 530)

        return window1
    def __init__(self):
        super()





























class AutomaticWindow:

    def create(window,x1,y1,x,y,z,b,u,l):
        window1 = Frame(window, width=800, height=600, bg="#aaa").place(x=x1, y=y1)
        toolb= Frame(window1,width=800,height=80,bg="#eee",bd=2,relief=GROOVE).place(x=x1,y=y1)
        Label(toolb, text="Current Position:", font=("Arial", 10, "bold italic")).place(x=x1, y=y1+1 )
        Label(toolb,text="X:",font=("Forte", 30, "bold ")).place(x=x1,y=y1+20)
        Label(toolb, text=str(x), font=("OCR A Extended", 30, "")).place(x=x1+50, y=y1 + 20)
        Label(toolb, text="Y:", font=("Forte", 30, "bold ")).place(x=x1+200, y=y1 + 20)
        Label(toolb, text=str(y), font=("OCR A Extended", 30, "")).place(x=x1 +250, y=y1 + 20)
        Label(toolb, text="Z:", font=("Forte", 30, "bold ")).place(x=x1 + 400, y=y1 + 20)
        Label(toolb, text=str(z), font=("OCR A Extended", 30, "")).place(x=x1 + 450, y=y1 + 20)
        Label(toolb, text="Angles:", font=("Arial", 10, "bold italic")).place(x=x1 + 600, y=y1+5 )
        Label(toolb, text="-Base:", font=("Arial", 9, "bold italic")).place(x=x1 + 660, y=y1+10)
        Label(toolb, text="-Upper:", font=("Arial", 9, "bold italic")).place(x=x1 + 660, y=y1 + 30)
        Label(toolb, text="-Lower:", font=("Arial", 9, "bold italic")).place(x=x1 + 660, y=y1 + 50)

        Label(toolb, text=str(b), font=("Arial", 9, "bold italic")).place(x=x1 + 730, y=y1 + 10)
        Label(toolb, text=str(u), font=("Arial", 9, "bold italic")).place(x=x1 + 730, y=y1 + 30)
        Label(toolb, text=str(l), font=("Arial", 9, "bold italic")).place(x=x1 + 730, y=y1 + 50)
        ###entry section

        #corrdinate panel
        coordinate = Frame(window1, width=399, height=665, bg="#eee", bd=5, relief=RAISED).place(x=x1, y=y1 + 80)
        Label(coordinate, text="Using Coordinates :", font=("Arial", 20, "bold  italic")).place(x=x1 + 5, y=y1 + 85)
        Label(coordinate, text="X value:", font=("Arial", 16, "")).place(x=x1 + 5, y=y1 + 200)
        vx = StringVar()
        ex=Entry(coordinate,textvariable=vx,font=("OCR A Std", 14, ""),width=10).place(x=x1+160,y=y1+203)
        Label(coordinate, text="Y value:", font=("Arial", 16, "")).place(x=x1 + 5, y=y1 + 300)
        vy = StringVar()
        ey = Entry(coordinate, textvariable=vx, font=("OCR A Std", 14, ""), width=10).place(x=x1 + 160, y=y1 + 303)
        Label(coordinate, text="Z value:", font=("Arial", 16, "")).place(x=x1 + 5, y=y1 + 400)
        vz = StringVar()
        ez = Entry(coordinate, textvariable=vx, font=("OCR A Std", 14, ""), width=10).place(x=x1 + 160, y=y1 + 403)
        b1=Button(coordinate,text="Set Coordinates",font=("Arial", 14, "")).place(x=x1+100,y=y1+500)

        #*************************************************************

        angle = Frame(window1, width=395, height=665, bg="#eee", bd=5, relief=RAISED).place(x=x1+402, y=y1 + 80)
        Label(angle, text="Using Angles :", font=("Arial", 20, "bold  italic")).place(x=x1 + 405, y=y1 + 85)
        Label(angle, text="Upper Angle value:", font=("Arial", 16, "")).place(x=x1 + 405, y=y1 + 200)
        vu = StringVar()
        eu = Entry(coordinate, textvariable=vu, font=("OCR A Std", 14, ""), width=10).place(x=x1 + 620, y=y1 + 203)
        Label(coordinate, text="Lower Angle value:", font=("Arial", 16, "")).place(x=x1 + 405, y=y1 + 300)
        vl = StringVar()
        el = Entry(coordinate, textvariable=vl, font=("OCR A Std", 14, ""), width=10).place(x=x1 + 620, y=y1 + 303)
        Label(coordinate, text="Base Angle value:", font=("Arial", 16, "")).place(x=x1 + 405, y=y1 + 400)
        vb = StringVar()
        eb = Entry(coordinate, textvariable=vb, font=("OCR A Std", 14, ""), width=10).place(x=x1 + 620 , y=y1 + 403)
        b2 = Button(coordinate, text="Set Angles", font=("Arial", 14, "")).place(x=x1 + 500, y=y1 + 500)





        return window1
    def __init__(self):
        super()



