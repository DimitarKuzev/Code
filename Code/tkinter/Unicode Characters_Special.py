from logging import root
from tkinter import *

root = Tk()
root.title("Unicode Characters!")
root.iconbitmap('d:/Code/tkinter/icon/python.ico')
root.geometry("400x400")

my_label = Label(root, text='41' + u'\u00b0', font=("Helvetica", 32)).pack()

my_button = Button(root, text='41' + u'\u00b0', font=("Helvetica", 32)).pack()
my_button1 = Button(root, text='22' + u'\u00b2', font=("Helvetica", 32)).pack()

root.mainloop()