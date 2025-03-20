def counting(text):
    words = text.split()
    lines = text.splitlines()
    chr = len(text)
    print(f" The number of the word in the file is {len(words)}.")
    print(f" The number of the lines in the file is {len(lines)}")
    print(f" The number of the charachters in the file is {chr}")
    return len(words),len(lines),chr
with open("/home/vighnesh/Desktop/Phython/Papers/2023-24(sem4)/ABC.txt","r") as file:
    text = file.read()
words, lines ,chr = counting(text)
with open("/home/vighnesh/Desktop/Phython/Papers/2023-24(sem4)/ABC.txt","a") as file:

    file.write(f"\nThe number of the words in this file is {words}")
    file.write(f"\nThe number of the lines in this file is {lines}")
    file.write(f"\nThe number of the charachter in  this file is {chr}")