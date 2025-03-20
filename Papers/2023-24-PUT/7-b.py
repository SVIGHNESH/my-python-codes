from tkinter import *
from tkinter import messagebox
def login():
    username = username_entry.get()
    password = password_entry.get()
    if username and password:
        messagebox.showinfo("Login Success","Logged Successfully")
    else:
        messagebox.showwarning("Something Wrong","Not Right")
root = Tk()
root.title("Login Page")

label1 = Label(root,text="Username")
label1.pack()

username_entry = Entry(root)
username_entry.pack()

label2 = Label(root,text="Password").pack()
password_entry = Entry(root,show="*")
password_entry.pack()

Login = Button(root,text="Login",command=login).pack()






root.mainloop()