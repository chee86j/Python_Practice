# Determine the total number of digits in the integer (n>=0) 
# given as input to the function. For example, 9 is a single 
# digit, 66 has 2 digits and 128685 has 6 digits. Be careful 
# to avoid overflows/underflows.

# All inputs will be valid.

# -------------------------------------------------------------------------------------
# -----Solution 1-----len() & str() functions-----
def digits(n):
    return len(str(n))
#   1. The digits() function takes an integer n as input.
#   2. It converts the integer to a string using the str() function.
#   3. It then calculates the length of the string using the len() function.
#   4. The final result is the total number of digits in the integer.

# This solution has a time complexity of O(log n) because it converts the integer to a string
# and calculates the length of the string, which has a logarithmic time complexity based on the
# value of the integer. For the space complexity, it is O(log n) because the string representation
# of the integer grows with the size of the integer. 

# -------------------------------------------------------------------------------------
# -----Solution 2-----While Loop-----
def digits(n):
    digits = 1
    while n // 10 > 0:
        n //= 10
        digits += 1
    
    return digits
#   1. The digits() function takes an integer n as input.
#   2. It initializes a variable digits to 1 to account for the last digit.
#   3. It enters a while loop that divides the integer by 10 until it reaches 0.
#   4. In each iteration, it updates the integer by integer division and increments the digits count.
#   5. The final result is the total number of digits in the integer.

# This solution has a time complexity of O(log n) because it divides the integer by 10 in each iteration,
# which has a logarithmic time complexity based on the value of the integer. For the space complexity,
# it is O(1) because it uses a constant amount of space to store the digits count.
# Compare this solution to the previous one, it is more efficient in terms of space complexity
# because it does not create a string representation of the integer.

# -------------------------------------------------------------------------------------
# -----Solution 3-----Javascript Solution-----
# function digits(n) {
#     return n.toString().length;
# }
# 1. The digits() function takes an integer n as input.
# 2. It converts the integer to a string using the toString() method.
# 3. It then calculates the length of the string using the length property.
# 4. The final result is the total number of digits in the integer.

# This solution has a time complexity of O(log n) because it converts the integer to a string
# and calculates the length of the string, which has a logarithmic time complexity based on the
# value of the integer. For the space complexity, it is O(log n) because the string representation
# of the integer grows with the size of the integer. It is a concise & efficient solution similar to
# the first solution in Python.