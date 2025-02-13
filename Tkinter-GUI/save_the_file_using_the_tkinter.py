from tkinter import *
from tkinter import filedialog
def saveFile():
    file= filedialog.asksaveasfile(initialdir="/home/vighnesh/Desktop/Phython/Tkinter-GUI",
                                   defaultextension='.txt',
                                   filetypes=[
                                       ('Text Files','.txt'),
                                       ('HTML','.html'),
                                       ('All Files','.*')
                                   ])
    fileText=str(text.get(1.0,END))
    file.write(fileText)
    file.close()

window=Tk()

button = Button(window,text ="save",command=saveFile)
button.pack()

text=Text(window,
          font=('Ink free',30),
          )
text.pack()

window.mainloop()
