lines=[]
while True:
    try:
        line = input()
        if line:
            lines.append(line.upper())
        else:
            break
    except :
            break
 
print("\n".join(lines))

