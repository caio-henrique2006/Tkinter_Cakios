from tkinter import *
from tkinter import ttk

def Send():
    text = "Seu nome é " + userName.get()
    answer.set(text)

def checkOnOff():
    if checkText.get() == "I'm off":
        checkText.set("I'm on")
    else:
        checkText.set("I'm off")

def buttonAble():
    buttonText.set("You can't press me")
    button.state(["disabled"])

root = Tk()

# Frame principal:
mainFrame = ttk.Frame(root, padding="10 10 10 10")
mainFrame.grid(column=0, row=0, sticky=(N, W, S, E))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Segundo Frame:
sideFrame = ttk.Frame(root, padding="10 10 10 10")
sideFrame.grid(column=1, row=0, sticky=(N, S, W, E))

# Botão:
buttonText = StringVar(value="Press me")
button = ttk.Button(mainFrame, textvariable=buttonText, command=buttonAble)
button.grid(column=0, row=0, sticky=(N))

# Texto:
text = ttk.Label(mainFrame, text="This is the Hollow Knight")
text.grid(column=0, row=1, sticky=(N))

# Imagem:
myImage = PhotoImage(file="Images/knightGif.gif")
image = ttk.Label(mainFrame, image=myImage)
image.grid(column=0, row=3, sticky=(W))

# Botão cheque:
checkText = StringVar(value="I'm off")
check = ttk.Checkbutton(mainFrame, textvariable=checkText, command=checkOnOff)
check.grid(column=0, row=2, sticky=(W))

# Radio Botão:
language = StringVar()
English = ttk.Radiobutton(sideFrame, text="English", variable=language, value="english")
Portuguese = ttk.Radiobutton(sideFrame, text="Portuguese", variable=language, value="portuguese")
Spanish = ttk.Radiobutton(sideFrame, text="Spanish", variable=language, value="spanish")
English.grid(column=0, row=0, sticky=(N))
Portuguese.grid(column=0, row=1, sticky=(N))
Spanish.grid(column=0, row=2, sticky=(N))

radioText = ttk.Label(sideFrame, textvariable=language)
radioText.grid(column=0, row=3, sticky=(N)) 

# Entry:
userName = StringVar()
Name = ttk.Entry(sideFrame, textvariable=userName)
Name.grid(column=1, row=0, sticky=(N))

answer = StringVar()
entryButton = ttk.Button(sideFrame, text="Send", command=Send)
entryText = ttk.Label(sideFrame, textvariable=answer)
entryButton.grid(column=2, row=0, sticky=(N))
entryText.grid(column=1, row=1, sticky=(N))

# Combobox:
chosenCountry = StringVar()
country = ttk.Combobox(sideFrame, textvariable=chosenCountry)
country["values"] = ('Brasil', 'Alemanha', 'India', 'China')
country.grid(column=1, row=2, sticky=(N))


root.mainloop()