with open("P.txt","w") as f :
    data = ["My Name is Vighnesh Shukla\n","My Father Name is afjfeih"]
    f.writelines(data)
with open("P.txt","r") as f:
    data = f.read()
print(data)