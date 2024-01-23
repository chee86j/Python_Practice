# In this project, you will develop a Random Number Generator
# (RNG) as a Command Line Interface (CLI) tool in Python. Your program 
# will import the `random` module to generate random numbers, initially 
# between 1 and 100. It will then be enhanced to accept user input via
# command-line arguments, using the `sys` module, to specify the minimum 
# and maximum values for the random number range. You'll implement default 
# values for these ranges for cases where the user provides insufficient 
# input and add error handling to manage non-integer inputs and ensure 
# the maximum value is not less than the minimum. Optionally, you can 
# further extend the program to generate multiple random numbers, improve 
# user interaction with flag options using `optparse`, allow setting of 
# random seeds, generate random floats, add output beautification, and 
# select random items from a user-provided list.

import random

value = random.randint(1, 100)

print(value)

# To run this program, type the following command in the terminal within the same directory as the file:
# python rng.py

#-----------------------------------------------------------------------
# With Error Handling if User does not provide enough arguments

import sys # this module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.
import random # this module implements pseudo-random number generators for various distributions.

DEFAULT_MIN = 1 # the default minimum range is 1
DEFAULT_MAX = 100 # the default maximum range is 100

if len(sys.argv) > 3: # if the length of the argument vector is greater than 3
  print("Usage: python ./rng [min] [max]") # print this message
  sys.exit(1) # exit with a status of 1

if len(sys.argv) == 3: # if the length of the argument vector is equal to 3
  range_min = DEFAULT_MIN = int(sys.argv[1]) # the minimum range is the first argument parsed as an integer
  range_max = DEFAULT_MAX = int(sys.argv[2]) # the maximum range is the second argument parsed as an integer
elif len(sys.argv) == 2:
    range_min = DEFAULT_MIN
    range_max = int(sys.argv[1])
else:
    range_min = int(sys.argv[1]) # the minimum range is the first argument parsed as an integer
    range_max = int(sys.argv[2]) # the maximum range is the second argument parsed as an integer

value = random.randint(range_min, range_max) # the value is a random integer between the minimum and maximum range

print(value)

# -----------------------------------------------------------------------
# What if you try to use a non-integer value for the minimum or maximum range?
# or if you try to set the maximum range to a value less than the minimum range?
import sys 
import random 

DEFAULT_MIN = 1 
DEFAULT_MAX = 100 

if len(sys.argv) > 3: 
  print("Usage: python ./rng [min] [max]") 
  sys.exit(1) 

# We add a try-except block to catch the ValueError exception that is raised 
# or when minimum > maximum range.
try:  
  if len(sys.argv) == 1: 
    range_min, range_max = DEFAULT_MIN, DEFAULT_MAX
  elif len(sys.argv) == 2: 
    range_min, range_max = DEFAULT_MIN, int(sys.argv[1])
  else:
    range_min, range_max = int(sys.argv[1]), int(sys.argv[2])

except ValueError: # similar to a TypeError in JavaScript
  print("Random number generator endpoints must be integers.")
  sys.exit(1)

# additional check to ensure the maximum range is not less than the minimum
if range_max < range_min: 
  print("Maximum range must be greater than minimum range.")
  sys.exit(1)

value = random.randint(range_min, range_max)

print(value)

# -----------------------------------------------------------------------
# This Project's Notes From a JavaScript Background:



# 1. Command Line Arguments in Python:
# Python uses the 'sys.argv' list to access command-line arguments, unlike process.argv in Node.js.

# 2. Default Argument Values:
# Python allows setting default values in the script, used when no command-line arguments are provided.

# 3. Error Handling with Try-Except:
# Python uses try-except blocks for error handling, akin to try-catch in JavaScript.

# 4. Random Number Generation:
# Python's 'random' module provides functions for random number generation, similar to Math.random() in JS.

# 5. Data Type Conversion:
# Explicit conversion between data types is a common practice in Python, e.g., 'int()' to convert to an integer.

# 6. Conditional Statements:
# Python's if-elif-else statements are used for conditional logic, similar to JavaScript's if-else.

# 7. Script Execution Entry Point:
# Python's 'if __name__ == "__main__":' is a unique way to define the starting point of a script.

# 8. Importing Modules:
# Python's 'import' statement is used to include modules, somewhat similar to JavaScript's import, but with different syntax and semantics.

# 9. Python's sys Module:
# Explored the use of the 'sys' module for system-specific parameters and functions, including exiting the script.

# 10. List Indexing:
# Accessing command-line arguments via indexing, showcasing Python's zero-based list indexing.

# Each point highlights a new aspect of Python you encountered, enhancing your understanding of programming beyond JavaScript.