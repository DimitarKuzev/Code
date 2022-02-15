from doctest import master
from tkinter import *
import tkinter as tk
from click import command
from matplotlib import image
import PIL
from PIL import ImageTk
from PIL import Image
from matplotlib.pyplot import text

from tkinter import Tk
from tkinter.ttk import *

root = tk.Tk()
root.title('Learn To Code at Codemy.com')
# root.iconphoto(False, tk.PhotoImage(file='/home/codesdk/Code/tkinter/gui/Papirus-Apps-Ring-9.png'))
# root.iconbitmap('/home/codesdk/Code/tkinter/gui/Papirus-Apps-Ring-9.ico')
# root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='/home/codesdk/Code/tkinter/gui/bmp file.png'))

photo = PhotoImage(file="/home/codesdk/Code/tkinter/gui/78.png")
root.iconphoto(False, photo)


my_img = ImageTk.PhotoImage(Image.open("/home/codesdk/Code/tkinter/gui/asian girl.jpg"))
my_label = Label(image=my_img)
my_label.pack()





button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()




root.mainloop()