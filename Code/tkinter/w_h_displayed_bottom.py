from tkinter import *  
from PIL import ImageTk,Image  

ws = Tk()  
ws.title('PythonGuides')
ws.geometry('500x500')

canvas = Canvas(
        ws, 
        width = 500, 
        height = 400
        )  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open('/home/codesdk/Pictures/girl4.jpg'))  

canvas.create_image(
        10, 
        10, 
        anchor=NW, 
        image=img
        ) 
Label(
    ws,
    text=f'width: {img.width()} height: {img.height()}'
).pack()

ws.mainloop() 