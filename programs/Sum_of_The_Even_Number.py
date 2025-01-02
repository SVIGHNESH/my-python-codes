def Sum_Of_The_Even_Loop(n):
    sum = 0
    if n<1:
        return -1
    for i in range(2,n+1):
        if i%2 == 0:
            sum = sum + i

    return sum


    
n =  int(input("Enter the number :"))
print(Sum_Of_The_Even_Loop(n))
