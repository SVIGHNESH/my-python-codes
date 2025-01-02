def replace(s,n,char):
    if n == 0:
        return s
    else:
        return char + replace(s[1:],n-1,char)
s =  input("Enter a string: ")
n =  int(input("Enter the index:"))
char = input("Enter the character:")
replace(s,n,char)