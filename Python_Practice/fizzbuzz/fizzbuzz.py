# This short project is based on a classic "group word game for children" 
# that helps them learn division. Children sit in a circle; One child says
# "1," the next child says "2," and so on. However, any number divisible 
# by three is replaced with "fizz," any number divisible by five is replaced 
# with "buzz," and any number divisible by both three and five is replaced by 
#"fizz buzz." Children are eliminated if they hesitate or make a mistake.

# Solution 1
for var in range(1, 21):
    if var % 5 == 0 and var % 3 == 0:
        print("FizzBuzz")
    elif var % 3 == 0:
        print("Fizz")
    elif var % 5 == 0:
        print("Buzz")
    else:
        print(var)

# Python vs JavaScript - Learning Summary

# Syntax Differences:
    # - Python uses indentation for blocks, no curly braces {} as in JavaScript.
    # - No semicolons at the end of statements in Python.

# For Loop Structure:
    # - JavaScript: for (let i = start; i < end; i++) {}
    # - Python: for var in range(start, end):

# Conditional Statements:
    # - Python uses 'elif' instead of JavaScript's 'else if'.
    # - Parentheses around conditions are not required in Python.

# Print Function:
    # - Python uses 'print()' instead of JavaScript's 'console.log()'.

# Modulo Operator:
    # - The modulo operator '%' works similarly in both Python and JavaScript.

# String Quotes:
    # - Python allows single, double, and triple quotes for strings.

# Logical Operators:
    # - Python uses 'and', 'or', 'not' instead of JavaScript's '&&', '||', '!'.

# Remember, these are foundational differences and similarities. Python has many more features and nuances that you'll learn as you continue your coding journey.

# ---------------------------------------------------------------
# Solution 2
# Python Explanation for JavaScript Developers
result = []  # This is like initializing an empty array in JS: let result = [];

for i in range(1, 21):  # For loop, similar to JS: for (let var = 1; var <= 20; var++) {
    output = ""  # Initializing an empty string for each iteration, like let output = "";

    # The following are similar to JS. If the conditions are true, concatenate the string.
    if i % 3 == 0:  
        output += "Fizz"  # Similar to output = output + "Fizz" or output += "Fizz" in JS
    if i % 5 == 0:
        output += "Buzz"  # Similar to output = output + "Buzz"

    # If output is still an empty string, convert the number to a string.
    if output == "":  
        output = str(i)  # In JS, this would be output = String(var) or using template literals

    result.append(output)  # Similar to result.push(output) in JS; adds output to the result list
    # append() method in Python adds a single item to the end of a list. This is akin to 
    # JavaScript's array push() method.
# The result list now contains the FizzBuzz outputs, analogous to an array in JS

# ---------------------------------------------------------------
#Solution 2 Logic
    # Start a for loop to iterate through the numbers (e.g., range(1, 21))

    # Initialize an empty string for each iteration

    # Check if the current number is divisible by 3
    # If yes, concatenate 'Fizz' to the string

    # Check if the current number is divisible by 5
    # If yes, concatenate 'Buzz' to the string

    # Check if the string is still empty
    # If it is, print the number
    # Otherwise, print the string

# End of for loop

# ---------------------------------------------------------------
# Solution 3 - More Modular and ReUsable
# Python Explanation for JavaScript Developers

# Defining a function in Python
def fizzbuzz(n):  # Similar to JavaScript's function fizzbuzz(n) { ... }
    # For loop in Python
    for i in range(1, n+1):  # Similar to for (let i = 1; i <= n; i++) { ... } in JavaScript

        # Conditional logic - if, elif (else if in JS), and else
        if i % 5 == 0 and i % 3 == 0:  # Checks if divisible by both 3 and 5
            print("FizzBuzz")  # Similar to console.log("FizzBuzz") in JavaScript
        elif i % 3 == 0:  # Checks if divisible by 3
            print("Fizz")  # Similar to console.log("Fizz") in JavaScript
        elif i % 5 == 0:  # Checks if divisible by 5
            print("Buzz")  # Similar to console.log("Buzz") in JavaScript
        else:  # Executes if none of the above conditions are true
            print(i)  # Prints the number, similar to console.log(i) in JavaScript

# Getting user input in Python
end = int(input("How high should FizzBuzz go? > "))  # Similar to parseInt(prompt("...")) in JavaScript

# Calling the function
fizzbuzz(end)  # Similar to calling a function in JavaScript: fizzbuzz(end);

# ---------------------------------------------------------------
# Solution 4 - Using a While Loop with Error Handling
# Function Definition in Python
def fizzbuzz(n): # Similar to JS's function fizzbuzz(n) { ... }
    # For loop - iterating from 1 to n (inclusive)
    for i in range(1, n+1):
        # Conditional checks for FizzBuzz, Fizz, and Buzz
        if i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Infinite loop - keeps running until a break statement is encountered
while True: # ~ to JS's while (true) { ... }
    # Getting user input
    user_input = input("How high should FizzBuzz go? > ") # ~ to JS's prompt("...")
    try: # try block for error handling ~ JS's try catch block
        # Attempt to convert input to an integer
        end = int(user_input)
        # If successful, call the fizzbuzz function and pass the integer
        fizzbuzz(end)
        # Exit the loop after successful execution
        break
    except ValueError: #ValueError ~ to JS's TypeError
        # Error handling: informs the user if the input is not a valid integer
        print(f"{user_input} is not a valid integer.")
        # ~ to JS's console.log(`${user_input} is not a valid integer.`)
        # String interpolation in Python ~ JavaScript's template literals

# This script keeps asking for a valid integer input and runs fizzbuzz up to that number.
# It only stops (breaks the loop) when a valid integer is provided.

# ---------------------------------------------------------------
# Run the Script through the Terminal (Command Line):

# 1. Open the terminal and navigate to the directory where the script is saved.
# 2. Type the following command and press Enter:
# python fizzbuzz.py
# 3. Enter a valid integer when prompted.
# 4. Press Ctrl+C to exit the script.
    
# ---------------------------------------------------------------
# Solution 5 - Importing the Script Function into another Python
# Script or Interactive Session (like the Python shell or an 
# IPython notebook).
        
import sys

def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# __name__ == '__main__' Explanation:
# - This block allows you to import the fizzbuzz function and 
#   use it in another Python script or interactive session.
# - When a Python script is run, Python sets some special 
#   variables; __name__ is one of them.
# - If the script is run directly (e.g., python fizzbuzz.py), 
#   __name__ is '__main__'.
# - If imported (e.g., import fizzbuzz), __name__ is the 
#   script/module name ('fizzbuzz'), and this block won't execute.
# - This structure lets you use the fizzbuzz function by importing 
#   it (e.g., fizzbuzz.fizzbuzz(5)) and also to run it directly 
#   with arguments from the command line (e.g., python fizzbuzz.py 20).


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <number>")
        exit(1)
    try:
        end = int(sys.argv[1])
        fizzbuzz(end)
    except ValueError:
        print(f"The argument '{sys.argv[1]}' is not a valid integer.")

#   This allow you to import the function and run it in the terminal 
#   ('import fizbuzz' then 'fizbuzz.fizzbuzz(5)')?
        
#        if __name__ == '__main__'::

#   This is a common Python idiom. When a Python script is run, Python sets some special variables, and __name__ is one of them. If the script is run directly (like python fizzbuzz.py), __name__ is set to '__main__'.
#   However, if the script is imported into another script (like import fizzbuzz), __name__ is set to the name of the script/module (in this case, 'fizzbuzz'). Thus, the code inside this if block won't run when the script is imported as a module.
#   This structure lets you use the fizzbuzz function by importing it (like fizzbuzz.fizzbuzz(5)) and also to run it directly with arguments from the command line (like python fizzbuzz.py 20).
        

# ---------------------------------------------------------------
# Solution 5 Explained in terms familiar to a JavaScript developer:
        
        # Python Script Explanation for a JavaScript Developer

import sys  # Similar to 'require' in Node.js

def fizzbuzz(n):
    # Function definition in Python, like 'function fizzbuzz(n) { ... }' in JavaScript
    for i in range(1, n+1):  # For loop, similar to 'for (let i = 1; i <= n; i++) { ... }' in JS
        # Conditional checks as in JavaScript (if, else if, else)
        if i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz")  # Similar to 'console.log("FizzBuzz")' in JS
        elif i % 3 == 0:
            print("Fizz")  # Similar to 'console.log("Fizz")' in JS
        elif i % 5 == 0:
            print("Buzz")  # Similar to 'console.log("Buzz")' in JS
        else:
            print(i)  # Similar to 'console.log(i)' in JS

# Special '__name__' variable in Python
if __name__ == '__main__':
    # This block checks if the script is run directly or imported
    # Similar to 'if (require.main === module) { ... }' in Node.js
    if len(sys.argv) != 2:  # Checking the number of command-line arguments
        print(f"Usage: python {sys.argv[0]} <number>")  # Usage message, like 'console.log' in JS
        exit(1)  # Exiting the script, akin to 'process.exit(1)' in Node.js
    try:
        # Try-Except block in Python, similar to try-catch in JavaScript
        end = int(sys.argv[1])  # Attempting to convert argument to an integer
        fizzbuzz(end)  # Calling the fizzbuzz function
    except ValueError:
        # Handling ValueError if conversion fails
        print(f"The argument '{sys.argv[1]}' is not a valid integer.")  # Error message, like 'console.error' in JS

# This script can be run directly with a command-line argument or imported into another Python script.

"""
Summary: Transition from JavaScript to Python - FizzBuzz Example

1. Python Syntax vs JavaScript Syntax:
   - Python uses indentation for code blocks, not braces {}.
   - No semicolons at the end of statements in Python.

2. For Loop:
   - Python’s 'for i in range(1, n+1)' is like JavaScript’s 'for (let i = 1; i <= n; i++)'.
   - 'range(start, stop)' in Python generates numbers, where 'stop' is exclusive.

3. Conditional Statements:
   - Python uses 'if', 'elif' (else if), and 'else', similar to JavaScript.
   - Conditions in Python do not require parentheses.

4. Function Definition:
   - Functions are defined using 'def' in Python, akin to 'function' in JavaScript.
   - Example: 'def fizzbuzz(n):' vs 'function fizzbuzz(n) { ... }'.

5. Print Function:
   - Python uses 'print()' for console output, equivalent to 'console.log()' in JavaScript.

6. Command-Line Arguments:
   - Python uses the 'sys' module for command-line arguments.
   - 'sys.argv' is a list containing arguments, similar to 'process.argv' in Node.js.

7. Modular Code with '__name__ == "__main__"':
   - Allows script to be used both as an importable module and standalone script.
   - Similar to using a function call based on a condition in JavaScript.

8. Error Handling:
   - Python uses 'try-except' blocks, akin to 'try-catch' in JavaScript.

9. SSH and Git Usage in Python Development:
   - Understanding SSH and GitHub setup is important for managing Python code.

10. The FizzBuzz Logic:
    - Involves iterating through a range of numbers and applying conditional checks.
    - Prints "Fizz", "Buzz", "FizzBuzz", or the number based on divisibility by 3 and 5.

This summary encapsulates key points for JavaScript developers transitioning to Python, using the FizzBuzz problem as an illustrative example.
"""
# An Alternative Solution using a List of Comprensions to Create a List of Strings
import sys

def fizzbuzz(n):
    return '\n'.join(
        "FizzBuzz" if i % 3 == 0 and i % 5 == 0 else
        "Fizz" if i % 3 == 0 else
        "Buzz" if i % 5 == 0 else
        str(i) 
        for i in range(1, n+1)
    )

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <number>")
        sys.exit(1)
    
    try:
        end = int(sys.argv[1])
        print(fizzbuzz(end))
    except ValueError:
        print(f"The argument '{sys.argv[1]}' is not a valid integer.")
        sys.exit(1)

# ---------------------------------------------------------------
# Explanation of the Alternative Solution 
"""
Python FizzBuzz Explanation for a JavaScript Developer

1. List Comprehension:
   - This implementation uses Python's list comprehension to create a list.
   - Similar to JavaScript's map() or a loop to construct an array.
   - The 'join()' function concatenates list elements into a single string, separated by newlines.

2. Inline Conditional (Ternary) Operators:
   - Uses inline conditional expressions, like ternary operators in JavaScript (condition ? trueCase : falseCase).
   - Evaluates and assigns "Fizz", "Buzz", "FizzBuzz", or the string of the number to each list element.

3. Function Return:
   - The 'fizzbuzz' function returns a single string, concatenating all elements with newlines.
   - Comparable to constructing and joining an array into a single string in JavaScript.

4. Command-Line Argument Handling:
   - Checks and uses command-line arguments ('sys.argv'), similar to JavaScript.
   - 'sys.exit(1)' exits the program with an error status, like 'process.exit(1)' in Node.js.

5. Error Handling with Try-Except:
   - Similar to try-catch in JavaScript, used here for validating and converting command-line arguments.

6. Differences from Previous Example:
   - Earlier example printed results in a loop, directly to the console.
   - This approach builds a list with list comprehension and returns a formatted string.
   - The result is printed after calling the function, not line-by-line in the loop.

This script showcases Python's list comprehension and inline conditional logic, offering a compact and Pythonic way to solve FizzBuzz, compared to a traditional loop approach in JavaScript.
"""

# With In-Line Comments
import sys

def fizzbuzz(n):
    # Using list comprehension, similar to JavaScript's map() or loops for array construction.
    # Inline conditional expressions (like ternary operators in JS) determine the FizzBuzz value.
    return '\n'.join(
        "FizzBuzz" if i % 3 == 0 and i % 5 == 0 else  # Both divisible by 3 and 5
        "Fizz" if i % 3 == 0 else                    # Divisible by 3
        "Buzz" if i % 5 == 0 else                    # Divisible by 5
        str(i)                                       # Not divisible by 3 or 5, return number
        for i in range(1, n+1)                       # Looping from 1 to n
    )

if __name__ == '__main__':
    # Command-line argument handling, similar to process.argv in Node.js.
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <number>")  # Print usage if incorrect arguments
        sys.exit(1)  # Exit with error status, akin to process.exit(1) in Node.js

    try:
        # Convert argument to integer, similar to parseInt in JS.
        end = int(sys.argv[1])
        print(fizzbuzz(end))  # Call fizzbuzz and print result
    except ValueError:
        # Error handling: if conversion fails, print error message.
        print(f"The argument '{sys.argv[1]}' is not a valid integer.")
        sys.exit(1)  # Exit with error status

# This script demonstrates a Pythonic approach to FizzBuzz using list comprehension
# and inline conditional logic, contrasting with more traditional loop-based approaches in JavaScript.


