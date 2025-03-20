def count_letters(content):
    words = content.split()
    lines = content.splitlines()
    print(f"Total Lines:{len(lines)}")
    print(f"Total Words:{len(words)}")
    print(f"Total Charachters:{len(content)}")
try:

    with open("input.txt","r") as file:
        content = file.read() 

except:
    print("File Not Found")  

