# In mathematics, the factorial of a non-negative integer n, 
# denoted by n!, is the product of all positive integers less 
# than or equal to n. For example: 5! = 5 * 4 * 3 * 2 * 1 = 120. 
# By convention the value of 0! is 1.

# Write a function to calculate factorial for a given input. 
# If input is below 0 or above 12 throw an exception of 
# type ArgumentOutOfRangeException (C#) or IllegalArgumentException 
# (Java) or RangeException (PHP) or throw a RangeError (JavaScript) 
# or ValueError (Python) or return -1 (C).

# More details about factorial can be found here.

# -------------------------------------------------------------------------------------
# -----Solution 1-----Recursion & ValueError-----
def factorial(n):
    if n < 0 or n > 12:
        raise ValueError
    return 1 if n == 0 else n * factorial(n - 1)

#  1. The function takes in a non-negative integer n.
#  2. If n is less than 0 or greater than 12, a ValueError is raised.
#     In Python, 'raise ValueError' is used to raise an exception. 
#  3. If n is equal to 0, 1 is returned.
#  4. If n is not equal to 0, n * factorial(n - 1) is returned.
#     This is a recursive function that calls itself with n - 1 until n is equal to 0.
#     For example, if n is 5, the function will return 5 * 4 * 3 * 2 * 1 = 120.

# -------------------------------------------------------------------------------------
# -----Solution 2-----Javascript Solution-----RangeError & Recursion-----
# function factorial(n) {
#     if (n < 0 || n > 12) {
#         throw new RangeError();
#     }
#     return n === 0 ? 1 : n * factorial(n - 1);
# }

#  1. The function takes in a non-negative integer n.
#  2. If n is less than 0 or greater than 12, a RangeError is thrown.
#     In JavaScript, 'throw new RangeError()' is used to throw an exception.
#  3. If n is equal to 0, 1 is returned.
#  4. If n is not equal to 0, n * factorial(n - 1) is returned.
#     This is a recursive function that calls itself with n - 1 until n is equal to 0.
#     For example, if n is 5, the function will return 5 * 4 * 3 * 2 * 1 = 120.

