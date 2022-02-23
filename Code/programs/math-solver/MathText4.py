#########################################
# IMPORT

from logging import root
from tkinter import *
from tkinter.ttk import *
from tkinter import font
from PIL import Image, ImageTk
from tkinter import Tk, Frame, Menu, Button
from tkinter import LEFT, TOP, X, FLAT, RAISED
import tkinter.font as font
import sys
import os
from numpy import size


root = Tk()
root.geometry("800x400")
root.title("Kuzev Math Solver")

##########################################
# Menubar
menubar = Menu(root)    
root.config(menu=menubar)


#########################################
# DEFINITIONS 

def  donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()


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
filemenu.add_command(label="Exit", command=donothing)      
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
stylemenu.add_command(label="Math", command=donothing)
stylemenu.add_command(label="Text", command=donothing)
stylemenu.add_command(label="Function", command=donothing)
stylemenu.add_command(label="Variable", command=donothing)
stylemenu.add_command(label="Greek-Symbol", command=donothing)
stylemenu.add_command(label="Vector-Matrix", command=donothing)
stylemenu.add_command(label="User 1", command=donothing)
stylemenu.add_command(label="Untitled", command=donothing)
stylemenu.add_command(label="Untitled", command=donothing)
stylemenu.add_command(label="Untitled", command=donothing)
stylemenu.add_separator()
stylemenu.add_command(label="Other...", command=donothing)
stylemenu.add_command(label="Define...", command=donothing)
# Add Style menu
menubar.add_cascade(label="Style", menu=stylemenu)

########################################################
# Create Size menu

sizemenu = Menu(menubar, tearoff=0)
sizemenu.add_command(label="Full", command=donothing)
sizemenu.add_command(label="Subscript", command=donothing)
sizemenu.add_command(label="Sub-Subscript", command=donothing)
sizemenu.add_command(label="Symbol", command=donothing)
sizemenu.add_command(label="Sub-Siymbol", command=donothing)
sizemenu.add_command(label="User 1", command=donothing)
sizemenu.add_command(label="Other...", command=donothing)
sizemenu.add_separator()
sizemenu.add_command(label="Smaller", command=donothing)
sizemenu.add_command(label="Larger", command=donothing)
sizemenu.add_command(label="Reset Smaller/Larger", command=donothing)
sizemenu.add_separator()
sizemenu.add_command(label="Untitled", command=donothing)
sizemenu.add_command(label="Define...", command=donothing)
# Add Size menu
menubar.add_cascade(label="Size", menu=sizemenu)


########################################################
# Create Preferences menu
prefmenu = Menu(menubar, tearoff=0)
prefmenu.add_command(label="Cut and Copy Preferences", command=donothing)
prefmenu.add_command(label="Web and Gif Preferences", command=donothing)
prefmenu.add_command(label="Functions Recognized", command=donothing)
prefmenu.add_command(label="Workspace Preferences", command=donothing)
prefmenu.add_command(label="Customize Keyboard", command=donothing)
prefmenu.add_command(label="Object Editing Preferences", command=donothing)
prefmenu.add_separator()
prefmenu.add_command(label="Equation Preferences", command=donothing)
# Add Preferences menu
menubar.add_cascade(label="Preferences", menu=prefmenu)


########################################################
# Create Selection menu
selmenu = Menu(menubar, tearoff=0)
selmenu.add_command(label="Select All", command=donothing)
selmenu.add_command(label="Expand Selection", command=donothing)
selmenu.add_command(label="Shrink Selection", command=donothing)
selmenu.add_separator()
selmenu.add_command(label="Copy Line Up", command=donothing)
selmenu.add_command(label="Copy Line Down", command=donothing)
selmenu.add_command(label="Move Line Up", command=donothing)
selmenu.add_command(label="Move Line Down", command=donothing)
selmenu.add_command(label="Duplicate Selection", command=donothing)
selmenu.add_separator()
selmenu.add_command(label="Add Cursoe Above", command=donothing)
selmenu.add_command(label="Add Cursor Below", command=donothing)
selmenu.add_command(label="Add Cursors to Line Ends", command=donothing)
selmenu.add_command(label="Add Next Occurrence", command=donothing)
selmenu.add_command(label="Add Previous Occurrence", command=donothing)
selmenu.add_command(label="Select All Occurrence", command=donothing)
selmenu.add_separator()
selmenu.add_command(label="Untitled", command=donothing)
selmenu.add_command(label="Column Selection Mode", command=donothing)
# Add Selection menu
menubar.add_cascade(label="Selection", menu=selmenu)

########################################################
# Create Go menu
gomenu = Menu(menubar, tearoff=0)
gomenu.add_command(label="1 Untitled 1", command=donothing)
gomenu.add_command(label="1 Untitled 1", command=donothing)
gomenu.add_command(label="1 Untitled 1", command=donothing)
gomenu.add_command(label="1 Untitled 1", command=donothing)
gomenu.add_command(label="1 Untitled 1", command=donothing)
gomenu.add_command(label="1 Untitled 1", command=donothing)
gomenu.add_command(label="1 Untitled 1", command=donothing)
gomenu.add_command(label="1 Untitled 1", command=donothing)
gomenu.add_command(label="1 Untitled 1", command=donothing)
gomenu.add_command(label="1 Untitled 1", command=donothing)
gomenu.add_command(label="1 Untitled 1", command=donothing)
gomenu.add_command(label="1 Untitled 1", command=donothing)
gomenu.add_command(label="1 Untitled 1", command=donothing)
gomenu.add_command(label="1 Untitled 1", command=donothing)
gomenu.add_command(label="1 Untitled 1", command=donothing)
gomenu.add_command(label="1 Untitled 1", command=donothing)
gomenu.add_command(label="1 Untitled 1", command=donothing)
gomenu.add_command(label="1 Untitled 1", command=donothing)
gomenu.add_command(label="1 Untitled 1", command=donothing)
gomenu.add_command(label="1 Untitled 1", command=donothing)
# Add Go menu
menubar.add_cascade(label="Go", menu=gomenu)

########################################################
# Create Run menu
runmenu = Menu(menubar, tearoff=0)
runmenu.add_command(label="1 Untitled 1", command=donothing)
runmenu.add_command(label="1 Untitled 1", command=donothing)
runmenu.add_command(label="1 Untitled 1", command=donothing)
runmenu.add_command(label="1 Untitled 1", command=donothing)
runmenu.add_command(label="1 Untitled 1", command=donothing)
runmenu.add_command(label="1 Untitled 1", command=donothing)
runmenu.add_command(label="1 Untitled 1", command=donothing)
runmenu.add_command(label="1 Untitled 1", command=donothing)
runmenu.add_command(label="1 Untitled 1", command=donothing)
runmenu.add_command(label="1 Untitled 1", command=donothing)
runmenu.add_command(label="1 Untitled 1", command=donothing)
runmenu.add_command(label="1 Untitled 1", command=donothing)
runmenu.add_command(label="1 Untitled 1", command=donothing)
runmenu.add_command(label="1 Untitled 1", command=donothing)
runmenu.add_command(label="1 Untitled 1", command=donothing)
runmenu.add_command(label="1 Untitled 1", command=donothing)
# Add Run menu
menubar.add_cascade(label="Run", menu=runmenu)

########################################################
# Create Terminal menu
termenu = Menu(menubar, tearoff=0)
termenu.add_command(label="1 Untitled 1", command=donothing)
termenu.add_command(label="1 Untitled 1", command=donothing)
termenu.add_command(label="1 Untitled 1", command=donothing)
termenu.add_command(label="1 Untitled 1", command=donothing)
termenu.add_command(label="1 Untitled 1", command=donothing)
termenu.add_command(label="1 Untitled 1", command=donothing)
termenu.add_command(label="1 Untitled 1", command=donothing)
termenu.add_command(label="1 Untitled 1", command=donothing)
termenu.add_command(label="1 Untitled 1", command=donothing)
termenu.add_command(label="1 Untitled 1", command=donothing)
termenu.add_command(label="1 Untitled 1", command=donothing) 
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
insertmenu.add_command(label="1 Untitled 1", command=donothing)
insertmenu.add_command(label="1 Untitled 1", command=donothing)
insertmenu.add_command(label="1 Untitled 1", command=donothing)
insertmenu.add_command(label="1 Untitled 1", command=donothing)
insertmenu.add_command(label="1 Untitled 1", command=donothing)
insertmenu.add_command(label="1 Untitled 1", command=donothing)
insertmenu.add_command(label="1 Untitled 1", command=donothing)
insertmenu.add_command(label="1 Untitled 1", command=donothing)
insertmenu.add_command(label="1 Untitled 1", command=donothing)
insertmenu.add_command(label="1 Untitled 1", command=donothing)
insertmenu.add_command(label="1 Untitled 1", command=donothing)
insertmenu.add_command(label="1 Untitled 1", command=donothing)
insertmenu.add_command(label="1 Untitled 1", command=donothing)
insertmenu.add_command(label="1 Untitled 1", command=donothing)
insertmenu.add_command(label="1 Untitled 1", command=donothing)
insertmenu.add_command(label="1 Untitled 1", command=donothing)
insertmenu.add_command(label="1 Untitled 1", command=donothing)
insertmenu.add_command(label="1 Untitled 1", command=donothing)
insertmenu.add_command(label="1 Untitled 1", command=donothing)
insertmenu.add_command(label="1 Untitled 1", command=donothing)
insertmenu.add_command(label="1 Untitled 1", command=donothing)
insertmenu.add_command(label="1 Untitled 1", command=donothing)
insertmenu.add_command(label="1 Untitled 1", command=donothing)
insertmenu.add_command(label="1 Untitled 1", command=donothing)
insertmenu.add_command(label="1 Untitled 1", command=donothing)
insertmenu.add_command(label="1 Untitled 1", command=donothing)
insertmenu.add_command(label="1 Untitled 1", command=donothing)
# Add Insert menu
menubar.add_cascade(label="Insert", menu=insertmenu)


########################################################
# Create Symbol menu
symbolmenu = Menu(menubar, tearoff=0)
symbolmenu.add_command(label="1 Untitled 1", command=donothing)
symbolmenu.add_command(label="1 Untitled 1", command=donothing)
symbolmenu.add_command(label="1 Untitled 1", command=donothing)
symbolmenu.add_command(label="1 Untitled 1", command=donothing)
# Add Symbol menu
menubar.add_cascade(label="Symbols", menu=symbolmenu)


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


####################################################
# Toolbar Definitions

def submenu1():
    submenu1 = Menu(toolbar, tearoff=0).pack()
    submenu1.add_command()






############################################
# Create Font object
# myFont = font.Font(family='Helvetica', size=20)

################################################
# Create 9 in 1 toolbar...


####  IMAGE ON BUTTON  ####################
# here, image option is used to
# set image on button
# Button(root, text = 'Click Me !', image = photo).pack(side = TOP)
# Creating a photoimage object to use image
# eimg = PhotoImage(file = r"D:\Code\tkinter\icon\fraction\2-fractions.gif")
# img1 = PhotoImage(file = r"D:\Code\tkinter\icon\Symbol Palettes\relational_symbols.gif")
# img1.resize((50, 50), Image.ANTIALIAS)
# Resize image to fit on button
# img1.subsample(1, 2)

# Image Toolbar
img1 = PhotoImage(file = r"D:\Code\programs\math-solver\icon\Symbol Palettes\A1-relational_symbols.gif")
img2 = PhotoImage(file = r"D:\Code\programs\math-solver\icon\Symbol Palettes\A2-spaces.gif")
img3 = PhotoImage(file = r"D:\Code\programs\math-solver\icon\Symbol Palettes\A3-embellishments.gif")
img4 = PhotoImage(file = r"D:\Code\programs\math-solver\icon\Symbol Palettes\A4-operators.gif")
img5 = PhotoImage(file = r"D:\Code\programs\math-solver\icon\Symbol Palettes\A5-arrows.gif")
img6 = PhotoImage(file = r"D:\Code\programs\math-solver\icon\Symbol Palettes\A6-logic.gif")
img7 = PhotoImage(file = r"D:\Code\programs\math-solver\icon\Symbol Palettes\A7-sets.gif")
img8 = PhotoImage(file = r"D:\Code\programs\math-solver\icon\Symbol Palettes\A8-misc.gif")
img9 = PhotoImage(file = r"D:\Code\programs\math-solver\icon\Symbol Palettes\A9-lc_greek.gif")
img10 = PhotoImage(file = r"D:\Code\programs\math-solver\icon\Symbol Palettes\A10-uc_greek.gif")



####################################################
# FONT BUTTONS - Toolbar
# toolFont = font.Font(family='Helvetica', size=10)

# Toolbar 
toolbar = Frame(root, bd=1, relief=RAISED) 
toolbar.pack(side=TOP, fill=X)

btn1 = Button(toolbar, relief=FLAT, compound= LEFT, text="",image=img1, command=submenu1)
# btn1['font'] = toolFont
btn1.pack(side=LEFT, padx=0, pady=0)

btn2 = Button(toolbar, relief=FLAT, compound= LEFT, text="", image=img2, command=donothing)
# btn2['font'] = toolFont
btn2.pack(side=LEFT, padx=0, pady=0)

btn3 = Button(toolbar, relief=FLAT, compound= LEFT, text="", image=img3, command=donothing)
# btn3['font'] = toolFont
btn3.pack(side=LEFT, padx=0, pady=0)

btn4 = Button(toolbar, relief=FLAT, compound= LEFT, text="", image=img4, command=donothing)
# btn4['font'] = toolFont
btn4.pack(side=LEFT, padx=0, pady=0)

btn5 = Button(toolbar, relief=FLAT, compound= LEFT, text="", image=img5, command=donothing)
# btn5['font'] = toolFont
btn5.pack(side=LEFT, padx=0, pady=0)

btn6 = Button(toolbar, relief=FLAT, compound= LEFT, text="", image=img6, command=donothing)
# btn6['font'] = toolFont
btn6.pack(side=LEFT, padx=0, pady=0)

btn7 = Button(toolbar, relief=FLAT, compound= LEFT, text="", image=img7, command=donothing)
# btn7['font'] = toolFont
btn7.pack(side=LEFT, padx=0, pady=0)

btn8 = Button(toolbar, relief=FLAT, compound= LEFT, text="", image=img8, command=donothing)
# btn8['font'] = toolFont
btn8.pack(side=LEFT, padx=0, pady=0)

btn9 = Button(toolbar, relief=FLAT, compound= LEFT, text="",image=img9, command=donothing)
# btn9['font'] = toolFont
btn9.pack(side=LEFT, padx=0, pady=0)

btn10 = Button(toolbar, relief=FLAT, compound= LEFT, text="",image=img10, command=donothing)
# btn10['font'] = toolFont
btn10.pack(side=LEFT, padx=0, pady=0)

root.config(menu=menubar)

# Image Toolbar#
img11 = PhotoImage(file = r"D:\Code\programs\math-solver\icon\Template Palettes\B1-fences.gif")
img12 = PhotoImage(file = r"D:\Code\programs\math-solver\icon\Template Palettes\B2-fractions.gif")
img13 = PhotoImage(file = r"D:\Code\programs\math-solver\icon\Template Palettes\B3-subscripts.gif")
img14 = PhotoImage(file = r"D:\Code\programs\math-solver\icon\Template Palettes\B4-summations.gif")
img15 = PhotoImage(file = r"D:\Code\programs\math-solver\icon\Template Palettes\B5-integrals.gif")
img16 = PhotoImage(file = r"D:\Code\programs\math-solver\icon\Template Palettes\B6-overbars.gif")
img17 = PhotoImage(file = r"D:\Code\programs\math-solver\icon\Template Palettes\B7-labeled_arrows.gif")
img18 = PhotoImage(file = r"D:\Code\programs\math-solver\icon\Template Palettes\B8-products.gif")
img19 = PhotoImage(file = r"D:\Code\programs\math-solver\icon\Template Palettes\B9-matrices.gif")
img20 = PhotoImage(file = r"D:\Code\programs\math-solver\icon\Template Palettes\B10-box_templates.gif")


####################################################
# FONT BUTTONS - Toolbar 1
# myFont = font.Font(family='Helvetica', size=20)

# Toolbar 1

toolbar1 = Frame(root, bd=1, relief=RAISED)
toolbar1.pack(side=TOP, fill=X)

btn01 = Button(toolbar1, relief=FLAT, compound= LEFT, text="", image=img11, command=donothing)
btn01.pack(side=LEFT, padx=0, pady=0)

btn02 = Button(toolbar1, relief=FLAT, compound= LEFT, text="",image=img12, command=donothing)
btn02.pack(side=LEFT, padx=0, pady=0)

btn03 = Button(toolbar1, relief=FLAT, compound= LEFT, text="",image=img13, command=donothing)
btn03.pack(side=LEFT, padx=0, pady=0)

btn04 = Button(toolbar1, relief=FLAT, compound= LEFT, text="",image=img14, command=donothing)
btn04.pack(side=LEFT, padx=0, pady=0)

btn05 = Button(toolbar1, relief=FLAT, compound= LEFT, text="",image=img15, command=donothing)
btn05.pack(side=LEFT, padx=0, pady=0)

btn06 = Button(toolbar1, relief=FLAT, compound= LEFT, text="",image=img16, command=donothing)
btn06.pack(side=LEFT, padx=0, pady=0)

btn07 = Button(toolbar1, relief=FLAT, compound= LEFT, text="",image=img17, command=donothing)
btn07.pack(side=LEFT, padx=0, pady=0)

btn08 = Button(toolbar1, relief=FLAT, compound= LEFT, text="",image=img18, command=donothing)
btn08.pack(side=LEFT, padx=0, pady=0)

btn09 = Button(toolbar1, relief=FLAT, compound= LEFT, text="",image=img19, command=donothing)
btn09.pack(side=LEFT, padx=0, pady=0)

btn010 = Button(toolbar1, relief=FLAT, compound= LEFT, text="",image=img20, command=donothing)
btn010.pack(side=LEFT, padx=0, pady=0)

toolbar1.pack(side=TOP, fill=X)
root.config(menu=menubar)
       
# Toolbar 3

toolbar3 = Frame(root, bd=1, relief=RAISED)
toolbar3.pack(side=TOP, fill=X)

btn17 = Button(toolbar3, relief=FLAT, compound= LEFT, text="Algebra", command=donothing)
btn17.pack(side=LEFT, padx=0, pady=0)

btn18 = Button(toolbar3, relief=FLAT, compound= LEFT, text="Derivs", command=donothing)
btn18.pack(side=LEFT, padx=0, pady=0)

btn19 = Button(toolbar3, relief=FLAT, compound= LEFT, text="Statistics", command=donothing)
btn19.pack(side=LEFT, padx=0, pady=0)

btn20 = Button(toolbar3, relief=FLAT, compound= LEFT, text="Matrices", command=donothing)
btn20.pack(side=LEFT, padx=0, pady=0)

btn21 = Button(toolbar3, relief=FLAT, compound= LEFT, text="Sets", command=donothing)
btn21.pack(side=LEFT, padx=0, pady=0)

btn22 = Button(toolbar3, relief=FLAT, compound= LEFT, text="Trig", command=donothing)
btn22.pack(side=LEFT, padx=0, pady=0)

btn23 = Button(toolbar3, relief=FLAT, compound= LEFT, text="Geometry", command=donothing)
btn23.pack(side=LEFT, padx=0, pady=0)

btn24 = Button(toolbar3, relief=FLAT, compound= LEFT, text="Tab 8", command=donothing)
btn24.pack(side=LEFT, padx=0, pady=0)

btn25 = Button(toolbar3, relief=FLAT, compound= LEFT, text="Tab 9", command=donothing)
btn25.pack(side=LEFT, padx=0, pady=0)

root.config(menu=menubar)  

# Toolbar 4

# Image Toolbar 4
imgpar = PhotoImage(file = r"D:\Code\programs\math-solver\icon\Fence templates\parentheses.gif")
imgbrac = PhotoImage(file = r"D:\Code\programs\math-solver\icon\Fence templates\brackets.gif")

toolbar4 = Frame(root, bd=1, relief=RAISED)
toolbar4.pack(side=TOP, fill=X)

b1 = Button(toolbar4, relief=FLAT, compound= LEFT, text="π", command=donothing)
# b1['font'] = myFont
b1.pack(side=LEFT, padx=0, pady=0)

b2 = Button(toolbar4, relief=FLAT, compound= LEFT, text="θ", command=donothing)
# b2['font'] = myFont
b2.pack(side=LEFT, padx=0, pady=0)

b3 = Button(toolbar4, relief=FLAT, compound= LEFT, text="∞", command=donothing)
# b3['font'] = myFont
b3.pack(side=LEFT, padx=0, pady=0)

b4 = Button(toolbar4, relief=FLAT, compound= LEFT, text="∈", command=donothing)
# b4['font'] = myFont
b4.pack(side=LEFT, padx=0, pady=0)

b5 = Button(toolbar4, relief=FLAT, compound= LEFT, text="→", command=donothing)
b5.pack(side=LEFT, padx=0, pady=0)

b6 = Button(toolbar4, relief=FLAT, compound= LEFT, text="new", command=donothing)
b6.pack(side=LEFT, padx=0, pady=0)

b7 = Button(toolbar4, relief=FLAT, compound= LEFT, text="≤", command=donothing)
b7.pack(side=LEFT, padx=0, pady=0)

b8 = Button(toolbar4, relief=FLAT, compound= LEFT, text="≠", command=donothing)
b8.pack(side=LEFT, padx=0, pady=0)

b9 = Button(toolbar4, relief=FLAT, compound= LEFT, text="±", command=donothing)
b9.pack(side=LEFT, padx=0, pady=0)

b10 = Button(toolbar4, relief=FLAT, compound= LEFT, text="",image=imgpar, command=donothing)
b10.pack(side=LEFT, padx=0, pady=0)

b11 = Button(toolbar4, relief=FLAT, compound= LEFT, text="",image=imgbrac, command=donothing)
b11.pack(side=LEFT, padx=0, pady=0)

b12 = Button(toolbar4, relief=FLAT, compound= LEFT, text="new", command=donothing)
b12.pack(side=LEFT, padx=0, pady=0)

b13 = Button(toolbar4, relief=FLAT, compound= LEFT, text="new", command=donothing)
b13.pack(side=LEFT, padx=0, pady=0)

b14 = Button(toolbar4, relief=FLAT, compound= LEFT, text="new", command=donothing)
b14.pack(side=LEFT, padx=0, pady=0)

b15 = Button(toolbar4, relief=FLAT, compound= LEFT, text="new", command=donothing)
b15.pack(side=LEFT, padx=0, pady=0)

b16 = Button(toolbar4, relief=FLAT, compound= LEFT, text="new", command=donothing)
b16.pack(side=LEFT, padx=0, pady=0)

b17 = Button(toolbar4, relief=FLAT, compound= LEFT, text="new", command=donothing)
b17.pack(side=LEFT, padx=0, pady=0)

b18 = Button(toolbar4, relief=FLAT, compound= LEFT, text="new", command=donothing)
b18.pack(side=LEFT, padx=0, pady=0)

b19 = Button(toolbar4, relief=FLAT, compound= LEFT, text="new", command=donothing)
b19.pack(side=LEFT, padx=0, pady=0)

b20 = Button(toolbar4, relief=FLAT, compound= LEFT, text="new", command=donothing)
b20.pack(side=LEFT, padx=0, pady=0)

root.config(menu=menubar)

# Toolbar 5

toolbar5 = Frame(root, bd=1, relief=RAISED)
toolbar5.pack(side=TOP, fill=X)

b21 = Button(toolbar5, relief=FLAT, compound= LEFT, text="√", command=donothing)
# b21['font'] = myFont
b21.pack(side=LEFT, padx=0, pady=0)

b22 = Button(toolbar5, relief=FLAT, compound= LEFT, text="⊏", command=donothing)
# b22['font'] = myFont
b22.pack(side=LEFT, padx=0, pady=0)

b23 = Button(toolbar5, relief=FLAT, compound= LEFT, text="⬚", command=donothing)
# b23['font'] = myFont
b23.pack(side=LEFT, padx=0, pady=0)

b24 = Button(toolbar5, relief=FLAT, compound= LEFT, text="", command=donothing)
# b24['font'] = myFont
b24.pack(side=LEFT, padx=0, pady=0)

b25 = Button(toolbar5, relief=FLAT, compound= LEFT, text="new", command=donothing)
b25.pack(side=LEFT, padx=0, pady=0)

b26 = Button(toolbar5, relief=FLAT, compound= LEFT, text="new", command=donothing)
b26.pack(side=LEFT, padx=0, pady=0)

b27 = Button(toolbar5, relief=FLAT, compound= LEFT, text="new", command=donothing)
b27.pack(side=LEFT, padx=0, pady=0)

b28 = Button(toolbar5, relief=FLAT, compound= LEFT, text="new", command=donothing)
b28.pack(side=LEFT, padx=0, pady=0)

b29 = Button(toolbar5, relief=FLAT, compound= LEFT, text="new", command=donothing)
b29.pack(side=LEFT, padx=0, pady=0)

b30 = Button(toolbar5, relief=FLAT, compound= LEFT, text="new", command=donothing)
b30.pack(side=LEFT, padx=0, pady=0)

root.config(menu=menubar)

# Toolbar 6

toolbar6 = Frame(root, bd=1, relief=RAISED)
toolbar6.pack(side=TOP, fill=X)

btn001 = Button(toolbar6, relief=FLAT, compound= LEFT, text="√", command=donothing)
btn001.pack(side=LEFT, padx=0, pady=0)

btn002 = Button(toolbar6, relief=FLAT, compound= LEFT, text="⊏", command=donothing)
btn002.pack(side=LEFT, padx=0, pady=0)

btn003 = Button(toolbar6, relief=FLAT, compound= LEFT, text="⬚", command=donothing)
btn003.pack(side=LEFT, padx=0, pady=0)

btn004 = Button(toolbar6, relief=FLAT, compound= LEFT, text="", command=donothing)
btn004.pack(side=LEFT, padx=0, pady=0)

btn005 = Button(toolbar6, relief=FLAT, compound= LEFT, text="new", command=donothing)
btn005.pack(side=LEFT, padx=0, pady=0)

btn006 = Button(toolbar6, relief=FLAT, compound= LEFT, text="new", command=donothing)
btn006.pack(side=LEFT, padx=0, pady=0)

btn007 = Button(toolbar6, relief=FLAT, compound= LEFT, text="new", command=donothing)
btn007.pack(side=LEFT, padx=0, pady=0)

btn008 = Button(toolbar6, relief=FLAT, compound= LEFT, text="new", command=donothing)
btn008.pack(side=LEFT, padx=0, pady=0)

btn009 = Button(toolbar6, relief=FLAT, compound= LEFT, text="new", command=donothing)
btn009.pack(side=LEFT, padx=0, pady=0)

btn0010 = Button(toolbar6, relief=FLAT, compound= LEFT, text="new", command=donothing)
btn0010.pack(side=LEFT, padx=0, pady=0)

root.config(menu=menubar)




















root.mainloop()