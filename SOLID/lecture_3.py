class Switch:
    def __init__(self,appliance):
        self.appliance = appliance

    def toggle(self,state):
        if state == "on":
            self.appliance.turn_on()
        else:
            self.appliance.turn_off()

class Light():
    def turn_on(self):
        print("Light Turning On")
    def turn_off(self):
         print("Light Turning Off")

class Fan():
    def turn_on_fan(self):
        print("Fan Turning On")
    def turn_off_fan(self):
         print("Fan Turning Off")


light = Light()
s = Switch(light)
s.toggle("on")
s.toggle("off")

fan = Fan()
s1 = Switch(fan)
s1.toggle("on")
s1.toggle("off")