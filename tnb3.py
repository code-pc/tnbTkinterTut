from tkinter import *

root = Tk()
one = Label(root, text="One", bg="red", fg="white")
one.pack(side=RIGHT, fill=Y)
two = Label(root, text="Two", bg="green", fg="black")
two.pack(fill=X)
three = Label(root, text="Three", bg="blue", fg="yellow")
three.pack(side=LEFT, fill=Y)

root.mainloop()
