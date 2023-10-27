import math
from tkinter import *

userNumber = 0
gameEnd = True

root = Tk()
root.title("prime number checker")
root.config(bg="#CF5858")
root.config(width=350, height=250)

greetingLabel = Label(root)
greetingLabel.config(text="Enter number")
greetingLabel.place(x=150, y=10)

inputEntry = Entry(root)
inputEntry.place(x=130, y=40)

screenLabel = Label(root)

def primeNumber():
    global userNumber
    global gameEnd
    userNumber = int(inputEntry.get())
    gameEnd = True

    for n in range(2, userNumber):
        if userNumber % n == 0:
            gameEnd = False
            break

    if gameEnd:
        screenLabel.place(x=130, y=120)
        screenLabel.config(text="Your number is prime")
    else:
        screenLabel.place(x=120, y=120)
        screenLabel.config(text="Your number isn't prime")

checkButton = Button(root)
checkButton.config(text="CHECK", command=primeNumber)
checkButton.place(x=160, y=150)

root.mainloop()
