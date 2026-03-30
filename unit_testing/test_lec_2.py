import pytest

def add_numbers(a, b):
    return a + b

@pytest.mark.skip(reason="Test not ready yet")
def test_add_numbers_skipped():
    result = add_numbers(2, 3)
    assert result == 5

def test_add_numbers_conditional_skip():
    if 'a' == 'a':
        pytest.skip("Skipping due to condition")
    result = add_numbers(2, 3)
    assert result == 5