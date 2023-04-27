import mysql.connector

# mydb = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='xyz1234',
#     database='careopedia')

mydb=mysql.connector.connect(host="localhost",user="root",passwd="hell0w0rld!*",database="careopedia")

mycursor=mydb.cursor(buffered=True)
import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

class heart(tkinter.Tk):
    def __init__(self):
        def detection():
            # importing the libraries
            import numpy as np
            import pandas as pd
            from sklearn.model_selection import train_test_split
            from sklearn.preprocessing import StandardScaler
            from sklearn import svm
            from sklearn.metrics import accuracy_score

            # loadind the data from csv file to a Pandas DataFrame
            heart_data = pd.read_csv('heart.csv')

            # 1...>Heart Disease positive
            # 0...>Healthy

            # Separating the features & Target

            X = heart_data.drop(columns=['target'], axis=1)
            Y = heart_data['target']

            # Splitting the data into training data & testing data
            X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)
            # print(X.shape, X_train.shape, X_test.shape)

            # Data Standardization
            scaler = StandardScaler()
            scaler.fit(X_train)

            X_train = scaler.transform(X_train)
            X_test = scaler.transform(X_test)

            # Model training
            # Support Vector Machine Model
            model = svm.SVC(kernel='linear')
            # TRAINING THE SVM MODEL  WITH TRAINING DATA
            model.fit(X_train, Y_train)

            # MODEL EVALUATION

            # ACCURACY SCORE ON TRAINING DATA
            X_train_prediction = model.predict(X_train)
            training_data_accuracy = accuracy_score(Y_train, X_train_prediction)

            # ACCURACY SCORE ON Test DATA
            X_test_prediction = model.predict(X_test)
            test_data_accuracy = accuracy_score(Y_test, X_test_prediction)

            # Building a predictive system:
            
            e1=entry_1.get()
            e2=entry_2.get()
            e3=entry_3.get()
            e4 =entry_4.get()
            e5 =entry_5.get()
            e6 =entry_6.get()
            e7 =entry_7.get()
            e8 =entry_8.get()
            e9 =entry_9.get()
            e10 = entry_10.get()
            e11 = entry_11.get()
            e12 = entry_12.get()
            e13 = entry_13.get()
            e14 = entry_14.get()
            
            try:
                input_data = (e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13)
                # changing the input data into numpy array
                input_data_numpy_array = np.asarray(input_data)

                # Reshape the numpy array
                input_data_reshaped = input_data_numpy_array.reshape(1, -1)

                # standarize the input data
                std_input_data = scaler.transform(input_data_reshaped)

                prediction = model.predict(std_input_data)
                print(prediction)

                if prediction[0] == 0:
                    messagebox.showinfo("Diseases report", "The person does not have Heart Disease")
                    print("The person does not have Heart Disease")
                    sql = "UPDATE mrno_records SET heart_diseases ='NO' WHERE mr_no = '"+e14+"'"
                    mycursor.execute(sql)
                    mydb.commit()
                else:
                    messagebox.showinfo("Diseases report", "The person have Heart Disease")
                    print('The person have Heart Disease')
                    sql = "UPDATE mrno_records SET heart_diseases ='YES' WHERE mr_no = '"+e14+"' "
                    mycursor.execute(sql)
                    mydb.commit()
            except Exception as e:
                messagebox.showerror("Error", e)

            entry_1.delete(0,END)
            entry_2.delete(0,END)
            entry_3.delete(0,END)
            entry_4.delete(0,END)
            entry_5.delete(0,END)
            entry_6.delete(0,END)
            entry_7.delete(0,END)
            entry_8.delete(0,END)
            entry_9.delete(0,END)
            entry_10.delete(0,END)
            entry_11.delete(0,END)
            entry_12.delete(0,END)
            entry_13.delete(0,END)
            entry_14.delete(0,END)
            
        #Creating object 'root' of Tk()
        root = Toplevel()

        #Providing Geometry to the form
        root.geometry("1800x1800")

        #Providing title to the form
        root.title('Careopedia')

        root.configure(background = "pink")

        label =Label(root,text="HEART DISEASE DIAGNOSIS", justify=CENTER, font=("Arial", 40, "italic", "bold", "underline"), bg='pink', bd= 20)
        label.place(x=400,y=30)

        # picture label

        img = tkinter.PhotoImage(file="heart_symptoms.png")
        imglabel = tkinter.Label(root, image=img, width=550, height=620)
        imglabel.place(x=900, y=150)


        label_0 =Label(root,text="Please enter the values for given parameters:", justify=CENTER, font=("Arial", 15, "italic", "bold", "underline"), bg='pink', bd= 20)
        label_0.place(x=100,y=110)

        label_1 =Label(root,text="Age", width=25, bg='pink', font=("arial",12, "italic", "bold"))
        label_1.place(x=150,y=180)

        entry_1=Entry(root, width= 25, bd=5)
        entry_1.place(x=500,y=180)

        label_2 =Label(root,text="Sex", width=25, bg='pink',font=("arial",12, "italic", "bold"))
        label_2.place(x=150,y=230)

        entry_2=Entry(root, width= 25, bd=5)
        entry_2.place(x=500,y=230)

        #the variable 'var' mentioned here holds Integer Value, by deault 0
##        var=IntVar()
##
##        Radiobutton(root,text="Male",padx= 5, variable= var, value=1, bg='pink', font=("arial",10, "italic", "bold")).place(x=500,y=230)
##        Radiobutton(root,text="Female",padx= 20, variable= var, value=2, bg='pink', font=("arial",10, "italic", "bold")).place(x=580,y=230)
##        Radiobutton(root,text="Other",padx= 20, variable= var, value=3, bg='pink', font=("arial",10, "italic", "bold")).place(x=690,y=230)

        label_3 =Label(root,text="Chest Pain Type", width=25, bg='pink',font=("arial",12, "italic", "bold"))
        label_3.place(x=150,y=280)

        entry_3=Entry(root, width= 25, bd=5)
        entry_3.place(x=500,y=280)

        label_4=Label(root,text="Resting BP",width=25, bg='pink',font=("arial",12, "italic", "bold"))
        label_4.place(x=150,y=320)

        entry_4=Entry(root, width= 25, bd=5)
        entry_4.place(x=500,y=320)

        label_5=Label(root,text="cholestoral",width=25, bg='pink',font=("arial",12, "italic", "bold"))
        label_5.place(x=150,y=360)

        entry_5=Entry(root, width= 25, bd=5)
        entry_5.place(x=500,y=360)

        label_6=Label(root,text="fasting blood sugar",width=25, bg='pink',font=("arial",12, "italic", "bold"))
        label_6.place(x=150,y=400)

        entry_6=Entry(root, width= 25, bd=5)
        entry_6.place(x=500,y=400)

        label_7=Label(root,text="electrocardiographic result",width=25, bg='pink',font=("arial",12, "italic", "bold"))
        label_7.place(x=150,y=440)

        entry_7=Entry(root, width= 25, bd=5)
        entry_7.place(x=500,y=440)

        label_8=Label(root,text="Maximum Heart Rate",width=25, bg='pink',font=("arial",12, "italic", "bold"))
        label_8.place(x=150,y=480)

        entry_8=Entry(root, width= 25, bd=5)
        entry_8.place(x=500,y=480)

        label_9=Label(root,text="Exercise Induced Angina",width=25, bg='pink',font=('arial',12, "italic", "bold"))
        label_9.place(x=150,y=520)

        entry_9=Entry(root, width= 25, bd=5)
        entry_9.place(x=500,y=520)

        label_10=Label(root,text="Oldpeak",width=25, bg='pink',font=('arial',12, "italic", "bold"))
        label_10.place(x=150,y=560)

        entry_10=Entry(root, width= 25, bd=5)
        entry_10.place(x=500,y=560)

        label_11=Label(root,text="Slope",width=25, bg='pink',font=('arial',12, "italic", "bold"))
        label_11.place(x=150,y=600)

        entry_11=Entry(root, width= 25, bd=5)
        entry_11.place(x=500,y=600)

        label_12=Label(root,text="Number of Major Vessels",width=25, bg='pink',font=('arial',12, "italic", "bold"))
        label_12.place(x=150,y=640)

        entry_12=Entry(root, width= 25, bd=5)
        entry_12.place(x=500,y=640)

        label_13=Label(root,text="Thal",width=25, bg='pink',font=('arial',12, "italic", "bold"))
        label_13.place(x=150,y=680)

        entry_13=Entry(root, width= 25, bd=5)
        entry_13.place(x=500,y=680)

        label_14=Label(root,text="MR No.",width=25, bg='pink',font=('arial',12, "italic", "bold"))
        label_14.place(x=150,y=720)

        entry_14=Entry(root, width= 25, bd=5)
        entry_14.place(x=500,y=720)

    
        #this creates button for submitting the details provides by the user
        Button(root, text='SUBMIT' , width=20,bg="red",fg='white',font=('arial',12, "italic", "bold"), bd=14,command=detection).place(x=260,y=760)


        #this will run the mainloop.
        root.mainloop()

