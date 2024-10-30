# Given two numbers and an arithmetic operator (the name of it, as a string), 
# return the result of the two numbers having that operator used on them.

# a and b will both be positive integers, and a will always be the first 
# number in the operation, and b always the second.

# The four operators are "add", "subtract", "divide", "multiply".

# A few examples:(Input1, Input2, Input3 --> Output)

# 5, 2, "add"      --> 7
# 5, 2, "subtract" --> 3
# 5, 2, "multiply" --> 10
# 5, 2, "divide"   --> 2.5

# Try to do it without using if statements!

# -------------------------------------------------------------------------------------
# -----Solution 1-----Dictionary Mapping-----
def arithmetic(a, b, operator):
    return {
        'add': a + b,
        'subtract': a - b,
        'multiply': a * b,
        'divide': a / b,
    }[operator]
#   This solution uses a dictionary to map each operator to its corresponding operation
#   It then returns the result of the operation using the operator as the key to access the value in the dictionary

#   It has a time complexity of O(1) because it uses a dictionary to store the operations
#   The dictionary has a fixed size of 4, so the time complexity is constant. For the space
#   complexity, it is also O(1) because the dictionary has a fixed size of 4.
#   It is a very concise and efficient solution that avoids using if statements to provide
#   direct access to the result of the operation based on the operator.

# -------------------------------------------------------------------------------------
# -----Solution 2-----If-Elif-Else-----
def arithmetic(a, b, operator):
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    elif operator == "divide":
        return a / (b * 1.0)
#   This method used if-elif-else statements to determine the operator and perform the operation
#   It has a time complexity of O(1) because it uses if-elif-else statements to determine the operator
#   and perform the operation. The time complexity is constant because the number of operations is fixed.
#   For the space complexity, it is also O(1) because it does not use any additional data structures.
#   It is a straightforward solution that uses conditional statements to determine the operator and perform the operation.
#   This was the solution that was restricted in the prompt, but it is still a valid and efficient solution.
#   It is easier to read for beginners and provides a clear way to understand the logic behind the operation.


# -------------------------------------------------------------------------------------
# -----Solution 3-----Operator Module-----
from operator import add, mul, sub, truediv


def arithmetic(a, b, operator):
    ops = {'add': add, 'subtract': sub, 'multiply': mul, 'divide': truediv}
    return ops[operator](a, b)
#   This solution uses the operator module to perform the operation based on the operator
#   It creates a dictionary that maps each operator to the corresponding function from the operator module
#   It then uses the operator as the key to access the function and perform the operation on the two numbers
#   It has a time complexity of O(1) because it uses the operator module to perform the operation
#   The time complexity is constant because the number of operations is fixed
#   For the space complexity, it is also O(1) because it does not use any additional data structures
#   It is a concise and efficient solution that leverages the operator module to perform the operation
#   It avoids using if statements and provides direct access to the function based on the operator

#   Compared to the other Solutions, this solution is more concise and uses the operator module to perform the operation.
#   It is a more advanced solution that leverages the built-in functions from the operator module to perform the operation.

# -------------------------------------------------------------------------------------
# -----Solution 4-----Javascript Solution-----
# function arithmetic(a, b, operator){
#   switch(operator) {
#     case 'add':
#       return a + b;
#     case 'subtract':
#       return a - b;
#     case 'multiply':
#       return a * b;
#     case 'divide':
#       return a / b;
#   }
# }

#   This is a JavaScript solution that uses a switch statement to determine the operator and perform the operation.
#   It has a similar structure to the if-elif-else solution in Python and provides a clear way to handle different cases.
#   The switch statement is a control flow statement that evaluates an expression and executes the corresponding case.
#   It is a common pattern in JavaScript for handling multiple cases and providing a concise way to write conditional logic.
#   The switch statement is an alternative to if-elif-else statements and can be used to improve readability and maintainability.
#   It is a straightforward solution that demonstrates how to handle different cases based on the operator in JavaScript.