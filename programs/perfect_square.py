import math
def Perfect_Square(n):
    sqrt=n**0.5
    if n == sqrt*sqrt:
        return 1
    else:
        return -1

n = int(input("Enter the number :"))
print (Perfect_Square(n))