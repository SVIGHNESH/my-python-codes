
def replace_nth_char(s, n, char):
    if n < len(s):
        return s[:n] + char + s[n+1:]
    else:
        return s
    

s = input("Enter the strigs: ")
n = int(input("Enter the index: "))
char = input("Enter the charachter you want to replaced with : ")
print(replace_nth_char(s,n,char))       
