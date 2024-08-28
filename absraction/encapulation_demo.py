class Student:
    def __init__(self,name,age,class_no):
        self.name = name 
        self._age = age
        self.__class_no = class_no

    def __display(self):
        print(f"student name is {self.name} with age {self._age} and reading in class {self.__class_no}")

    def displayprivate(self):
        self.__display()

    def get_class(self):
        return self.__class_no

    def set_class(self,number):
        if number > 12:
            print("invalid ")
        else:
            self.__class_no = number
class Branch(Student):
    def show(self):
        print(f"my age is {self._age}")


s = Student("ashwini",24,10)
# s.displayprivate()
# print(s._Student__class_no)
# print(s.__class_no)
print(s.get_class())
s.set_class(13)
print(s.get_class())
s.set_class(12)
print(s.get_class())