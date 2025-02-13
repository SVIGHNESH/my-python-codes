from tkinter import *
from tkinter import filedialog
def openFile():
    filePath= filedialog.askopenfilename(initialdir="//home//vighnesh//Desktop//Phython//Tkinter-GUI",
                                         title="Open File(txt) Okay?",
                                         filetypes=(("Text Files.","*.txt"),("all files","*.*"))
                                         )
    file = open(filePath,'r') 
    print(file.read())
    file.close()

window = Tk()

button = Button(window,text="Open",command=openFile)
button.pack()

window.mainloop()