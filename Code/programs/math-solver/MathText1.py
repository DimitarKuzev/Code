#########################################
# IMPORT

from logging import root
from tkinter import *
from PIL import Image, ImageTk
from click import command
import glob
import os

from matplotlib.pyplot import text


#########################################
# DEFINITIONS 

def  donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()
    
##########################################
# MENU

root = Tk()
root.geometry("400x400")
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

############################################
# TOOLBAR

toolbar = Frame(root)
toolbar.pack(side=TOP, fill=X)

b1 = Button(toolbar, relief=FLAT, compound= LEFT, text="new", command=donothing)
b1.pack(side=LEFT, padx=0, pady=0)

b2 = Button(toolbar, relief=FLAT, compound= LEFT, text="new", command=donothing)
b2.pack(side=LEFT, padx=0, pady=0)

b3 = Button(toolbar, relief=FLAT, compound= LEFT, text="new", command=donothing)
b3.pack(side=LEFT, padx=0, pady=0)

b4 = Button(toolbar, relief=FLAT, compound= LEFT, text="new", command=donothing)
b4.pack(side=LEFT, padx=0, pady=0)

b5 = Button(toolbar, relief=FLAT, compound= LEFT, text="new", command=donothing)
b5.pack(side=LEFT, padx=0, pady=0)

b6 = Button(toolbar, relief=FLAT, compound= LEFT, text="new", command=donothing)
b6.pack(side=LEFT, padx=0, pady=0)

b7 = Button(toolbar, relief=FLAT, compound= LEFT, text="new", command=donothing)
b7.pack(side=LEFT, padx=0, pady=0)

root.config(menu=menubar)
root.mainloop()