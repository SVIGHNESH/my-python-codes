class Animal:
    def __init__(self,name):

        self.name = name
        self.isalive = True
    def eat(self):
        print(f"{self.name} is eating.")
    
    def sleep(self):
        print(f"{self.name} is sleeping.")
    
class Dog(Animal):
    pass


class Cat(Animal):
    pass

class Mouse(Animal):
    pass

dog = Dog("Charlie")

cat = Cat("Bruno")

mouse = Mouse("Stwert")

dog.eat()
cat.sleep()
print(mouse.name)
print(mouse.isalive)
