# classmethod and static method
# in classmethod class wih be our 1st agrument instead of instance

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


# emp1 = Employee('Ashwini','Samal',70000)
# emp2 = Employee('Dakshina','Thapa',100000)

# Employee.set_raise(1.05)

# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)

# emp1.set_raise(1.06)

# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)


emp_str_1 = 'Ashwini-Samal-70000'
emp_str_2 = 'Dakshina-Thapa-100000'

new_emp_1 = Employee.from_string(emp_str_1)
new_emp_2 = Employee.from_string(emp_str_2)

print(new_emp_1.email)
print(new_emp_2.email)




