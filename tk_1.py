# python application to create a simple button

from tkinter import *

top =Tk()# create object of tkinter class 

top.geometry("200x100")

b= Button(top,text="Dhiraj")

b.pack()

top.mainloop() # to hold the output screen
