#!/usr/bin/python
# -*- coding: utf-8 -*-
import six
from abc import ABCMeta

######################################################################

@six.add_metaclass(ABCMeta)
class Abstract_Coffee(object):

    #abstract
    def get_cost(self):
        pass

    #abstract
    def get_ingredients(self):
        pass

    #abstract/implemented
    def get_tax(self):
        return 0.1 * self.get_cost()

class Concrete_Coffee(Abstract_Coffee):

    #implemented
    def get_cost(self):
        return 1.00

    #implemented
    def get_ingredients(self):
        return 'coffee'
    
######################################################################

@six.add_metaclass(ABCMeta)
class Abstract_Coffee_Decorator(Abstract_Coffee):

    def __init__(self, decorated_coffee):
        self.decorated_coffee = decorated_coffee

    def get_cost(self):
        return self.decorated_coffee.get_cost()

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients()


class Sugar(Abstract_Coffee_Decorator):

    def __init__(self, decorated_coffee):
        Abstract_Coffee_Decorator.__init__(self, decorated_coffee)

    def get_cost(self):
        return self.decorated_coffee.get_cost()

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients() + ', sugar'


class Milk(Abstract_Coffee_Decorator):

    def __init__(self, decorated_coffee):
        Abstract_Coffee_Decorator.__init__(self, decorated_coffee)

    def get_cost(self):
        return self.decorated_coffee.get_cost() + 0.25

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients() + ', milk'


class Vanilla(Abstract_Coffee_Decorator):

    def __init__(self, decorated_coffee):
        Abstract_Coffee_Decorator.__init__(self, decorated_coffee)

    def get_cost(self):
        return self.decorated_coffee.get_cost() + 0.75

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients() + ', vanilla'
