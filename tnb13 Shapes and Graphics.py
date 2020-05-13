from tkinter import *

root=Tk()

canvas = Canvas(root, width=200, height=100)
canvas.pack()

blackLine = canvas.create_line(0,0,200,50)
blueLine = canvas.create_line(0,100,200,50,fill="red")
greenBox = canvas.create_rectangle(40,40,100,250,fill="green")

canvas.delete(blueLine)

root.mainloop()