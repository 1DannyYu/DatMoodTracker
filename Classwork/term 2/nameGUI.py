from tkinter import * 
from tkinter import messagebox
def SayHello():
    global txtFirstname, txtLastname
    firstname = txtFirstname.get()
    lastname = txtLastname.get()
    messagebox.showinfo(message=f"Hello {firstname} {lastname}")

root = Tk()

Label(root, text="First name"). grid (row=0)
txtFirstname = Entry(root)
txtFirstname.grid(row=0, column=1)

Label(root, text="Last name"). grid (row=1)
txtLastname = Entry(root)
txtLastname.grid(row=1, column=1)

Button (root, text="Say hello", command=SayHello).grid(row=2, columnspan=2)

root.mainloop()