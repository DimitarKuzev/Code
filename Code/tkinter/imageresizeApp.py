
# How to install Pillow on Ubuntu20.04? (terminal:)
# python3 -m pip install --upgrade pip
# python3 -m pip install --upgrade Pillow

from logging import root
from tkinter import *
from turtle import width
import PIL
from PIL import ImageTk
from PIL import Image
from cv2 import resize
from matplotlib import image
from numpy import disp


root = Tk()
root.title('PythonGuides')
root.geometry('500x500')
root.config(bg='#4a7a8c')


def  resize_func():
    image = Image.open("/home/codesdk/Pictures/girl4.jpg")
    w = int(width.get())
    h = int(height.get())
    resize_img = image.resize((w, h))
    img = ImageTk.PhotoImage(resize_img)
    disp_img.config(image=img)
    disp_img.image = img
    

frame = Frame(root)
frame.pack()

Label(frame, text='Width').pack(side=LEFT)
width = Entry(frame, width=10)
width.insert(END, 300)
width.pack(side=LEFT)

Label(frame, text='Height').pack(side=LEFT)
height = Entry(frame, width=10)
height.insert(END, 350)
height.pack(side=LEFT)

resize_btn = Button(frame, text='Resize', command=resize_func)
resize_btn.pack(side=LEFT)

disp_img = Label()
disp_img.pack(pady=20)

img = ImageTk.PhotoImage(Image.open("/home/codesdk/Pictures/girl4.jpg"))
Label(root, text=f'width: {img.width()} height: {img.height()}').pack()

root.mainloop()