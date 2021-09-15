# python tkinter for showing text on python application

from tkinter import *

top =Tk()

text = Text(top)

text.insert(INSERT,"Name---")
text.insert(END,"Salary----")

text.pack()

text.tag_add("Write here","1.0","1.4")
text.tag_add("Click here","1.8","1.13")

text.tag_config("Write here",background="yellow",foreground="black")
text.tag_config("Click here",background="pink",foreground="red")

top.mainloop()