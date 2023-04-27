import tkinter
from tkinter import *
from PIL import ImageTk,Image

import draccess
import mraccesswindow
import staffactivities


class SpecifyRole(Tk):
    def __init__(self):
        root = Tk()
        root.geometry('500x300')
        root.resizable(0,0)
        root.title("Specify your role")
        root.configure(bg='pink')
        label_0 = Label(root, text="SPECIFY YOUR ROLE", justify=CENTER,
                        font=("Arial", 20, "italic", "bold", "underline"), bg='pink', bd=20)
        label_0.place(x=60, y=33)
        label_1 = Label(root, text="Choose the correct option:", width=25, bg='pink', justify=CENTER,
                        font=("arial", 15, "italic", "bold"))
        label_1.place(x=80, y=100)
        Button(root, text='Medical Staff', width=20, bg="red", fg='white',command=lambda:[root.destroy(),staffactivities.StaffPanel()],
                    font=('arial', 12, "italic", "bold"),
                    bd=14).place(x=110, y=140)
        Button(root, text='General Viewer', width=20, bg="red", fg='white',command=lambda:[root.destroy(),mraccesswindow.MRAccess()],
                    font=('arial', 12, "italic", "bold"), bd=14).place(x=110, y=210)


        root.mainloop()
        # root.exit()
