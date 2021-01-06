class Assembler:
    __builder = None
   
    def ToBuild(self, builder):
        self.__builder = builder
   
    def GetterAndSetter(self):
        car = CarSkeleton()
      
        # First goes the body
        body = self.__builder.getBody()
        car.setBody(body)
        
        # Then engine
        engine = self.__builder.getEngine()
        car.setEngine(engine)
        
        # And four wheels
        i = 0
        while i < 4:
            wheel = self.__builder.getWheel()
            car.attachWheel(wheel)
            i += 1
        return car

# The whole product
class CarSkeleton:
    def __init__(self):
        self.__wheels = list()
        self.__engine = None
        self.__body = None

    def setBody(self, body):
        self.__body = body

    def attachWheel(self, wheel):
        self.__wheels.append(wheel)

    def setEngine(self, engine):
        self.__engine = engine

    def specification(self):
        print("body: %s" % self.__body.shape)
        print("engine horsepower: %d" % self.__engine.horsepower)
        print("tire size: %d\'" % self.__wheels[0].size)

#####################################################################################
# Abstract

class Builder:
    def getWheel(self): pass
    def getEngine(self): pass
    def getBody(self): pass

# Car parts
class Wheel:
    size = None

class Engine:
   horsepower = None

class Body:
   shape = None

#####################################################################################
# Definition
class Jeep(Builder):
   
    def getWheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel
   
    def getEngine(self):
        engine = Engine()
        engine.horsepower = 400
        return engine
   
    def getBody(self):
        body = Body()
        body.shape = "SUV"
        return body

class Volkswagen(Builder):
   
    def getWheel(self):
        wheel = Wheel()
        wheel.size = 32
        return wheel
   
    def getEngine(self):
        engine = Engine()
        engine.horsepower = 800
        return engine
   
    def getBody(self):
        body = Body()
        body.shape = "Hatchback"
        return body

#####################################################################################

def main():
    # initializing the class
    assembler = Assembler()
    jeep = Jeep() 
    volkswagen = Volkswagen()
    
    # Build Jeep
    print("Jeep")
    assembler.ToBuild(jeep)
    jeep = assembler.GetterAndSetter()
    jeep.specification()
    print("--")
    # Build Volkswagen
    print("Volkswagen")
    assembler.ToBuild(volkswagen)
    volkswagen = assembler.GetterAndSetter()
    volkswagen.specification()

if __name__ == "__main__":
    main()