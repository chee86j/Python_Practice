# Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.
# Examples

# Input: [1, 5.2, 4, 0, -1]
# Output: 9.2

# Input: []
# Output: 0

# Input: [-2.398]
# Output: -2.398
# Assumptions

#     You can assume that you are only given numbers.
#     You cannot assume the size of the array.
#     You can assume that you do get an array and if the array is empty, return 0.

# What We're Testing

# We're testing basic loops and math operations. This is for beginners who are just learning loops and math operations.
# Advanced users may find this extremely easy and can easily write this in one line.

# -------------------------------------------------------------------------------------
# -----Solution 1-----Built-in sum() function-----
def sum_array(a):
  return sum(a)
    # we can use the built-in sum() function to add up the numbers in the array

# -------------------------------------------------------------------------------------
# -----Solution 2-----Loops-----
def sum_array(a):
    sum = 0
    for i in a:
        sum += i
    return sum
    # we can use a for loop to iterate through the array and add up the numbers