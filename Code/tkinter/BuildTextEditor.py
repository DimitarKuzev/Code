from  tkinter import *
from tkinter import filedialog
from tkinter import font
from turtle import undo

from matplotlib.pyplot import fill

root = Tk()
root.title('Text Editor')
photo = PhotoImage(file="/home/codesdk/Code/tkinter/icon/78.png")
root.iconphoto(False, photo)
root.geometry("1200x660")

# Create New File Function

def  new_file():
    my_text.delete("1.0", END)
    root.title('New File - TextPad!')
    status_bar.config(text="New File         ")




##################
# Create Main Frame

my_frame = Frame(root)
my_frame.pack(pady=5)

###################
# Create Scrollbar for the Text Box
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)


###################
# Create Text Box

my_text = Text(my_frame, width=97, height=25, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
my_text.pack()

###################
# Configure our Scrollbar
text_scroll.config(command=my_text.yview)


###################
# Create Menu

my_menu = Menu(root, tearoff=0)
root.config(menu=my_menu)

# Add File Menu

file_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_command(label="Save As")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Add Edit Menu

edit_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")

# Add Status Bar To Bottom of App

status_bar = Label(root, text='Redy         ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)



root.mainloop()