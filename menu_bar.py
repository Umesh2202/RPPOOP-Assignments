from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog as fd

m = Tk()

menubar = Menu(m)

m.geometry("300x300")

file = Menu(menubar)
file.add_command(label='New File', command=lambda: print("new file"))
file.add_command(label='Open File', command=lambda: fd.askopenfilename())

menubar.add_cascade(label='File', menu=file)


view = Menu(menubar)
view.add_command(label='Small View', command=lambda: m.geometry("300x300"))
view.add_command(label='Big View', command=lambda: m.geometry("900x900"))
menubar.add_cascade(label='View', menu=view)

about = Menu(menubar)
about.add_command(label='About Us', command=lambda: print("about"))
menubar.add_cascade(label='About', menu=about)


m.config(menu=menubar)
m.mainloop()
