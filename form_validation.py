from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Info")

def validate():
    name_value = in_name.get()
    number_value = in_number.get()
    address_value = in_address.get()
    email_value = in_email.get()

    if(len(name_value) == 0):
        messagebox.showerror("Error","Please enter name")
        return
    else:
        print("Name:",name_value)
    
    if(number_value.isdigit()):
        if(len(number_value) != 10):
            messagebox.showerror("Error","Please enter valid number")
            return
        else:
            print("Number:",number_value)

    else:
        messagebox.showerror("Error","Please enter digit")
        return

    if(len(address_value) == 0):
        messagebox.showerror("Error","Enter valid address")
        return
    else:
        print("Address:",address_value)
    
    
    if(email_value.endswith("gmail.com") == FALSE):
        messagebox.showerror("Error","You need a Google ID")
        return
    else:
        print("Email:",email_value)

def delete():
    in_name.delete(0, "end")
    in_number.delete(0, "end")
    in_address.delete(0, "end")
    in_email.delete(0, "end")

number_value = StringVar()

name = Label(window, text="Name").grid(row=0,column=0,padx=10,pady=10)
number = Label(window, text="Mobile No").grid(row=1,column=0,padx=10,pady=10)
address = Label(window, text="Address").grid(row=2,column=0,padx=10,pady=10)
email = Label(window, text="Email").grid(row=3,column=0,padx=10,pady=10)

in_name = Entry(window)
in_name.grid(row=0,column=1,padx=10,pady=10)
in_number = Entry(window)
in_number.grid(row=1,column=1,padx=10,pady=10)
in_address = Entry(window)
in_address.grid(row=2,column=1,padx=10,pady=10)
in_email = Entry(window)
in_email.grid(row=3,column=1,padx=10,pady=10)

submit = Button(window, text="Submit" ,command=validate).grid(row=4,column=1,padx=10,pady=10)
clear = Button(window, text="Clear" ,command=delete).grid(row=4,column=2,padx=10,pady=10)

window.mainloop()