def count1(s):
    vowels = "AEIOUaeiou"
    count = 0
    for i in s:
        if i in vowels:
            count += 1 
    return count 
print(count1("I Love India"))
#this program is the program to check the number of the vowels in a given string 