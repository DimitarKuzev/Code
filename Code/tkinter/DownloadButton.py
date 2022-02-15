from logging import root
from tkinter import *
import PIL
from PIL import ImageTk
from PIL import Image
from matplotlib import image


root = Tk()
root.title('PythonGuides')

img = PhotoImage(file='/home/codesdk/Pictures/download_button.png')

Button(root, image=img, command=None).pack()

root.mainloop()