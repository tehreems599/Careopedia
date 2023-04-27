import tkinter
from tkinter import *
from tkinter import messagebox

from PIL import ImageTk,Image
# import python_mysql_connect
import mysql.connector

import mraccesswindow

# mydb = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='xyz1234',
#     port='3306',
#     database='careopedia')

mydb=mysql.connector.connect(host="localhost",user="root",passwd="hell0w0rld!*",database="careopedia")

mycursor=mydb.cursor()
class StaffPanel(tkinter.Tk):
    def __init__(self):
        root1 = Tk()
        root1.geometry('600x400')
        root1.resizable(0,0)
        root1.title("Staff Panel")
        root1.configure(bg='pink')
        label_0 = Label(root1, text="WELCOME TO THE STAFF PANEL", justify=CENTER,
                        font=("Arial", 20, "italic", "bold", "underline"), bg='pink', bd=20)
        label_0.place(x=50, y=70)
        label_1 = Label(root1, text="Please choose one option:", width=25, bg='pink', justify=CENTER,
                        font=("arial", 15, "italic", "bold"))
        label_1.place(x=140, y=190)
        b1=Button(root1, text='Add new Patient', width=20, bg="red", fg='white',command=lambda:[root1.destroy(),AddNewPatient()],font=('arial', 12, "italic", "bold"), bd=14).place(x=180, y=230)
        b2=Button(root1, text='View Medical Profile', width=20, bg="red", fg='white',command=lambda:[root1.destroy(),mraccesswindow.MRAccess()], font=('arial', 12, "italic", "bold"),bd=14).place(x=180, y=300)

        #
        # mrNo_data = pd.read_csv('Downloads/admin.csv')

        root1.mainloop()

class AddNewPatient(tkinter.Tk):
    def __init__(self):
        def viewSelected():
            global e3
            choice = var.get()
            if choice == 1:
                e3 = "Male"

            elif choice == 2:
                e3 = "Female"

            elif choice == 3:
                e3 = "Others"
            return e3
        def enterintodb():
            viewSelected()
            e1 = entry_1.get()
            e12 = entry_12.get()
            e2 = entry_2.get()
            # e3 = var.get()
            e4 = entry_4.get()
            e5 = entry_5.get()
            e6 = entry_6.get()
            e7=entry_7.get()
            e8=entry_8.get()
            e9=entry_9.get()
            e11=entry_11.get()
            enteries=[e11,e1,e12,e2,e5,e4,e3,e6,e7,e8,e9]
            x=e11.strip("'")
            mycursor.execute('Select `mr_no` from `mrno_records`')
            a = mycursor.fetchall()
            final_result = [list(i) for i in a]
            b=[list(i) for i in final_result]
            c=[list(i) for i in b]
            if x not in c:
                    sql = 'INSERT INTO `mrno_records` (`mr_no`,`patient_fname`,`patient_lname`,`blood_group`, `Age`, `Weight`, `gender`,`heart_diseases`,`liver_diseases`,`diabetes_diseases`,`parkinsons_diseases`) VALUES (%s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s)'

                    mycursor.execute(sql, enteries)
                    # rec += [e11]
                    mydb.commit()
                    messagebox.showinfo("Record Added", "Patient record has been addedd successfully")
            else:
                messagebox.showerror("Record Added", "Patient record has been addedd successfully")


        root1 = Tk()
        root1.geometry('700x700')
        root1.resizable(0,0)
        root1.title("Add new patient")
        root1.configure(bg='pink')
        label_0 = Label(root1, text="ADD A NEW PATIENT", justify=CENTER,
                        font=("Arial", 30, "italic", "bold", "underline"), bg='pink', bd=20)
        label_0.place(x=130, y=53)

        label_1 = Label(root1, text="First Name:", width=20, bg='pink', justify=CENTER,
                        font=("arial", 15, "italic", "bold"))
        label_1.place(x=90, y=130)
        entry_1 = Entry(root1, width=25, bd=5)
        entry_1.place(x=360, y=130)
        label_12 = Label(root1, text="Last Name:", width=20, bg='pink', justify=CENTER,
                        font=("arial", 15, "italic", "bold"))
        label_12.place(x=90, y=170)
        entry_12 = Entry(root1, width= 25, bd=5)
        entry_12.place(x=360, y=170)
        label_2 = Label(root1, text="Blood Group:", width=20, bg='pink', justify=CENTER,
                        font=("arial", 15, "italic", "bold"))
        label_2.place(x=90, y=220)

        entry_2 = Entry(root1,  width= 25, bd=5)
        entry_2.place(x=360, y=220)

        label_3 = Label(root1, text="Gender:", width=20, bg='pink', justify=CENTER,
                        font=("arial", 15, "italic", "bold"))
        label_3.place(x=90, y=260)
        var = IntVar()
        Radiobutton(root1, text="Male", padx=5, variable=var, value=1, bg='pink',
                    font=("arial", 10, "italic", "bold")).place(x=350, y=260)
        Radiobutton(root1, text="Female", padx=20, variable=var, value=2, bg='pink',
                    font=("arial", 10, "italic", "bold")).place(x=420, y=260)
        Radiobutton(root1, text="Other", padx=20, variable=var, value=3, bg='pink',
                    font=("arial", 10, "italic", "bold")).place(x=530, y=260)
        label_4 = Label(root1, text="Weight:", width=20, bg='pink', justify=CENTER,
                        font=("arial", 15, "italic", "bold"))
        label_4.place(x=90, y=300)
        entry_4 = Entry(root1, width= 25, bd=5)
        entry_4.place(x=360, y=300)
        label_5 = Label(root1, text="Age:", width=20, bg='pink', justify=CENTER,
                        font=("arial", 15, "italic", "bold"))
        label_5.place(x=90, y=340)
        entry_5 = Entry(root1, width= 25, bd=5)
        entry_5.place(x=360, y=340)
        label_6 = Label(root1, text="History in HEART:", width=20, bg='pink', justify=CENTER,
                        font=("arial", 15, "italic", "bold"))
        label_6.place(x=90, y=380)
        entry_6 = Entry(root1, width= 25, bd=5)
        entry_6.place(x=360, y=380)
        label_7 = Label(root1, text="History in LIVER:", width=20, bg='pink', justify=CENTER,
                        font=("arial", 15, "italic", "bold"))
        label_7.place(x=90, y=420)
        entry_7 = Entry(root1, width=25, bd=5)
        entry_7.place(x=360, y=420)
        label_8 = Label(root1, text="History in DIABETIES:", width=20, bg='pink', justify=CENTER,
                        font=("arial", 15, "italic", "bold"))
        label_8.place(x=90, y=460)
        entry_8 = Entry(root1, width=25, bd=5)
        entry_8.place(x=360, y=460)
        label_9 = Label(root1, text="History in PARKINSONS:", width=20, bg='pink', justify=CENTER,
                        font=("arial", 15, "italic", "bold"))
        label_9.place(x=90, y=500)
        entry_9 = Entry(root1, width=25, bd=5)
        entry_9.place(x=360, y=500)
        label_10 = Label(root1,
                        text="* Note: You can only enter either yes or no in past history."
                        , width=50,bg='pink', justify=CENTER,
                        font=("arial", 15, "italic", "bold"))
        label_10.place(x=80, y=540)
        label_11 = Label(root1, text="MR No.:", width=20, bg='pink', justify=CENTER,
                        font=("arial", 15, "italic", "bold"))
        label_11.place(x=90, y=580)
        entry_11 = Entry(root1, width=25, bd=5)
        entry_11.place(x=360, y=580)
        Button(root1, text='SUBMIT', width=10, bg="red", command=lambda:[enterintodb(),  root1.destroy()], fg='white', font=('arial', 12, "italic", "bold"), bd=14).place(
            x=270, y=620)

        root1.mainloop()

