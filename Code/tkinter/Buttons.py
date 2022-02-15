# -*- coding: utf-8 -*-

from faulthandler import disable
from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look! I clicked a Button!!")
    myLabel.pack()
    

myButton = Button(root, text="Click me!", command= myClick, fg="blue")
myButton.pack()
# state=DISABLED
#, padx=50
# , pady=50
# , fg="blue"
# , bg="red" #ffffff (white), #000000 (black)


root.mainloop()

