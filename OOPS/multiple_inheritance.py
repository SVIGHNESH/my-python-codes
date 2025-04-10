class Predator:
    def flee(self):
        print("This animal is Runnning Behind the Prey")
    def hunt(self):
        print("This animal is Hunting.")
class Prey:
    
    def flee(self):
        print("This animal is Runnig!")


class Rabbit(Prey):
    pass
    
class Hawk(Predator):
    pass
class Fish(Predator,Prey):
    pass

# rabbit = Rabbit()
# rabbit.flee()

fish = Fish()
fish.flee()
fish.hunt()