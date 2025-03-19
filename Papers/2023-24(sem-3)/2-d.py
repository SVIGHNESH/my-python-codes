with open("Papers/2023-24(sem-3)/abc.txt","r") as file:
    content = file.read()
    output=",".join(content)
with open("Papers/2023-24(sem-3)/abc.txt","w") as file:
    file.write(output)