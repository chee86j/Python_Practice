# DESCRIPTION:
# You are going to be given an array of integers. Your job is to take 
# that array and find an index N where the sum of the integers to the 
# left of N is equal to the sum of the integers to the right of N. If 
# there is no index that would make this happen, return -1.

# For example:
# Let's say you are given the array {1,2,3,4,3,2,1}:
# Your function will return the index 3, because at the 3rd position 
# of the array, the sum of left side of the index ({1,2,3}) and the 
# sum of the right side of the index ({3,2,1}) both equal 6.

# Let's look at another one.
# You are given the array {1,100,50,-51,1,1}:
# Your function will return the index 1, because at the 1st position 
# of the array, the sum of left side of the index ({1}) and the sum 
# of the right side of the index ({50,-51,1,1}) both equal 1.

# Last one:
# You are given the array {20,10,-80,10,10,15,35}
# At index 0 the left side is {}
# The right side is {10,-80,10,10,15,35}
# They both are equal to 0 when added. (Empty arrays are equal to 0 
#                                       in this problem)
# Index 0 is the place where the left side and right side are equal.

# Note: Please remember that in most languages the index of an array 
# starts at 0.

# Input
# An integer array of length 0 < arr < 1000. The numbers in the array 
# can be any integer positive or negative.

# Output
# The lowest index N where the side to the left of N is equal to the 
# side to the right of N. If you do not find an index that fits these 
# rules, then you will return -1.

# Note
# If you are given an array with multiple answers, return the lowest 
# correct index.

# -------------------------------------------------------------------------------------
# -----Solution 1-----
def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1
#   1. Define a function named find_even_index that takes an array as input.
#   2. Iterate through the array using a for loop with the index range of the array.
#   3. Check if the sum of elements from the beginning of the array up to the current index ([:i])
#      is equal to the sum of elements from the next index to the end of the array.
#   4. If the condition is met, return the current index.
#   5. If no index is found, return -1.

# -------------------------------------------------------------------------------------
# -----Solution 2-----
# --- NOTE ---In Python, "1st" stands for "first", indicating the initial value or position in a sequence. 
def find_even_index(lst):
    left_sum = 0
    right_sum = sum(lst)
    for i, a in enumerate(lst):
        right_sum -= a
        if left_sum == right_sum:
            return i
        left_sum += a
    return -1
#   1. Define a function named find_even_index that takes an array as input.
#   2. Initialize a variable named left_sum with a value of 0 to keep track of the sum of elements
#      to the left of the current index.
#   3. Initialize a variable named right_sum with the sum of all elements in the array to represent
#      the sum of elements to the right of the current index.
#   4. Iterate through the array using a for loop and the enumerate function to access both the index
#      and the value of each element.

#   ----- NOTE ----- The "ENUMERATE" function in Python is used to iterate over a sequence 
#   (such as a list, tuple, or string) along with its index. It returns both the index and the value 
#   of each element in the sequence. 

#   5. In each iteration, subtract the value of the current element from right_sum to update the sum
#      of elements to the right.
#   6. Check if left_sum is equal to right_sum. If they are equal, return the current index.
#   7. Update left_sum by adding the value of the current element.
#   8. If no index is found, return -1.

