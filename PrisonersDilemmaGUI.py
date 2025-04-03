from tkinter import *
from tkinter import ttk

class GUI:
    def __init__(self, root):
        self.root = root
        root.title("Prisoner's Dilemma")
        mainframe = ttk.Frame(root, padding = "3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.label = ttk.Label(root, text= "test").grid(column=1, row=1, sticky=(W, E))
        self.algo0val = StringVar()
        self.algo0 = ttk.Combobox()
        self.algo0["values"] = ('USA', 'Canada', 'Australia')

root = Tk()
app = GUI(root)

root.mainloop()