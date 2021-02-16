class Publisher:

    def __init__(self):
        self.observers = []

    def add(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
        else:
            print('Failed to add: {}'.format(observer))

    def remove(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            print('Failed to remove: {}'.format(observer))

    def notify(self):
        for o in self.observers:
            o.notify(self)

# Formatter

class DefaultFormatter(Publisher):

    def __init__(self, name):
        Publisher.__init__(self)
        self.name = name
        self._data = 0

    def __str__(self):
        return "{}: '{}' has data = {}".format(type(self).__name__,self.name, self._data)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_value):
        try:
            self._data = int(new_value)
        except ValueError as e:
            print('Error: {}'.format(e))
        else:
            self.notify()
            
class HexFormatter:

    def notify(self, publisher):
        print("{}: '{}' has now hex data = {}. Original = {}".format(
            type(self).__name__, publisher.name, hex(publisher.data),publisher.data))

class BinaryFormatter:

    def notify(self, publisher):
        print("{}: '{}' has now bin data = {}. Original = {}".format(
            type(self).__name__, publisher.name, bin(publisher.data),publisher.data))

def main():
    print('--')
    df = DefaultFormatter('test1')
    print(df)
    print('--')

    hf = HexFormatter()
    df.add(hf)
    df.data = 3
    print(df)
    print('--')

    bf = BinaryFormatter()
    df.add(bf)
    df.data = 21
    print(df)
    print('--')

    # remove hexa
    df.remove(hf)
    # change value
    df.data = 40
    print(df)
    print('--')

    # error bcs try to remove non existent hexa
    df.remove(hf)
    # error bcs try to add again the bin
    df.add(bf)
    # error bcs the data must be integer
    df.data = 'hello'
    print('--')

    # rollback
    print(df)
    print('--')
    df.data = 15.8
    print(df)

if __name__ == '__main__':
    main()