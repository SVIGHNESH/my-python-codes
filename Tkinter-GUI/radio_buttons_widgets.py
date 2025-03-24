# radio button-similar to checkbox but you can only select one from a group

from tkinter import *

food = ['Pizza      ','HamBurger','HotDog']
window = Tk()
pizzaImage=PhotoImage(file="/home/vighnesh/Desktop/Phython/Tkinter-GUI/pizza.png")
hotdogImage=PhotoImage(file="/home/vighnesh/Desktop/Phython/Tkinter-GUI/hotdog.png")
burgerImage=PhotoImage(file="/home/vighnesh/Desktop/Phython/Tkinter-GUI/hamburger.png")
foodImages=[pizzaImage,burgerImage,hotdogImage]

def order():
    if(x.get() == 0):
        print("You ordered the Pizza!")
    elif(x.get() == 1):
        print("You ordered the HotDog!")
    elif(x.get()==2):
        print("You ordered a Burger.")
    else:
        print("Huh?") #am ia 
    

x=IntVar()
for index in range(len(food)):
    radio = Radiobutton(window,text=food[index],#adds text to the radio button
                            variable=x,#groups radiobutton together if they share the same variable
                            value=index,#assigns each radiobutton a different value
                            padx=14,
                            pady=10,
                            font=("Impact",50),
                            image=foodImages[index],# adds the image for the specific index 
                            compound=LEFT,# puts image at the left of the text 
                            indicatoron=False, # eliminate the circle indicators
                            width=450,#sets widh of radio button
                            command=order,

                            )
    radio.pack(anchor="w")


window.mainloop()

