import unittest
from PySide6.QtWidgets import QApplication
from calculator import AdvancedCalculator
import sys

class TestAdvancedCalculator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication(sys.argv)  # Set up a QApplication for testing

    def setUp(self):
        self.calculator = AdvancedCalculator()

    def test_basic_operations(self):
        # Test basic arithmetic operations
        self.assertEqual(self.calculator.evaluate_expression("2+2"), 4)
        self.assertEqual(self.calculator.evaluate_expression("10-3"), 7)
        self.assertEqual(self.calculator.evaluate_expression("4*5"), 20)
        self.assertEqual(self.calculator.evaluate_expression("20/4"), 5)

def test_advanced_functions(self):
    # Advanced mathematical functions
    self.assertEqual(self.calculator.evaluate_expression("math.pow(2,3)"), 8)
    self.assertAlmostEqual(self.calculator.evaluate_expression("sqrt(9)"), 3)
    self.assertAlmostEqual(self.calculator.evaluate_expression("log(100)"), 2)
    self.assertAlmostEqual(self.calculator.evaluate_expression("ln(math.exp(1))"), 1)
    self.assertAlmostEqual(self.calculator.evaluate_expression("sin(0)"), 0)
    self.assertAlmostEqual(self.calculator.evaluate_expression("cos(0)"), 1)
    self.assertAlmostEqual(self.calculator.evaluate_expression("tan(0)"), 0)

    def test_invalid_input(self):
        # Test invalid expressions
        with self.assertRaises(Exception):
            self.calculator.evaluate_expression("2//")

        with self.assertRaises(Exception):
            self.calculator.evaluate_expression("sqrt(-1)")

    def test_history(self):
        # Test history functionality
        self.calculator.history = []
        self.calculator.evaluate_expression("2+3")
        self.calculator.history.append("2+3 = 5")
        self.calculator.evaluate_expression("sqrt(9)")
        self.calculator.history.append("sqrt(9) = 3")

        self.assertEqual(len(self.calculator.history), 2)
        self.assertEqual(self.calculator.history[0], "2+3 = 5")
        self.assertEqual(self.calculator.history[1], "sqrt(9) = 3")

    def tearDown(self):
        del self.calculator

    @classmethod
    def tearDownClass(cls):
        cls.app.exit()

if __name__ == "__main__":
    unittest.main()

# To run the unit tests, use the following command in your terminal:
# `python unittest_calculator.py`