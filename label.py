from tkinter.ttk import *
from tkinter import *

m = Tk()

m.geometry("750x250+400+300")

m.rowconfigure(10)
m.columnconfigure(10)


l1 = Label(m, text="First:", font=("Arial", 25))
l2 = Label(m, text="Second:", font=("Arial", 25))

clr1 = str(input("Enter color one: "))
clr2 = str(input("Enter color two: "))
l1.configure(background=clr1)
l2.configure(background=clr2)
l1.grid(row=0, column=0, sticky=W, pady=2)
l2.grid(row=1, column=0, sticky=W, pady=2)


m.mainloop()
