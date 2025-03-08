def remove_nth_occurrence(s, char, n):
    count = 0
    result = ""
    for c in s:
        if c == char:
            count += 1
            if count == n: 
                continue
            result += c
           
        else:
            result += c
            return result
s = input("Enter the string:")
char = input("Enter the character:")    
n = int(input("Enter the occurrence:"))
print(remove_nth_occurrence(s,char,n))

#this is the only program in my college exam that i got wrong 
