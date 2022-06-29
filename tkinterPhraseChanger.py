from tkinter import *
from tkinter import ttk

def changer():
    text = "Eu sou "+ name.get() +", Tenho "+ age.get() +" anos e gosto de "+chosenTaste.get()+" :D"
    phrase.set(text)

root = Tk()

mainFrame = ttk.Frame(root, padding="10 10 10 10")
mainFrame.grid(column=0, row=0, sticky=(N, S, W, E))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

phrase = StringVar()
mainText = ttk.Label(mainFrame, textvariable=phrase)
mainText.grid(column=0, row=0, sticky=(N))

buttonStart = ttk.Button(mainFrame, text="Criar frase", command=changer)
buttonStart.grid(column=0, row=1, sticky=(N))

name = StringVar()
age = StringVar()

textName = ttk.Label(mainFrame, text="Nome:")
textAge = ttk.Label(mainFrame, text="Idade:")
textName.grid(column=0, row=2, sticky=(W))
textAge.grid(column=0, row=4, sticky=(W))

entryName = ttk.Entry(mainFrame, textvariable=name)
entryAge = ttk.Entry(mainFrame, textvariable=age)
entryName.grid(column=0, row=3, sticky=(W))
entryAge.grid(column=0, row=5, sticky=(W))

textTaste = ttk.Label(mainFrame, text="Gosto:")
textTaste.grid(column=0, row=6, sticky=(W)) 

chosenTaste = StringVar()
taste = ttk.Combobox(mainFrame, textvariable=chosenTaste)
taste["values"] = ('programar', 'jogar', 'assistir netflix', 'anime', 'estudar')
taste.grid(column=0, row=7, sticky=(W))




root.mainloop()