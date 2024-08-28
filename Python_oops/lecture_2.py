class Dog:

    species = "Canis familiaris"

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

miles = Dog("Miles", 4)
buddy = Dog("Buddy", 9)
# print(miles.name,miles.age)
# print(buddy.name,buddy.age)
# print(buddy.species)
# miles.species = "Felis silvestris"
# print(miles.species)
# print(miles.description())

print(miles)