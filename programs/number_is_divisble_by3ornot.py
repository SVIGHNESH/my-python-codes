number = int(input("Enter the number:"))
if number % 3 == 0 and number%5==0:
    print(f"{number} is divisble by both 3 and 5.")
elif number %3==0 and number%5!=0  :
    print(f"{number} is only divisible by 3.")  
elif number%3!=0 and number%5==0 :
    print (f"{number} is only divisible by 5 only.")
else:
    print(f"{number} is not divisible by both 3 and 5.")  