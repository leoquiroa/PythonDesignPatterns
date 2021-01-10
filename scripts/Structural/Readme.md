# Adapter pattern

Adapter is a structural design pattern that helps us make two incompatible interfaces compatible. 
First, let's answer what incompatible interfaces really mean. If we have an old component and we want to use it in a new system, or a new component that we want to use in an old system, the two can rarely communicate without requiring any code changes. But changing the code is not always possible, either because we don't have access to it (for example, the component is provided as an external library) or because it is impractical. In such cases, we can write an extra layer that makes all the required modifications for enabling the communication between the two interfaces. This layer is called the Adapter.

Use cases 
- Does not require access to the source code of the foreign interface
- Does not violate the open/closed principle