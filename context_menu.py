
from tkinter import *

#create window

root=Tk()
root.geometry("250x250")
root.title("Context menu")

# create Text box
text= Text(root,font=("haveltica 15 bold"),bd=2)
text.focus()
text.pack()

# define function to cut the selected text

def cut_text():
    text.event_generate(("<<Cut>>"))

# define function to copy the selected text
def copy_text():
    text.event_generate(("<<Copy>>"))

# define function to paste the previously selected text

def paste_text():
    text.event_generate(("<<Paste>>"))

# create menubar

menu = Menu(root,tearoff=0)
menu.add_command(label="Cut",command=cut_text)
menu.add_command(label="Copy",command=copy_text)
menu.add_command(label="Paste",command=paste_text)
menu.add_separator()
menu.add_command(label="Exit",command=root.destroy)

# define function to popup the context menu on right button click

def context_menu(event):
    try:
        menu.tk_popup(event.x_root,event.y_root)
    finally:
        menu.grab_release()

    
# binding right click button to root

root.bind("<Button-3>",context_menu)
root.mainloop()



