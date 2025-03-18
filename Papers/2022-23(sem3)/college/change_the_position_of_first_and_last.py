def change_str(s):
    return s[-1:] + s[1:-1] + s[:1]

str = "Hello"
changed_str = change_str(str)
print(changed_str)

print()
print()

def triangle(N):
    for i in range(1,N+1):
        print("* "*i)
triangle(4)

print()
print()
def half_diamond(N):
    for i in range(1,N+1):
        print("* "*i)
    for i in range(N-1,0,-1):
        print("* "*i)


half_diamond(6)