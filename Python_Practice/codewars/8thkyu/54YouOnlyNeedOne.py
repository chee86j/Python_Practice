# You will be given an array a and a value x. All you need 
# to do is check whether the provided array contains the value.

# Array can contain numbers or strings. X can be either.

# Return true if the array contains the value, false if not.

# -------------------------------------------------------------------------------------
# -----Solution 1----In Operator-----
def check(seq, elem):
    return elem in seq
#   1.  The `in` operator checks if the element `elem` is present in the sequence `seq`.
#   2.  If the element is present, it returns True, otherwise it returns False.
#   3.  This solution has a time complexity of O(n) where n is the length of the sequence `seq`.
#       This is because the `in` operator may need to iterate over the entire sequence to find the element.
#       The space complexity is O(1) because the function uses a constant amount of 
#       extra space regardless of the size of the sequence.

# -------------------------------------------------------------------------------------
# -----Solution 2----Ternary Operator-----
def check(seq, elem):
    return True if elem in seq else False
#   1.  This solution is similar to Solution 1 but uses a ternary operator to return True or False explicitly.
#   2.  The ternary operator checks if the element `elem` is present in the sequence `seq`. 
#       If it is present, it returns True, otherwise it returns False.
#   3.  This solution has a time complexity of O(n) where n is the length of the sequence `seq`. 
#       This is because the `in` operator. The space complexity is O(1) because the function 
#       uses a constant amount of extra space regardless of the size of the sequence.

# -------------------------------------------------------------------------------------
# -----Solution 3----Javascript Solution-----Includes()-----
# function check(a, x) {
#     return a.includes(x);
# }
#   1.  The includes() method checks if an element `x` is present in the array `a`.
#   2.  If the element is present, it returns True, otherwise it returns False.
#   3.  This solution has a time complexity of O(n) where n is the length of the array `a`.
#       This is because the includes() method may need to iterate over the entire array to find the element.
#       The space complexity is O(1) because the function uses a constant amount of 
#       extra space regardless of the size of the array. This solution is similar to Solution 1 
#       but uses the includes() method instead of the `in` operator.
