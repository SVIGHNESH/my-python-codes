number = int(input("Enter the number: "))
length = len(str(number))
sum = 0
temp = number

while temp > 0:
    digit = temp % 10
    sum += digit ** length
    temp //= 10

print(f"The given number is {number} and the sum is {sum}")

if sum == number:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")