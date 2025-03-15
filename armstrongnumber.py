number =int (input("Enter the number:"))
length = len(str(number))
temp = number
sum = 0
while temp > 0:
    digit = temp % 10
    sum +=digit ** length
    temp = temp // 10
print (f"The given number is {number} and the sum is {sum} ")
if sum == number:
    print(f"Number {number} is armstrong number")
else:
    print("The given numbe is not armstrong number. " )  

#rr huss edits shyd S ekta se umbrella

