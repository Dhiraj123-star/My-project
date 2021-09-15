# python application to draw canvas

from tkinter import *

top =Tk()# create object of tkinter class 

top.geometry("200x200")

# creating a simple canvas

c=Canvas(top,bg="red",height="200")

c.pack() # it is used to organise widget in the block 

top.mainloop() 