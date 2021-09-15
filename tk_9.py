# python program to delete the active items from the list

from tkinter import *

top =Tk() # create object of tkinter class 

top.geometry()

lbl = Label(top,text="A list of favourite places----")

listbox = Listbox(top)

listbox.insert(1,"New Delhi")

listbox.insert(2,"Jaipur")

listbox.insert(3,"Gurgaon")

listbox.insert(4,"Noida")

listbox.insert(5,"Varanshi")

# this button will delete the selected item from the list

btn= Button(top,text="Delete",command=lambda listbox= listbox:listbox.delete(ANCHOR))


lbl.pack()

listbox.pack()

btn.pack()

top.mainloop()

