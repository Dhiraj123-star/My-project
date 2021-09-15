# python tkinter to draw scrollbar

from tkinter import *

top =Tk()

sb= Scrollbar(top)

sb.pack(side=RIGHT,fill=Y)  # right side scroll bar

mylist=Listbox(top,yscrollcommand=sb.set)

list1 = ["Python","Java","C","C++","JavaScript","C#","Scala","Kotlin","HTML","CSS","TypeScript","Swift","Go","R"]
for line in list1:
    mylist.insert(END,str(line))


mylist.pack(side=LEFT)

sb.config(command=mylist.yview)

mainloop() # to hold the output screen



