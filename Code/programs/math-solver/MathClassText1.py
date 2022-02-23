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

#########################################
# CLASS

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Kuzev Math Solver")
        ##########################################
        # Menubar
        menubar = Menu(self.master)    
        self.master.config(menu=menubar)


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
        filemenu.add_command(label="Exit", command=self.onExit)
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

        ############################################
        # Create Font object
        myFont = font.Font(family='Helvetica', size=30)

        ################################################
        # Create 6 in 1 toolbar...
        toolbar = Frame(self.master, bd=1, relief=RAISED) 

        ####  IMAGE ON BUTTON  ####################
        # here, image option is used to
        # set image on button
        # Button(root, text = 'Click Me !', image = photo).pack(side = TOP)
        # Creating a photoimage object to use image
        # eimg = PhotoImage(file = r"D:\Code\tkinter\icon\fraction\2-fractions.gif")
        img1 = PhotoImage(file = r"D:\Code\tkinter\icon\Symbol Palettes\relational_symbols.gif")
        # img1.resize((50, 50), Image.ANTIALIAS)
        # Resize image to fit on button
        # img1.subsample(1, 2)
        
        
        
        
        # ИКОНИТЕ ТУК НЕ СЕ ПОКАЗВАТ ПРАВИЛНО.
        # БЕЗ КЛАСА СЕ ПОКАЗВАТ ПРАВИЛНО



        
        b1 = Button(toolbar, compound= LEFT, text=" ",image=img1, command=donothing)
        b1.pack(side=LEFT, padx=0, pady=0)

        b2 = Button(toolbar, relief=FLAT, compound= LEFT, text="⊏", command=donothing)
        b2['font'] = myFont
        b2.pack(side=LEFT, padx=0, pady=0)

        b3 = Button(toolbar, relief=FLAT, compound= LEFT, text="⬚", command=donothing)
        b3['font'] = myFont
        b3.pack(side=LEFT, padx=0, pady=0)

        b4 = Button(toolbar, relief=FLAT, compound= LEFT, text="", command=donothing)
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


        toolbar1 = Frame(self.master, bd=1, relief=RAISED)
        toolbar1.pack(side=TOP, fill=X)

        b11 = Button(toolbar1, relief=FLAT, compound= LEFT, text="√", command=donothing)
        b11['font'] = myFont
        b11.pack(side=LEFT, padx=0, pady=0)

        b12 = Button(toolbar1, relief=FLAT, compound= LEFT, text="⊏", command=donothing)
        b12['font'] = myFont
        b12.pack(side=LEFT, padx=0, pady=0)

        b13 = Button(toolbar1, relief=FLAT, compound= LEFT, text="⬚", command=donothing)
        b13['font'] = myFont
        b13.pack(side=LEFT, padx=0, pady=0)

        b14 = Button(toolbar1, relief=FLAT, compound= LEFT, text="", command=donothing)
        b14['font'] = myFont
        b14.pack(side=LEFT, padx=0, pady=0)

        b15 = Button(toolbar1, relief=FLAT, compound= LEFT, text="new", command=donothing)
        b15.pack(side=LEFT, padx=0, pady=0)

        b16 = Button(toolbar1, relief=FLAT, compound= LEFT, text="new", command=donothing)
        b16.pack(side=LEFT, padx=0, pady=0)

        b17 = Button(toolbar1, relief=FLAT, compound= LEFT, text="new", command=donothing)
        b17.pack(side=LEFT, padx=0, pady=0)

        b18 = Button(toolbar1, relief=FLAT, compound= LEFT, text="new", command=donothing)
        b18.pack(side=LEFT, padx=0, pady=0)

        b19 = Button(toolbar1, relief=FLAT, compound= LEFT, text="new", command=donothing)
        b19.pack(side=LEFT, padx=0, pady=0)

        b20 = Button(toolbar1, relief=FLAT, compound= LEFT, text="new", command=donothing)
        b20.pack(side=LEFT, padx=0, pady=0)

        toolbar.pack(side=TOP, fill=X)
        self.master.config(menu=menubar)
        self.pack()

    
    def onExit(self):

        self.quit()



def main():

    root = Tk()
    root.geometry("800x400")
    app = Example()
    root.mainloop()



if __name__ == '__main__':
    main()
