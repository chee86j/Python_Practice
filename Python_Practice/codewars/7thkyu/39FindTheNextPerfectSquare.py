# You might know some pretty large perfect squares. 
# But what about the NEXT one?

# Complete the findNextSquare method that finds the 
# next integral perfect square after the one passed 
# as a parameter. Recall that an integral perfect 
# square is an integer n such that sqrt(n) is also 
# an integer.

# If the argument is itself not a perfect square 
# then return either -1 or an empty value like 
# None or null, depending on your language. 
# You may assume the argument is non-negative.

# Examples ( Input --> Output )
# 121 --> 144
# 625 --> 676
# 114 --> -1  #  because 114 is not a perfect square

# -------------------------------------------------------------------------------------
# -----Solution 1-----Simple Arithmetic Solution-----
def find_next_square(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1)**2
    return -1
#   1. Find the square root of the input number by raising it to the power of 0.5
#   2. Check if the square root is an integer by using the is_integer() method which
#      returns True if the number is an integer & False if it is not.
#   3. If the square root is an integer, return the square of the next number by adding 
#      1 to the square root & squaring it.
#   4. If the square root is not an integer, return -1.
#   This method works for both perfect squares & non-perfect squares & is the most
#   efficient solution as it only requires one calculation to find the next perfect square.
#   with constant time complexity O(1) & space complexity O(1).

# -------------------------------------------------------------------------------------
# -----Solution 2-----Ternary Operator Solution-----
def find_next_square(sq):
    x = sq**0.5    
    return -1 if x % 1 else (x+1)**2
#   1. Find the square root of the input number by raising it to the power of 0.5
#   2. Check if the square root is an integer by using the modulo operator % to check if
#      the remainder of the square root divided by 1 is 0.
#   3. If the square root is an integer, return the square of the next number by adding
#      1 to the square root & squaring it.
#   4. If the square root is not an integer, return -1.
#   This method works for both perfect squares & non-perfect squares & is the most, but
#   it requires two calculations to find the next perfect square with constant time.

# -------------------------------------------------------------------------------------
# -----Solution 3-----Math Solution-----
import math

def find_next_square(sq):
    return (math.sqrt(sq) + 1) ** 2 if (math.sqrt(sq)).is_integer() else -1
#   1. Find the square root of the input number using the math.sqrt() method from the math
#      module.
#   2. Check if the square root is an integer by using the is_integer() method which returns
#      True if the number is an integer & False if it is not.
#   3. If the square root is an integer, return the square of the next number by adding 1 to
#      the square root & squaring it.
#   4. If the square root is not an integer, return -1.
#   This method works for both perfect squares & non-perfect squares & is the least efficient
#   solution as it requires two calculations to find the next perfect square with constant time
#   complexity O(1) & space complexity O(1).

# -------------------------------------------------------------------------------------
# -----Solution 4-----Javascript Solution-----
# function findNextSquare(sq) {
#   return Math.sqrt(sq)%1? -1 : Math.pow(Math.sqrt(sq)+1,2);
# }
#   This is the Javascript version of the ternary operator solution. It uses the Math.sqrt()
#   method to find the square root of the input number & the modulo operator % to check if the
#   square root is an integer. If the square root is an integer, it returns the square of the next
#   number by adding 1 to the square root & squaring it. If the square root is not an integer, it
#   returns -1.

#   It has the same time complexity O(1) & space complexity O(1) as the Python version.