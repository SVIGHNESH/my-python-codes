f = open("/home/vighnesh/Desktop/Phython/File Operation/akshat.txt","r")

data = f.read(25)
f.seek(0,0)
print(data)

data1 = f.readline()
print(data1)


f.close()

