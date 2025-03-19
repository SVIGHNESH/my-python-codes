with open("mint.txt","r") as file :
    content = file .read
    content = content.split()
    digits = [x for x in content if x.isdigit() ]
print("".join(digit))
