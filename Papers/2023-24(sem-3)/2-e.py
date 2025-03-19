import matplotlib.pyplot as plt

Food = ["Meat","Banana","Avacados","Sweet Potatoes","Spinach","WaterMelon","Coconut Water","Beans","Legumes","Tomato"]
Calories=[250,130,140,120,20,20,10,50,40,19]
Potassium=[40,55,20,30,40,32,10,26,25,20]
Fat=[8,5,3,6,1,1.5,0,2,1.5,2.5]

plt.plot(Food,Calories,marker="o",label="Calories",color = "red")
plt.plot(Food,Potassium,marker="o",label="Potassium",color = "blue")
plt.plot(Food,Fat,marker="o",label="Fat",color = "green")

plt.title("FOOD CHART")
plt.ylabel("NUTRITIONS")
plt.xlabel("FOODS")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
