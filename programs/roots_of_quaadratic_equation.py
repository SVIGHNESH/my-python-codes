import math 
a = float(input("Enter the coefficiant of x^2:"))
b = float(input("Enter the coefficant of x:"))
c = float(input("Enter the constant:"))
d= b**2-4*a*c
if d>0:
    root1=(-b+math.sqrt(d)) /(2*a)
    root2=(-b-math.sqrt(d)) /(2*a)
    print(f"The quation has two real and equal distinct root:{root1} and {root2}")
elif d == 0:
    root=-b/(2*a)
    print(f"The given equation has repeated roots:{root}")
else:
    print("The given equation has not real roots.")    
    