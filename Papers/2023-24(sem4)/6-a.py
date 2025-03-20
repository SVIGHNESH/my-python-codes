with open("/home/vighnesh/Desktop/Phython/Papers/2023-24(sem4)/example.txt","r") as file:
    content = file.read()
    new_content = content.title()
with open("/home/vighnesh/Desktop/Phython/Papers/2023-24(sem4)/example.txt","w") as file:
    file.write(new_content)