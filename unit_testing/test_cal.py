import pytest
from calculator import add_numbers

def test_add_numbers_float():
    result = add_numbers(0.1, 0.2)
    assert result == pytest.approx(0.3, rel=1e-9), "0.1 + 0.2 should be approximately 0.3"


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, -4, -5),
    (10, 0, 10),
])
def test_add_numbers(a, b, expected):
    result = add_numbers(a, b)
    assert result == expected, f"Adding {a} and {b} should return {expected}"