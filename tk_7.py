# python program to draw label

from tkinter import *

top =Tk() # create object of tkinter class 

top.geometry("300x200")

# creating label

uname = Label(top,text="Username").place(x=30,y=50)

# creating label

password = Label(top,text="Password").place(x=30,y=90)

sbbutton= Button(top,text="Submit",activebackground="pink",activeforeground="red").place(x=30,y=120)

e1= Entry(top,width=20).place(x=100,y=50)

e2= Entry(top,width=20).place(x=100,y=90)

top.mainloop() # to hold the output screen 