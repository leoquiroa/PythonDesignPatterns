'''
*What is this pattern about?
The Facade pattern is a way to provide a simpler unified interface to
a more complex system. It provides an easier way to access functions
of the underlying system by providing a single entry point.
This kind of abstraction is seen in many real life situations. For
example, we can turn on a computer by just pressing a button, but in
fact there are many procedures and operations done when that happens
(e.g., loading programs from disk to memory). In this case, the button
serves as an unified interface to all the underlying procedures to
turn on a computer.
'''

# Complex computer part #1
class CPU:
    """
    Simple CPU representation.
    """

    def freeze(self):
        print("Freezing processor.")

    def jump(self, position):
        print("Jumping to:", position)

    def execute(self):
        print("Executing.")

# Complex computer part #2
class Memory:
    """
    Simple memory representation.
    """

    def load(self, position, data):
        print(f"Loading from {position} data: '{data}'.")

# Complex computer part #3
class SolidStateDrive:
    """
    Simple solid state drive representation.
    """

    def read(self, lba, size):
        return f"Some data from sector {lba} with size {size}"

# Facade
class ComputerFacade:
    """
    Represents a facade for various computer parts.
    """

    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.ssd = SolidStateDrive()

    def start(self):
        self.cpu.freeze()
        self.memory.load("0x00", self.ssd.read("100", "1024"))
        self.cpu.jump("0x00")
        self.cpu.execute()


def main():
    computer_facade = ComputerFacade()
    computer_facade.start()
    """
    Freezing processor.
    Loading from 0x00 data: 'Some data from sector 100 with size 1024'.
    Jumping to: 0x00
    Executing.
    """


if __name__ == "__main__":
    main()