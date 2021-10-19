# password generator with python tkinter

from tkinter import *

import random

import string

def gen():
    password=[]
    for i in range(2):
        lower= random.choice(string.ascii_lowercase)
        upper= random.choice(string.ascii_uppercase)
        numbers= random.choice(string.digits)
        password.append(lower)
        password.append(upper)
        password.append(numbers)
        pass_=" ".join(str(x) for x in password)
        label.config(text=pass_)


root=Tk()
label= Label(root,font=('arial',40,'bold'))
label.pack()
button1= Button(root,text="Generate",font=('arial',40,'bold'),command=gen).place(x=100,y=200)

root.geometry("500x500")

root.title("password")

root.mainloop()

