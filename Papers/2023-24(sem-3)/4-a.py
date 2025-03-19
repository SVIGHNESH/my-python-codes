import re
def is_valid_password(password):
    if ((6<=len(password) <= 12) and 
        re.search("[A-Z]",password) and 
        re.search("[a-z]",password) and 
        re.search("[0-9]",password) and
        re.search("[@#$]",password)):
            return True
    return False
passwords=input("Enter a comma separated sequence of passwords:")
passwords = passwords.split(",")
valid_passwords=[]
for password in passwords:
      password = password.strip()
      if(is_valid_password(password)):
            valid_passwords.append(password)
result = ",".join(valid_passwords)
print(result)
        
        
        