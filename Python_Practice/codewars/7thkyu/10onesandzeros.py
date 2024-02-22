# DESCRIPTION:
# Given an array of ones and zeroes, convert the equivalent binary value to an integer.

# Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

# Examples:

# Testing: [0, 0, 0, 1] ==> 1
# Testing: [0, 0, 1, 0] ==> 2
# Testing: [0, 1, 0, 1] ==> 5
# Testing: [1, 0, 0, 1] ==> 9
# Testing: [0, 0, 1, 0] ==> 2
# Testing: [0, 1, 1, 0] ==> 6
# Testing: [1, 1, 1, 1] ==> 15
# Testing: [1, 0, 1, 1] ==> 11
# However, the arrays can have varying lengths, not just limited to 4.
   
# -------------------------------------------------------------------------------------
# -----Solution 1-----Using map function-----
def binary_array_to_number(arr):
    return int("".join(map(str, arr)), 2)
    # 1. join elements into a single string
    # 2. convert string to an integer using int function
    #    specifying base as 2 to convert string to a binary number
    #    using map function to convert each element to a string
    
# -------------------------------------------------------------------------------------
# -----Solution 2-----For loop w/ join method & int function-----
def binary_array_to_number(arr):
    return int("".join(str(i) for i in arr), 2)
    # 1. iterate through each element in the array
    # 2. join elements into a single string
    # 3. convert string to an integer using int function
    #    specifying base as 2 to convert string to a binary number
    
# -------------------------------------------------------------------------------------
# -----Solution 3-----For loop-----
def binary_array_to_number(arr):
    s = 0
    for digit in arr:
        s = s * 2 + digit
        # 1. iterate through each element in array
        # 2. multiply s by 2 and add the current digit
    return s
    # 3. return the result