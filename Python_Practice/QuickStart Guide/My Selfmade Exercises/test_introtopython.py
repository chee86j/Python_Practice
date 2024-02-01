from introtopython import (
    safe_divide, safe_divide_with_message, safe_divide_with_finally, 
    handle_multiple_exceptions, check_positive, handle_index_error, 
    read_file, divide_with_assert, add, NegativeNumberError
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

def test_read_file():
    # Note: This test requires a 'testfile.txt' with known content for accurate testing
    assert read_file('testfile.txt') == 'test'
    assert read_file('nonexistent.txt') == "File not found"

def test_divide_with_assert():
    assert divide_with_assert(10, 2) == 5
    with pytest.raises(AssertionError):
        divide_with_assert(10, 0)

def test_add_function():
    assert add(5, 3) == 8
