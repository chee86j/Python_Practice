import pytest
from introtopython import (
    safe_divide, safe_divide_with_message, safe_divide_with_finally, 
    handle_multiple_exceptions, check_positive, handle_index_error, divide_with_assert, add, NegativeNumberError
)

def test_safe_divide():
    assert safe_divide(10, 2) == 5
    assert safe_divide(10, 0) == "Cannot divide by zero"

def test_safe_divide_with_message():
    assert safe_divide_with_message(10, 2) == "Division successful: 5.0"
    assert safe_divide_with_message(10, 0) == "Cannot divide by zero"

def test_safe_divide_with_finally():
    assert safe_divide_with_finally(10, 2) == 5
    # Testing for ZeroDivisionError handled within the function

def test_handle_multiple_exceptions():
    assert handle_multiple_exceptions(10, 2) == 25
    assert handle_multiple_exceptions(10, 0) == "Cannot divide by zero"
    assert handle_multiple_exceptions("10", "2") == "Invalid types used for division"

def test_check_positive():
    assert check_positive(10) == 10
    with pytest.raises(NegativeNumberError):
        check_positive(-10)

def test_handle_index_error():
    assert handle_index_error() == "Index out of range"

def test_divide_with_assert():
    assert divide_with_assert(10, 2) == 5
    with pytest.raises(AssertionError):
        divide_with_assert(10, 0)

def test_add_function():
    assert add(5, 3) == 8

# run 'python -m pytest test_introtopython.py' in the terminal to execute the tests
# if installed but not recognized in your command prompt. This can happen if the path 
# to the Python Scripts folder is not added to your system's PATH environment variable. 
# Here's how you can resolve this:

#     Add Python Scripts to PATH:
#           Find the path to the Python Scripts directory. It is usually something like 
#           C:\Python312\Scripts based on your Python installation path.
#           Add this path to your system's PATH environment variable. You can do this 
#           by searching for "Environment Variables" in Windows settings, then editing 
#           the PATH variable to include the Python Scripts path.

#     Use Python -m Option:
#           Alternatively, you can run pytest using the -m option with Python, which does 
#           not require modifying the PATH. Try this command:

#               bash

#               python -m pytest test_introtopython.py