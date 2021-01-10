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

# Prototype pattern

Sometimes, we need to create an exact copy of an object. For instance, assume that you want to create an application for storing, sharing, and editing (such as modifying, adding notes, and removing) culinary recipes. User Bob finds a cake recipe and after making a few modifications he thinks that his cake is delicious, and he wants to share it with his friend, Alice. But what does sharing a recipe mean? If Bob wants to do some further experimentation with his recipe after sharing it with Alice, will the new changes also be visible in Alice's recipe? Can Bob keep two copies of the cake recipe? His delicious cake recipe should remain unaffected by any changes made in the experimental cake recipe.

Such problems can be solved by allowing the users to have more than one independent copy of the same recipe. Each copy is called a clone, because it is an exact copy of the original object at a specific point in time. The time aspect is important, since it affects what the clone contains.

Prototype is used for creating exact copies of objects. Creating a copy of an object can actually mean two things:

- Relying on references, which happens when a shallow copy is created
- Duplicating everything, which happens when a deep copy is created
- "A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.
- A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.