def check_Armstrong(n):
    temp = n
    sum = 0
    while temp > 0:
            digit = temp % 10
            sum +=digit ** length
            temp = temp // 10
    
    if sum == n:
        return "Yes"
    else:
        return "No"

     
n =int (input("Enter the number:"))

length = len(str(n))
print(check_Armstrong(n))
#this is program that shows whether the number is Armstrong 
#program od th
#thinf'lf eifmicm isn  in  if iw ie