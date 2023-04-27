import tkinter
from tkinter import *
from PIL import ImageTk,Image

import mraccesswindow
import python_mysql_connect
import mysql.connector
# mydb=mysql.connector.connect(host="localhost",user="root",passwd="qualifer*1",database="ayesha")
mydb=mysql.connector.connect(host="localhost",user="root",passwd="hell0w0rld!*",database="careopedia")
mycursor=mydb.cursor()
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='xyz1234',
    port='3306',
    database='careopedia'

)

mycursor=mydb.cursor()
# import tkinter
# from tkinter import *
# from PIL import ImageTk,Image
#
# import demoprofile
class ProfileDemo(tkinter.Tk):
    a1=mraccesswindow.entry_1.get()
    mycursor = python_mysql_connect.mydb.cursor()
    root1 = Tk()
    root1.geometry('600x600')
    root1.resizable(0,0)
    root1.title("Medical Records")
    root1.configure(bg='pink')
    label_0 = Label(root1, text="MEDICAL RECORD", justify=CENTER,
                    font=("Arial", 20, "italic", "bold", "underline"), bg='pink', bd=20)
    label_0.place(x=130, y=53)
    label_1 = Label(root1, text="First Name:",width=25, bg='pink', justify=CENTER,
                        font=("arial", 15, "italic", "bold"))
    label_1.place(x=30, y=130)

    q1=mycursor.execute('SELECT patient_fname from mrno_records where mr_no=" '+a1+ '"')
    label_12 = Label(root1, text=q1, width=25, bg='pink', justify=CENTER,
                        font=("arial", 15, "italic", "bold"))
    label_12.place(x=240, y=130)


    label_2 = Label(root1, text="Last Name:",width=25, bg='pink', justify=CENTER,
                        font=("arial", 15, "italic", "bold"))
    label_2.place(x=30, y=180)
    q2= mycursor.execute('SELECT patient_lname from mrno_records mr_no=" '+a1+ '"')
    label_22 = Label(root1, text=q2, width=25, bg='pink', justify=CENTER,
                        font=("arial", 15, "italic", "bold"))
    # entry_2 = Entry(root1)
    label_22.place(x=240, y=180)

    label_3 = Label(root1, text="Gender:", width=25, bg='pink', justify=CENTER,
                        font=("arial", 15, "italic", "bold"))
    label_3.place(x=30, y=230)
    q3=mycursor.execute('SELECT gender from mrno_records where mr_no=" '+a1+ '"')
    label_32 = Label(root1, text=q3, width=25, bg='pink', justify=CENTER,
                        font=("arial", 15, "italic", "bold"))
    label_32.place(x=240, y=230)

    label_4 = Label(root1, text="Weight:", width=25, bg='pink', justify=CENTER,
                        font=("arial", 15, "italic", "bold"))
    q4= mycursor.execute('SELECT Weight from mrno_records mr_no=" '+a1+ '"')
    label_4.place(x=30, y=280)
    label_42 = Label(root1, text=q4, width=25, bg='pink', justify=CENTER,
                        font=("arial", 15, "italic", "bold"))
    label_42.place(x=240, y=280)
    # entry_4 = Entry(root1)
    # entry_4.place(x=240, y=280)
    label_5 = Label(root1, text="Age:", width=25, bg='pink', justify=CENTER,
                        font=("arial", 15, "italic", "bold"))
    label_5.place(x=30, y=330)
    q5=mycursor.execute('SELECT Age from mrno_records mr_no=" '+a1+ '"')
    label_52 = Label(root1, text=q5,width=25, bg='pink', justify=CENTER,
                        font=("arial", 15, "italic", "bold"))
    label_52.place(x=240, y=330)
    # entry_5 = Entry(root1)
    # entry_5.place(x=240, y=320)
    label_61 = Label(root1, text="Blood Group:", width=25, bg='pink', justify=CENTER,
                    font=("arial", 15, "italic", "bold"))
    label_61.place(x=20, y=380)
    q6=mycursor.execute('SELECT Blood group from mrno_records mr_no=" '+a1+ '"')
    label_62 = Label(root1, text=q6, width=25, bg='pink', justify=CENTER,
                     font=("arial", 15, "italic", "bold"))
    label_62.place(x=240, y=380)
    label_6 = Label(root1, text="Past History:", width=25, bg='pink', justify=CENTER,
                  font=("arial", 15, "italic", "bold"))
    label_6.place(x=20, y=430)
    q7=mycursor.execute('SELECT disease from disease_info mr_no=" '+a1+ '"')
    label_62 = Label(root1, text="Heart Disease", width=25, bg='pink', justify=CENTER,
                        font=("arial", 15, "italic", "bold"))
    label_62.place(x=240, y=430)
    Button(root1, text='GO BACK', width=10, bg="red", fg='white', font=('arial', 12, "italic", "bold"), bd=14).place(
        x=230, y=490)

    root1.mainloop()
