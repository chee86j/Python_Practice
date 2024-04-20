# DESCRIPTION:
# Implement the function unique_in_order which takes as 
# argument a sequence and returns a list of items without 
# any elements with the same value next to each other and 
# preserving the original order of elements.

# For example:

# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
# unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]

# -------------------------------------------------------------------------------------
# -----Solution 1-----For Loop-----
def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result
#   1. Define a () named unique_in_order that takes a sequence as input.
#   2. Initialize an empty list named result to store unique elements.
#   3. Initialize a var named prev to None to store previous element.
#   4. Iterate through each element in sequence using a for loop.
#   5. Check if current element is not equal to previous element.
#   6. If current element is not equal to previous element, append it to result list.
#   7. Update previous element to current element.
#   8. Return result list.


# -------------------------------------------------------------------------------------
# -----Solution 2-----Similar to above but with a return statement-----
def unique_in_order(iterable):
    res = []
    for item in iterable:
        if len(res) == 0 or item != res[-1]:
            res.append(item)
        return res
#   1. Define a () named unique_in_order that takes a sequence as input.
#   2. Initialize an empty list named res to store unique elements.
#   3. Iterate through each element in sequence using a for loop.
#   4. Check if length of res is 0 or current element is not equal to last element in res.
#   5. If length of res is 0 or current element is not equal to last element in res, append current element to res.
#   6. Return res.

# -------------------------------------------------------------------------------------
# -----Solution 3-----Using List Comprehension and Groupby-----
from itertools import groupby

def unique_in_order(iterable):
    return [k for (k, _) in groupby(iterable)]
#   1. Import groupby function from itertools module.
#   2. Define a () named unique_in_order that takes a sequence as input.
#   3. Use a list comprehension to iterate through elements in sequence.
#   4. Use groupby function to group consecutive elements that are same.
#      The groupby function returns a tuple with key and an iterator of group.
#      It groups consecutive elements that are same together.
#   5. Return a list of unique elements by extracting key from each group.

