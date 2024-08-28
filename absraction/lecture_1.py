from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self,n):
        self.no_of_types = n

    @abstractmethod
    def start(self):
        pass
    def display(self):
        print("HI i am calling vehicle")


class Bike(Vehicle):
    def __init__(self,n,color):
        super().__init__(n)
    def start(self):
        print("start with kick")
    def display(self):
        print("i am in bike class")

class Car(Vehicle):
    def __init__(self,n):
        self.no_of_tyres = n
    def start(self):
        print("start with key")


bike = Bike(2,"black")
bike.start()
bike.display()