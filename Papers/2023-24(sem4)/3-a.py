import  math
def find_lcm(a,b):
    return abs(a*b) // math.gcd(a,b)
a = 3
b = 4
print(f" The lowest common multiple of {a} and {b} is {find_lcm(a,b)}")