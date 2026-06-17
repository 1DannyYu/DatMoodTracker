from tkinter import *
from tkinter import messagebox

def CheckFruit():
    global var

    if var.get() == 1:
        messagebox.showinfo(message="Apples are great!")
    elif var.get() == 2:
        messagebox.showinfo(message="Bananas rock!")
    elif var.get() == 3:
        messagebox.showinfo(message="Carrots... aren't even a fruit")

root = Tk()
var = IntVar()

Label(root, text="What is the best fruit?")
Radiobutton(root,text="Apple", variable = var, value = 1).grid(row=1, sticky=W)
Radiobutton(root,text="Banana", variable = var, value = 2).grid(row=2, sticky=W)
Radiobutton(root,text="Carrot", variable = var, value = 3).grid(row=3, sticky=W)

Button(root, text="Answer", command=CheckFruit).grid(row=5)

root.mainloop()