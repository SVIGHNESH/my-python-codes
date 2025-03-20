import re
def is_Valid_Password(password):
    if ((8<=len(password) <= 16) and
    re.search("[A-z]",password) and
    re.search("[a-z]",password) and
    re.search("[0-9]",password) and 
    re.search("[@#$]",password)):
        return True
    return False
passwords=input("Enter the sequence of comma-separated sequence of Passwords:")
valid_passwords = []
passwords=passwords.split(",")
for password in passwords:
    password = password.strip()
    if(is_Valid_Password(password)):
        valid_passwords.append(password)
result =",".join(valid_passwords)
print(result)

    