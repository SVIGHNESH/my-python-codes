def is_perfect_cube(number):
    cbrt = number ** (1/3)
    if number == cbrt*cbrt*cbrt:
        return True
    else :
        return False
    
number = int (input("ENter the Number To Checked:"))
print(is_perfect_cube(number))