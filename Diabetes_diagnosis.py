import mysql.connector

# mydb = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='xyz1234',
#     database='careopedia')

mydb=mysql.connector.connect(host="localhost",user="root",passwd="hell0w0rld!*",database="careopedia")

mycursor=mydb.cursor(buffered=True)
# import tkinker module
from tkinter import *
from tkinter import messagebox

class diabetes(Tk):
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
            diabetes_data = pd.read_csv('diabetes.csv')

            # 1...> Diabetes
            # 0...>Healthy

            # Separating the features & Target

            X = diabetes_data.drop(columns=['Outcome'], axis=1)
            Y = diabetes_data['Outcome']

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

            e1 = entry_1.get()
            e2 = entry_2.get()
            e3 = entry_3.get()
            e4 = entry_4.get()
            e5 = entry_5.get()
            e6 = entry_6.get()
            e7 = entry_7.get()
            e8 = entry_8.get()
            e9 = entry_9.get()

            try:
                input_data = (e1, e2, e3, e4, e5, e6, e7, e8)
                # changing the input data into numpy array
                input_data_numpy_array = np.asarray(input_data)

                # Reshape the numpy array
                input_data_reshaped = input_data_numpy_array.reshape(1, -1)

                # standarize the input data
                std_input_data = scaler.transform(input_data_reshaped)

                prediction = model.predict(std_input_data)
                print(prediction)

                if prediction[0] == 0:
                    messagebox.showinfo("Diseases report", "The person does not have diabetes")
                    print("The person does not have diabetes")
                    sql = "UPDATE user SET parkinsons_diseases ='NO' WHERE mr_no = '" + e9 + "'"
                    mycursor.execute(sql)
                    mydb.commit()
                else:
                    messagebox.showinfo("Diseases report", "The person have diabetes")
                    print('The person have diabetes')
                    sql = "UPDATE user SET diabetes_diseases ='YES' WHERE mr_no = '" + e9 + "' "
                    mycursor.execute(sql)
                    mydb.commit()
            except Exception as e:
                messagebox.showerror("Error", e)

            entry_1.delete(0, END)
            entry_2.delete(0, END)
            entry_3.delete(0, END)
            entry_4.delete(0, END)
            entry_5.delete(0, END)
            entry_6.delete(0, END)
            entry_7.delete(0, END)
            entry_8.delete(0, END)
            entry_9.delete(0, END)

        #Creating object 'root' of Tk()
        root = Toplevel()

        #Providing Geometry to the form
        root.geometry("1850x1850")

        #Providing title to the form
        root.title('Careopedia')

        root.configure(background = "pink")

        label =Label(root,text="DIABETES DIAGNOSIS", justify=CENTER, font=("Arial", 40, "italic", "bold", "underline"), bg='pink', bd= 20)
        label.place(x=500,y=30)

        # picture label

        img = PhotoImage(file="diabetes_symptoms.png")
        imglabel = Label(root, image=img, width=500, height=650)
        imglabel.place(x=900, y=150)

        label_0 =Label(root,text="Please enter the values for given parameters:", justify=CENTER, font=("Arial", 15, "italic", "bold", "underline"), bg='pink', bd= 20)
        label_0.place(x=100,y=110)

        label_1 =Label(root,text="Pregnancies", width=25, bg='pink', font=("arial",12, "italic", "bold"))
        label_1.place(x=150,y=180)

        entry_1=Entry(root, width= 25, bd=5)
        entry_1.place(x=500,y=180)

        label_2 =Label(root,text="Glucose", width=25, bg='pink',font=("arial",12, "italic", "bold"))
        label_2.place(x=150,y=230)

        entry_2=Entry(root, width= 25, bd=5)
        entry_2.place(x=500,y=230)

        label_3 =Label(root,text="BloodPressure", width=25, bg='pink',font=("arial",12, "italic", "bold"))
        label_3.place(x=150,y=280)

        entry_3=Entry(root, width= 25, bd=5)
        entry_3.place(x=500,y=280)

        label_4=Label(root,text="SkinThickness",width=25, bg='pink',font=("arial",12, "italic", "bold"))
        label_4.place(x=150,y=330)

        entry_4=Entry(root, width= 25, bd=5)
        entry_4.place(x=500,y=330)

        label_5=Label(root,text="Insulin",width=25, bg='pink',font=("arial",12, "italic", "bold"))
        label_5.place(x=150,y=380)

        entry_5=Entry(root, width= 25, bd=5)
        entry_5.place(x=500,y=380)

        label_6=Label(root,text="BMI",width=25, bg='pink',font=("arial",12, "italic", "bold"))
        label_6.place(x=150,y=430)

        entry_6=Entry(root, width= 25, bd=5)
        entry_6.place(x=500,y=430)

        label_7=Label(root,text="DiabetesPedigreeFunction",width=25, bg='pink',font=("arial",12, "italic", "bold"))
        label_7.place(x=150,y=480)

        entry_7=Entry(root, width= 25, bd=5)
        entry_7.place(x=500,y=480)

        label_8=Label(root,text="Age",width=25, bg='pink',font=("arial",12, "italic", "bold"))
        label_8.place(x=150,y=530)

        entry_8=Entry(root, width= 25, bd=5)
        entry_8.place(x=500,y=530)

        label_9 = Label(root, text="MR_NO", width=25, bg='pink', font=("arial", 12, "italic", "bold"))
        label_9.place(x=150, y=600)

        entry_9 = Entry(root, width=25, bd=5)
        entry_9.place(x=500, y=600)

        #this creates button for submitting the details provides by the user
        Button(root, text='SUBMIT' , width=20,bg="red",fg='white',font=('arial',12, "italic", "bold"), bd=14,command=detection).place(x=240,y=700)


        #this will run the mainloop.
        root.mainloop()

