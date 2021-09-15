# python tkinter for askretrycancel()

from  tkinter import *

from tkinter import messagebox

top =Tk()

top.geometry("100x100")

messagebox.askretrycancel("Application","try again ?")

top.mainloop()