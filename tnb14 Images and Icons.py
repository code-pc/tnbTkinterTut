from tkinter import *

root=Tk()

photo = PhotoImage(file="plane.png")
label = Label(root, image=photo)
label.pack()

root.mainloop()