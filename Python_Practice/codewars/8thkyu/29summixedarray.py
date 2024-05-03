# Given an array of integers as strings and numbers, 
# return the sum of the array values as if all were numbers.

# Return your answer as a number.

# -------------------------------------------------------------------------------------
# -----Solution 1-----Map, Sum-----
def sum_mix(arr):
    return sum(map(int, arr))
#   1.  Create a () that takes in an argument, arr
#   2.  Return the sum of the elements in arr as integers using map
#   3.  Map through arr and convert each element to an integer
#   4.  Sum the elements in the mapped list


# -------------------------------------------------------------------------------------
# -----Solution 2-----Sum & For Loop-----
def sum_mix(arr):
    return sum(int(n) for n in arr)
#   1.  Create a () that takes in an argument, arr
#   2.  Return the sum of the elements in arr as integers w/ a generator expression
#   3.  Convert each element in arr to an integer using int()
#   4.  Sum the elements in the generator expression by iterating through each element
#       using a for loop


