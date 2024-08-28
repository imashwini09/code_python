class Student:
    def __init__(self,name,age,class_no):
        self.name = name 
        self._age = age
        self.__class_no = class_no

    def __display(self):
        print(f"student name is {self.name} with age {self._age} and reading in class {self.__class_no}")

    def displayprivate(self):
        self.__display()


s = Student("ashwini",24,10)
s.displayprivate()
print(s._Student__class_no)
# print(s.__class_no)