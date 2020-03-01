from tkinter import *

root = Tk()

def raiseframe(frame):
    frame.tkraise()

frame1 = Frame(root)
frame2 = Frame(root)

for used in (frame1,frame2):
    used.grid(row=0,column=0)

def submit():
    f2_name = Label(frame2, text="Name:").grid(row=0,column=0,padx=10,pady=10)
    f2_email = Label(frame2, text="Email:").grid(row=1,column=0,padx=10,pady=10)
    f2d_name = Label(frame2, text=f1_in_name.get()).grid(row=0,column=1,padx=10,pady=10)
    f2d_mail = Label(frame2, text=f1_in_email.get()).grid(row=1,column=1,padx=10,pady=10)
    frame1.destroy()
    raiseframe(frame2)


f1_name = Label(frame1, text="Name").grid(row=0,column=0,padx=10,pady=10)
f1_email = Label(frame1, text="Email").grid(row=1,column=0,padx=10,pady=10)

f1_in_name = Entry(frame1)
f1_in_name.grid(row=0,column=1,padx=10,pady=10)
f1_in_email = Entry(frame1)
f1_in_email.grid(row=1,column=1,padx=10,pady=10)

Button(frame1, text="SUBMIT", command=submit).grid(row=3,column=1,padx=10,pady=10)

raiseframe(frame1)

root.mainloop()