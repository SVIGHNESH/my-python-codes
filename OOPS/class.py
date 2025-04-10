from car import  Car

car_1 = Car("TATA","Safari",2019,"White")
car_2 = Car("MARUTI","Brezza",2016,"Maroon")


print(car_1.make)
print(car_1.color)
print(car_1.year)
print(car_1.model)
car_1.drive()
car_1.stop()

print(car_2.make)
print(car_2.color)
print(car_2.year)
print(car_2.model)
car_2.drive()
car_2.stop()