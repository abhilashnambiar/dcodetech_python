#send sms via way2sms api
from tkinter import *
import requests
import json

URL = 'https://www.way2sms.com/api/v1/sendCampaign'
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  print(requests.post(reqUrl, req_params).text)

window = Tk()
window.geometry("320x240")
window.title("way2sms")

number = Label(window,text="Number:").place(x=20,y=20)
in_number = Entry(window)
in_number.place(x=120,y=20)

message = Label(window,text="Message:").place(x=20,y=60)
in_message = Text(window,width=20,height=5)
in_message.place(x=120,y=60)

send = Button(window,text="SEND",command= lambda: sendPostRequest(URL,'315BFI7KHV7VBQRAN3QG8O9Q97FFISHM','I7RQIX0GDDGJ4FUS','stage',in_number.get(),'abhi.sn0909@gmail.com',in_message.get(1.0,"end"))).place(x=160,y=180)

window.mainloop()