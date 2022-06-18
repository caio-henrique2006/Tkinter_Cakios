from tkinter import *
from tkinter import ttk

def soma():
    value1 = int(text.get())
    value2 = int(text2.get())
    resultado.set(value1 + value2)


root = Tk()
root.title("Soma")

mainFrame = ttk.Frame(root, padding="10 10 10 10")
mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

text = StringVar()
value1 = ttk.Entry(mainFrame, width=15, textvariable=text)
value1.grid(column=1, row=1, sticky=(N))

text2 = StringVar()
value2 = ttk.Entry(mainFrame, width=20, textvariable=text2)
value2.grid(column=3, row=1, sticky=(N))

ttk.Label(mainFrame, text="+").grid(column=2, row=1, sticky=(N))

ttk.Button(mainFrame, text="=", command=soma).grid(column=4, row=1, sticky=(N))

resultado = StringVar()
ttk.Label(mainFrame, textvariable=resultado).grid(column=5, row=1, sticky=(N))

root.mainloop()