import unittest

# Function to test
def add_numbers(a, b):
    return a + b

class TestCalculator(unittest.TestCase):
    def test_add_numbers_positive(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 5, "Adding 2 and 3 should return 5")
    
    def test_add_numbers_negative(self):
        result = add_numbers(-1, -4)
        self.assertEqual(result, -5, "Adding -1 and -4 should return -5")
    
    def test_add_numbers_zero(self):
        result = add_numbers(10, 0)
        self.assertEqual(result, 10, "Adding 10 and 0 should return 10")

if __name__ == '__main__':
    unittest.main()