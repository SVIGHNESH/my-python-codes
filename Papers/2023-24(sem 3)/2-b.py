L = [1,2,3,4,5,6,7,8,9]

# i
a = L[-1:0:-1]
print(a)

# ii
b = L[2:-1]
print(b)
# iii
M = L[::2]
print(M)
# iv
middle = len(L) //2
c = L[middle : ]
print(c)

# v
N = L.copy()
L[:middle] = L[:middle][::-1]
print(L)
print(N)
# vi
N=[x%2 for x in N]
print(N)