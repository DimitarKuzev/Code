from tkinter import *
import tkinter.ttk as ttk


window= Tk()
window.title('customers information')


e = Entry(window, width=50)

button1 = Button(window,text='1',padx=40,pady=40)
button2 = Button(window,text='2',padx=40,pady=40)
button3 = Button(window,text='3',padx=40,pady=40)

button4 = Button(window,text='4',padx=40,pady=40)
button5 = Button(window,text='5',padx=40,pady=40)
button6 = Button(window,text='6',padx=40,pady=40)

button7 = Button(window,text='7',padx=40,pady=40)
button8 = Button(window,text='8',padx=40,pady=40)
button9 = Button(window,text='9',padx=40,pady=40)

button0 = Button(window,text='0',padx=40,pady=40)

buttoneq = Button(window,text='=',padx=40,pady=40,fg='black',bg="silver")
buttonplus = Button(window,text='+',padx=40,pady=40,fg='black',bg='silver')
buttonminus = Button(window,text='-',padx=40,pady=40,fg='black',bg='silver')
buttonclear = Button(window,text='C',padx=40,pady=40,fg='black',bg='silver')


button1.grid(row=1,column=1)
button2.grid(row=1,column=2)
button3.grid(row=1,column=3)

button4.grid(row=2,column=1)
button5.grid(row=2,column=2)
button6.grid(row=2,column=3)

button7.grid(row=3,column=1)
button8.grid(row=3,column=2)
button9.grid(row=3,column=3)

button0.grid(row=4,column=1)

buttonplus.grid(row=4,column=2)
buttonminus.grid(row=4,column=3)
buttoneq.grid(row=5,column=2)
buttonclear.grid(row=5,column=1)



e.grid(row=0,column=0,columnspan=5,padx=10,pady=10)

window.mainloop()