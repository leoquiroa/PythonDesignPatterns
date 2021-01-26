'''
The Prototype design pattern helps us with creating object clones. In its simplest
version, the Prototype pattern is just a clone() function that accepts an object as
an input parameter and returns a clone of it.
'''

import copy
    
class A:
    def __init__(self):
        self.x = 18
        self.msg = 'Hello'

class B(A):
    def __init__(self):
        A.__init__(self)
        self.y = 34
    def __str__(self):
        return '{}, {}, {}'.format(self.x, self.msg, self.y)

if __name__ == '__main__':
    b = B()
    c = copy.deepcopy(b)
    print([str(i) for i in (b, c)])
    print([i for i in (b, c)])
    
    '''
    what's important is to notice that the two objects reside in two different memory addresses 
    (the 0x... part). This means that the two objects are two independent copies.
    '''