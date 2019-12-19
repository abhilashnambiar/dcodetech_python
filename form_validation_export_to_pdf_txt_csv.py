# enter data to TXT, PDF and CSV
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from fpdf import FPDF
from csv import DictWriter
import os.path
import pdfkit

window = Tk()
window.geometry("360x520")
window.title("Info")
flag = IntVar()

def validate():
    flag.set(0)

    if(len(in_name.get()) == 0):
        messagebox.showerror("Error","Please enter name")
    
    elif(len(in_number.get()) != 10 or not in_number.get().isdigit()):
        messagebox.showerror("Error","Please enter valid number")

    elif(int(in_age.get()) > 100 or int(in_age.get()) < 1):
        messagebox.showerror("Error","Enter valid age")
        
    elif(in_email.get().lower().endswith("gmail.com") == FALSE):
        messagebox.showerror("Error","You need a Google ID")
    
    elif(in_gender.get() == "Not specified"):
        messagebox.showerror("Error","Please select Gender")

    elif(check_value.get() == 0):
        messagebox.showerror("Error","Please agree to the terms & conditions")

    else:
        in_text.delete(1.0, "end")
        in_text.insert(INSERT, "\nName: "+in_name.get())
        in_text.insert(INSERT, "\nNumber: "+in_number.get())
        in_text.insert(INSERT, "\nAge: "+in_age.get())
        in_text.insert(INSERT, "\nEmail: "+in_email.get())
        in_text.insert(INSERT, "\nGender: "+in_gender.get())
        if(radio_value.get() == 1):
            in_text.insert(INSERT, "\nEligible\n")
        else:
            in_text.insert(INSERT, "\nNot Eligible\n")
        flag.set(1)

def delete():
    in_name.delete(0, "end")
    in_number.delete(0, "end")
    in_age.delete(0, "end")
    in_email.delete(0, "end")
    in_gender.delete(0, "end")
    in_text.delete(1.0, "end")
    check_value.set(0)
    radio_value.set(0)

def gettxt():
    if(flag.get() == 1):
        txt = open("getTXT.txt", "a+")
        txt.seek(0)
        txt_data = txt.read()

        if in_number.get() in txt_data:
            messagebox.showerror("Error","Number already added to TXT")
        elif in_email.get() in txt_data:
            messagebox.showerror("Error","Email already added to TXT")
        else:
            txt.write("\nName: "+in_name.get())
            txt.write("\nNumber: "+in_number.get())
            txt.write("\nAge: "+in_age.get())
            txt.write("\nEmail: "+in_email.get())
            txt.write("\nGender: "+in_gender.get())
            if(radio_value.get() == 1):
                txt.write("\nEligible\n")
            else:
                txt.write("\nNot Eligible\n")
            in_text.delete(1.0, "end")
            in_text.insert(INSERT, "Data added to getTXT.txt")
            flag.set(0)
    else:
        messagebox.showerror("Error","Please Check your Data first")

def getpdf():
    if(flag.get() == 1):
        pdf_txt = open("PDFtoTXT.txt", "a+")
        pdf_txt.seek(0)
        pdf_txt_data = pdf_txt.read()

        if in_number.get() in pdf_txt_data:
            messagebox.showerror("Error","Number already added to PDF")
        elif in_email.get() in pdf_txt_data:
            messagebox.showerror("Error","Email already added to PDF")
        else:
            pdf_txt.write("\nName: "+in_name.get())
            pdf_txt.write("\nNumber: "+in_number.get())
            pdf_txt.write("\nAge: "+in_age.get())
            pdf_txt.write("\nEmail: "+in_email.get())
            pdf_txt.write("\nGender: "+in_gender.get())
            if(radio_value.get() == 1):
                pdf_txt.write("\nEligible\n")
            else:
                pdf_txt.write("\nNot Eligible\n")
            pdf_txt.write(":--------------- ")
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font('Arial','B',16)
            pdf_txt.seek(0)
            for line in pdf_txt:
                if ':' in line:
                    pdf.cell(20,10,line,ln=2)
            pdf.output('getPDF.pdf')
            in_text.delete(1.0, "end")
            in_text.insert(INSERT, "Data added to getPDF.pdf")
            flag.set(0)
    else:
        messagebox.showerror("Error","Please Check your Data first")

def getcsv():
    if(flag.get() == 1):
        csv_exists = os.path.isfile("getCSV.csv")
        csv = open("getCSV.csv","a+",newline="")
        csv.seek(0)
        csv_data = csv.read()

        if in_number.get() in csv_data:
            messagebox.showerror("Error","Number already added to CSV")
        elif in_email.get() in csv_data:
            messagebox.showerror("Error","Email already added to CSV")
        else:
            dict_write = DictWriter(csv, fieldnames = ['Name','Number','Age','Email','Gender','Eligibility'])
            if not csv_exists:
                dict_write.writeheader()
            if(radio_value.get() == 1):
                eligible_value = "Eligible"
            else:
                eligible_value = "Not Eligible"
            dict_write.writerow({
                'Name':in_name.get(),
                'Number':in_number.get(),
                'Age':in_age.get(),
                'Email':in_email.get(),
                'Gender':in_gender.get(),
                'Eligibility':eligible_value
            })
            in_text.delete(1.0, "end")
            in_text.insert(INSERT, "Data added to getCSV.csv")
            flag.set(0)
    else:
        messagebox.showerror("Error","Please Check your Data first")
    
name = Label(window, text="Name").place(x=20,y=20)
number = Label(window, text="Mobile No").place(x=20,y=60)
age = Label(window, text="Age").place(x=20,y=100)
email = Label(window, text="Email").place(x=20,y=140)
gender = Label(window, text="Gender").place(x=20,y=180)
eligible = Label(window, text="Eligile").place(x=70,y=220)
not_eligible = Label(window, text="Not Eligible").place(x=150,y=220)
checkbox = Label(window, text="Agree terms & conditions").place(x=70,y=260)

in_name = Entry(window)
in_name.place(x=120,y=20)
in_number = Entry(window)
in_number.place(x=120,y=60)
in_age = Spinbox(window, from_=0, to=100)
in_age.place(x=120,y=100)
in_email = Entry(window)
in_email.place(x=120,y=140)
in_gender = ttk.Combobox(window, values=["Not specified","Male","Female"])
in_gender.current(0)
in_gender.place(x=120,y=180)

radio_value = IntVar()
in_eligible = Radiobutton(window, variable=radio_value, value=1)
in_eligible.place(x=40,y=220)
in_noteligible = Radiobutton(window, variable=radio_value, value=2)
in_noteligible.place(x=120,y=220)

check_value = IntVar()
in_checkbox = Checkbutton(window, variable=check_value)
in_checkbox.place(x=40,y=260)

in_text = Text(window, width=28,height=10)
in_text.place(x=40,y=340)

gettxt = Button(window, text="getTXT", command=gettxt).place(x=40,y=300)
getcsv = Button(window, text="getCSV", command=getcsv).place(x=160,y=300)
getpdf = Button(window, text="getPDF", command=getpdf).place(x=280,y=300)
check = Button(window, text="Check", command=validate).place(x=280,y=380)
clear = Button(window, text="Clear", command=delete).place(x=280,y=460)

window.mainloop()