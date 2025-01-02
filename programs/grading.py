marks = float(input("Enter the number:"))
if marks > 100:
    print ("Your entered value is not recognized by the system")
    grade ='0'   
elif marks >= 90:
    grade = 'A'
elif marks >= 70:
    grade = 'B' 

elif marks >= 60:
    grade = 'C' 
elif marks >= 45:
    grade = 'D'
elif marks >= 30:
    grade = 'E'
else:
    grade = 'F'
print (f"Your grade is :",grade)    
