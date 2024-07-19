# We need a simple function that determines if a plural is needed or not. 
# It should take a number, and return true if a plural should be used with 
# that number or false if not. This would be useful when printing out a 
# string such as 5 minutes, 14 apples, or 1 sun.

#     You only need to worry about english grammar rules for this kata, 
#     where anything that isn't singular (one of something), it is plural 
#     (not one of something).

# All values will be positive integers or floats, or zero.

# -------------------------------------------------------------------------------------
# -----Solution 1-----Straightforward Comparison-----
def plural(n):
    return n != 1
#  1.  Return True if n is not equal to 1, otherwise return False.

# -------------------------------------------------------------------------------------
# -----Solution 2-----If Else One Liner-----
def plural(n):
    return False if n == 1 else True
#  1.  Return False if n is equal to 1, otherwise return True.

# -------------------------------------------------------------------------------------
# -----Solution 3-----If Else-----
def plural(n):
    if n == 1:
        return False
    else:
        return True
#  1.  If n is equal to 1, return False.
#  2.  Otherwise, return True.