# Task
# Given three integers a ,b ,c, return the largest number obtained after inserting 
# the following operators and brackets: +, *, ()
# In other words , try every combination of a,b,c with [*+()] , and return the Maximum 
# Obtained (Read the notes for more detail about it)

# Example
# With the numbers are 1, 2 and 3 , here are some ways of placing signs and brackets:

# 1 * (2 + 3) = 5
# 1 * 2 * 3 = 6
# 1 + 2 * 3 = 7
# (1 + 2) * 3 = 9
# So the maximum value that you can obtain is 9.

# -------------------------------------------------------------------------------------
# -----Solution 1-----Max-----
def expression_matter(a, b, c):
    return max(a*b*c, a+b+c, (a+b)*c, a*(b+c))
#   1.  Create a () that takes in three arguments, a, b, and c
#   2.  Return the maximum value obtained by inserting operators and brackets
#   3.  The maximum value will be the maximum of the following:
#       a.  a*b*c
#       b.  a+b+c
#       c.  (a+b)*c
#       d.  a*(b+c)

# -------------------------------------------------------------------------------------
# -----Solution 2-----Similar To Solution 1-----
def expression_matter(a, b, c):
    return max(a + b + c, a * b * c, (a + b) * c, a * (b + c))
#   1.  Create a () that takes in three arguments, a, b, and c
#   2.  Return the maximum value obtained by inserting operators and brackets
#   3.  The maximum value will be the maximum of the following:
#       a.  a+b+c
#       b.  a*b*c
#       c.  (a+b)*c
#       d.  a*(b+c)
#   4.  This solution is the same as Solution 1, but with the order of the arguments changed
#       in the max() function. 