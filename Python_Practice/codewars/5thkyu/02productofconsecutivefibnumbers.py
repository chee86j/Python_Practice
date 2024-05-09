# DESCRIPTION:
# The Fibonacci numbers are the numbers in the following integer sequence (Fn):

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...

# such as

# F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.

# Given a number, say prod (for product), we search two Fibonacci 
# numbers F(n) and F(n+1) verifying

# F(n) * F(n+1) = prod.

# Your function productFib takes an integer (prod) and returns an array:

# [F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)
# depending on the language if F(n) * F(n+1) = prod.

# If you don't find two consecutive F(n) verifying F(n) * F(n+1) = prodyou will return

# [F(n), F(n+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)
# F(n) being the smallest one such as F(n) * F(n+1) > prod.

# Some Examples of Return:
# (depend on the language)

# productFib(714) # should return (21, 34, true), 
#                 # since F(8) = 21, F(9) = 34 and 714 = 21 * 34

# productFib(800) # should return (34, 55, false), 
#                 # since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55
# -----
# productFib(714) # should return [21, 34, true], 
# productFib(800) # should return [34, 55, false], 
# -----
# productFib(714) # should return {21, 34, 1}, 
# productFib(800) # should return {34, 55, 0},        
# -----
# productFib(714) # should return {21, 34, true}, 
# productFib(800) # should return {34, 55, false}, 


# -------------------------------------------------------------------------------------
# -----Solution 1-----
def productFib(prod):
    a, b = 0, 1
    while a * b < prod:
        a, b = b, a + b
    return [a, b, prod == a * b]

#   1.  Initialize a and b to 0 and 1 respectively
#   2.  While the product of a and b is less than prod
#   3.  Set a to b and b to a + b
#   4.  Return a, b, and a * b == prod

#   This solution is efficient because it uses the Fibonacci sequence to
#   find the two numbers that multiply to prod. It is efficient
#   because the Fibonacci sequence is generated in linear time and the
#   product is checked in constant time.