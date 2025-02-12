
#button:you click it that it does stuff
from tkinter import *

count = 0
def click():
     
    global count
    count+=1
    label.config(text=count)
   
    
   

window=Tk()

button = Button(window, text = "Click  ME!")
button.config(command=click)# perform the call back of the function 
button.config(font=('Ink Free',34,'bold'))
button.config(bg="#7f7")
button.config(fg="#f77")
button.config(activebackground='#7f7')
button.config(activeforeground="#f77")
image=PhotoImage(file="/home/vighnesh/Desktop/Phython/Tkinter-GUI/point_emoji.png")
button.config(image=image)
button.config(compound='left')
#button.config(state=ACTIVE) # disable button (ACTIVE/DISABLED )
label=Label(window,text=count)
label.config(font=('Monospace',50))
label.pack()

button.pack()


window.mainloop()