# python tkinter to display menubutton

from tkinter import *

top =Tk()

top.geometry("200x250")

menubutton = Menubutton(top,text="Language",relief=FLAT) 

menubutton.grid()

menubutton.menu =Menu(menubutton)

menubutton["menu"] = menubutton.menu

menubutton.menu.add_checkbutton(label = "Python",variable=IntVar())

menubutton.menu.add_checkbutton(label = "PHP",variable=IntVar())

menubutton.menu.add_checkbutton(label = "C#",variable=IntVar())

menubutton.menu.add_checkbutton(label = "Julia",variable=IntVar())

menubutton.pack()

top.mainloop() 

