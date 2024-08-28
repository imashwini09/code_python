class Employee:
    def __init__(self,name,empid,age,salary):
        self.name = name
        self.empid = empid
        self.age = age
        self.salary = salary

    def details(self):
        return f"{self.name} with employee id is {self.empid} has salary {self.salary}"


class Developer(Employee):
    pass

Dev = Employee('Ashwini',1,24,70000)
print(Dev.details())

