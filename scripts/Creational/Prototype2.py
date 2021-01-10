import copy

class Prototype:

    _type = None
    _amount = None
    _name = None

    def clone(self):
        pass

    def getType(self):
        return self._type

    def getValue(self):
        return self._amount

    def getName(self):
        return self._name

class McDonalds(Prototype):

    def __init__(self, number, name):
        self._type = "Hamburger"
        self._amount = number
        self._name = name

    def clone(self):
        return copy.copy(self)

class HomeMade(Prototype):

    """ Concrete prototype. """

    def __init__(self, number, name):
        self._type = "Own Meal"
        self._amount = number
        self._name = name

    def clone(self):
        return copy.copy(self)

class FoodFactory:

    """ Manages prototypes.
    Static factory, that encapsulates prototype
    initialization and then allows instatiation
    of the classes from these prototypes.
    """

    __bigmac = None
    __cheeseburger = None
    __shake = None
    __salad = None

    @staticmethod
    def initialize():
        FoodFactory.__bigmac = McDonalds(1, 'BigMac')
        FoodFactory.__cheeseburger = McDonalds(2, 'CheeseBurger')
        FoodFactory.__shake = HomeMade(3, 'Shake')
        FoodFactory.__salad = HomeMade(5, 'Salad')

    @staticmethod
    def getBigMac():
        return FoodFactory.__bigmac.clone()

    @staticmethod
    def getCheeseBurger():
        return FoodFactory.__cheeseburger.clone()

    @staticmethod
    def getShakeClone():
        return FoodFactory.__shake.clone()

    @staticmethod
    def getShakeOriginal():
        return FoodFactory.__shake

    @staticmethod
    def getSalad():
        return FoodFactory.__salad.clone()

def main():
    FoodFactory.initialize()

    instance = FoodFactory.getBigMac()
    print("%s: I get %s %s" % (instance.getType(), instance.getValue(), instance.getName()))

    instance = FoodFactory.getCheeseBurger()
    print("%s: I get %s %s" % (instance.getType(), instance.getValue(), instance.getName()))

    instance = FoodFactory.getSalad()
    print("%s: I get %s %s" % (instance.getType(), instance.getValue(), instance.getName()))

    # with no clone
    print('--')
    print('Initial conditions for Original and Clone')

    original = FoodFactory.getShakeOriginal()
    print("original -> %s: I get %s %s" % (original.getType(), original.getValue(), original.getName()))

    clone = FoodFactory.getShakeClone()
    print("clone ->%s: I get %s %s" % (clone.getType(), clone.getValue(), clone.getName()))

    print('--')
    print('Original_A and new clone_A after set original._amount = 8')
    print('--')
    original._amount = 8
    original_A = FoodFactory.getShakeOriginal()
    clone_A = FoodFactory.getShakeClone()
    print("original -> %s: I get %s %s" % (original.getType(), original.getValue(), original.getName()))
    print("clone -> %s: I get %s %s" % (clone.getType(), clone.getValue(), clone.getName()))
    print("original_A -> %s: I get %s %s" % (original_A.getType(), original_A.getValue(), original_A.getName()))
    print("clone_A -> %s: I get %s %s" % (clone_A.getType(), clone_A.getValue(), clone_A.getName()))

    print('--')
    print('Original_B and new clone_B after set clone._amount = 11')
    print('--')
    clone._amount = 11
    original_B = FoodFactory.getShakeOriginal()
    clone_B = FoodFactory.getShakeClone()
    print("original -> %s: I get %s %s" % (original.getType(), original.getValue(), original.getName()))
    print("clone -> %s: I get %s %s" % (clone.getType(), clone.getValue(), clone.getName()))
    print("original_A -> %s: I get %s %s" % (original_A.getType(), original_A.getValue(), original_A.getName()))
    print("clone_A -> %s: I get %s %s" % (clone_A.getType(), clone_A.getValue(), clone_A.getName()))
    print("original_B -> %s: I get %s %s" % (original_B.getType(), original_B.getValue(), original_B.getName()))
    print("clone_B -> %s: I get %s %s" % (clone_B.getType(), clone_B.getValue(), clone_B.getName()))

if __name__ == "__main__":
    main()