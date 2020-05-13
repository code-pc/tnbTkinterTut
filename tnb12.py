from tkinter import *
import tkinter.messagebox

root=Tk()

tkinter.messagebox.showinfo('Window Title', 'Turtles can live up to 300 yrs')

answer = tkinter.messagebox.askquestion('Question', 'Do you like silly faces?')
if answer == 'yes':
    print(" 8===D- ")
root.mainloop()