class Father:
    def eat(self):
        print("Eating breakfast")

    def sleep(self):
        print("sleeping early")


class Son(Father):
    def sleep(self):
        print("sleeping late")
        super().sleep()

s = Son()
s.sleep()
s.eat()

