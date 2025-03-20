str1 = input("Enter the first String:")
str2 = input("Enter the second String:")
def common_letter(str1,str2):
    return set(str1) & set(str2)
print(f"The Common Letter in the \"{str1}\" and \"{str2}\" is \"{common_letter(str1,str2)}\"")