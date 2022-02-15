# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()
#, bg="blue", fg="white", borderwidth=5
e.insert(0, "Напиши задача: ")


def myClick():
    calc = "Решението е: " + e.get()
    myLabel = Label(root, text=calc)
    myLabel.pack()
    
myButton = Button(root, text="Реши", command= myClick)
myButton.pack()


root.mainloop()
