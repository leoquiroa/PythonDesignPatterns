'''
*What is this pattern about?
In Java and other languages, the Abstract Factory Pattern serves to provide an interface for
creating related/dependent objects without need to specify their
actual class.
The idea is to abstract the creation of objects depending on business
logic, platform choice, etc.
In Python, the interface we use is simply a callable, which is "builtin" interface
in Python, and in normal circumstances we can simply use the class itself as
that callable, because classes are first class objects in Python.
'''

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
    possible = [Dog, Cat]
    return random.choice(possible)()


# Show pets with various factories
def main():
    
    # A Shop that sells only cats
    print("A Shop that sells only cats")
    cat_shop = PetShop(Cat)
    cat_shop.show_pet()
    print("=" * 20)

    # A Shop that sells all animals
    print("A Shop that sells all animals")
    possible = [Dog, Cat, Parrot, Monkey]
    for i in range(len(possible)):
        print(i,"--")
        shop = PetShop(possible[i])
        shop.show_pet()
    print("=" * 20)

    # A Shop that sells only dogs and cats
    print("A Shop that sells only dogs and cats")
    shop = PetShop(random_animal)
    for i in range(4):
        print(i,"--")
        shop.show_pet()
    print("=" * 20)

if __name__ == "__main__":
    random.seed(42)  # for deterministic doctest outputs
    #import doctest
    #doctest.testmod()
    main()