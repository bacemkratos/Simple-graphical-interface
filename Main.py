from tkinter import *
from views import *
from PIL import Image, ImageTk

main=Tk()
mw = None
aw = None
x=15
y=5
z=12
b=0.0
u=56.1
l=59.14
def choice1():
    global mw
    global aw
    global x,y,z

    a=v.get()
    if (a == 1 ):
        mw=ManualWindow.create(main,0,30,x,y,z,b,u,l)
        if aw != None:
            a = aw
            a.destroy()
            aw=None



        print(a)
    elif (a== 2) :
        aw = AutomaticWindow.create(main, 0, 30,x,y,z,b,u,l)
        if mw != None:
            a = mw
            a.destroy()
            mw = None

        print(a)


main.title("Robot Arm");
main.geometry("800x600+100+10");
imag1e = Image.open('back1.jpg')
photo_image = ImageTk.PhotoImage(imag1e)
im2= ImageTk.PhotoImage(Image.open("banner1.jpg"))
c = Canvas(main,height=600,width=800)
c.create_image(400,300, image=photo_image)
c.create_image(400,13, image=im2)
c.place(x=0,y=0)

v=IntVar()




Radiobutton(main,text="Manual Mode",variable=v,indicatoron=0,width=25,value=1,command=choice1,font=("Arial",12,"bold"),bg="#14739f",fg="#33abe3").place(x=0,y=0)
Radiobutton(main,text="Automatic Mode",variable=v,indicatoron=0,width=25,value=2,command=choice1,font=("Arial",12,"bold"),bg="#14739f",fg="#33abe3").place(x=230,y=0)


main.mainloop()

