class NamingConventionMeta(type):
    def __new__(cls, name, bases, attrs):
        if not name.startswith("My"):
            raise ValueError("Class name must start with 'My'")
        # Add a default method
        attrs["get_class_name"] = lambda self: name
        return super().__new__(cls, name, bases, attrs)

class MyCalculator(metaclass=NamingConventionMeta):
    def add_numbers(self, a, b):
        return a + b

# This will raise ValueError
# class Calculator(metaclass=NamingConventionMeta):
#     pass