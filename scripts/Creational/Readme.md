# Factory pattern

Creational design patterns deal with an object creation. The aim of a creational design pattern is to provide better alternatives for situations where a direct object creation (which in Python happens by the __init__() function) is not convenient.

A client asks for an object without knowing where the object is coming from. The idea behind a factory is to simplify an object creation. It is easier to track which objects are created if this is done through a central function, in contrast to letting a client create objects using a direct class instantiation

The Abstract Factory design pattern is implemented as a number of Factory Methods
that belong to a single class and are used to create a family of related objects (the
parts of a car, the environment of a game, and so forth). 

Use cases

- track an object
- decouple an object creation from an object usage
- improve the performance and resource usage of an application



# Builder pattern

Imagine that we want to create an object that is composed of multiple parts and the composition needs to be done step by step. The object is not complete unless all its parts are fully created. The Builder pattern separates the construction of a complex object from its representation. In this way, the same construction can be used to create several different representations.
Builder pattern for creating an object in situations where using the Factory pattern (either a Factory Method or an Abstract Factory) is not a good option. Use cases:

- We want to create a complex object (an object composed of many parts and created in different steps that might need to follow a specific order).
- Different representations of an object are required, and we want to keep the construction of an object decoupled from its representation
- We want to create an object at one point in time but access it at a later point