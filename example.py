import tkinter as tk

root = tk.Tk()
root.geometry("400x300")
root.title("Hello")

Label = tk.Label(root,text="Hello",font=("Italic",18))
Label.pack(padx = 30,pady=40)



root.mainloop()