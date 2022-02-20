#########################################
# IMPORT

from logging import root
from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
import glob
import os
import tkinter.font as font
from matplotlib.pyplot import text

#########################################
# DEFINITIONS 

def  donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()
    


root = Tk()
root.geometry("800x400")

##########################################
# MENU

##########################################
# Menubar

menubar = Menu(root)
###########################################
# Create File menu

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open...", command=donothing)
filemenu.add_command(label="Close", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Print", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
# Add file menu
menubar.add_cascade(label="File", menu=filemenu)

##############################################
# Create Edit menu

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo Template", command=donothing)
editmenu.add_command(label="Undo", command=donothing)
editmenu.add_command(label="Can't Redo", command=donothing)
editmenu.add_separator()
editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Clear", command=donothing)
editmenu.add_separator()
editmenu.add_command(label="Insert Symbol...", command=donothing)
editmenu.add_command(label="Open Math Input Panel...", command=donothing)
editmenu.add_command(label="Select All", command=donothing)
# Add Edit menu
menubar.add_cascade(label="Edit", menu=editmenu)

################################################
# Create View menu

viewmenu = Menu(menubar, tearoff=0)
viewmenu.add_command(label="Zoom", command=donothing)
viewmenu.add_command(label="Show All", command=donothing)
viewmenu.add_command(label="Show Nesting.", command=donothing)
viewmenu.add_separator()
viewmenu.add_command(label="Symbol Palettes", command=donothing)
viewmenu.add_command(label="Template Palettes", command=donothing)
viewmenu.add_command(label="Small Bar", command=donothing)
viewmenu.add_command(label="Large Tabbed Bar", command=donothing)
viewmenu.add_command(label="Small Tabbed Bar", command=donothing)
viewmenu.add_separator()
viewmenu.add_command(label="Toolbar", command=donothing)
viewmenu.add_command(label="Ruler", command=donothing)
viewmenu.add_separator()
viewmenu.add_command(label="View in Wolfram Alpha", command=donothing)
viewmenu.add_separator()
viewmenu.add_command(label="1 Untitled 1", command=donothing)
viewmenu.add_separator()
# Add View menu
menubar.add_cascade(label="View", menu=viewmenu)

###################################################
# Create Format menu

formatmenu = Menu(menubar, tearoff=0)
formatmenu.add_command(label="Zoom", command=donothing)
formatmenu.add_command(label="Show All", command=donothing)
formatmenu.add_command(label="Show Nesting.", command=donothing)
formatmenu.add_command(label="Symbol Palettes", command=donothing)
formatmenu.add_command(label="Template Palettes", command=donothing)
formatmenu.add_separator()
formatmenu.add_command(label="Small Bar", command=donothing)
formatmenu.add_command(label="Large Tabbed Bar", command=donothing)
formatmenu.add_command(label="Small Tabbed Bar", command=donothing)
formatmenu.add_separator()
formatmenu.add_command(label="Toolbar", command=donothing)
formatmenu.add_command(label="Ruler", command=donothing)
formatmenu.add_command(label="Toolbar", command=donothing)
formatmenu.add_command(label="Ruler", command=donothing)
formatmenu.add_command(label="Toolbar", command=donothing)
formatmenu.add_command(label="Ruler", command=donothing)
formatmenu.add_separator()
formatmenu.add_command(label="View in Wolfram Alpha", command=donothing)
formatmenu.add_separator()
formatmenu.add_command(label="1 Untitled 1", command=donothing)
formatmenu.add_command(label="1 Untitled 1", command=donothing)
formatmenu.add_command(label="1 Untitled 1", command=donothing)
formatmenu.add_command(label="1 Untitled 1", command=donothing)
formatmenu.add_separator()
formatmenu.add_command(label="1 Untitled 1", command=donothing)
formatmenu.add_command(label="1 Untitled 1", command=donothing)
# Add Format menu
menubar.add_cascade(label="Format", menu=formatmenu)

########################################################
# Create Style menu

stylemenu = Menu(menubar, tearoff=0)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_separator()
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
# Add Style menu
menubar.add_cascade(label="Style", menu=stylemenu)

########################################################
# Create Size menu

sizemenu = Menu(menubar, tearoff=0)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_separator()
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
# Add Size menu
menubar.add_cascade(label="Style", menu=sizemenu)


########################################################
# Create Preferences menu
prefmenu = Menu(menubar, tearoff=0)
prefmenu.add_command(label="1 Untitled 1", command=donothing)
prefmenu.add_command(label="1 Untitled 1", command=donothing)
prefmenu.add_command(label="1 Untitled 1", command=donothing)
prefmenu.add_command(label="1 Untitled 1", command=donothing)
prefmenu.add_command(label="1 Untitled 1", command=donothing)
prefmenu.add_command(label="1 Untitled 1", command=donothing)
prefmenu.add_command(label="1 Untitled 1", command=donothing)
# Add Preferences menu
menubar.add_cascade(label="Preferences", menu=prefmenu)


########################################################
# Create Selection menu
stylemenu = Menu(menubar, tearoff=0)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_separator()
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
# Add Selection menu
menubar.add_cascade(label="Style", menu=stylemenu)

########################################################
# Create Go menu
stylemenu = Menu(menubar, tearoff=0)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
# Add Go menu
menubar.add_cascade(label="Style", menu=stylemenu)

########################################################
# Create Run menu
stylemenu = Menu(menubar, tearoff=0)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
# Add Run menu
menubar.add_cascade(label="Style", menu=stylemenu)

########################################################
# Create Terminal menu
termenu = Menu(menubar, tearoff=0)
termenu.add_command(label="1 Untitled 1", command=donothing)
termenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing) 
# Add Terminal menu 
menubar.add_cascade(label="Terminal", menu=termenu)


##########################################################
# Create Solver menu

solvermenu = Menu(menubar, tearoff=0)
solvermenu.add_command(label="Solve", command=donothing)
solvermenu.add_command(label="Lessons", command=donothing)
solvermenu.add_command(label="Practice", command=donothing)
# Add solver menu
menubar.add_cascade(label="Solver", menu=solvermenu)

########################################################
# Create Insert menu
insertmenu = Menu(menubar, tearoff=0)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
# Add Insert menu
menubar.add_cascade(label="Insert", menu=insertmenu)


########################################################
# Create Symbol menu
stylemenu = Menu(menubar, tearoff=0)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
stylemenu.add_command(label="1 Untitled 1", command=donothing)
# Add Symbol menu
menubar.add_cascade(label="Symbols", menu=stylemenu)


########################################################
# Create Equation menu

equationmenu = Menu(menubar, tearoff=0)
equationmenu.add_command(label="1 Untitled 1", command=donothing)
equationmenu.add_command(label="1 Untitled 1", command=donothing)
equationmenu.add_command(label="1 Untitled 1", command=donothing)
equationmenu.add_command(label="1 Untitled 1", command=donothing)
# Add Equation menu
menubar.add_cascade(label="Equation", menu=equationmenu)


########################################################
# Create Encodeng menu

encodingmenu = Menu(menubar, tearoff=0)
encodingmenu.add_command(label="ANSI", command=donothing)
encodingmenu.add_command(label="Unicode", command=donothing)
encodingmenu.add_command(label="Unicode Big Endian", command=donothing)
encodingmenu.add_command(label="UTF-8", command=donothing)
encodingmenu.add_command(label="UTF-8 with Signature", command=donothing)
encodingmenu.add_command(label="Recode", command=donothing)
encodingmenu.add_command(label="Default..", command=donothing)
encodingmenu.add_command(label="More...", command=donothing)
# Add Encoding menu
menubar.add_cascade(label="Encoding", menu=encodingmenu)


########################################################
# Create Character menu

charmenu = Menu(menubar, tearoff=0)
charmenu.add_command(label="Unicode Character Table", command=donothing)
charmenu.add_command(label="ASCII Table", command=donothing)
charmenu.add_command(label="Approved Special Characters", command=donothing)
charmenu.add_command(label="Character Symbols", command=donothing)
# Add Character menu
menubar.add_cascade(label="Character Tables", menu=charmenu)


############################################################
# Create Help menu

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
# Add Help menu
menubar.add_cascade(label="Help", menu=helpmenu)









































############################################

############################################
# Create Font object
myFont = font.Font(family='Helvetica', size=30)

# Creating a photoimage object to use image
photo = PhotoImage(file = r"D:\Code\tkinter\icon\fraction\2-fractions.gif")

####  IMAGE ON BUTTON  ####################
# here, image option is used to
# set image on button
# Button(root, text = 'Click Me !', image = photo).pack(side = TOP)
# TOOLBAR

################################################
# Create 6 toolbar...



toolbar = Frame(root)
toolbar.pack(side=TOP, fill=X)

b1 = Button(toolbar, relief=FLAT, compound= LEFT, text="√", command=donothing)
b1['font'] = myFont
b1.pack(side=LEFT, padx=0, pady=0)

b2 = Button(toolbar, relief=FLAT, compound= LEFT, text="⊏", command=donothing)
b2['font'] = myFont
b2.pack(side=LEFT, padx=0, pady=0)

b3 = Button(toolbar, relief=FLAT, compound= LEFT, text="⬚", command=donothing)
b3['font'] = myFont
b3.pack(side=LEFT, padx=0, pady=0)

b4 = Button(toolbar, relief=FLAT, compound= LEFT, text="", image=photo, command=donothing)
b4['font'] = myFont
b4.pack(side=LEFT, padx=0, pady=0)

b5 = Button(toolbar, relief=FLAT, compound= LEFT, text="new", command=donothing)
b5.pack(side=LEFT, padx=0, pady=0)

b6 = Button(toolbar, relief=FLAT, compound= LEFT, text="new", command=donothing)
b6.pack(side=LEFT, padx=0, pady=0)

b7 = Button(toolbar, relief=FLAT, compound= LEFT, text="new", command=donothing)
b7.pack(side=LEFT, padx=0, pady=0)

b8 = Button(toolbar, relief=FLAT, compound= LEFT, text="new", command=donothing)
b8.pack(side=LEFT, padx=0, pady=0)

b9 = Button(toolbar, relief=FLAT, compound= LEFT, text="new", command=donothing)
b9.pack(side=LEFT, padx=0, pady=0)

b10 = Button(toolbar, relief=FLAT, compound= LEFT, text="new", command=donothing)
b10.pack(side=LEFT, padx=0, pady=0)


toolbar1 = Frame(root, bd=1, relief=RAISED)
toolbar1.pack(side=TOP, fill=X)

b11 = Button(toolbar, relief=FLAT, compound= LEFT, text="√", command=donothing)
b11['font'] = myFont
b11.pack(side=LEFT, padx=0, pady=0)

b12 = Button(toolbar, relief=FLAT, compound= LEFT, text="⊏", command=donothing)
b12['font'] = myFont
b12.pack(side=LEFT, padx=0, pady=0)

b13 = Button(toolbar, relief=FLAT, compound= LEFT, text="⬚", command=donothing)
b13['font'] = myFont
b13.pack(side=LEFT, padx=0, pady=0)

b14 = Button(toolbar, relief=FLAT, compound= LEFT, text="", image=photo, command=donothing)
b14['font'] = myFont
b14.pack(side=LEFT, padx=0, pady=0)

b15 = Button(toolbar, relief=FLAT, compound= LEFT, text="new", command=donothing)
b15.pack(side=LEFT, padx=0, pady=0)

b16 = Button(toolbar, relief=FLAT, compound= LEFT, text="new", command=donothing)
b16.pack(side=LEFT, padx=0, pady=0)

b17 = Button(toolbar, relief=FLAT, compound= LEFT, text="new", command=donothing)
b17.pack(side=LEFT, padx=0, pady=0)

b18 = Button(toolbar, relief=FLAT, compound= LEFT, text="new", command=donothing)
b18.pack(side=LEFT, padx=0, pady=0)

b19 = Button(toolbar, relief=FLAT, compound= LEFT, text="new", command=donothing)
b19.pack(side=LEFT, padx=0, pady=0)

b20 = Button(toolbar, relief=FLAT, compound= LEFT, text="new", command=donothing)
b20.pack(side=LEFT, padx=0, pady=0)



root.config(menu=menubar)


root.mainloop()