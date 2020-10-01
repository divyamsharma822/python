from tkinter import *
from tkinter import Toplevel, messagebox
import sqlite3

root = Tk()
root.title('Payroll Management System')
root.config(bg='white')
root.geometry('520x620+470+100')
root.resizable(FALSE, FALSE)

DataEntryFrame = Frame(root, bg='lightblue', relief=GROOVE, borderwidth=5)
DataEntryFrame.place(x=10, y=10, width=500, height=600)
frontlabel = Label(DataEntryFrame, text='Payroll Management System', width=30,
                   font=('arial', 22, 'italic bold'), bg='white')
frontlabel.place(x=44, y=100)

name = StringVar()
id = StringVar()
namebtn = Label(DataEntryFrame, text='Enter Name', width=10, font=('chiller', 19, 'bold'), bd=2, bg='skyblue3',
                activebackground='blue', relief=RIDGE,
                activeforeground='white')
namebtn.place(x=55, y=260)
namebtntxt = Entry(DataEntryFrame, font=('roman', 15, 'bold'), bd=2, textvariable=name)
namebtntxt.place(x=200, y=260)

idbtn = Label(DataEntryFrame, text='Enter ID', width=10, font=('chiller', 19, 'bold'), bd=2, bg='skyblue3',
              activebackground='blue', relief=RIDGE,
              activeforeground='white')
idbtn.place(x=55, y=320)
idbtntxt = Entry(DataEntryFrame, font=('roman', 15, 'bold'), bd=2, textvariable=id)
idbtntxt.place(x=200, y=320)

submitbtn = Button(DataEntryFrame, text='Submit', font=('roman', 17, 'bold'), width=31, bd=2, activebackground='blue',
                   activeforeground='white',
                   bg='red', command=searchstudent)
submitbtn.place(x=55, y=370)
connectbutton = Button(DataEntryFrame, text='Add Data', font=('roman', 12, 'bold'), width=31, bd=2,
                       activebackground='blue',
                       activeforeground='white',
                       bg='red', command=Adddb)
connectbutton.place(x=110, y=560)

root.mainloop()
