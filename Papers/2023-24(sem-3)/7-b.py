from tkinter import *
def button_press(s):
    global equation_text
    equation_text = equation_text+str(s)
    equation_label.set(equation_text)
def equals():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except:
        equation_label.set("Something Went Wrong!")
def clear():
    global equation_text
    equation_label.set(" ")
    equation_text=" "

root = Tk()
equation_text = ""
equation_label = StringVar()

label = Entry(root,textvariable= equation_label)
label.pack()

frame = Frame(root)

button1 = Button(frame,text="1",command=lambda:button_press(1))
button1.grid(row=0,column=0)

button2= Button(frame,text="2",command=lambda:button_press(2))
button2.grid(row=0,column=1)

button3= Button(frame,text="3",command=lambda:button_press(2))
button3.grid(row=0,column=2)

button4= Button(frame,text="4",command=lambda:button_press(4))
button4.grid(row=1,column=0)

button5= Button(frame,text="5",command=lambda:button_press(5))
button5.grid(row=1,column=1)

button6= Button(frame,text="6",command=lambda:button_press(6))
button6.grid(row=1,column=2)

button7= Button(frame,text="7",command=lambda:button_press(7))
button7.grid(row=2,column=0)

button8= Button(frame,text="8",command=lambda:button_press(8))
button8.grid(row=2,column=1)

button9= Button(frame,text="9",command=lambda:button_press(9))
button9.grid(row=2,column=2)

button0= Button(frame,text="0",command=lambda:button_press(0))
button0.grid(row=3,column=0)

equal= Button(frame,text="=",command=equals)
equal.grid(row=3,column=2)

button_plus= Button(frame,text="+",command=lambda:button_press("+"))
button_plus.grid(row=0,column=3)

button_minus= Button(frame,text="-",command=lambda:button_press("-"))
button_minus.grid(row=1,column=3)

button_mul= Button(frame,text="*",command=lambda:button_press("*"))
button_mul.grid(row=2,column=3)

button_div= Button(frame,text="/",command=lambda:button_press("/"))
button_div.grid(row=3,column=3)
 
button_clear = Button(frame,text="CLR",command=clear)
button_clear.grid(row = 3,column=1)

frame.pack()
root.title("Calcy")
root.mainloop()


