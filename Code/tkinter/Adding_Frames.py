from  tkinter import *
from PIL import ImageTk, Image
# from tkinter.ttk import * this will avoid error
# If you still want to import tkinter.ttk, import it, for example, like that:
# import tkinter.ttk as ttk

root = Tk()
root.title('Adding Frames')

# icon
# photoimage can read only GIF and PGM/PPM images.

img = PhotoImage(file='/home/codesdk/Code/tkinter/gui/icon/bmp file.png')
root.tk.call('wm', 'iconphoto', root._w, img)

# Frame

frame = LabelFrame(root, padx=50, pady=50)
frame.pack(padx=10, pady=10)


#Buttons

b = Button(frame, text="Click")
b.grid(row=0, column=0)

b1 = Button(frame, text="Click")
b1.grid(row=0, column=1)

b2 = Button(frame, text="Click")
b2.grid(row=0, column=2)

b3 = Button(frame, text="Click")
b3.grid(row=0, column=3)

b4 = Button(frame, text="Click")
b4.grid(row=0, column=4)

# This is dont work: How to show this frames?
frame1 = LabelFrame(root, text="Another Tools Frame..", padx=5, pady=5)
frame1.pack(padx=10, pady=10)





root.mainloop()