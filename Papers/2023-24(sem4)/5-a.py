s = {1,2,3,4,2,2,1}
print(s)
s.add(45)
print(s)
s.remove(45)
print(s)
popped = s.pop()
print(popped)
print(s)
s.update([35,32,2,4])
print(s)

s1 = {23,2,3,35}
print(s1.union(s))
s2 = set()

print(type(s2))