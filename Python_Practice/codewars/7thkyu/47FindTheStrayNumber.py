# You are given an odd-length array of integers, in 
# which all of them are the same, except for one single number.

# Complete the method which accepts such an array, and 
# returns that single different number.

# The input array will always be valid! (odd-length >= 3)
# Examples

# [1, 1, 2] ==> 2
# [17, 17, 3, 17, 17, 17, 17] ==> 3

# -------------------------------------------------------------------------------------
# -----Solution 1----Iterative w/ if & count----
def stray(arr):
    for x in arr:
        if arr.count(x) == 1:
            return x
#   1. Loop through the list
#   2. Check if the count of the element is equal to 1
#   3. If it is, return the element

#   The time complexity of this solution is O(n^2) because the count method is called for each element in the list
#   This is inefficient for large lists, however it is very straightforward to understand. Not made
#   for performance, but for simplicity.


# -------------------------------------------------------------------------------------
# -----Solution 2----Min w/ count as key----
def stray(arr):
    return min(arr, key=arr.count)
#   1. Return the element with the minimum count in the list
#   2. The key parameter is used to specify a function to be called on each list element prior to making comparisons.
#   3. The key function takes in 1 value & returns 1 value, & the returned "key" value is used for the comparisons within the sort.

#   This solution is more efficient than the previous one, but it is still not the most efficient.
#   The time complexity of this solution is O(n) because the count method is called once for each element in the list.
#   In terms of readability, this solution is more concise than the previous one.

# -------------------------------------------------------------------------------------
# -----Solution 3----Set w/ count----
def stray(arr):
    for x in set(arr):
        if arr.count(x) == 1: return x
#   1. Loop through the set of the list
#   2. Check if the count of the element is equal to 1
#   3. If it is, return the element

#   This solution is more efficient than the 1st one, but it is still not the most efficient.
#   The time complexity of this solution is O(n) because the count method is called once for each element in the list.
#   In terms of readability, this solution is more concise than the 1st one, but less concise than the 2nd one.

#  For small arrays or where performance is not critical, any solution would work. 
#  Solution 3 offers a slight optimization that might be beneficial in cases with many duplicates.