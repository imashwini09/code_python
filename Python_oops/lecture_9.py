# multiple inheritance


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


class Developer(Employee):
    raise_amount = 1.02

    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        # Employee.__init__(self,first,last,pay) same as super
        self.prog_lang = prog_lang

class Manager(Developer):
    pass


mgr_1 = Manager("Ashwini","Samal",70000,"Python")

print(help(Manager))