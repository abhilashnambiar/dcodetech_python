#create and insert data into database
from tkinter import *
import pymysql

window = Tk()

try:
    database = pymysql.connect(host="localhost",user="",password="")
except pymysql.err.OperationalError:
    print("Could not connect to DB")
    exit()

cursor = database.cursor()

try:
    cursor.execute("CREATE DATABASE college_db")
    print("DB - college_db created")
except pymysql.err.ProgrammingError:
    print("Database Already Exists!")
finally:
    print("college_db ready")

try:
    database.select_db("college_db")
    cursor.execute("CREATE TABLE student(S_ID INT PRIMARY KEY AUTO_INCREMENT,S_Name VARCHAR(30),Gender VARCHAR(10),Address VARCHAR(100),DOB VARCHAR(10))")
    cursor.execute("CREATE TABLE department(D_ID INT PRIMARY KEY AUTO_INCREMENT,D_Name VARCHAR(30))")
    cursor.execute("CREATE TABLE course(C_ID INT PRIMARY KEY AUTO_INCREMENT,C_Name VARCHAR(30),C_Code VARCHAR(10))")
    cursor.execute("CREATE TABLE faculty(F_ID INT PRIMARY KEY AUTO_INCREMENT,F_Name VARCHAR(30),Gender VARCHAR(10),Salary INT,AGE INT,Experience INT)")
    cursor.execute("CREATE TABLE research_project(P_ID INT PRIMARY KEY AUTO_INCREMENT,P_Name VARCHAR(30),Duration INT)")
except pymysql.err.InternalError:
    print("Tables Already Created!")
finally:
    print("TABLES - student, department,course,faculty,research_project READY")

def submit_t1():
    cursor.execute("INSERT INTO student(S_Name,Gender,Address,DOB) VALUES(%s,%s,%s,%s)",(t1_name_in.get(),t1_gender_in.get(),t1_add_in.get(),t1_dob_in.get()))
    database.commit()
    print("Added to Student")

def submit_t2():
    cursor.execute("INSERT INTO department(D_Name) VALUES(%s)",(t2_name_in.get()))
    database.commit()
    print("Added to Department")

def submit_t3():
    cursor.execute("INSERT INTO course(C_Name,C_Code) VALUES(%s,%s)",(t3_name_in.get(),t3_code_in.get()))
    database.commit()
    print("Added to Course")

def submit_t4():
    cursor.execute("INSERT INTO faculty(F_Name,Gender,Salary,AGE,Experience) VALUES(%s,%s,%s,%s,%s)",(t4_name_in.get(),t4_gender_in.get(),t4_salary_in.get(),t4_age_in.get(),t4_experience_in.get()))
    database.commit()
    print("Added to Faculty")

def submit_t5():
    cursor.execute("INSERT INTO research_project(P_Name,Duration) VALUES(%s,%s)",(t5_name_in.get(),t5_duration_in.get()))
    database.commit()
    print("Added to Research Project")

t1 = Label(window, text="Student").grid(row=0,column=0)
t1_name = Label(window, text="Name").grid(row=1,column=0)
t1_gender = Label(window, text="Gender").grid(row=2,column=0)
t1_add = Label(window, text="Address").grid(row=3,column=0)
t1_dob = Label(window, text="D.O.B").grid(row=4,column=0)
t1_name_in = Entry(window)
t1_name_in.grid(row=1,column=1)
t1_gender_in = Entry(window)
t1_gender_in.grid(row=2,column=1)
t1_add_in = Entry(window)
t1_add_in.grid(row=3,column=1)
t1_dob_in = Entry(window)
t1_dob_in.grid(row=4,column=1)
t1_submit = Button(window,text="Submit_T1", command=submit_t1).grid(row=6,column=1)

t2 = Label(window, text="Department").grid(row=0,column=3)
t2_name = Label(window, text="Name").grid(row=1,column=3)
t2_name_in = Entry(window)
t2_name_in.grid(row=1,column=4)
t2_submit = Button(window,text="Submit_T2", command=submit_t2).grid(row=6,column=4)

t3 = Label(window, text="Course").grid(row=0,column=6)
t3_name = Label(window, text="Name").grid(row=1,column=6)
t3_gender = Label(window, text="Code").grid(row=2,column=6)
t3_name_in = Entry(window)
t3_name_in.grid(row=1,column=7)
t3_code_in = Entry(window)
t3_code_in.grid(row=2,column=7)
t3_submit = Button(window,text="Submit_T3", command=submit_t3).grid(row=6,column=7)

t4 = Label(window, text="Faculty").grid(row=0,column=8)
t4_name = Label(window, text="Name").grid(row=1,column=8)
t4_gender = Label(window, text="Gender").grid(row=2,column=8)
t4_salary = Label(window, text="Salary").grid(row=3,column=8)
t4_age = Label(window, text="Age").grid(row=4,column=8)
t4_experience = Label(window, text="Experience").grid(row=5,column=8)
t4_name_in = Entry(window)
t4_name_in.grid(row=1,column=9)
t4_gender_in = Entry(window)
t4_gender_in.grid(row=2,column=9)
t4_salary_in = Entry(window)
t4_salary_in.grid(row=3,column=9)
t4_age_in = Entry(window)
t4_age_in.grid(row=4,column=9)
t4_experience_in = Entry(window)
t4_experience_in.grid(row=5,column=9)
t4_submit = Button(window,text="Submit_T4", command=submit_t4).grid(row=6,column=9)

t5 = Label(window, text="Research Project").grid(row=0,column=10)
t5_name = Label(window, text="Name").grid(row=1,column=10)
t5_gender = Label(window, text="Duration").grid(row=2,column=10)
t5_name_in = Entry(window)
t5_name_in.grid(row=1,column=11)
t5_duration_in = Entry(window)
t5_duration_in.grid(row=2,column=11)
t5_submit = Button(window,text="Submit_T5", command=submit_t5).grid(row=6,column=11)

window.mainloop()