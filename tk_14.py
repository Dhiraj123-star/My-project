# python tkinter is used to draw radio button

from tkinter import *

def selection():
    selection = "You selected the option "+str(radio.get())
    label.config(text=selection)


top =Tk()

top.geometry("300x150")
radio= IntVar()

lbl = Label(text= "Favourite Programming Language :")

lbl.pack()

R1= Radiobutton(top,text ="Julia",variable=radio,value=1,command=selection)

R1.pack(anchor=W) # anchor represents the exact position of text within the widget(default=Center)

R2 = Radiobutton(top,text="JavaScript",variable=radio,value=2,command=selection)

R2.pack(anchor=W)


R3 = Radiobutton(top,text="Java",variable=radio,value=3,command=selection)

R3.pack(anchor=W)

R4 = Radiobutton(top,text="TypeScript",variable=radio,value=4,command=selection)

R4.pack(anchor=W)

label=Label(top)

label.pack()

top.mainloop()

