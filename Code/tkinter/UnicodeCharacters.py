from logging import root
from struct import pack
from tkinter import *
root = Tk()
root.title('Import Characters in Python')
root.iconbitmap('d:/Code/tkinter/icon/python.ico')
root.geometry("400x400")
my_label = Label(root, text='41' + u'\u00b0', font=("Helvetica", 32)).pack(pady=10)
# text = u'\u00A9'
# text = u'\u00A2'

my_button = Button(root, text=u'\u00bb', font=("Helvetica", 32)).pack(pady=10)



root.mainloop()