class Human:
    def __init__(self,gender):
        self.gender = gender

    def eat(self):
        print("Hi i can eat")

class Man(Human):
    pass


m = Man("male")
m.eat()

    