from tkinter import *

window = Tk() #it will instantizate an instance of windows 

window.geometry("300x500")
window.title("HELLLO")

icon = PhotoImage(file="/home/vighnesh/Desktop/Phython/Tkinter-GUI/Logo1.png")
window.iconphoto(True,icon)
window.config(background="#77f")
#i don;t knoe the col



window.mainloop() #place window on computer screen
