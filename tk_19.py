# python tkinter spinbox (alternative to the entry widget)
# it is used in the case where a user is given some fixed number of values to choose from

from tkinter import *

top =Tk()

top.geometry("200x200")

spin = Spinbox(top,from_=0,to=25)  # spin from 0 to 25

spin.pack()

top.mainloop()



