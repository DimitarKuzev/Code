from logging import root
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title("Message Box")
photo = PhotoImage(file="/home/codesdk/Code/tkinter/icon/78.png")
root.iconphoto(False, photo)

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    messagebox.showinfo("This is my Popup!", "Hello World")


Button(root, text="Popup", command=popup).pack()



mainloop()