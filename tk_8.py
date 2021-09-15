# python program to create listBox

from tkinter import *

top =Tk() # create object of tkinter class 

top.geometry("200x250")

lbl= Label(top,text="A list of favourite programming languages ----")

listbox = Listbox(top)

listbox.insert(1,"Python")

listbox.insert(2,"Java")

listbox.insert(3,"C")

listbox.insert(4,"JavaScript")

listbox.insert(5,"Julia")

lbl.pack()

listbox.pack()

top.mainloop() # to hold the output screen

