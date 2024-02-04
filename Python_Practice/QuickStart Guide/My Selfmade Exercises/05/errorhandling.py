# Error Handling Practice Problems

# 1. Handle Division by Zero
# Write a script with a try-except block to catch and handle a division by zero error.
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Division by zero is not allowed"

# 2. Successful Division Message
# Create a try-except-else block where the else part prints a success message for division.
def divide_with_success_message(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Division by zero is not allowed"
    else:
        return f"Successful division: {result}"

# 3. Finally in Error Handling
# Demonstrate the use of a finally block in error handling which executes regardless of error occurrence.
def divide_with_finally(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Division by zero is not allowed"
    finally:
        print("Operation attempted")

# 4. Multiple Exception Types
# Write a function that handles multiple exception types including division by zero and type errors.
def handle_multiple_exceptions(a, b):
    try:
        return a / b
    except (ZeroDivisionError, TypeError) as e:
        return f"Error occurred: {e}"

# 5. Custom Exception Class
# Create and use a custom exception class in your script.
class NegativeNumberError(Exception):
    """Exception raised for negative numbers."""
    pass

def check_positive(number):
    if number < 0:
        raise NegativeNumberError("Negative numbers are not allowed")
    return number

# 6. Catching IndexError
# Write a script that safely handles an IndexError exception.
def access_list_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range"

# 7. Handle File Not Found Error
# Use a try-except block to handle an incorrect file name error while reading a file.
def read_file_safe(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found"

# 8. Input Validation with Exceptions
# Write a script to ask for user input and handle invalid input using exceptions.
def get_integer_input():
    while True:
        try:
            return int(input("Enter an integer: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")

# 9. Assert for Input Validation
# Use assert in a script for input validation, specifically for checking non-zero denominators.
def divide_with_assert(a, b):
    assert b != 0, "Denominator cannot be zero"
    return a / b

# 10. Syntax Errors vs Exceptions
# Explain the difference between syntax errors and exceptions in Python.
# Answer: Syntax errors occur when the Python parser detects incorrect code structure. Exceptions are errors detected during execution.
