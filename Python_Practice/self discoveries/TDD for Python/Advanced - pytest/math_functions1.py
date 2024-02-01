# pytest
# -------------------------------------------------------------------------------------------

# Advance Testing - Using the Third-Party Library pytest is more sophisticated output and 
# additional features, consider using a third-party library like pytest. It's a popular 
# testing framework in the Python community, known for its simple syntax and powerful 
# features, including detailed and readable error reporting.

# To run the pytest test you go to the directory where the test file is located and 
# run 'pytest test_math_functions.py' in the terminal.
# -------------------------------------------------------------------------------------------

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def square(a):
    return a * a

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number")
    return a ** 0.5

def clear():
    return 0