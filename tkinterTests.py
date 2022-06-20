from tkinter import *
from tkinter import ttk

root = Tk()

mainFrame = ttk.Frame(root, padding="10 10 10 10")
mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frame1 = ttk.Frame(mainFrame, height=200, width=200, borderwidth=20, relief=SUNKEN)
frame1.grid(column=1, row=1, sticky=(N))
frame2 = ttk.Frame(mainFrame, height=1000, width=200, borderwidth=20, relief=RAISED)
frame2.grid(column=2, row=1, sticky=(N))

root.mainloop()