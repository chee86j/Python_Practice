# There is an array with some numbers. All numbers are equal except for one. Try to find it!

# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains at least 3 numbers.

# The tests contain some very huge arrays, so think about performance.

# This is the first kata in series:

# Find the unique number (this kata)
# Find the unique string (https://www.codewars.com/kata/585d8c8a28bc7403ea0000c3)
# Find The Unique (https://www.codewars.com/kata/5862e0db4f7ab47bed0000e5)

# -------------------------------------------------------------------------------------
# -----Solution 1-----Set, Count-----
def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b
#   1.  Create a () that takes in an argument, arr
#   2.  Create two vars, a and b, and set them to set of arr
#   3.  Return a if count of a in arr is equal to 1, else return b

# -------------------------------------------------------------------------------------
# -----Solution 2-----Set, For Loop, Count-----
def find_uniq(arr):
    s = set(arr)
    for e in s:
        if arr.count(e) == 1:
            return e
#   1.  Create a () that takes in an argument, arr
#   2.  Create a var s and set it to set of arr
#   3.  Create a for loop that will iterate through s
#   4.  Check if count of e in arr is equal to 1
#   5.  Return e

# -------------------------------------------------------------------------------------
# -----Solution 3-----Min, Set, Count-----
def find_uniq(arr):
    return min(set(arr), key=arr.count)
#   1.  Create a () that takes in an argument, arr
#   2.  Return the minimum value of set of arr based on count of elements in arr
#       Key is used to specify the function that will be used to determine value on which to base minimum value
#   3.  This will return the element that occurs only once in arr
