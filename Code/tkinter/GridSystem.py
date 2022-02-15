# -*- coding: utf-8 -*-

from tkinter import *

root = Tk()

# Creating a Label Widget

myLabel1 = Label(root, text="  First Column")
myLabel2 = Label(root, text=" My Name is Dimitar Kuzev")
myLabel3 = Label(root, text="     Column 3")

# Grid System - Table(таблица) Shoving it onto the screen - positions

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)
myLabel3.grid(row=1, column=3)







# Looping
root.mainloop()

