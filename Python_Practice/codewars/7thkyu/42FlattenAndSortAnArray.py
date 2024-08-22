# Challenge:

# Given a two-dimensional array of integers, return the flattened version of the array 
# with all the integers in the sorted (ascending) order.

# Example:

# Given [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]], your function should return 
# [1, 2, 3, 4, 5, 6, 7, 8, 9].

# Note: Essentially you are to efficiently flatten & sort the array.

# -------------------------------------------------------------------------------------
# -----Solution 1-----Nested For Loop & Sorted-----
def flatten_and_sort(array):
    return sorted([i for j in array for i in j])
#   1.  The nested for loop is used to iterate through the list of lists & flatten it
#       into a single list by appending the elements to a new list
#   2.  The built-in sorted function is then used to sort the list in ascending order
#   3.  The sorted list is then returned
#   4.  The time complexity is O(n^2) because of the nested for loop &
#       sorted, while the space complexity is O(n) because of the new list created.

#   This Brute Force Solution code has a time complexity of O(n^2) because of the nested for loop & is not
#   the most efficient way to solve this problem.

# -------------------------------------------------------------------------------------
# -----Solution 2-----itertools.chain & sorted-----BEST SOLUTION-----
from itertools import chain
def flatten_and_sort(array):
    return sorted((chain(*array)))
#   1.  The chain function is used to flatten the list of lists into a single list by
#       unpacking the list of lists w/o creating a new intermediate lists
#   2.  The built-in sorted function is then used to sort the list in ascending order
#   3.  The sorted list is then returned
#   4.  The time complexity is O(n log n) because of the use of itertools.chain & sorted, 
#       while the space complexity is O(1) because no additional space is used.

#   This code has more more efficient than the previous solution. 

# -------------------------------------------------------------------------------------
# -----Solution 3-----Sum & Sorted-----
def flatten_and_sort(array):
    return sorted(sum(array, []))
#   1.  The sum function w/ initial empty list to flatten & concatenate all the sublists
#       into a single list
#   2.  The built-in sorted function is then used to sort the list in ascending order
#   3.  The sorted list is then returned
#   4.  The time complexity is O(n log n) because of the use of itertools.chain & sorted, 
#       while the space complexity is O(n) because of the new list created.

# -------------------------------------------------------------------------------------
# -----Solution 4-----Javascript Solution-----Spread Operator & Concat & Sort-----
# "use strict";

# function flattenAndSort(array) {
#   return [].concat(...array).sort((a,b) => a - b);
# }

#   1.  The spread operator within the concat function is used to flatten the array
#       of arrays into a single array
#   2.  The sort function is then used to sort the array in ascending order
#   3.  The time complexity is O(n log n) because of the use of sorted, 
#       while the space complexity is O(n) because of the new list created.

#   This code has a time complexity of O(n) because of the use of the spread operator &
#   is more efficient than the previous solution because it is a built-in function that is optimized for this.