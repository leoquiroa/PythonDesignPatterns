'''
*What is this pattern about?
This patterns aims to reduce the number of classes required by an
application. Instead of relying on subclasses it creates objects by
copying a prototypical instance at run-time.
This is useful as it makes it easier to derive new kinds of objects,
when instances of the class have only a few different combinations of
state, and when instantiation is expensive.
'''

class Prototype:

    value = "default"
    number = 111

    def clone(self, **attrs):
        """Clone a prototype and update inner attributes dictionary"""
        # Python in Practice, Mark Summerfield
        obj = self.__class__()
        obj.__dict__.update(attrs)
        return obj


class PrototypeDispatcher:
    def __init__(self):
        self._objects = {}

    def get_objects(self):
        """Get all objects"""
        return self._objects

    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Unregister an object"""
        del self._objects[name]


def main():
    dispatcher = PrototypeDispatcher()
    prototype = Prototype()
    d = prototype.clone()
    a = prototype.clone(value='a-value', category='a', color="Red")
    b = prototype.clone(value='b-value', number=333, is_checked=True)
    dispatcher.register_object('objecta', a)
    dispatcher.register_object('objectb', b)
    dispatcher.register_object('default', d)
    # all three objects
    z = [{n: p.value} for n, p in dispatcher.get_objects().items()]
    print('all three objects')
    print(z)
    dispatcher.unregister_object('default')
    # only two objects
    z = [{n: p.value} for n, p in dispatcher.get_objects().items()]
    print('only two objects')
    print(z)
    # print all the attributes per object
    print('attributes per class')
    for n, p in dispatcher.get_objects().items():
        print('n ',n)
        for k,v in p.__dict__.items():
            print(k,' : ',v)
        print('--')
    
if __name__ == "__main__":
    main()