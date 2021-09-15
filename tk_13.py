# python  tkinter to display message 

from tkinter import *

top =Tk()

top.geometry("200x100")

var = StringVar()

msg= Message(top,text= "Welcome Users On Python !!")

msg.pack()

top.mainloop() # to hold the output 