# DESCRIPTION:
# Implement a function that accepts 3 integer values a, b, c. 
# The function should return true if a triangle can be built 
# with the sides of given length and false in any other case.

# (In this case, all triangles must have surface greater than 
#  0 to be accepted).

# Examples:

# Input -> Output
# 1,2,2 -> true
# 4,2,3 -> true
# 2,2,2 -> true
# 1,2,3 -> false
# -5,1,3 -> false
# 0,2,3 -> false
# 1,2,9 -> false 

# -------------------------------------------------------------------------------------
# -----Solution 1-----Conditional Statements-----
def is_triangle(a, b, c):
    # 1. check if sides a, b, c form a valid triangle
    # 2. a triangle is valid if sum of any two sides is greater than third side
    # 3. return True if conditions are met, indicating a valid triangle, otherwise False
    return (a < b + c) and (b < a + c) and (c < a + b)

# -------------------------------------------------------------------------------------
# -----Solution 2-----Sort Sides-----
def is_triangle(a, b, c):
    # 1. sort sides a, b, c in ascending order
    # 2. shortest side (a) will always be at index 0 after sorting
    # 3. check if sum of two shortest sides is greater than longest side
    # 4. return True if condition is met, indicating a valid triangle, otherwise False
    a, b, c = sorted([a, b, c])
    return a + b > c
