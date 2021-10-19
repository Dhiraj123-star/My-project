# gui calendar

from tkinter import *

from tkcalendar import Calendar

root = Tk()

root.geometry("400x400")

yr= int(input("Enter your year: "))
mth = int(input("Enter your month: "))
myday = int(input("Enter your day: "))
cal = Calendar(root,selectmode='day',year=yr,month=mth,day=myday)

cal.pack(pady=20)
def grad_date():
    date.config(text="Selected Date is: "+cal.get_date())

Button(root,text="Get Date",command=grad_date).pack(pady=20)

date= Label(root,text=" ")
date.pack(pady=20)
root.mainloop()