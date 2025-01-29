import tkinter as tk

root = tk.Tk()
root.geometry("400x300")
root.title("Hello")

myLabel = tk.Label(root,text="Hello World from the Tkinter ")
myLabel.pack()
root.mainloop()