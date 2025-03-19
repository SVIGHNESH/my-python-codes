def perfect_square(number):
    if (number**0.5)**2 == number:
        return 1
    return -1
print(perfect_square(15))