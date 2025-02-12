from tkinter import *

window=Tk()




label = Label(window,text="Hello World",
              font=("Arial",40,"bold"),
              fg="green",
              bg="black",
              relief=RAISED,
              bd=3,
              padx=20,                                  
              image=PhotoImage(file="/home/vighnesh/Desktop/Phython/Tkinter-GUI/Logo1.png"),
              compound=BOTTOM)



#Hello i am here to show you what the tkinter can do
label.pack()
#window.geometry("400x400")
#label.place(x=100,y=1)

window.mainloop()