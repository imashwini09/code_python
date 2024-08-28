'''
1. What is inheritence?
It is a method that allows us to create a new class that shares the same attributes and method with the original function, and add some extra functionality to the new class. It also does not disturb the original class.


2. How to make a class inherit from another class?
class Developer(Employee):


3. Structure of classes and subclasses.
When we input a function to a subclass, python follows the 'method resolution order', which is the chain of classes that it goes through to find what the method is. All classes have the built-in group of methods and attributes as their primary order.


4. How to initiate the subclass so that it can handle more information than its original class can?
There are 2 ways.
first, using the super method as follows and pass in the arguments in interest.
super.__init__()


Second, call the parent's init method explicitly and pass in the arguments in interest.
Employee.init(self, first, last, )


5. Useful tools when exploring the inheritance system.
.isinstance(instance, class)
This method returns the boolean value of whether an instance belongs to a calss
.issubclass(subclass, class)
This method returns the boolean value of whether a class has inherited from the second class.


6. Example of class inheritance
Whisky library 

++ when setting a default value for an ungiven argument, avoid using an empty mutable data type. 

'''