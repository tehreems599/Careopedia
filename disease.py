# import tkinker module
from tkinter import *

from Careopedia import parkinsons_diagnosis, Diabetes_diagnosis, Liver_diagnosis, heart_diagnosis
def get1():
    Liver_diagnosis.liver()
def get2():
    heart_diagnosis.heart()
def get3():
    Diabetes_diagnosis.diabetes()
def get4():
    parkinsons_diagnosis.parkinsons()


class options(Tk):
    def __init__(self):

        #Creating object 'root' of Tk()
        root = Toplevel()

        #Providing Geometry to the form
        root.geometry("1800x1800")

        #Providing title to the form
        root.title('Cardeopedia')

        root.configure(background = "pink")

        label =Label(root,text="DISEASE DETECTION", justify=CENTER, font=("Arial", 40, "italic", "bold", "underline"), bg='pink', bd= 20)
        label.place(x=400,y=30)

        # picture label

        pic1 = PhotoImage(file="plus2.png")
        pic1 = pic1.subsample(3, 3)
        pic1label = Label(root, image=pic1)
        pic1label.place(x=0,y=0)

        pic2 = PhotoImage(file="medical2.png")
        pic2label = Label(root, image=pic2, width=500, height=500)

        pic2label.place(x=1000, y=200)


        Font = ("arial", 20, "italic", "bold")

        # Creating the buttons
        Button(root, text='LIVER DIAGNOSIS', width=30, bg="red", fg='white', command=lambda:[root.destroy(), get1()],font=Font, bd=20).place(x=370, y=200)

        Button(root, text='HEART DIAGNOSIS', width=30, bg="red", fg='white',command=lambda:[root.destroy(), get2()], font=Font, bd=20).place(x=370, y=330)

        Button(root, text='DIABETES DIAGNOSIS', width=30, bg="red", command=lambda:[root.destroy(), get3()], fg='white', font=Font, bd=20).place(x=370, y=460)

        Button(root, text='PARKINSON\'S DISEASE DIAGNOSIS', width=30, bg="red", command=lambda:[root.destroy(), get4()] ,fg='white', font=Font, bd=20).place(x=370, y=590)

       




        root.mainloop()



