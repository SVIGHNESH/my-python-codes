from tkinter import *

def submit():
    username = entry.get()
    print(username)

def delete():

    entry.delete(0,END) #this delete the line of text 
def back():
    entry.delete(len(entry.get()) - 1 ,END)
window = Tk()

submit = Button(window,text = "Submit",command=submit)
submit.pack(side = RIGHT)

delete = Button(window,text = "Delete",command=delete)
delete.pack(side = RIGHT)

backspace = Button(window,text = "backspace",command=back)
backspace.pack(side = RIGHT)


entry = Entry()
entry.config(font=('Ink Free',50))
entry.config(fg="#00ff00")
entry.config(insertbackground="white")
entry.config(bg='black')
#entry.insert(0,'Spingebob')
#  entry.config(state=ACTIVE) # Active /Disable 
#entry.config(show='*')

entry.pack()

window.mainloop()