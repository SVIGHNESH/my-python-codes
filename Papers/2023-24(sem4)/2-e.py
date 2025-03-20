import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y =[1,4,9,16,25]

plt.plot(x,y,marker="o",color="red")
plt.grid(True,alpha=0.2)
plt.tight_layout()
plt.show()