# generator function
def count_upto(n):
    count = 0
    while count <=n:
        yield count
        count+=1
for number in count_upto(5):
    print(number)


# generator expression
print("Printing the generator expression")
squares = (x**2 for x in range(1,6))
for square in squares:
    print(square)


