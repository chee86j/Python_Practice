# Create a function that returns the sum of the two lowest positive 
# numbers given an array of minimum 4 positive integers. No floats 
# or non-positive integers will be passed.

# For example, when an array is passed like [19, 5, 42, 2, 77], the 
# output should be 7.

# [10, 343445353, 3453445, 3453545353453] should return 3453455.

# -------------------------------------------------------------------------------------
# -----Solution 1-----Slice-----
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])
#   1. sorts input array in ascending order.
#   2. get first two numbers from sorted array using slicing.
#   3. sum first two numbers and return result.

# -------------------------------------------------------------------------------------
# -----Solution 2-----Sort-----
def sum_two_smallest_numbers(num_list):
    num_list.sort()
    return num_list[0] + num_list[1]
#   1. sorts input array in ascending order.
#   2. get first two numbers from sorted array.
