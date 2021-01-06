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
    def getShake():
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
    print('with no clone')

    instance = FoodFactory.getShakeOriginal()
    print("%s: I get %s %s" % (instance.getType(), instance.getValue(), instance.getName()))

    instance = FoodFactory.getShake()
    print("%s: I get %s %s" % (instance.getType(), instance.getValue(), instance.getName()))

if __name__ == "__main__":
    main()