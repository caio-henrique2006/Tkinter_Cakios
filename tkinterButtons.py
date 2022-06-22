from tkinter import *
from tkinter import ttk

def buttonAble():
    buttonText.set("You can't press me")
    button.state(["disabled"])

root = Tk()

mainFrame = ttk.Frame(root, padding="10 10 10 10")
mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

buttonText = StringVar(value="Press me")
button = ttk.Button(mainFrame, textvariable=buttonText, command=buttonAble)
button.grid(column=0, row=0, sticky=(N))

root.mainloop()