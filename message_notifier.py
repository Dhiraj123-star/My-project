from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("200x200")

def msg():
    messagebox.showwarning("Alert Box","stop virus found")

but= Button(root,text="ok",command=msg)
but.place(x=100,y=100)

root.mainloop()