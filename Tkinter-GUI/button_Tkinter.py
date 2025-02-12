
#button:you click it that it does stuff
from tkinter import *

def click():
     
    print("Hello!!")

window=Tk()

button = Button(window, text = "Click  ME!")
button.config(command=click)# perform the call back of the function 
button.config(font=('Ink Free',34,'bold'))
button.config(bg="#7f7")
button.config(fg="#f77")
button.config(activebackground='#7f7')
button.config(activeforeground="#f77")
button.pack()

window.mainloop()