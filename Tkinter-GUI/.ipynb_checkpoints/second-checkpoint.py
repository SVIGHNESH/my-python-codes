from tkinter import *

window=Tk()

label = Label(window,text="Hello World",font=("Cursive",40,"bold"))
label.pack()
window.geometry("400x400")
#label.place(x=100,y=1)

window.mainloop()