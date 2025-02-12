from tkinter import *

def display():
    if(x.get() == 1) & (y.get() == 0):
        print("I Like the Python.")
    elif(x.get() == 0) & (y.get() == 1):
        print("I Like the Java.")
    elif(x.get() == 1) & (y.get() == 1):
        print("I Like the both Python & Java")
    else:
        print("I don't like either. ")
    

window = Tk()
window.title("The CheckBox")

x = IntVar()
y = IntVar()
checkbox = Checkbutton(window,text="Python",variable=x,onvalue=1,offvalue=0,command= display,
                       font=("Arial",20),#change the font to Arial
                       fg="#0000ff",#the color of the text 
                       bg="#000000",#the color of the background
                       activebackground="#000000",#active background color 
                       activeforeground="#0000ff",#active foreground color 
                        padx=70,
                        pady=70,   
                        anchor='w'             

                       )
checkbox.pack()
photo1 = PhotoImage(file="/home/vighnesh/Desktop/Phython/Tkinter-GUI/python.png")

checkbox.config(image=photo1,compound=RIGHT)# sets the image to the checkbox 



checkbox2 = Checkbutton(window,text="Python",variable=y,onvalue=1,offvalue=0,command= display,
                       font=("Arial",20),#change the font to Arial
                       fg="#0000ff",#the color of the text 
                       bg="#000000",#the color of the background
                       activebackground="#000000",#active background color 
                       activeforeground="#0000ff",#active foreground color 
                        padx=70,
                        pady=70, 
                        anchor='w' #anchors widget to relative cardinal direction            

                       )
checkbox2.pack()
photo2 = PhotoImage(file="/home/vighnesh/Desktop/Phython/Tkinter-GUI/java.png")

checkbox2.config(image=photo2,compound=RIGHT)# sets the image to the checkbox 

window.mainloop()