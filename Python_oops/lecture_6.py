# static methods

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
        
    @classmethod
    def set_raise(cls,amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp1 = Employee('Ashwini','Samal',70000)
emp2 = Employee('Dakshina','Thapa',100000)

import datetime
my_date = datetime.date(2024, 6, 7)
print(Employee.is_workday(my_date))
my_date = datetime.date(2024, 6, 8)
print(Employee.is_workday(my_date))