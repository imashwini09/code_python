# calculator.py
# def add_numbers(a, b):
#     return a + b

# test_calculator.py
import pytest
from calculator import add_numbers

def test_add_numbers_positive():
    result = add_numbers(2, 3)
    assert result == 5, "Adding 2 and 3 should return 5"

def test_add_numbers_negative():
    result = add_numbers(-1, -4)
    assert result == -5, "Adding -1 and -4 should return -5"

def test_add_numbers_zero():
    result = add_numbers(10, 0)
    assert result == 10, "Adding 10 and 0 should return 10"

def test_add_numbers_type_error():
    with pytest.raises(TypeError):
        add_numbers("2", 3)  # Should raise TypeError for invalid input

# test_add_numbers_type_error()