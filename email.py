#send mail 
import smtplib
from tkinter import *

window = Tk()

window.geometry("320x240")

server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login('t5468574@gmail.com','abhilashn9')

to = Label(window, text="To").place(x=20,y=20)
message = Label(window, text="Message").place(x=20,y=60)

def send():
    server.sendmail('t5468574@gmail.com',in_to.get(),in_message.get(1.0,"end"))
    server.quit()
    print("Message Sent!")

in_to = Entry(window)
in_to.place(x=120,y=20)
in_message = Text(window,width=15,height=5)
in_message.place(x=120,y=60)

send = Button(window,text="Send",command=send).place(x=160,y=180)

window.mainloop()