from tkinter import Label,Tk
import time

root=Tk()
root.title("Digital Clock created by Dhiraj !!!")
root.geometry("400x150")
root.resizable(0,0)
text_font= ("Boulder",68,'bold')
background="#f2e750"
foreground="#363529"
border_width=25

label= Label(root,font=text_font,bg=background,fg=foreground,bd=border_width)
label.grid(row=0,column=1)

def digital_clock():
    time_live=time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200,digital_clock)  # for every 200 milliseconds it refreshes

digital_clock()
root.mainloop() # for holding screeen 

