file = open("mint.txt","r")
content  = file.readline()
while content:
    print(content.strip())
    content = file.readline()
file.close()



import os

file_path="/home/vighnesh/Desktop/Phython/Papers/2022-23(sem3)/college/hello.txt"
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"{file_path} is successfully deleted.")
else:
    print(f"{file_path} is not exists.")