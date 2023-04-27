from tkinter import *
from PIL import ImageTk, Image
import webbrowser as wb
import random
#MAIN WINDOW
class health(Tk):
    def __init__(self):
        root = Tk()
        root.geometry("1800x1800")
        topFrame = Frame(root)
        topFrame.pack(side= TOP)
        bottomFrame = Frame(root)
        bottomFrame.pack(side=BOTTOM)
        rightFrame=Frame(root)
        rightFrame.pack(side=RIGHT)
        root.title('Health blogs')
         #set window color
        root.configure(bg='pink')
        #SETTING TITLE OF SCREEN
        l = Label(root, text ="CAREOPEDIA", justify= CENTER, font=("Arial", 30,"italic","bold","underline"),bd=20, fg="black",bg="pink")
        l.place(x=800, y=100, anchor=CENTER)
        l2 = Label(root, text ="Health blogs", justify= CENTER, font=("Arial", 20,"italic","bold","underline"),bd=20,fg="black", bg="pink")
        l2.place(x=800, y=250, anchor=CENTER)
        l3 = Label(root, text ="_________________________________________________________________________", justify= CENTER, font=("Arial", 30,"italic","bold","underline"),bd=20, fg="black",bg="pink")
        l3.place(x=800, y=175, anchor=CENTER)
        #CREATE BUTTON FUNCTIONALITIES
        def  b1():
            wb.open("https://www.webmd.com")
            return
        def  b2():
            wb.open("https://www.medicalnewstoday.com")
            return
        def  b3():
            wb.open("https://www.foodpolitics.com")
            return
        def  b4():
            wb.open("https://www.healthline.com")
            return
        #HEALTH BLOG BUTTONS
        button1 = Button(root,text="Health Blog 1 by",font=("Arial", 20,"italic","bold","underline"),fg="white",bg="red")
        button1.place(x=300,y=300)
        button1['command']=b1
        button2 = Button(root,text="Health Blog 2 by",font=("Arial", 20,"italic","bold","underline"),fg="white",bg="red")
        button2.place(x=950,y=300)
        button2['command']=b2
        button3 = Button(root,text="Health Blog 3 by",font=("Arial", 20,"italic","bold","underline"),fg="white",bg="red")
        button3.place(x=300,y=400)
        button3['command']=b3
        button4 = Button(root,text="Health Blog 4 by",font=("Arial", 20,"italic","bold","underline"),fg="white",bg="red")
        button4.place(x=950,y=400)
        button4['command']=b4
        button5 = Button(root,text="Back",justify=RIGHT,font=("Arial",20,"italic","bold","underline"),bd=20,fg="white",bg="red")
        button5.place(relx=0.8,rely=0.8)
        button5['command']=root.destroy
        #CREATING HEALTH TIPS GENERATOR
        def popupmsg(self):
                    root = Tk()
                    root.title("health tips")
                    health_tips = ["Drink at least 8 glasses of water per day","Good ways to improve gut health include eating probiotic foods like yogurt","Vegetables and fruits are loaded with prebiotic fiber, vitamins, minerals, and antioxidants","Reduce your salt intake to 5g per day, equivalent to about one teaspoon","Fats consumed should be less than 30% of your total energy intake","Check your blood pressure regularly to avoid hyper tension"]
                    random_num = random.choice(health_tips)
                    h=str(random_num)
                    label = Label(root, text=h)
                    label.pack(side='top',fill='x',pady=10)
                    B1 = Button(root, text="Got it!", command = root.destroy)
                    B1.pack(side=RIGHT)
                    root.mainloop()
        a = Button(root,text="Health tips",font=("Arial",15,"bold"),bd=20,fg='white',bg='red')
        a['command']=popupmsg
        a.place(relx=0.45,rely=0.82)
        root.mainloop()

