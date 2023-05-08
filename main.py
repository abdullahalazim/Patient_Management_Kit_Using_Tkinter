'''
Copyright (c) 2023 Abdullah Al Azim
'''
from tkinter import *
from tkinter import ttk as tk
from tkinter import messagebox
from tkinter.ttk import Separator
import sqlite3

conn = sqlite3.connect('patient_db.db')
c = conn.cursor()

color = 'lightblue'

class PatientApp:
    def __init__(self,window):
        self.window = window
        self.ttk_style = tk.Style()
        self.ttk_style.configure('color.TRadiobutton',background = color)

        self.home_frame = Frame(window,background=color,height=350,width=400,relief=SUNKEN)
        self.one_patient_detail_frame = Frame(window,background=color,height=350,width=400,relief=SUNKEN)
        self.all_patient_detail_frame = Frame(window,height=350,width=400,relief=SUNKEN)
        self.update_frame = Frame(window,background=color,height=350,width=400,relief=SUNKEN)
        self.delete_frame = Frame(window,background=color,height=350,width=400,relief=SUNKEN)

    def home_menu(self):
        # first page home page declaring through menu button Home > Register 
        self.home_frame.destroy()
        self.one_patient_detail_frame.destroy()
        self.all_patient_detail_frame.destroy()
        self.update_frame.destroy()
        self.delete_frame.destroy()
        self.__init__(self.window)
        self.home_page()
        self.home_frame.pack()

    def home_page(self):
        # home opening
        self.main_label = Label(self.home_frame,font=('Ariel 20 bold'),text='Patient Register Form',bg=color)
        self.main_label.place(x=50,y=2)

        tk.Label(self.home_frame,text='Patient Id',background=color).place(x=15,y=45)
        self.id = tk.Entry(self.home_frame,width=30)
        self.id.place(x=95,y=45)

        tk.Label(self.home_frame,text='Patient Name',background=color).place(x=15,y=75)
        self.name = tk.Entry(self.home_frame,width=30)
        self.name.place(x=95,y=75)

        tk.Label(self.home_frame,text='Patient Age',background=color).place(x=15,y=105)
        self.age = tk.Entry(self.home_frame)
        self.age.place(x=95,y=105)

        self.gender_value = IntVar()
        tk.Label(self.home_frame,text='Gender',background=color).place(x=15,y=135)
        tk.Radiobutton(self.home_frame,text='Male',value=1,variable=self.gender_value,style='color.TRadiobutton').place(x=95,y=135)
        tk.Radiobutton(self.home_frame,text='Female',value=2,variable=self.gender_value,style='color.TRadiobutton').place(x=155,y=135)

        tk.Label(self.home_frame,text='Phone no',background=color).place(x=15,y=165)
        self.phone_no = tk.Entry(self.home_frame,width=30)
        self.phone_no.place(x=95,y=165)

        tk.Label(self.home_frame,text='Location',background=color).place(x=15,y=195)
        self.location = tk.Entry(self.home_frame,width=30)
        self.location.place(x=95,y=195)

        Button(self.home_frame,text='Add Patient',width=25,bg='green',command=self.register_patient).place(x=95,y=225)

        self.home_frame.pack()

    def register_patient(self):
        # Register a patient where all requirement successfully completed from home page 
        self.id = self.id.get()
        self.name = self.name.get()
        self.age = self.age.get()

        if self.gender_value.get() == 1:
            self.gender = 'Male'
        elif self.gender_value.get() == 2:
            self.gender = 'Female'
        else:
            self.gender = 'Not Selected'
        self.phone_no = self.phone_no.get()
        self.location = self.location.get()

        if self.id == '' or self.name == '' or self.age == '' or self.gender == '' or self.phone_no == '' or self.location == '':
            messagebox.showwarning('Warring','Please fill up every options')
        else:
            sql = "INSERT INTO 'patient' (p_id, name, age, gender, phone_no,location) VALUES (?,?,?,?,?,?)"
            c.execute(sql,(self.id, self.name, self.age, self.gender, self.phone_no, self.location))
            conn.commit()
            messagebox.showinfo('Success', '\n Patient '+str(self.name)+' is successfully registered into system')

        self.home_frame.destroy()
        self.__init__(self.window)
        self.home_page()

    def one_patent_detail_menu(self):
        # redirect detail page declaring through menu button Detail > one patient
        self.home_frame.destroy()
        self.one_patient_detail_frame.destroy()
        self.all_patient_detail_frame.destroy()
        self.update_frame.destroy()
        self.delete_frame.destroy()
        self.__init__(self.window)


        self.main_label = Label(self.one_patient_detail_frame,font=('Ariel 20 bold'),text='Patient Detail',bg=color)
        self.main_label.place(x=105,y=2)
        tk.Label(self.one_patient_detail_frame,text='Enter Patient Id here',background=color).place(x=15,y=45)
        self.id = tk.Entry(self.one_patient_detail_frame)
        self.id.place(x=135,y=45)
        Button(self.one_patient_detail_frame,text='Search',bg='green',command=self.show_one_patient).place(x=265,y=45)
        self.one_patient_detail_frame.pack(fill='both',expand=True)   

    def show_one_patient(self):
        # showing patient detail
        self.id = self.id.get()
        if self.id == '':
            messagebox.showwarning('Warring','Please Enter Patient Id')
        else:
            sql = "SELECT * FROM patient WHERE p_id LIKE ?"
            self.response = c.execute(sql,(self.id,))

            for self.detail_data in self.response:
                self.id = self.detail_data[0]
                self.name = self.detail_data[1]
                self.age = self.detail_data[2]
                self.gender = self.detail_data[3]
                self.phone_no = self.detail_data[4]
                self.location = self.detail_data[5]

                tk.Label(self.one_patient_detail_frame,text='Patient Id',background=color,font=('Ariel 8 bold')).place(x=15,y=75)
                tk.Label(self.one_patient_detail_frame,text=self.id,background=color,font=('Ariel 8 bold')).place(x=95,y=75)
                tk.Label(self.one_patient_detail_frame,text='Patient Name',background=color,font=('Ariel 8 bold')).place(x=15,y=95)
                tk.Label(self.one_patient_detail_frame,text=self.name,background=color,font=('Ariel 8 bold')).place(x=95,y=95)
                tk.Label(self.one_patient_detail_frame,text='Patient Age',background=color,font=('Ariel 8 bold')).place(x=15,y=115)
                tk.Label(self.one_patient_detail_frame,text=self.age,background=color,font=('Ariel 8 bold')).place(x=95,y=115)
                tk.Label(self.one_patient_detail_frame,text='Gender',background=color,font=('Ariel 8 bold')).place(x=15,y=135)
                tk.Label(self.one_patient_detail_frame,text=self.gender,background=color,font=('Ariel 8 bold')).place(x=95,y=135)
                tk.Label(self.one_patient_detail_frame,text='Phone no',background=color,font=('Ariel 8 bold')).place(x=15,y=155)
                tk.Label(self.one_patient_detail_frame,text=self.phone_no,background=color,font=('Ariel 8 bold')).place(x=95,y=155)
                tk.Label(self.one_patient_detail_frame,text='Location',background=color,font=('Ariel 8 bold')).place(x=15,y=175)
                tk.Label(self.one_patient_detail_frame,text=self.location,background=color,font=('Ariel 8 bold')).place(x=95,y=175)
        self.one_patient_detail_frame.pack()

    def all_patient_detail_menu(self):
        # redirect detail page declaring through menu button Detail > all patient
        self.home_frame.destroy()
        self.one_patient_detail_frame.destroy()
        self.all_patient_detail_frame.destroy()
        self.update_frame.destroy()
        self.delete_frame.destroy()
        self.__init__(self.window)

        sql = "SELECT * from patient"
        c.execute(sql)
        self.all_data = c.fetchall()
        row = 2
        column = 0
        self.column_name = ['Patient Id','Name','Age','Gender','Phone no','Location']
        for i in range(len(self.column_name)):
            tk.Label(self.all_patient_detail_frame,text=self.column_name[i],font=('Ariel 10 bold')).grid(row=2,column=i*2,sticky='ns')
            Separator(self.all_patient_detail_frame,orient=VERTICAL).grid(row=2,column=i*2+1,sticky='ns')
        for i in range(len(self.all_data)):
            for j in range(6):
                tk.Label(self.all_patient_detail_frame,text=self.all_data[i][j],font=('Ariel 10 bold')).grid(row=row+2,column=column*2,sticky='ns')
                Separator(self.all_patient_detail_frame,orient=VERTICAL).grid(row=row+2,column=column*2+1,sticky='ns')
                column += 1
            column = 0
            row += 1

        self.all_patient_detail_frame.pack()
    
    def update_menu(self):
        # redirect update page declaring through menu button update
        self.home_frame.destroy()
        self.one_patient_detail_frame.destroy()
        self.all_patient_detail_frame.destroy()
        self.update_frame.destroy()
        self.delete_frame.destroy()
        self.__init__(self.window)

        self.main_label = Label(self.update_frame,font=('Ariel 20 bold'),text='Update Patient Info',bg=color)
        self.main_label.place(x=55,y=2)
        tk.Label(self.update_frame,text='Enter Patient Id here',background=color).place(x=15,y=45)
        self.id = tk.Entry(self.update_frame)
        self.id.place(x=135,y=45)
        Button(self.update_frame,text='Search',bg='green',command=self.show_patient_detail).place(x=265,y=45)

        self.update_frame.pack(fill='both',expand=True)

    def show_patient_detail(self):
        # show patient info for updating
        self.id = self.id.get()
        if self.id == '':
            messagebox.showwarning('Warring','Please Enter Patient Id')
        else:
            sql = "SELECT * FROM patient WHERE p_id LIKE ?"
            self.response = c.execute(sql,(self.id,))

            for self.detail_data in self.response:
                self.id = self.detail_data[0]
                self.name = self.detail_data[1]
                self.age = self.detail_data[2]
                self.gender = self.detail_data[3]
                self.phone_no = self.detail_data[4]
                self.location = self.detail_data[5]

                tk.Label(self.update_frame,text='Patient Id',background=color).place(x=15,y=75)
                self.p_id = tk.Entry(self.update_frame,width=30)
                self.p_id.place(x=95,y=75)
                self.p_id.insert(END,self.id)

                tk.Label(self.update_frame,text='Patient Name',background=color).place(x=15,y=105)
                self.p_name = tk.Entry(self.update_frame,width=30)
                self.p_name.place(x=95,y=105)
                self.p_name.insert(END,self.name)

                tk.Label(self.update_frame,text='Patient Age',background=color).place(x=15,y=135)
                self.p_age = tk.Entry(self.update_frame)
                self.p_age.place(x=95,y=135)
                self.p_age.insert(END,self.age)

                self.p_gender_value = IntVar()
                if self.gender == 'Male':
                    self.p_gender_value.set(1)
                elif self.gender == 'Female':
                    self.p_gender_value.set(2)
                else:
                    print('Not Selected')
                tk.Label(self.update_frame,text='Gender',background=color).place(x=15,y=165)
                tk.Radiobutton(self.update_frame,text='Male',value=1,variable=self.p_gender_value,style='color.TRadiobutton').place(x=95,y=165)
                tk.Radiobutton(self.update_frame,text='Female',value=2,variable=self.p_gender_value,style='color.TRadiobutton').place(x=155,y=165)

                tk.Label(self.update_frame,text='Phone no',background=color).place(x=15,y=195)
                self.p_phone_no = tk.Entry(self.update_frame,width=30)
                self.p_phone_no.place(x=95,y=195)
                self.p_phone_no.insert(END,self.phone_no)

                tk.Label(self.update_frame,text='Location',background=color).place(x=15,y=225)
                self.p_location = tk.Entry(self.update_frame,width=30)
                self.p_location.place(x=95,y=225)
                self.p_location.insert(END,self.location)

                Button(self.update_frame,text='Update',width=25,bg='green',command=self.update_patient).place(x=95,y=255)
        self.update_frame.pack()
    
    def update_patient(self):
        # update patient info
        self.id = self.p_id.get()
        self.name = self.p_name.get()
        self.age = self.p_age.get()

        if self.p_gender_value.get() == 1:
            self.gender = 'Male'
        elif self.p_gender_value.get() == 2:
            self.gender = 'Female'
        else:
            self.gender = 'Not Selected'
        self.phone_no = self.p_phone_no.get()
        self.location = self.p_location.get()

        if self.id == '' or self.name == '' or self.age == '' or self.gender == '' or self.phone_no == '' or self.location == '':
            messagebox.showwarning('Warring','Please fill up every options')
        else:
            query = "UPDATE patient SET p_id=?, name=?, age=?, gender=?, phone_no=?, location=? WHERE p_id LIKE ?"
            c.execute(query,(self.id, self.name, self.age, self.gender, self.phone_no, self.location, self.p_id.get(),))
            conn.commit()
            messagebox.showinfo('Success', '\n Patient '+str(self.name)+' is successfully updated')

        self.update_frame.destroy()
        self.__init__(self.window)
        self.update_menu()
        self.update_frame.pack()

    def delete_menu(self):
        # redirect delete page declaring through menu button Delete
        self.home_frame.destroy()
        self.one_patient_detail_frame.destroy()
        self.all_patient_detail_frame.destroy()
        self.update_frame.destroy()
        self.__init__(self.window)

        self.main_label = Label(self.delete_frame,font=('Ariel 20 bold'),text='Delete Patient Info',bg=color)
        self.main_label.place(x=55,y=2)
        tk.Label(self.delete_frame,text='Enter Patient Id here',background=color).place(x=15,y=45)
        self.id = tk.Entry(self.delete_frame)
        self.id.place(x=135,y=45)
        Button(self.delete_frame,text='Delete',bg='red',command=self.delete_patient).place(x=265,y=45)

        self.delete_frame.pack()
    
    def delete_patient(self):
        # delete patient
        self.id = self.id.get()
        if self.id == '':
            messagebox.showwarning('Warring','Please Enter Patient Id')
        else:
            status = messagebox.askyesno('Delete patient','Are you sure?')

            if status == True:
                sql = "DELETE FROM patient WHERE p_id LIKE ?"
                self.response = c.execute(sql,(self.id,))
                messagebox.showinfo('Success', 'Patient delete Successfully')
                
                self.delete_frame.destroy()
                self.__init__(self.window)
                self.delete_menu()
            else:
                self.delete_frame.destroy()
                self.__init__(self.window)
                self.delete_menu()


def app_menubar():
    # app section
    main_menu = Menu()
    window.config(menu=main_menu)
    home_menu = Menu(main_menu,tearoff=False)
    main_menu.add_cascade(label='Home',menu=home_menu)
    home_menu.add_command(label='Register',command=app.home_menu)
    home_menu.add_command(label='Exit',command=window.quit)
    update_menu = Menu(main_menu,tearoff=False)
    main_menu.add_cascade(label='Detail',menu=update_menu)
    update_menu.add_command(label='One Patient',command=app.one_patent_detail_menu)
    update_menu.add_command(label='All Patient',command=app.all_patient_detail_menu)
    main_menu.add_cascade(label='Update',command=app.update_menu)
    main_menu.add_cascade(label='Delete',command=app.delete_menu)

window = Tk()
app = PatientApp(window)
window.title('Patient Management Kit')
window.iconbitmap(r'img/app_icon.ico')
window.geometry('400x350')
window.resizable(False,False)
window.config(menu=app_menubar())
app.home_page()
window.mainloop()