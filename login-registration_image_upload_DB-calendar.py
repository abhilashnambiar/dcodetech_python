from tkinter import *
from random import *
from tkcalendar import Calendar
import string
import pymysql
from tkinter import filedialog
from datetime import datetime

root = Tk()

database = pymysql.connect(host="localhost",user="", password="")
cursor = database.cursor()

def raiseframe(frame):
    frame.tkraise()

home = Frame(root)
login = Frame(root)
register = Frame(root)
acc_created = Frame(root)
loggedin = Frame(root)


for used in (home,login,register,acc_created,loggedin):
    used.grid(row=0,column=0,sticky=NSEW)

def gotoacc_created():
    Label(acc_created, text="Account Created").grid(row=0,column=0,padx=10,pady=10,sticky=NSEW)
    Button(acc_created, text="Login", command=gotologin).grid(row=1,column=0,padx=10,pady=10,sticky=NSEW)
    raiseframe(acc_created)

def gotoregister():

    def create_captcha():
        in_captcha.config(state=NORMAL)
        in_captcha.delete(0, "end")
        str_char = string.ascii_letters + string.digits
        empty_list = []
        for i in range(1,6):
            empty_list.append(choice(str_char))

        captcha = ""
        for i in empty_list:
            captcha += i
        in_captcha.insert(INSERT, captcha)
        in_captcha.config(state=DISABLED)

    def create_account():
        database.select_db("py_db")
        duplicate_mail = cursor.execute("SELECT email FROM user_credentials WHERE email = %s", email.get())
        if(duplicate_mail == 0):
            if(password.get() == confirm.get()):
                if(in_captcha.get() == out_captcha.get()):
                    cursor.execute("INSERT INTO user_credentials(name,email,password) VALUES(%s,%s,%s)",(name.get(),email.get(),password.get()))
                    database.commit()
                    register.destroy()
                    gotoacc_created()
                    print("Data Added")
                else:
                    print("Captcha Incorrect!")
            else:
                print("Password Mismatch!")
        else:
            print("Already exists")

    Label(register, text="Register").grid(row=0,column=0,padx=10,pady=10,sticky=NSEW)
    Label(register, text="Name: ").grid(row=1,column=0,padx=10,pady=10,sticky=NSEW)
    Label(register, text="Email: ").grid(row=2,column=0,padx=10,pady=10,sticky=NSEW)
    Label(register, text="Password: ").grid(row=3,column=0,padx=10,pady=10,sticky=NSEW)
    Label(register, text="Confirm Password: ").grid(row=4,column=0,padx=10,pady=10,sticky=NSEW)
    Label(register, text="Captcha:").grid(row=5,column=0,padx=10,pady=10,sticky=NSEW)

    name = Entry(register)
    name.grid(row=1,column=1,padx=10,pady=10,sticky=NSEW)
    email = Entry(register)
    email.grid(row=2,column=1,padx=10,pady=10,sticky=NSEW)
    password = Entry(register,show="*")
    password.grid(row=3,column=1,padx=10,pady=10,sticky=NSEW)
    confirm = Entry(register,show="*")
    confirm.grid(row=4,column=1,padx=10,pady=10,sticky=NSEW)
    in_captcha = Entry(register)
    in_captcha.grid(row=6,column=0,padx=10,pady=10,sticky=NSEW)
    out_captcha = Entry(register)
    out_captcha.grid(row=6,column=1,padx=10,pady=10,sticky=NSEW)

    Button(register, text="Refresh", command=create_captcha).grid(row=5,column=1,padx=10,pady=10,sticky=NSEW)
    Button(register, text="Register", command=create_account).grid(row=7,column=1,padx=10,pady=10,sticky=NSEW)
    Button(register, text="Login", command=gotologin).grid(row=7,column=0,padx=10,pady=10,sticky=NSEW)

    create_captcha()
    raiseframe(register)

def gotologin():
    def gotologgedin():
        def submit_data():
            database.select_db("py_db")
            cursor.execute("INSERT INTO user_data(email,dob,text) VALUES(%s,%s,%s)",(l_email.get(),in_dob.get(),in_about.get(1.0,"end")))
            database.commit()
            print("Data added")

        def date_format():
            top = Toplevel(loggedin)
            def print_sel():
                var = cal.selection_get()
                in_dob.insert(INSERT,var)
                top.destroy()

            cal = Calendar(top,font="Arial 14",selectmode="day",cursor="hand1")
            cal.pack()
            Button(top,text="OK",command=print_sel).pack()

        def upload():
            upload_image = filedialog.askopenfilename(initialdir=" ",title="Select Image File",filetypes=(("png files","*.png"),("all files",".")))
            upload_path.insert(INSERT, upload_image)
            with open(upload_image, "rb") as image:
                img_done = image.read()
                cursor.execute("INSERT INTO user_data(email,img) VALUES(%s,%s)",(l_email.get(),img_done))
                database.commit()
                print("Data added")

        def dwnld_img():
            cursor.execute("SELECT img from user_data WHERE email = %s",(l_email.get()))
            img_data = cursor.fetchone()
            now = datetime.now()
            current = now.strftime("%Y%m%d-%H%M%S")
            with open(l_email.get()+current+".png","wb") as f:
                f.write(img_data[0])
                print("Image downloaded")

        database.select_db("py_db")
        Label(loggedin, text="Welcome").grid(row=0,column=0,padx=10,pady=10,sticky=NSEW)
        cursor.execute("SELECT name FROM user_credentials WHERE email = %s", l_email.get())
        print_name = cursor.fetchone()
        Label(loggedin, text=print_name).grid(row=0,column=1,padx=10,pady=10,sticky=NSEW)
        Button(loggedin, text="Logout", command=gotologin).grid(row=1,column=0,padx=10,pady=10,sticky=NSEW)
        Label(loggedin, text=print_name).grid(row=0,column=1,padx=10,pady=10,sticky=NSEW)
        Label(loggedin, text="DOB").grid(row=2,column=1,padx=10,pady=10,sticky=NSEW)
        in_dob = Entry(loggedin)
        in_dob.grid(row=2,column=2,padx=10,pady=10,sticky=NSEW)
        Button(loggedin, text="^", command=date_format).grid(row=2,column=3,padx=10,pady=10,sticky=NSEW)
        upload_path = Entry(loggedin)
        upload_path.grid(row=3,column=2,padx=10,pady=10,sticky=NSEW)
        Button(loggedin, text="Upload IMG", command=upload).grid(row=3,column=1,padx=10,pady=10,sticky=NSEW)
        in_about = Text(loggedin,width=15,height=5)
        in_about.grid(row=4,column=2,padx=10,pady=10,sticky=NSEW)
        Label(loggedin, text="About").grid(row=4,column=1,padx=10,pady=10,sticky=NSEW)
        Button(loggedin, text="Submit", command=submit_data).grid(row=5,column=2,padx=10,pady=10,sticky=NSEW)
        Button(loggedin, text="Download IMG", command=dwnld_img).grid(row=5,column=3,padx=10,pady=10,sticky=NSEW)
        
        raiseframe(loggedin)

    def check_login():
        database.select_db("py_db")
        mail_check = cursor.execute("SELECT email FROM user_credentials WHERE email = %s", l_email.get())
        password_check = cursor.execute("SELECT password FROM user_credentials WHERE password = %s", l_password.get())
        if(mail_check == 1):
            if(password_check == 1):
                gotologgedin()
            else:
                print("Wrong Password!")
        else:
            print("Email not found!")

    Label(login, text="Login").grid(row=0,column=0,padx=10,pady=10,sticky=NSEW)
    Label(login, text="Email: ").grid(row=1,column=0,padx=10,pady=10,sticky=NSEW)
    Label(login, text="Password: ").grid(row=2,column=0,padx=10,pady=10,sticky=NSEW)

    l_email = Entry(login)
    l_email.grid(row=1,column=1,padx=10,pady=10,sticky=NSEW)
    l_password = Entry(login,show="*")
    l_password.grid(row=2,column=1,padx=10,pady=10,sticky=NSEW)

    Button(login, text="Login", command=check_login).grid(row=3,column=1,padx=10,pady=10,sticky=NSEW)
    Button(login, text="Register", command=gotoregister).grid(row=3,column=0,padx=10,pady=10,sticky=NSEW)

    raiseframe(login)

Label(home, text="Welcome").grid(row=0,column=0,padx=10,pady=10,sticky=NSEW)

Button(home, text="Register", command=gotoregister).grid(row=1,column=0,padx=10,pady=10,sticky=NSEW)
Button(home, text="Login", command=gotologin).grid(row=1,column=1,padx=10,pady=10,sticky=NSEW)

raiseframe(home)
root.mainloop()