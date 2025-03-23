# Create a function close_compare that accepts 3 parameters: a, b, and an optional margin. 
# The function should return whether a is lower than, close to, or higher than b.

# Please note the following:

# When a is close to b, return 0.
# --For this challenge, a is considered "close to" b if margin is greater than or equal to the 
# --absolute distance between a and b.

# Otherwise...

# -When a is less than b, return -1.

# -When a is greater than b, return 1.

# If margin is not given, treat it as if it were zero.

# Assume: margin >= 0

# Tip: Some languages have a way to make parameters optional.


# --Example 1--
# If a = 3, b = 5, and margin = 3, then close_compare(a, b, margin) should return 0.

# This is because a and b are no more than 3 numbers apart.

# --Example 2--
# If a = 3, b = 5, and margin = 0, then close_compare(a, b, margin) should return -1.

# This is because the distance between a and b is greater than 0, and a is less than b.

# -------------------------------------------------------------------------------------
# -----Solution 1-----Ternary Operator-----
def close_compare(a, b, margin = 0):
    return 0 if abs(a - b) <= margin else -1 if b > a else 1

#   1.  Check if the absolute difference between a & b is less than or equal to the margin.
#   2.  If true, return 0.  If false, check if b is greater than a.
#   3.  If true, return -1.  If false, return 1.

#   This has a time complexity of O(1) because it only performs a constant number of operations.
#   The space complexity is O(1) because it only uses a constant amount of memory.

#   This is the best for performance and readability, but may be less intuitive for beginners.


# -------------------------------------------------------------------------------------
# -----Solution 2-----If/Else Statements-----
def close_compare(a, b, margin=0):
    if a == b or abs(a - b) <= margin:
        return 0
    if a < b:
        return -1
    if a > b:
        return 1
    
#   1.  Check if a & b are equal or if the absolute difference between them is less than or equal to the margin.
#   2.  If true, return 0.  If false, check if a is less than b.
#   3.  If true, return -1.  If false, check if a is greater than b.
#   4.  If true, return 1.

#   This has a time complexity of O(1) because it only performs a constant number of operations.
#   The space complexity is O(1) because it only uses a constant amount of memory.

#   This is the best for beginners because it is more intuitive and easier to understand. It is easy
#   to follow the logic step by step.

# -------------------------------------------------------------------------------------
# -----Solution 3-----JavaScript Solution-----Math.abs() and Math.sign()-----
# function closeCompare(a, b, m = 0){
#   return Math.abs(a - b) <= m? 0: Math.sign(a - b);
# }

#   1.  Check if the absolute difference between a & b is less than or equal to the margin.
#   2.  If true, return 0.  If false, return the sign of the difference between a & b.

#   This has a time complexity of O(1) because it only performs a constant number of operations.
#   The space complexity is O(1) because it only uses a constant amount of memory.  

#   This is best for beginners because it is more intuitive and easier to understand. It is easy
#   to follow the logic step by step like Solution 2. It would be ideal for Web Development.














