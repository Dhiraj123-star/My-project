# python program to draw frame for organise the group of widgets

from tkinter import *

top =Tk()# create object of tkinter class 

top.geometry("140x100")

frame = Frame(top)

frame.pack()

leftframe = Frame(top)
leftframe.pack(side=LEFT)

rightframe = Frame(top)
rightframe.pack(side=RIGHT)

btn1 = Button(frame,text="Submit",fg="brown",activebackground="red")

btn1.pack(side=LEFT)

btn2 = Button(frame,text="Remove",fg="red",activebackground="brown")

btn2.pack(side=RIGHT)

btn3 = Button(rightframe,text="Add",fg="blue",activebackground="red")

btn3.pack(side=LEFT)

btn4 = Button(leftframe,text="Modify",fg="grey",activebackground="white")

btn4.pack(side=RIGHT)

top.mainloop() # for holding output screen






