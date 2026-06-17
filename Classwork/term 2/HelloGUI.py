from tkinter import *

root = Tk()
Label(root, text="First name").grid(row=0)
Label(root, text="Last name").grid(row=1)
Entry(root).grid(row=0, column=1)
Entry(root).grid(row=1, column=1)
Checkbutton(root, text="I'm not a robot").grid(row=2)

lstColours = Listbox(root)
lstColours.grid(row=3, columnspan=2)
lstColours.insert(1, "Blue")
lstColours.insert(2, "red")
lstColours.insert(3, "Green")
lstColours.insert(4, "Orange")

Button(root, text="Finished", command=root.destroy).grid(row=4, columnspan=2)
root.mainloop()
