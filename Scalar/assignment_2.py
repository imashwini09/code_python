class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def display(self):
        print(f"[{self._x}, {self._y}]")


class ThreedPoint(Point):
    def __init__(self, x, y, z):
        super().__init__(x,y)
        self.__z = z
        # """Todo for the learner"""

    def display(self):
        print(self._x,self._y,self.__z)
        # """Todo for the learner"""

a = ThreedPoint(1,2,3)
a.display()