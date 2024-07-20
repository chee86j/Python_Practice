# Task

# Given a list of digits, return the smallest number that could be formed 
# from these digits, using the digits only once (ignore duplicates).
# Notes:

#     Only positive integers will be passed to the function (> 0 ), no 
#     negatives or zeros.
#     Input >> Output Examples

# minValue ({1, 3, 1})  ==> return (13)

# Explanation:

# (13) is the minimum number could be formed from {1, 3, 1} , Without 
# duplications

# minValue({5, 7, 5, 9, 7})  ==> return (579)

# Explanation:

# (579) is the minimum number could be formed from {5, 7, 5, 9, 7} , 
# Without duplications

# minValue({1, 9, 3, 1, 7, 4, 6, 6, 7}) return  ==> (134679)

# Explanation:

# (134679) is the minimum number could be formed from 
# {1, 9, 3, 1, 7, 4, 6, 6, 7} , Without duplications 

# -------------------------------------------------------------------------------------
# -----Solution 1-----Int & Join & Map & Sorted & Set-----
def min_value(digits):
    return int(''.join(map(str, sorted(set(digits)))))
#  1.  Convert the set of digits to a list.
#  2.  Sort the list.
#  3.  Convert the list to a string.
#  4.  Convert the string to an integer.
#  5.  Return the integer.

# -------------------------------------------------------------------------------------
# -----Solution 2-----Int & Join & Sorted & Set & List Comprehension-----
def min_value(digits):
    return int("".join(str(x) for x in sorted(set(digits))))
#  1.  Convert the set of digits to a list.
#  2.  Sort the list.
#  3.  Convert the list to a string.
#  4.  Convert the string to an integer.
#  5.  Return the integer.

# -------------------------------------------------------------------------------------
# -----Solution 3-----Javacript Solution-----
# function minValue(values){
#   let arr = Array.from(new Set(values))
#   return parseInt(arr.sort().join(''))
# }

#  1. Presuming that the values are in an array of positive integers.
#  2. Convert the array to a set to remove duplicates.
#  3. Convert the set to an array.
#  4. Sort the array.
#  5. Join the array into a string.
#  6. Convert the string to an integer.
#  7. Return the integer.