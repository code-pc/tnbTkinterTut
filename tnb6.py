from tkinter import *

root = Tk()
def printName(event):
    print("Hello my name is CP")

button_1 = Button(root, text="Print My Name")
button_1.bind("<Button-1>", printName)
button_1.pack()


root.mainloop()
