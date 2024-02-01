# Using the basic unittest module
# -----------------------------------------------------------------------------------------------------------

import unittest # import the unittest module and the functions we want to test
from math_functions import add, subtract # import the functions we want to test from the math_functions module

class TestMathFunctions(unittest.TestCase): # create a class that inherits from unittest.TestCase

    # Test case for the add function
    def test_add(self):
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-1, 1), 0)

    # Test case for the subtract function
    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(2, 3), -1)

    # Test cases for multiply function
    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 3), -6)

    # Test cases for divide function
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertRaises(ValueError, divide, 10, 0)  # Testing division by zero

    # Test cases for square function
    def test_square(self):
        self.assertEqual(square(4), 16)
        self.assertEqual(square(-3), 9)

    # Test cases for square_root function
    def test_square_root(self):
        self.assertEqual(square_root(9), 3)
        self.assertRaises(ValueError, square_root, -4)  # Testing square root of negative number

    # Test case for clear function
    def test_clear(self):
        self.assertEqual(clear(), 0)

if __name__ == '__main__':
    unittest.main()
