from tkinter import *

master = Tk()

var= IntVar()

w = Scale(master, from_=0, to=200, orient=HORIZONTAL,variable=var)
w.pack()
mainloop()
print( var.get())
