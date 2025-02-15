# i = input("Enter a Number:")
# str=str(i)
# str1=str[::-1]
# print(int(str1))
def reverse(n):
    reverse_num = 0
    while(n > 0):
        digit = n % 10
        reverse_num=reverse_num*10 + digit
        n = n // 10 
    return reverse_num
num = int(input("Enter the Number:"))
print("The reversed number is ",reverse(num))