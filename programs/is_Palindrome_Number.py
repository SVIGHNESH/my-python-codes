def is_Palindrome_Number(Number):
    num = (Number)
    rev = num[::-1]
    if rev == num :
        return 1
    else:
        return 0
Number = input("Enter the Number To BE Checked :")
if is_Palindrome_Number(Number):
    print(f"{Number} is Palindrome Number.")
else:
    print(f"{Number} is not a Palindrome NUmber.")