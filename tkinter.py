import tkinter as tk

root = tk.Tk()

root.title("Hello")

Label = tk.Label(root,text="Hello",font=("Cursive",48))
Label.pack(padx = 30,pady=40)

textArea = tk.Text(root,height=7,font=("Arial",10))
textArea.pack(padx=10,pady=5)

buttonFrame=tk.Frame(root)

buttonFrame.columnconfigure(0,weight=1)
buttonFrame.columnconfigure(1,weight=1)
buttonFrame.columnconfigure(2,weight=1)

btn1=tk.Button(buttonFrame,text="1")
btn1.grid(row=0,column=0,sticky=tk.W+tk.E)

btn2=tk.Button(buttonFrame,text="2")
btn2.grid(row=0,column=1,sticky=tk.W+tk.E)

btn3=tk.Button(buttonFrame,text="3")
btn3.grid(row=0,column=2,sticky=tk.W+tk.E)

btn4=tk.Button(buttonFrame,text="4")
btn4.grid(row=1,column=0,sticky=tk.W+tk.E)

btn5=tk.Button(buttonFrame,text="5")
btn5.grid(row=1,column=1,sticky=tk.W+tk.E)

btn6=tk.Button(buttonFrame,text="6")
btn6.grid(row=1,column=2,sticky=tk.W+tk.E)

btn7=tk.Button(buttonFrame,text="7")
btn7.grid(row=2,column=0,sticky=tk.W+tk.E)

btn8=tk.Button(buttonFrame,text="8")
btn8.grid(row=2,column=1,sticky=tk.W+tk.E)


btn9=tk.Button(buttonFrame,text="9")
btn9.grid(row=2,column=2,sticky=tk.W+tk.E)


buttonFrame.pack(pady=10,fill="x")


root.mainloop() 