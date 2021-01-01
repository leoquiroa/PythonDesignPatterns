import random


class PetShop:

    """A pet shop"""

    def __init__(self, animal_factory=None):
        """pet_factory is our abstract factory.  We can set it at will."""

        self.pet_factory = animal_factory

    def show_pet(self):
        """Creates and shows a pet using the abstract factory"""

        pet = self.pet_factory()
        print("We have a lovely {}".format(pet))
        print("It says {}".format(pet.speak()))
        print("walks on {} legs".format(pet.legs()))


class Dog:
    def __str__(self): return "Dog"
    def speak(self): return "woof"
    def legs(self): return 4

class Cat:
    def __str__(self): return "Cat"
    def speak(self): return "meow"
    def legs(self): return 4
    
# Additional factories:

class Parrot:
    def __str__(self): return "Parrot"
    def speak(self): return "fiu fiu"
    def legs(self): return 2

class Monkey:
    def __str__(self): return "Monkey"
    def speak(self): return "uh ah"
    def legs(self): return 2
    

# Create a random animal
def random_animal():
    """Let's be dynamic!"""
    possible = [Dog, Cat, Parrot, Monkey]
    return random.choice(possible)()


# Show pets with various factories
def main():
    
    # A Shop that sells only cats
    cat_shop = PetShop(Cat)
    cat_shop.show_pet()
    #We have a lovely Cat
    #It says meow
    # A shop that sells random animals
    shop = PetShop(random_animal)
    for i in range(10):
        shop.show_pet()
        print("--")
    #We have a lovely Cat
    #It says meow
    #====================
    #We have a lovely Dog
    #It says woof
    #====================
    #We have a lovely Dog
    #It says woof
    #====================

if __name__ == "__main__":
    random.seed(42)  # for deterministic doctest outputs
    #import doctest
    #doctest.testmod()
    main()