from tkinter import messagebox

import mysql.connector

# mydb = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='xyz1234',
#     database='careopedia')

mydb=mysql.connector.connect(host="localhost",user="root",passwd="hell0w0rld!*",database="careopedia")

mycursor=mydb.cursor(buffered=True)

