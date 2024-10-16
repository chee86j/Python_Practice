# Task:
# Write a function that accepts two integers and returns the 
# remainder of dividing the larger value by the smaller value.

# Division by zero should return an empty value.

# Examples:
# n = 17
# m = 5
# result = 2 (remainder of `17 / 5`)

# n = 13
# m = 72
# result = 7 (remainder of `72 / 13`)

# n = 0
# m = -1
# result = 0 (remainder of `0 / -1`)

# n = 0
# m = 1
# result - division by zero (refer to the specifications 
# on how to handle this in your language)

# -------------------------------------------------------------------------------------
# -----Solution 1-----If / Else & min-----
def remainder(a,b):
    if min(a,b) == 0:
        return None
    elif a > b:
        return a % b
    else: 
        return b % a
#   This solution calculates the remainder of dividing the larger value by the smaller value.
#   It first checks if either of the input values is zero, in which case it returns None.
#   Then, it compares the input values to determine which is larger & calculates the remainder
#   accordingly. It has a time complexity of O(1) & a space complexity of O(1) since it only
#   performs a few comparisons & arithmetic operations before returning the result.

#   It is a straightforward solution that follows the problem specifications closely.
    
# -------------------------------------------------------------------------------------
# -----Solution 2-----One-liner w/ Ternary Operator-----
def remainder(a,b):
    if min(a,b)!=0: return max(a,b)%min(a,b)
#   Compared to Solution 1, this solution is more concise & uses a ternary operator to return
#   the result in a single line. It has a time complexity of O(1) & a space complexity of O(1)
#   since it only performs a few comparisons & arithmetic operations before returning the result.

#   It is a more compact solution that may be preferred by experienced Python programmers
#   for its brevity & readability.

    
# -------------------------------------------------------------------------------------
# -----Solution 3-----Combining Logic & Ternary Operator-----
def remainder(a,b):
    return max(a, b) % min(a, b) if min(a, b) else None
#   This solution calculates the remainder of dividing the larger value by the smaller value.
#   It uses the max & min functions to determine the larger & smaller values, respectively,
#   before calculating the remainder. It has a time complexity of O(1) & a space complexity of O(1)
#   since it only performs a few comparisons & arithmetic operations before returning the result.

#   This is the most concise solution that combines the logic of Solution 1 & the ternary operator
#   of Solution 2 into a single line. It is a good balance between readability & brevity.