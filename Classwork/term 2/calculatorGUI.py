from tkinter import *

# Setup the add function
def Add() :
    global txtNumber1, txtNumber2, IblAnswer
    # Get the number out of the text boxes
    num1 = int(txtNumber1.get())
    num2 = int(txtNumber2.get())
    answer = num1 + num2
    # Change the label text
    IblAnswer.config(text=answer)

root = Tk()

# Add the controls
Label(root, text="First number").grid(row=0)
txtNumber1 = Entry(root)
txtNumber1.grid(row=0, column=1)
Label(root, text="Second number").grid(row=1)
txtNumber2 = Entry(root)
txtNumber2.grid(row=1, column=1)
# Create button and hook up the add function
Button(root, text="Add", command=Add).grid(row=2)
Label(root, text="Answer: ").grid(row=3)
IblAnswer = Label(root, text="0")
IblAnswer.grid(row=3, column=1)
root.mainloop()