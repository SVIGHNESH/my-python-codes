def removenth(s,n):
    if n > len(s) :
        return s
    if n>=0:
        return s[:n] + s[n+1:]
    
print(removenth("MANGO",1))