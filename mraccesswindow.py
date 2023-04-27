import tkinter
from tkinter import *
from PIL import ImageTk,Image
# import python_mysql_connect
import mysql.connector

# import main
# import specifyrolewin

# mydb = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='xyz1234',
#     port='3306',
#     database='careopedia')

mydb=mysql.connector.connect(host="localhost",user="root",passwd="hell0w0rld!*",database="careopedia")

mycursor=mydb.cursor()
mycursor = mydb.cursor(buffered=True)

class MRAccess(tkinter.Tk):
    def __init__(self):
        global entry_1
        root = Tk()
        root.geometry('500x300')
        root.resizable(0, 0)
        root.title("Medical Records")
        root.configure(bg='pink')
        label_0 = Label(root, text="MEDICAL PROFILE ACCESS", justify=CENTER,
                        font=("Arial", 20, "italic", "bold", "underline"), bg='pink', bd=20)
        label_0.place(x=20, y=53)
        label_1 = Label(root, text="Enter MR no.", width=25, bg='pink', justify=CENTER,
                        font=("arial", 12, "italic", "bold"))
        label_1.place(x=20, y=130)

        entry_1 = Entry(root, width=25, bd=5)
        entry_1.place(x=220, y=130)
        # print(a1)
        def showProfile():
            self = entry_1.get()
            root1 = Tk()
            root1.geometry('700x700')
            root1.resizable(0, 0)
            root1.title("Medical Records")
            root1.configure(bg='pink')
            label_0 = Label(root1, text="MEDICAL RECORD", justify=CENTER,
                            font=("Arial", 20, "italic", "bold", "underline"), bg='pink', bd=20)
            label_0.place(x=130, y=53)
            label_1 = Label(root1, text="First Name:", width=25, bg='pink', justify=CENTER,
                            font=("arial", 15, "italic", "bold"))
            label_1.place(x=30, y=130)

            mycursor.execute("SELECT patient_fname FROM mrno_records WHERE mr_no='" + self + "'")
            q1 = mycursor.fetchall()
            label_12 = Label(root1, text=q1, width=25, bg='pink', justify=CENTER,
                             font=("arial", 15, "italic", "bold"))
            label_12.place(x=240, y=130)

            label_2 = Label(root1, text="Last Name:", width=25, bg='pink', justify=CENTER,
                            font=("arial", 15, "italic", "bold"))
            label_2.place(x=30, y=180)
            mycursor.execute("SELECT patient_lname FROM mrno_records WHERE mr_no='" + self + "'")
            q2 = mycursor.fetchall()
            label_22 = Label(root1, text=q2, width=25, bg='pink', justify=CENTER,
                             font=("arial", 15, "italic", "bold"))
            # entry_2 = Entry(root1)
            label_22.place(x=240, y=180)

            label_3 = Label(root1, text="Gender:", width=25, bg='pink', justify=CENTER,
                            font=("arial", 15, "italic", "bold"))
            label_3.place(x=30, y=230)
            mycursor.execute('SELECT gender from mrno_records where mr_no="' + self + '"')
            q3 = mycursor.fetchall()
            label_32 = Label(root1, text=q3, width=25, bg='pink', justify=CENTER,
                             font=("arial", 15, "italic", "bold"))
            label_32.place(x=240, y=230)

            label_4 = Label(root1, text="Weight:", width=25, bg='pink', justify=CENTER,
                            font=("arial", 15, "italic", "bold"))
            mycursor.execute("SELECT Weight from mrno_records where mr_no='" + self + "'")
            label_4.place(x=30, y=280)
            q4 = mycursor.fetchall()
            label_42 = Label(root1, text=q4, width=25, bg='pink', justify=CENTER,
                             font=("arial", 15, "italic", "bold"))
            label_42.place(x=240, y=280)
            # entry_4 = Entry(root1)
            # entry_4.place(x=240, y=280)
            label_5 = Label(root1, text="Age:", width=25, bg='pink', justify=CENTER,
                            font=("arial", 15, "italic", "bold"))
            label_5.place(x=30, y=330)
            mycursor.execute('SELECT Age from mrno_records where mr_no="' + self + '"')
            q5 = mycursor.fetchall()
            label_52 = Label(root1, text=q5, width=25, bg='pink', justify=CENTER,
                             font=("arial", 15, "italic", "bold"))
            label_52.place(x=240, y=330)
            # entry_5 = Entry(root1)
            # entry_5.place(x=240, y=320)
            label_61 = Label(root1, text="Blood Group:", width=25, bg='pink', justify=CENTER,
                             font=("arial", 15, "italic", "bold"))
            label_61.place(x=20, y=380)
            mycursor.execute('SELECT blood_group from mrno_records where mr_no="' + self + '"')
            q6 = mycursor.fetchall()
            label_62 = Label(root1, text=q6, width=25, bg='pink', justify=CENTER,
                             font=("arial", 15, "italic", "bold"))
            label_62.place(x=240, y=380)
            label_6 = Label(root1, text="Heart Disease:", width=25, bg='pink', justify=CENTER,
                            font=("arial", 15, "italic", "bold"))
            label_6.place(x=20, y=430)
            mycursor.execute('SELECT heart_diseases from mrno_records where mr_no="' + self + '"')
            q8 = mycursor.fetchall()
            label_63 = Label(root1, text=q8, width=25, bg='pink', justify=CENTER,
                             font=("arial", 15, "italic", "bold"))
            label_63.place(x=240, y=430)
            label_7 = Label(root1, text="Liver Disease:", width=25, bg='pink', justify=CENTER,
                            font=("arial", 15, "italic", "bold"))
            label_7.place(x=20, y=480)
            mycursor.execute('SELECT liver_diseases from mrno_records where mr_no="' + self + '"')
            q9 = mycursor.fetchall()
            label_71 = Label(root1, text=q9, width=25, bg='pink', justify=CENTER,
                             font=("arial", 15, "italic", "bold"))
            label_71.place(x=240, y=480)
            label_8 = Label(root1, text="Diabeties:", width=25, bg='pink', justify=CENTER,
                            font=("arial", 15, "italic", "bold"))
            label_8.place(x=20, y=530)
            mycursor.execute('SELECT diabetes_diseases from mrno_records where mr_no="' + self + '"')
            q10 = mycursor.fetchall()
            label_81 = Label(root1, text=q10, width=25, bg='pink', justify=CENTER,
                             font=("arial", 15, "italic", "bold"))
            label_81.place(x=240, y=530)
            label_9 = Label(root1, text="Parkinson", width=25, bg='pink', justify=CENTER,
                            font=("arial", 15, "italic", "bold"))
            label_9.place(x=20, y=580)
            mycursor.execute('SELECT parkinsons_diseases from mrno_records where mr_no="' + self + '"')
            q10 = mycursor.fetchall()
            label_91 = Label(root1, text=q10, width=25, bg='pink', justify=CENTER,
                             font=("arial", 15, "italic", "bold"))
            label_91.place(x=240, y=580)
            # Button(root1, text='GO BACK', width=10, bg="red" fg='white', font=('arial', 12, "italic", "bold"),
            #        bd=14).place(
            #     x=230, y=640)
            root1.mainloop()
        Button(root, text='SUBMIT', width=10, bg="red", fg='white', command=lambda: [ showProfile(),root.destroy()],
               font=('arial', 12, "italic", "bold"), bd=14).place(
            x=120, y=190)
        # Button(root, text='GO BACK', width=10, bg="red", fg='white', command=lambda: [main.mainpage(), root.destroy()],
        #        font=('arial', 12, "italic", "bold"), bd=14).place(
        #     x=230, y=190)
        root.mainloop()

# MRAccess()
# MRAccess.accessWin(self)


