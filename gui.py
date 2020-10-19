import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox as mb
from data import search_row,add_row
class Application(Frame):

    
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.createWidgets()
        self.master.title('Payroll')
        self.master.iconbitmap('payroll.ico')
        self.master.maxsize(500,700)
        self.style = Style()
        self.style.configure('BW.TLabel',font=('Roboto',12))

    def set_male(self):
        self.new_gender.set('male')

    def set_female(self):
        self.new_gender.set('female')

    def add_data(self,event=None):

        #To not throw an error in console if one or two inputs are empty
        try:
            name = self.add_name_entry.get()
            eid = int(self.add_eid_entry.get())
            gender = self.new_gender.get()
            salary = int(self.add_salary_entry.get())
            new_row = [eid,name,gender,salary]
            print(eid,name,gender,salary)
            add_row(new_row)


        except ValueError:
            #To check if all inputs are being given
            if(not self.add_name_entry.get()):
                mb.showwarning(title='Invalid Input',message='Please Enter all values to proceed.')
            elif(not self.new_gender.get()):
                mb.showwarning(title='Invalid Input',message='Please Enter all values to proceed.')
            elif(not self.add_eid_entry.get()):
                mb.showwarning(title='Invalid Input',message='Please Enter all values to proceed.')
            elif(not self.add_salary_entry.get()):
                mb.showwarning(title='Invalid Input',message='Please Enter all values to proceed.')


        self.add_eid_entry.delete(0,'end')
        self.add_name_entry.delete(0,'end')
        self.add_salary_entry.delete(0,'end')
        self.add_eid_entry.delete(0,'end')



    def searchEmp(self,event=None):
        try:
            self.eid = int(self.eid_entry.get())
            self.name = self.name_entry.get()
            self.dat = search_row(self.eid)
        except ValueError:
            mb.showerror(title='Error!',message='Enter a Valid Employee Id')
        if(self.dat == None):
            mb.showerror(title='Not Found',message='Invalid Input')
            return
        elif(not self.dat):
            mb.showwarning(title='Not Found',message='The instance doesn\'t exist in csv.')
            return

        root = Tk()
        root.title('Search')
        root.iconbitmap('payroll.ico')
        root.geometry('1350x650+0+0')
        self.days= IntVar()
        self.leave=IntVar()
        self.GST=DoubleVar()
        self.Gross=DoubleVar()



        f2 = Frame(root, width=300, height=700)
        f2.place(x=500, y=50)

        self.txtPaySlip = Text(f2,font=('arial', 12, 'bold'))
        self.txtPaySlip.pack(anchor='e')

        #Employee ID Label widget
        self.eid_label = Label(root,text='Employee ID',font=('Calibri',12))
        self.eid_label.grid(row=0,column=0,padx=10,pady=(10,0),sticky='W')

        #Employee Name Label widget
        self.name_label = Label(root,text='Name',font=('Calibri',12))
        self.name_label.grid(row=1,column=0,padx=10,sticky='W')

        # Employee Gender Label Widget
        self.gender_label = Label(root, text='Gender', font=('Calibri', 12))
        self.gender_label.grid(row=2, column=0, padx=10, sticky='W')

        # Employee Salary Label Widget
        self.salary_label = Label(root, text='Salary', font=('Calibri', 12))
        self.salary_label.grid(row=3, column=0, padx=10, sticky='W')

        #Employee Working days Widget
        self.days_label = Label(root, text='Working days',font=('Calibri', 12) )
        self.days_label.grid(row=4, column=0, padx=10, pady=(0, 10), sticky='W')

        # Employee wage per day Widget
        self.wage_label = Label(root, text='Wage per day', font=('Calibri', 12))
        self.wage_label.grid(row=5, column=0, padx=10, pady=(0, 10), sticky='W')

        # Employee Leave Widget
        self.leave_label = Label(root, text='Leave', font=('Calibri', 12))
        self.leave_label.grid(row=6, column=0, padx=10, pady=(0, 10), sticky='W')

        # Tax Widget
        self.taxes_label = Label(root, text='GST', font=('Calibri', 12))
        self.taxes_label.grid(row=7, column=0, padx=10, pady=(0, 10), sticky='W')

        # Gross Salary
        self.Gross_label = Label(root, text='Gross Salary', font=('Calibri', 12))
        self.Gross_label.grid(row=8, column=0, padx=10, pady=(0, 10), sticky='W')


        #Employee ID text widget
        self.eid_text = Text(root,height=1,width=20)
        self.eid_text.grid(row=0,column=1,padx=10,pady=(10,0),sticky='W')
        self.eid_text.configure(font='calibri 12')
        self.eid_text.insert(END,str(self.dat[0]))

        #Employee Name text Widget
        self.name_text = Text(root,height=1,width=20)
        self.name_text.grid(row=1,column=1,padx=10,sticky='W')
        self.name_text.configure(font='calibri 12')
        self.name_text.insert(END,str(self.dat[1]))

        #Employee Gender Text Widget
        self.gender_text = Text(root,height=1,width=20)
        self.gender_text.grid(row=2,column=1,padx=10,sticky='W')
        self.gender_text.configure(font='calibri 12')
        self.gender_text.insert(END,str(self.dat[2]))

        #Employee Salary Text Widget
        self.salary_text = Text(root,height=1,width=20)
        self.salary_text.grid(row=3,column=1,padx=10,sticky='W')
        self.salary_text.configure(font='calibri 12')
        self.salary_text.insert(END,str(self.dat[3]))

        # Employee working days
        self.days_entry = tk.Scale(root, from_=0, to=31, orient=HORIZONTAL, variable=self.days)
        self.days_entry.grid(row=4, column=1, sticky='W', padx=(10, 10), pady=(0, 10))

        # Employee wage per days

        self.wage = self.dat[3] / 30
        self.wage_text = Text(root, height=1, width=20)
        self.wage_text.grid(row=5, column=1, padx=10, sticky='W')
        self.wage_text.configure(font='calibri 12')
        self.wage_text.insert(END, str(self.wage))

        # Employee leave
        self.leave_entry = Entry(root, width=20, textvariable=self.leave)
        self.leave_entry.grid(row=6, column=1, sticky='W', padx=(10, 10), pady=(0, 10))

        #Taxes
        self.taxes_entry = Entry(root, width=20, textvariable=self.GST)
        self.taxes_entry.grid(row=7, column=1, sticky='W', padx=(10, 10), pady=(0, 10))

        #Gross salary
        self.Gross_entry = Entry(root, width=20, textvariable=self.Gross)
        self.Gross_entry.grid(row=8, column=1, sticky='W', padx=(10, 10), pady=(0, 10))

        #Compute button
        self.add_new_button = Button(root, text='Compute', command=self.EnterInfo)
        self.add_new_button.grid(row=9, column=0, pady=(0, 10), padx=10, columnspan=3, ipadx=5)


    def EnterInfo(self):
        self.txtPaySlip.insert(END, "\t\tPay Slip\n\n")
        self.txtPaySlip.insert(END, 'Employer ID:\t\t' + str(self.dat[0]) + "\n\n")
        self.txtPaySlip.insert(END, 'Name:\t\t' + str(self.dat[1]) + "\n\n")
        self.txtPaySlip.insert(END, 'Gender:\t\t' + str(self.dat[2]) + "\n\n")
        self.txtPaySlip.insert(END, 'Gross Salary :\t\t' + str(self.dat[3]) + "\n\n")
        self.txtPaySlip.insert(END, 'Working days of company:\t\t' + str(self.days_entry.get()) + "\n\n")
        self.txtPaySlip.insert(END, 'Leave:\t\t' + str(self.leave_entry.get() )+ "\n\n")
        self.txtPaySlip.insert(END, 'Wages Per day:\t\t' + str(self.wage) + "\n\n")
        self.txtPaySlip.insert(END, 'GST is:\t\t' + str(self.taxes_entry.get()) +"%"+ "\n\n")
        self.payableTax = (int(self.taxes_entry.get()) / 100) * int(self.dat[3])

        self.txtPaySlip.insert(END, 'Tax payable:\t\t' + str(self.payableTax) + "\n\n")
        if(self.days_entry.get() <self.leave_entry.get()):
            self.netSalary = (self.days_entry.get() - self.leave_entry.get()) * (self.wage)
        else:
            self.netSalary=0
        self.txtPaySlip.insert(END, 'Net salary:\t\t{}'.format(self.netSalary))





    def addEmp(self,event=None):
        root=Tk()
        root.title('Add New Employee')
        root.iconbitmap('payroll.ico')
        root.geometry("500x500")
        self.style = Style()
        self.style.configure('BW.TLabel',font=('Roboto',12))
        self.new_eid = StringVar()
        self.new_name = StringVar()
        self.new_salary = StringVar()
        self.new_gender = StringVar()

        #Employee ID Label Widget
        self.add_eid_label = Label(root,text='Employee ID',style='BW.TLabel')
        self.add_eid_label.grid(row=0,column=0,pady=10,padx=10,sticky='W')

        #Employee Name Lable Widget
        self.add_name_label = Label(root,text='Employee Name',style='BW.TLabel')
        self.add_name_label.grid(row=1,column=0,padx=10,pady=(0,10),sticky='W')

        #Employee Gender Label Widget
        self.add_gender_label = Label(root,text='Gender',style='BW.TLabel')
        self.add_gender_label.grid(row=2,column=0,padx=10,pady=(0,10),sticky='W')

        #Employee Salary Label Widget
        self.add_salary_label = Label(root,text='Salary',style='BW.TLabel')
        self.add_salary_label.grid(row=4,column=0,padx=10,pady=(0,10),sticky='W')


        #Employee ID entry Widget
        self.add_eid_entry = Entry(root,width=20,textvariable=self.new_eid)
        self.add_eid_entry.grid(row=0,column=1,sticky='W',pady=10,padx=(0,10),columnspan=2)

        #Employee Name Entry Widget
        self.add_name_entry = Entry(root,width=20,textvariable=self.new_name)
        self.add_name_entry.grid(row=1,column=1,sticky='W',padx=(0,10),pady=(0,10),columnspan=2)

        #Employee Gender Radio Widget
        self.add_gender_radio_m = Radiobutton(root,text='Male',value='male',variable=self.new_gender,command=self.set_male)
        self.add_gender_radio_m.grid(row=2,column=1,sticky='W',padx=(0,10),pady=(0,10))

        self.add_gender_radio_f = Radiobutton(root,text='Female',value='female',variable=self.new_gender,command=self.set_female)
        self.add_gender_radio_f.grid(row=2,column=2,sticky='W',padx=(0,10),pady=(0,10))

        #Employee Salary Entry Widget
        self.add_salary_entry = Entry(root,width=20,textvariable=self.new_salary)
        self.add_salary_entry.grid(row=4,column=1,sticky='W',padx=(0,10),pady=(0,10),columnspan=2)

        #ADD new button
        self.add_new_button = Button(root,text='Add to Database',command=self.add_data)
        self.add_new_button.grid(row=5,column=0,pady=(0,10),padx=10,columnspan=3,ipadx=5)

        # Enter key functionality on Add to database button
        self.add_new_button.bind('<Return>',self.add_data)



    def createWidgets(self):

        self.empId = StringVar()
        self.name = StringVar()

        #Employee ID Label widget
        self.eid_label = Label(self.master,text='Employee ID',font=('Calibri',12))
        self.eid_label.grid(row=0,column=0,padx=10,pady=(10,0),sticky='W')

        #Employee Name Label widget
        self.name_label = Label(self.master,text='Name',font=('Calibri',12))
        self.name_label.grid(row=1,column=0,padx=10,pady=(0),sticky='W')

        #Employee ID Entry Widget
        self.eid_entry = Entry(self.master, width=20,textvariable=self.empId)
        self.eid_entry.grid(row=0,column=1,sticky='W',pady=(10,0),padx=(0,10))

        #Employee Name Entry Widget
        self.name_entry = Entry(self.master, width=20,textvariable=self.name)
        self.name_entry.grid(row=1,column=1,pady=(10,10),padx=(0,10),sticky='W')

        #Search Button
        self.search_button = Button(self.master,text='Search',width=18,command=self.searchEmp)
        self.search_button.grid(row=2,column=0,pady=(0,10),padx=10,columnspan=2)

        #Add new Employee Button
        self.add_button = Button(self.master,text='Add New Employee',command=self.addEmp)
        self.add_button.grid(row=3,column=0,pady=(0,10),padx=10,columnspan=2,ipadx=5)

        # Enter key functionality for buttons
        self.search_button.bind("<Return>", self.searchEmp)
        self.add_button.bind("<Return>",self.addEmp)


root =Tk()
root.geometry("500x500")
app = Application(master=root)
app.mainloop()
