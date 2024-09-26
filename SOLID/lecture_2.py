from abc import ABC, abstractmethod


class SwitchAble(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass


class Switch:
    def __init__(self,appliance):
        self.appliance = appliance

    def toggle(self,state):
        if state == "on":
            self.appliance.turn_on()
        else:
            self.appliance.turn_off()

class Light(SwitchAble):
    def turn_on(self):
        print("Light Turning On")
    def turn_off(self):
         print("Light Turning Off")

class Fan(SwitchAble):
    def turn_on(self):
        print("Fan Turning On")
    def turn_off(self):
         print("Fan Turning Off")

light = Light()
s = Switch(light)
s.toggle("on")
s.toggle("off")

fan = Fan()
s1 = Switch(fan)
s1.toggle("on")
s1.toggle("off")


# In this method Nobody is tightly coupled so we can create any number of class