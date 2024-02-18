# Task:
# Given a list of integers, determine whether the sum of its elements is odd or even.

# Give your answer as a string matching "odd" or "even".

# If the input array is empty consider it as: [0] (array with a zero).

# Examples:
# Input: [0]
# Output: "even"

# Input: [0, 1, 4]
# Output: "odd"

# Input: [0, -1, -5]
# Output: "even"

# -------------------------------------------------------------------------------------
# -----Solution 1-----Using sum function and % operator-----
def odd_or_even(arr):
    return 'even' if sum(arr) % 2 == 0 else 'odd'
    # 1. return 'even' if the sum of the elements in the list is even, else return 'odd'
    #    using the sum function to find the sum of the elements in the list
    #    using the % operator to find the remainder when the sum is divided by 2
    #    if the remainder is 0, return 'even', else return 'odd'
    

    