def Calculate_Factorial(n):
    if n == 0 or n == 1:
        return 1
    return n*Calculate_Factorial(n-1)
n = int (input ("Enter the Number :" ))
print(Calculate_Factorial(n))