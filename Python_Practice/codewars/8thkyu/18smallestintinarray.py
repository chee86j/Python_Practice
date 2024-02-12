# Description:

# Given an array of integers your solution should find the smallest integer.

# For example:

#     Given [34, 15, 88, 2] your solution will return 2
#     Given [34, -345, -1, 100] your solution will return -345

# You can assume, for the purpose of this kata, that the supplied array will not be empty.

# -------------------------------------------------------------------------------------
# -----Solution 1-----min()-----
def find_smallest_int(arr):
    return min(arr)

# -------------------------------------------------------------------------------------
# -----Solution 2-----sort()-----
def findSmallestInt(arr):
    #sort array
    arr.sort()
    return arr[0]