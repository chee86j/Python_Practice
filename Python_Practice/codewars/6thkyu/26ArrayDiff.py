# Your goal in this kata is to implement a difference function, 
# which subtracts one list from another and returns the result.

# It should remove all values from list a, which are present 
# in list b keeping their order.

# arrayDiff([1,2],[1]) == [2]
# If a value is present in b, all of its occurrences must be 
# removed from the other:

# arrayDiff([1,2,2,2,3],[2]) == [1,3]
# -------------------------------------------------------------------------------------
# -----Solution 1-----List Comprehension & Not In-----
def array_diff(a, b):
    return [x for x in a if x not in b]
#  1. The function takes in two lists a and b.
#  2. A list comprehension is used to iterate through each element x in list a.
#  3. If the element x is not in list b, it is kept in the resulting list.
#  4. The resulting list is then returned.

#  For example with a = [1, 2, 2, 2, 3] and b = [2]:
#  Iterating through 'a':
#     'x = 1' is not in 'b', so it is kept.
#     'x = 2' is in 'b', so it is removed.
#     'x = 2' is in 'b', so it is removed.
#     'x = 2' is in 'b', so it is removed.
#     'x = 3' is not in 'b', so it is kept.
#  The resulting list is [1, 3].

# -------------------------------------------------------------------------------------
# -----Solution 2-----Set & List Comprehension & Not In-----
def array_diff(a, b):
    return [x for x in a if x not in set(b)]
#  1. The function takes in two lists a and b.
#  2. A set is created from list b to improve performance when checking membership.
#  3. A list comprehension is used to iterate through each element x in list a.
#  4. If the element x is not in the set of b, it is kept in the resulting list.
#  5. The resulting list is then returned.

#  For example with a = [1, 2, 2, 2, 3] and b = [2]:
#  Set Creation: 'set(b)' is {2}.
#  Iterating through 'a':
#     'x = 1' is not in 'set(b)', so it is kept.
#     'x = 2' is in 'set(b)', so it is removed.
#     'x = 2' is in 'set(b)', so it is removed.
#     'x = 2' is in 'set(b)', so it is removed.
#     'x = 3' is not in 'set(b)', so it is kept.
#  The resulting list is [1, 3].

# -------------------------------------------------------------------------------------
# -----Solution 3-----Javascript Solution-----Filter & Includes-----
# function arrayDiff(a, b) {
#     return a.filter(e => !b.includes(e));
# }

#  1. We start with an example where a = [1, 2, 2, 2, 3] and b = [2].
#  2. The filter method is used to iterate through each element e in a, which is [1, 2, 2, 2, 3].
#  3. For each element e, we check if it is not included in b using the includes method.
#  4. If e is not included in b, it is kept in the filtered arr.
#  5. The filtered arr is then returned, which is [1, 3].
#  6. This solution effectively removes all values from list a that are present in list b while 
#     keeping the order of the remaining values.

#  For example with a = [1, 2, 2, 2, 3] and b = [2]:
#  Filtering: 'a' is [1, 2, 2, 2, 3] and 'b' is [2].
#  Filter Method: 'a.filter(e => !b.includes(e))' 
#     Iterating through 'a':
#         'e = 1' is not in 'b', so it is kept.
#         'e = 2' is in 'b', so it is removed.
#         'e = 2' is in 'b', so it is removed.
#         'e = 2' is in 'b', so it is removed.
#         'e = 3' is not in 'b', so it is kept.
#  The filtered arr is [1, 3].
