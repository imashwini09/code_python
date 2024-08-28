class Human:
    def __init__(self,gender):
        self.gender = gender

    def eat(self):
        print("Human can eat")

class Man():
    def __init__(self,gender):
        self.gender = gender

    def eat(self):
        print("Hi i am man")
        print("I can eat")

class Boy(Human,Man):
    pass

class Woman:
    def __init__(self,gender):
        self.gender = gender

    def eat(self):
        print("Hi i am woman")
        print("I can eat")

class Girl(Woman,Human):
    pass

b = Boy("male")
b.eat()
g = Girl("female")
g.eat()

print(Boy.mro())

Human.eat(b)