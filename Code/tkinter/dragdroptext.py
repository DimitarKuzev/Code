# create windows
from logging import root
from tkinter import *

from django.forms import Textarea


root = Tk()

# functions

def show_text(event):
    Textarea.delete("1.0", "end")
    if event.data.endswith(".txt"):
        with open(event.data, "r") as file:
            for line in file:
                line=line.strip()
                Textarea.insert("end",f"{line}\n")
    

ws = TkinterDnD.Tk()
ws.title()



# Label
myLabel = Label(root, text="")


# Label Grid System
myLabel.grid(row=0,column=0)



# Buttons 
myButtons = Button()



# Button Grid System

root.mainloop()