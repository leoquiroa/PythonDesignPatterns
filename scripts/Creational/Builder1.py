'''
*What is this pattern about?
It decouples the creation of a complex object and its representation,
so that the same process can be reused to build objects from the same
family.
This is useful when you must separate the specification of an object
from its actual representation (generally for abstraction).
'''

# The __str__ function return a human-readable format, which is good for logging information about the object. 
# The __repr__ function return an “official” string representation of the object, which can be used to construct the object again.

# Abstract Building
class Building:
    # In a regular case the base class '__init__' has the building logic 
    def __init__(self):
        self.build_floor()
        self.build_size()

    def build_floor(self):
        raise NotImplementedError

    def build_size(self):
        raise NotImplementedError

    # the object representation in string format
    def __repr__(self):
        return "Floor: {0.floor} | Size: {0.size}".format(self)


# Concrete Buildings
class House(Building):
    def build_floor(self):
        self.floor = "Two"

    def build_size(self):
        self.size = "Big"


class Flat(Building):
    def build_floor(self):
        self.floor = "One"

    def build_size(self):
        self.size = "Small"

class Cottage(Building):
    def build_floor(self):
        self.floor = "One"

    def build_size(self):
        self.size = "Medium"


# In some very complex cases, it might be desirable to pull out the building
# logic into another function (or a method on another class), rather than being
# in the base class '__init__'. (This leaves you in the strange situation where
# a concrete class does not have a useful constructor)


class ComplexBuilding:
    def __repr__(self):
        return "Floor: {0.floor} | Size: {0.size}".format(self)


class ComplexHouse(ComplexBuilding):
    def build_floor(self):
        self.floor = "Three"

    def build_size(self):
        self.size = "Big and fancy"

class PentHouse(ComplexBuilding):
    def build_floor(self):
        self.floor = "Two"

    def build_size(self):
        self.size = "Big with a view of the city"

def construct_building(cls):
    building = cls()
    building.build_floor()
    building.build_size()
    return building


def main():
    
    house = House()
    print('house -> ',house)
    #Floor: Two | Size: Big
    flat = Flat()
    print('flat -> ',flat)
    #Floor: One | Size: Small
    cottage = Cottage()
    print('cottage -> ',cottage)
    #Floor: One | Size: Medium

    # Using an external constructor function:
    complex_house = construct_building(ComplexHouse)
    print('complex_house -> ',complex_house)
    pent_house = construct_building(PentHouse)
    print('pent_house -> ',pent_house)
    #Floor: One | Size: Big and fancy
    #"""


if __name__ == "__main__":
    main()