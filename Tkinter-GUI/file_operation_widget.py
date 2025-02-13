from tkinter import *
from tkinter import filedialog
def openFile():
    filePath= filedialog.askopenfile()
    file = open(filePath.name,'r')
    print(file.read())
    file.close()

window = Tk()

button = Button(window,text="Open",command=openFile)
button.pack()

window.mainloop()