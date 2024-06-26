# Build Tower
# Build a pyramid-shaped tower, as an array/list of strings, given a 
# positive integer number of floors. A tower block is represented 
# with "*" character.

# For example, a tower with 3 floors looks like this:

# [
#   "  *  ",
#   " *** ", 
#   "*****"
# ]
# And a tower with 6 floors looks like this:

# [
#   "     *     ", 
#   "    ***    ", 
#   "   *****   ", 
#   "  *******  ", 
#   " ********* ", 
#   "***********"
# ]

# -------------------------------------------------------------------------------------
# -----Solution 1-----List Comprehension & Center & For Loop-----
def tower_builder(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]
#   1.  Return a list comprehension that generates tower
#   2.  Generate tower by centering string of stars
#   3.  The string of stars is generated by multiplying number of stars
#       by 2 and subtracting 1
#   4.  The range starts at 1 and ends at n+1
#   5.  The center method is used to center string of stars
#   6.  The width of string is n*2-1


# -------------------------------------------------------------------------------------
# -----Solution 2-----If Else & For Loop & Append-----
def tower_builder(n_floors):
    if n_floors == 0:
        return []
        
    count = 1
    result = []
    
    for i in range(1, n_floors + 1):
        stars = '*' * (2 * i - 1)
        spaces = ' ' * (n_floors - i)
        result.append(spaces + stars + spaces)
        
    return result

#   1.  If number of floors is 0, return an empty list
#   2.  Initialize count to 1 & result to an empty list
#   3.  Loop through range of 1 to n_floors + 1
#   4.  Generate string of stars by multiplying 2 * i - 1
#   5.  Generate string of spaces by multiplying n_floors - i
#   6.  Append string of spaces, stars, and spaces to result list
#   7.  Return result list