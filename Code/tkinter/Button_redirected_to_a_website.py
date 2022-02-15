from curses import window
from hashlib import new
from logging import root
from tkinter import *
from tkinter import font
import PIL
from PIL import ImageTk
from PIL import Image
from matplotlib import image
import webbrowser


root = Tk()
root.title('PythonGuides')
root.geometry("500x400")

new = 1
url = "https://www.pythonguides.com"

def  openbrowser():
    webbrowser.open(url, new=new)

bg = ImageTk.PhotoImage(file='/home/codesdk/Pictures/sea.jpeg')

canvas = Canvas(root, width=500, height=400)
canvas.pack(fill='both', expand=True)

canvas.create_image(0, 0, image=bg, anchor="nw")
canvas.create_text(250, 150, text= 'PythonGuides', font=('Arial', 50), )

btn = Button(root, text= 'EXPLORE MORE' , command=openbrowser, width=20, height=2, relief=SOLID, font=('arial', 18))    
btn_canvas = canvas.create_window(100, 200, anchor="nw", window=btn, )


root.mainloop()