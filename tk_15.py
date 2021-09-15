# python tkinter Scale widget (implement graphical slider)

from tkinter import *

def select():
    sel= "Value : "+str(v.get())
    label.config(text=sel)

top =Tk()

top.geometry("200x100")

v=DoubleVar()

scale = Scale(top,variable=v, from_=1, to=50,orient=VERTICAL)#(can be Horizontal also)

scale.pack(anchor=CENTER)

btn= Button(top,text="Value",command=select)
btn.pack(anchor=CENTER)

label=Label(top)  # we pass top as a parameter to draw 

label.pack()

top.mainloop()