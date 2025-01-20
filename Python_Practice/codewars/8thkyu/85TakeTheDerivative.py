# This function takes two numbers as parameters, the first number being the 
# coefficient, and the second number being the exponent.

# Your function should multiply the two numbers, and then subtract 1 from the 
# exponent. Then, it has to return an expression (like 28x^7). "^1" should not 
# be truncated when exponent = 2.

# For example:

# derive(7, 8)
# In this case, the function should multiply 7 and 8, and then subtract 1 from 8. 
# It should output "56x^7", the first number 56 being the product of the two numbers,
# and the second number being the exponent minus 1.

# derive(7, 8) --> this should output "56x^7" 
# derive(5, 9) --> this should output "45x^8" 
# Notes:

# The output of this function should be a string
# The exponent will never be 1, and neither number will ever be 0

# -------------------------------------------------------------------------------------
# -----Solution 1-----
def derive(coefficient, exponent): 
    return f'{coefficient * exponent}x^{exponent - 1}'
#   1.  Multiply the coefficient and exponent
#   2.  Subtract 1 from the exponent
#   3.  Format the string using f-strings

#   The time complexity of this function is O(1) because it performs a constant 
#   number of operations.
#   The space complexity of this function is also O(1) because it uses a constant
#   amount of memory to store the result.

# -------------------------------------------------------------------------------------
# -----Solution 2-----
def derive(coefficient, exponent): 
    return("{}x^{}".format(coefficient*exponent, exponent-1))
#   1.  Multiply the coefficient and exponent
#   2.  Subtract 1 from the exponent
#   3.  Format the string using the format() method

#   The time complexity of this function is O(1) because it performs a constant
#   number of operations.
#   The space complexity of this function is also O(1) because it uses a constant
#   amount of memory to store the result.

#   Compared to Solution 1, this solution is slightly less efficient because it 
#   uses the format() method, which is slightly slower than using f-strings.

# -------------------------------------------------------------------------------------
# -----Solution 3-----
def derive(coefficient, exponent): 
    a=coefficient*exponent
    b=exponent-1
    txt="{}x^{}"
    return txt.format(a,b)
#   1.  Multiply the coefficient and exponent
#   2.  Subtract 1 from the exponent
#   3.  Format the string using the format() method
#   4.  Return the formatted string

#   The time complexity of this function is O(1) because it performs a constant
#   number of operations.
#   The space complexity of this function is also O(1) because it uses a constant
#   amount of memory to store the result.

#   Compared to Solution 1, this solution is slightly less efficient because it
#   uses the format() method, which is slightly slower than using f-strings.
#   Compared to Solution 2, this solution is slightly less efficient because it
#   uses an extra variable to store the formatted string.
