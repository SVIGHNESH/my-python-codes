number = int(input("Enter the number:"))
if number>0:
    print("The number is positive.")
elif number<0:
    print("The number is negative.")
else:
    print("The number i zero.")

if number%2==0:
    print("The number is even.")
else:
    print("The number is odd.")

if number%3==0 and number%2==0:
    print("THe number is divisble by both 2 and 3.")
else:
    print("The number is not divisible by 2 and 3.")    