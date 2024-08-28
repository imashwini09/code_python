# class variable and instance variable

class Employee:

    num_of_employee = 0
    raise_amount = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first +'.'+last + '@company.com'

        Employee.num_of_employee += 1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) 
        # self.pay = int(self.pay * Employee.raise_amount) 

emp1 = Employee('Ashwini','Samal',70000)
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
print(Employee.raise_amount)
print(emp1.raise_amount)
# print(Employee.__dict__)
Employee.raise_amount = 1.05
print(Employee.raise_amount)
print(emp1.raise_amount)
emp1.raise_amount = 1.06
print(Employee.raise_amount)
print(emp1.raise_amount)