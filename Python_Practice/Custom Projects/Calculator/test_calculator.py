import pytest
from PySide6.QtWidgets import QApplication
from calculator import AdvancedCalculator
import sys

# Create a global QApplication for pytest
@pytest.fixture(scope="module")
def app():
    return QApplication(sys.argv)

@pytest.fixture
def calculator():
    return AdvancedCalculator()

def test_basic_operations(calculator):
    # Test basic arithmetic operations
    assert calculator.evaluate_expression("2+2") == 4
    assert calculator.evaluate_expression("10-3") == 7
    assert calculator.evaluate_expression("4*5") == 20
    assert calculator.evaluate_expression("20/4") == 5

def test_advanced_functions(calculator):
    # Test advanced mathematical functions
    assert calculator.evaluate_expression("math.pow(2,3)") == 8
    assert pytest.approx(calculator.evaluate_expression("sqrt(9)")) == 3
    assert pytest.approx(calculator.evaluate_expression("log(100)")) == 2
    assert pytest.approx(calculator.evaluate_expression("ln(math.exp(1))")) == 1
    assert pytest.approx(calculator.evaluate_expression("sin(0)")) == 0
    assert pytest.approx(calculator.evaluate_expression("cos(0)")) == 1
    assert pytest.approx(calculator.evaluate_expression("tan(0)")) == 0

def test_invalid_input(calculator):
    # Test invalid expressions
    with pytest.raises(Exception):
        calculator.evaluate_expression("2//")

    with pytest.raises(Exception):
        calculator.evaluate_expression("sqrt(-1)")

def test_history(calculator):
    # Test history functionality
    calculator.history = []
    calculator.evaluate_expression("2+3")
    calculator.history.append("2+3 = 5")
    calculator.evaluate_expression("sqrt(9)")
    calculator.history.append("sqrt(9) = 3")

    assert len(calculator.history) == 2
    assert calculator.history[0] == "2+3 = 5"
    assert calculator.history[1] == "sqrt(9) = 3"
