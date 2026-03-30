# test_calculator.py
import unittest
from unittest.mock import patch
from calu import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_normal(self):
        # Actual function call
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)

    @patch.object(Calculator, 'add', return_value=10)
    def test_add_mocked(self, mock_add):
        # The real function is replaced with a mock
        result = self.calc.add(100, 200)
        self.assertEqual(result, 10)  # Mocked value
        mock_add.assert_called_once_with(100, 200)  # Verify call


if __name__ == "__main__":
    unittest.main()
