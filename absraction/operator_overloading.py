class ComplexNumber:
    def __init__(self,r,i):
        self.real = r
        self.imaginary = i

    def __add__(x,y):
        return f"{x.real + y.real}+{x.imaginary+y.imaginary}i"

c1 = ComplexNumber(1,2)
c2 = ComplexNumber(3,4)
print(c1+c2)