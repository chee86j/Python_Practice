# Error Handling Practice Problems

# 1. Write a script with a try-except block to handle a division by zero error.
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

# 2. Create a try-except-else block where the else part prints a success message.
def safe_divide_with_message(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    else:
        return f"Division successful: {result}"

# 3. Demonstrate the use of a finally block in error handling.
def safe_divide_with_finally(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    finally:
        print("Execution completed")

# 4. Write a function that handles multiple exception types.
def handle_multiple_exceptions(a, b):
    try:
        result = a / b
        return result ** 2
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Invalid types used for division"

# 5. Create a custom exception class and use it in your script.
class NegativeNumberError(Exception):
    pass

def check_positive(number):
    if number < 0:
        raise NegativeNumberError("Negative numbers are not allowed")
    return number

# 6. Write a script that catches the IndexError exception.
def handle_index_error():
    lst = [1, 2, 3]
    try:
        return lst[5]
    except IndexError:
        return "Index out of range"

# 7. Use a try-except block to handle an incorrect file name error.
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found"

# 8. Write a script to ask for user input and handle invalid input using exceptions.
def get_integer_input():
    try:
        return int(input("Enter an integer: "))
    except ValueError:
        return "Invalid input: Please enter an integer"

# 9. Demonstrate the use of assert for input validation.
def divide_with_assert(a, b):
    assert b != 0, "Cannot divide by zero"
    return a / b

# 10. Explain the difference between syntax errors and exceptions.
# Answer:   Syntax errors occur when the parser detects an incorrect statement. 
#           Exception errors occur during execution of a valid code.


# Basics of Python Programming Practice Problems
# 1. Print your name and current year.
print("Jeff - 2024")

# 2. Create a Python file and run it using the command line.
# Instruction: Create a .py file and execute it from the terminal by
# running the command `python filename.py`.

# 3. Explain the use of indentation in Python.
# Answer:   Indentation in Python is used to define the scope of loops, 
#           functions, and classes.

# 4. Convert a simple JavaScript function to Python.
# JavaScript: function add(a, b) { return a + b; }
# Python:
def add(a, b):
    return a + b

# 5. List and explain two Python syntax rules.
# Answer:   (1) Variables must be assigned before use. 
#           (2) Indentation defines code blocks.

# 6. Write a script that asks for user input and prints it.
user_input = input("Enter Input to Be Printed: ")
print(user_input)

# 7. Explain the difference between a script and a program.
# Answer:   A script is a simple, usually small, program, often used 
#           for automating tasks. A program is a collection of scripts 
#           and code modules that work together to perform complex tasks.

# 8. Create a Python script that calculates and prints the area of a rectangle.
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
area = length * width
print("Area of the rectangle:", area)

# 9. Describe how Python handles errors during script execution.
# Answer:   Python raises exceptions when it encounters errors and will stop 
#           the program unless the exception is handled.

# 10. Write a script that opens a text file and prints its contents.
with open('yourfile.txt', 'r') as file:
    print(file.read())
