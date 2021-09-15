# python tkinter menu to create various types of menu

from tkinter import *

top =Tk()

def hello():
    print("Hello Dhiraj!!")


# create a top level menu

menubar = Menu()

menubar.add_command(label="Hello!!",command=hello)

menubar.add_command(label="Quit!!",command=top.quit)

# display the menu

top.config(menu=menubar)

top.mainloop() # to hold the output screen

