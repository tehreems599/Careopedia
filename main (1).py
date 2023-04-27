# import tkinker module
from tkinter import *

from Careopedia import specifyrolewin, bmi_calculator, disease, MOODTRACKER, health


def get1():
    specifyrolewin.SpecifyRole()
def get2():
    bmi_calculator
def get3():
    disease.options()
def get4():
    MOODTRACKER.mood_tracker()
def get5():
    health.health()
class mainpage(Tk):
    def __init__(self):

        #Creating object 'root' of Tk()
        root = Tk()

        #Providing Geometry to the form
        root.geometry("1800x1800")

        #Providing title to the form
        root.title('Cardeopedia')

        root.configure(background = "pink")

        label =Label(root,text="WELCOME TO MY CARDEOPEDIA", justify=CENTER, font=("Arial", 40, "italic", "bold", "underline"), bg='pink', bd= 20)
        label.place(x=400,y=30)

        # picture label

        pic1 = PhotoImage(file="plus.png")
        pic1 = pic1.subsample(3, 3)
        pic1label = Label(root, image=pic1)
        pic1label.place(x=0,y=0)

        pic2 = PhotoImage(file="medical.png")
        pic2label = Label(root, image=pic2, width=500, height=500)

        pic2label.place(x=1000, y=250)


        Font = ("arial", 20, "italic", "bold")

        # Creating the buttons
        Button(root, text='View User Profile', width=20, bg="red", command=get1, fg='white', font=Font, bd=20).place(x=100, y=300)
        #
        #
        Button(root, text='Disease Diagnosis', width=20, bg="red", fg='white',command=get3, font=Font, bd=20).place(x=550, y=300)
        #
        Button (root, text='Calculate BMI', width=20, bg="red", command=get2,fg='white',font=Font, bd=20).place(x=100, y=460)

        Button (root, text='Mood Tracker', width=20, bg="red", fg='white', command=get4,font=Font, bd=20).place(x=550, y=460)

        Button (root, text='Health Blogs', width=20, bg="red", command=get5,fg='white', font=Font, bd=20).place(x=300, y=620)



        root.mainloop()

mainpage()
