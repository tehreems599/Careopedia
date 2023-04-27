import tkinter
from tkinter import *
from PIL import ImageTk,Image

import mraccesswindow
import staffactivities


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
        b1=Button(root1, text='Add new Patient', width=20, bg="red", fg='white',command=lambda:[root1.destroy(),staffactivities.AddNewPatient()],font=('arial', 12, "italic", "bold"), bd=14).place(x=180, y=230)
        b2=Button(root1, text='View Medical Profile', width=20, bg="red", fg='white',command=lambda:[root1.destroy(),mraccesswindow.MRAccess.accessWin(self)], font=('arial', 12, "italic", "bold"),bd=14).place(x=180, y=300)

        #
        # mrNo_data = pd.read_csv('Downloads/admin.csv')

        root1.mainloop()

# n=StaffPanel()
