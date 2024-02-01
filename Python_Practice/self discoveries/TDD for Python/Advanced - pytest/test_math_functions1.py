# Using 3rd Party Library pytest
# -----------------------------------------------------------------------------------------------------------

from math_functions import add, subtract, multiply, divide, square, square_root, clear
import pytest

def test_add():
    assert add(3, 4) == 7
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(2, 3) == -1

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6

def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):
        divide(10, 0)  # Testing division by zero

def test_square():
    assert square(4) == 16
    assert square(-3) == 9

def test_square_root():
    assert square_root(9) == 3
    with pytest.raises(ValueError):
        square_root(-4)  # Testing square root of negative number

def test_clear():
    assert clear() == 0
