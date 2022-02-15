from logging import root
import sys
from tkinter import *

root = Tk()
root.title('Gif icon')

if ( sys.platform.startswith('win')): 
    root.iconbitmap('/home/codesdk/Code/tkinter/gui/icon/python.ico')
else:
    logo = PhotoImage(file='/home/codesdk/icons/gif/circles-menu-1.gif')
    root.call('wm', 'iconphoto', root._w, logo)
    
