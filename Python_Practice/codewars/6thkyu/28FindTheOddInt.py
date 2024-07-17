# Given an array of integers, find the one that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.

# Examples
# [7] should return 7, because it occurs 1 time (which is odd).
# [0] should return 0, because it occurs 1 time (which is odd).
# [1,1,2] should return 2, because it occurs 1 time (which is odd).
# [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
# [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).


# -------------------------------------------------------------------------------------
# -----Solution 1-----For Loop & Count-----
def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i
#   1. The function takes in a list of integers.
#   2. A for loop is used to iterate through each element in the list.
#   3. The count method is used to count the number of occurrences of the current element in the list.
#   4. If the count of the element is odd (not divisible by 2), the element is returned.
#   5. If no element is found with an odd count, the function returns None.

# This solution is a brute force approach to the problem. It iterates through each element in the list with a 
# time complexity of O(n^2) and checks the count of each element with a time complexity of O(1), whereas if
# it used a dictionary, it would have a time complexity of O(n) and space complexity of O(k). This is great for
# small test cases but not for large test cases.

# -------------------------------------------------------------------------------------
# -----Solution 2-----Filter & List Comprehension-----
def find_it(seq):
    return [x for x in seq if seq.count(x) % 2][0]
#   1. The function takes in a list of integers.
#   2. A list comprehension is used to iterate through each element x in the list.
#   3. The count method is used to count the number of occurrences of the current element in the list.
#   4. If the count of the element is odd (not divisible by 2), the element is kept in the resulting list.
#   5. The first element of the resulting list is returned.
#   6. If no element is found with an odd count, the function returns None.

# This solution is more concise than the previous one, but it still has the same time complexity of O(n^2)
# and space complexity of O(n). It is not the most efficient solution for large test cases.
# Of the three solutions, this is the least efficient.

# -------------------------------------------------------------------------------------
# -----Solution 3-----For Loop & Set-----
def find_it(seq):
    for elem in set(seq):
        if seq.count(elem) % 2 == 1:
            return elem
#  1. The function takes in a list of integers.
#  2. The set function is used to get a unique set of elements in the list.
#  3. A for loop is used to iterate through each unique element in the set.
#  4. The count method is used to count the number of occurrences of the current element in the list.
#  5. If the count of the element is odd (not divisible by 2), the element is returned.
#  6. If no element is found with an odd count, the function returns None.

# This solution is more efficient than the previous ones because it uses a set to get unique elements in the list,
# reducing the number of iterations needed. However, it still has a time complexity of O(n^2) and space complexity of O(n).
# Of the three solutions, this is the most efficient for small test cases.
        
# -------------------------------------------------------------------------------------
# -----Solution 4-----Javascript Solution-----
# const findOdd = (xs) => xs.reduce((a, b) => a ^ b);

# 1. The function takes in an array of integers.
# 2. The reduce method is used to iterate through each element in the array.
# 3. The Bitwise XOR operator (^) is used to XOR each element in the array.
# 4. a ^ b will return 0 if a and b are the same, and 1 if they are different.
# 5. The result of the reduce operation is the integer that appears an odd number of times.
# 6. This solution has a time complexity of O(n) and space complexity of O(1).
# 7. It is the most efficient solution for large test cases.

