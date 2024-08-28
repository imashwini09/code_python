class Parent:
    def __init__(self):
        self.eye = 2

    def display(self):
        print("display parent")

class Child(Parent):

    def __init__(self,age):
        super().__init__() # if we dont call we cant call eye
        self.age = age

    pass

class Child1(Parent):

    def __init__(self,age):
        super().__init__() # order will change because python execute line by line
        self.eye = 1
        self.age = age

    pass

c = Child(4)
print(c.age)
print(c.eye)

c1 = Child1(4)
print(c1.age)
print(c1.eye)