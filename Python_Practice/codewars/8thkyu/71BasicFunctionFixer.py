# Fix the function
# I created this function to add five to any number that was 
# passed in to it and return the new value. It doesn't throw 
# any errors but it returns the wrong number.

# Can you help me fix the function?

# -------------------------------------------------------------------------------------
# -----Solution 1-----add 5 to the input number-----
def add_five(num):
    return num + 5
#   This solution fixes the function by adding 5 to the input number & returning the result.
#   It has a time complexity of O(1) & a space complexity of O(1) since it only performs a
#   single arithmetic operation & returns the result.

#   It is the most concise and straightforward solution to the problem.

# -------------------------------------------------------------------------------------
# -----Solution 2-----add an intermediate variable-----
def add_five(num):
    total = num + 5
    return total
#   This solution fixes the function by adding 5 to the input number & storing the result in
#   a variable before returning it. It has a time complexity of O(1) & a space complexity of O(1)
#   since it only performs a single arithmetic operation & returns the result.

#   It is slightly less concise than Solution 1 due to the use of an intermediate 
#   variable to store the result before returning it. It is easier to read & understand
#   for beginners who may not be familiar with Python's implicit return.

# -------------------------------------------------------------------------------------
# -----Solution 3-----math module-----
from math import pi, e, floor

def add_five(num):
    return num + floor(pi + e)
#   This solution fixes the function by adding the floor of the sum of pi & e to the input number
#   before returning the result. It has a time complexity of O(1) & a space complexity of O(1) since
#   it only performs a single arithmetic operation & returns the result.

#   It is a creative solution that demonstrates the use of the math module to perform arithmetic
#   operations on the input number. It is unecessary for the problem at hand but showcases the
#   flexibility of Python's math functions.
