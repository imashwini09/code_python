import pytest
from metaclass_example import MyCalculator, NamingConventionMeta

def test_metaclass_naming_convention():
    with pytest.raises(ValueError, match="Class name must start with 'My'"):
        class InvalidClass(metaclass=NamingConventionMeta):
            pass

def test_metaclass_added_method():
    calc = MyCalculator()
    assert calc.get_class_name() == "MyCalculator", "Metaclass should add get_class_name method"

def test_add_numbers():
    calc = MyCalculator()
    result = calc.add_numbers(2, 3)
    assert result == 5, "Adding 2 and 3 should return 5"