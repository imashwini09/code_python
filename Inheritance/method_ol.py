class Parent:
    def __init__(self):
        self.eye = 2

    def display(self,n):  # even if e are not passing n value it is executing because it is not overloading just skipping
        print("1st display parent")

    def display(self):
        print("2nd display parent")

class Child(Parent):

    def __init__(self,age):
        self.eye = 1
        self.age = age
        super().display()

    pass    

c = Child(4)
print(c.age)
print(c.eye)
