import pytest
from errorhandling import *

def test_safe_divide():
    assert safe_divide(10, 2) == 5
    assert safe_divide(10, 0) == "Division by zero is not allowed"

def test_divide_with_success_message():
    assert divide_with_success_message(10, 2) == "Successful division: 5.0"
    assert divide_with_success_message(10, 0) == "Division by zero is not allowed"

def test_divide_with_finally(capsys):
    divide_with_finally(10, 2)
    captured = capsys.readouterr()
    assert captured.out == "Operation attempted\n"
    
def test_handle_multiple_exceptions():
    assert handle_multiple_exceptions(10, 2) == 5
    assert handle_multiple_exceptions(10, 'a') == "Error occurred: unsupported operand type(s) for /: 'int' and 'str'"
    assert handle_multiple_exceptions(10, 0) == "Error occurred: division by zero"

def test_check_positive():
    assert check_positive(10) == 10
    with pytest.raises(NegativeNumberError):
        check_positive(-10)

def test_access_list_element():
    assert access_list_element([1, 2, 3], 1) == 2
    assert access_list_element([1, 2, 3], 3) == "Index out of range"

# def test_read_file_safe():
#     assert read_file_safe("nonexistent.txt") == "File not found"
# You can add a test case for a file that exists if you want to check successful file reading

# def test_get_integer_input():
# Mocking input can be complex and might need an approach to simulate user inputs

