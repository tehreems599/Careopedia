# connection python with mysql
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

class parkinsons(Tk):
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
            parkinsons_data = pd.read_csv('brain.csv')

            # 1...>Parkinsons positive
            # 0...>Healthy

            # Separating the features & Target

            X = parkinsons_data.drop(columns=['status'], axis=1)
            Y = parkinsons_data['status']

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
            e15 = entry_15.get()
            e16 = entry_16.get()
            e17 = entry_17.get()
            e18 = entry_18.get()
            e19 = entry_19.get()


            try:
                input_data = (e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e17, e16, e18)
                # changing the input data into numpy array
                input_data_numpy_array = np.asarray(input_data)

                # Reshape the numpy array
                input_data_reshaped = input_data_numpy_array.reshape(1, -1)

                # standarize the input data
                std_input_data = scaler.transform(input_data_reshaped)

                prediction = model.predict(std_input_data)
                print(prediction)

                if prediction[0] == 0:
                    messagebox.showinfo("Diseases report", "The person does not have parkinsons")
                    print("The person does not have parkinsons")
                    sql = "UPDATE mrno_records SET parkinsons_diseases ='NO' WHERE mr_no = '"+e19+"'"
                    mycursor.execute(sql)
                    mydb.commit()
                else:
                    messagebox.showinfo("Diseases report", "The person have parkinsons")
                    print('The person have parkinsons')
                    sql = "UPDATE mrno_records SET parkinsons_diseases ='YES' WHERE mr_no = '"+e19+"' "
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
            entry_15.delete(0,END)
            entry_16.delete(0,END)
            entry_17.delete(0,END)
            entry_18.delete(0,END)
            entry_19.delete(0, END)
        #Creating object 'root' of Tk()
        root = Toplevel()
        

        #Providing Geometry to the form
        root.geometry("1850x1850")

        #Providing title to the form
        root.title('Careopedia')

        root.configure(background = "pink")

        label =Label(root,text="PARKINSONS DISEASE DIAGNOSIS", justify=CENTER, font=("Arial", 40, "italic", "bold", "underline"), bg='pink')
        label.place(x=300,y=30)

        label_0 =Label(root,text="Please enter the values for given parameters:", justify=CENTER, font=("Arial", 15, "italic", "bold", "underline"), bg='pink')
        label_0.place(x=100,y=120)

        label_1 =Label(root,text="MDVP:Avg Vocal Fundamental Frequency", width=35, bg='pink', font=("arial",12, "italic", "bold"))
        label_1.place(x=150,y=200)

        entry_1=Entry(root, width= 25, bd=5)
        entry_1.place(x=550,y=200)

        label_2 =Label(root,text="MDVP:Max Vocal Fundamental Frequency", width=35, bg='pink',font=("arial",12, "italic", "bold"))
        label_2.place(x=150,y=250)

        entry_2=Entry(root, width= 25, bd=5)
        entry_2.place(x=550,y=250)

        label_3 =Label(root,text="MDVP:Min Vocal Fundamental Frequency", width=35, bg='pink',font=("arial",12, "italic", "bold"))
        label_3.place(x=150,y=300)

        entry_3=Entry(root, width= 25, bd=5)
        entry_3.place(x=550,y=300)

        label_4=Label(root,text="MDVP:Jitter(%)",width=35, bg='pink',font=("arial",12, "italic", "bold"))
        label_4.place(x=150,y=350)

        entry_4=Entry(root, width= 25, bd=5)
        entry_4.place(x=550,y=350)

        label_5=Label(root,text="MDVP:Jitter(Abs)",width=35, bg='pink',font=("arial",12, "italic", "bold"))
        label_5.place(x=150,y=400)

        entry_5=Entry(root, width= 25, bd=5)
        entry_5.place(x=550,y=400)

        label_6=Label(root,text="MDVP:PPQ",width=35, bg='pink',font=("arial",12, "italic", "bold"))
        label_6.place(x=150,y=450)

        entry_6=Entry(root, width= 25, bd=5)
        entry_6.place(x=550,y=450)

        label_7=Label(root,text="Jitter:DDP",width=35, bg='pink',font=("arial",12, "italic", "bold"))
        label_7.place(x=150,y=500)

        entry_7=Entry(root, width= 25, bd=5)
        entry_7.place(x=550,y=500)

        label_8=Label(root,text="MDVP:Shimmer",width=35, bg='pink',font=("arial",12, "italic", "bold"))
        label_8.place(x=150,y=550)

        entry_8=Entry(root, width= 25, bd=5)
        entry_8.place(x=550,y=550)

        label_9=Label(root,text="MDVP:Shimmer(dB)",width=35, bg='pink',font=("arial",12, "italic", "bold"))
        label_9.place(x=150,y=600)

        entry_9=Entry(root, width= 25, bd=5)
        entry_9.place(x=550,y=600)

        label_10 =Label(root,text="Shimmer:APQ3", width=35, bg='pink', font=("arial",12, "italic", "bold"))
        label_10.place(x=850,y=200)

        entry_10=Entry(root, width= 25, bd=5)
        entry_10.place(x=1250,y=200)

        label_11 =Label(root,text="Shimmer:APQ5", width=35, bg='pink',font=("arial",12, "italic", "bold"))
        label_11.place(x=850,y=250)

        entry_11=Entry(root, width= 25, bd=5)
        entry_11.place(x=1250,y=250)

        label_12 =Label(root,text="MDVP:APQ", width=35, bg='pink',font=("arial",12, "italic", "bold"))
        label_12.place(x=850,y=300)

        entry_12=Entry(root, width= 25, bd=5)
        entry_12.place(x=1250,y=300)

        label_13=Label(root,text="NHR",width=35, bg='pink',font=("arial",12, "italic", "bold"))
        label_13.place(x=850,y=350)

        entry_13=Entry(root, width= 25, bd=5)
        entry_13.place(x=1250,y=350)

        label_14=Label(root,text="HNR",width=35, bg='pink',font=("arial",12, "italic", "bold"))
        label_14.place(x=850,y=400)

        entry_14=Entry(root, width= 25, bd=5)
        entry_14.place(x=1250,y=400)

        label_15=Label(root,text="RPDE",width=35, bg='pink',font=("arial",12, "italic", "bold"))
        label_15.place(x=850,y=450)

        entry_15=Entry(root, width= 25, bd=5)
        entry_15.place(x=1250,y=450)

        label_16=Label(root,text="D2",width=35, bg='pink',font=("arial",12, "italic", "bold"))
        label_16.place(x=850,y=500)

        entry_16=Entry(root, width= 25, bd=5)
        entry_16.place(x=1250,y=500)

        label_17=Label(root,text="DFA",width=35, bg='pink',font=("arial",12, "italic", "bold"))
        label_17.place(x=850,y=550)

        entry_17=Entry(root, width= 25, bd=5)
        entry_17.place(x=1250,y=550)

        label_18=Label(root,text="PPE",width=35, bg='pink',font=("arial",12, "italic", "bold"))
        label_18.place(x=850,y=600)

        entry_18=Entry(root, width= 25, bd=5)
        entry_18.place(x=1250,y=600)

        label_19 = Label(root, text="MR_NO", width=35, bg='pink', font=("arial", 12, "italic", "bold"))
        label_19.place(x=550, y=700)

        entry_19 = Entry(root, width=25, bd=5)
        entry_19.place(x=800, y=700)



        #this creates button for submitting the details provides by the user
        Button(root, text='SUBMIT' , width=20,bg="red",fg='white',font=('arial',14, "italic", "bold"), bd=16,command=detection).place(x=700,y=800)


        #this will run the mainloop.
        root.mainloop()

