import tkinter as tk

class Window1(tk.Frame):

    def __init__(self, master):
        # send `root` to `Frame` as its parent
        tk.Frame.__init__(self, master) 
        # `Frame` will keep `master as `self.master` 
        # so we don't have to do `self.master = master` manually

        self.grid()
        self.btn = tk.Button(self, text="Hello Button", command=self.run)
        self.btn.grid(row=0, column=0)

    def run(self):
        # use `master` (`root`) to destroy  it
        self.master.destroy() 

class Window2(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)       
        self.grid()
        self.label = tk.Label(self, text="Hello Label")
        self.label.grid(row=0, column=0)

root = tk.Tk()  # create main window as `root`
Window1(root)   # send `root` to `Window1` and later to `Frame`
root.mainloop()

root = tk.Tk()
Window2(root)
root.mainloop()