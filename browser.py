import webbrowser
from tkinter import *

def query(event):
    if(radio_value.get() == 1):
        webbrowser.open("https://www.google.com/search?q="+search.get())
    if(radio_value.get() == 2):
        webbrowser.open("https://duckduckgo.com/?q="+search.get())

window = Tk()
window.title("Search")
temp = 0

radio_value = IntVar()
Label(window,text="Google").grid(row=0,column=3)
google = Radiobutton(window,variable=radio_value,value=1)
google.grid(row=0,column=2)
Label(window,text="DuckDuckGo").grid(row=0,column=5)
duck = Radiobutton(window,variable=radio_value,value=2)
duck.grid(row=0,column=4)

window.bind('<Return>',query)

search = Entry(window)
search.grid(row=0,column=0,padx=10,pady=10)
Button(window,text="Search",command= lambda: query(temp)).grid(row=0,column=1,padx=10,pady=10)

window.mainloop()