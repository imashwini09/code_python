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

class Manager(Employee):
    def __init__(self,first,last,pay,employees = None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
        
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self,emp):
        if emp not in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->' ,emp.fullname())


dev1 = Developer('Ashwini','Samal',70000,'Python')
dev2 = Developer('Dakshina','Thapa',100000,'Java')

# print(help(Developer))
# print(dev1.email,dev1.prog_lang)
# print(dev2.email,dev2.prog_lang)


mgr_1 = Manager('X','Y',150000,[dev1])

print(mgr_1.email)
mgr_1.print_emp()

mgr_1.add_emp(dev2)
print("after adding new")
mgr_1.print_emp()


print(isinstance(mgr_1,Employee))
print(isinstance(mgr_1,Developer))
print(isinstance(mgr_1,Manager))

print(issubclass(Developer,Employee))
print(issubclass(Manager,Developer))