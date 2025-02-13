#grid()= Geometry manages that organise widgets in a table like structure in a point
from tkinter import *
window = Tk()

titleLabel=Label(window,text="Enter your info",font=("Ink Free",30)).grid(row = 0,column=0,columnspan=2)
firstNameLabel=Label(window,text='First Name:',bg="red").grid(row=1,column=0)
firstNameEntry=Entry(window,).grid(row=1,column=1)
lastNameLabel=Label(window,text="Last Name:",bg="blue").grid(row=2,column=0)
lastNameEntry=Entry(window).grid(row=2,column=1)
emailAddrLabel=Label(window,text="Email Address:",bg="green").grid(row=3,column=0)
emailAddrEntry=Entry(window).grid(row=3,column=1)
submitButton=Button(window,text="Submit").grid(row=4,columnspan=2)



window.mainloop()