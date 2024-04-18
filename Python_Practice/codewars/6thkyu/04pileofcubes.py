# Build a pile of cubes

# This function or method takes in a single argument volume, 
# a positive integer, and returns the total number of cubes 
# needed to build a tower where the bottommost cube has volume, 
# the second-to-bottom has volume volume-1, the third-to-bottom 
# has volume volume-2, and so on.

# For example, if the volume of the pile is 1071225, then the 
# function should return 45. This is because the pile would 
# consist of 45 cubes with volumes 1, 2, 3, ..., and 45.

# -------------------------------------------------------------------------------------
# -----Solution 1-----Using While Loop-----
def find_nb(m):
    n = 1
    volume = 0
    while volume < m:
        volume += n**3
        if volume == m:
            return n
        n += 1
    return -1
#   1. Define a function named find_nb that takes an integer as input.
#   2. Initialize n and volume to 1 and 0 respectively.
#   3. Iterate through a while loop until volume is less than input integer.
#   4. Calculate the volume of the pile by adding the cube of n to the volume.
#   5. Check if the volume is equal to the input integer.
#   6. If the volume is equal to the input integer, return n.
#   7. Increment n by 1.
#   8. If no solution is found, return -1.


# -------------------------------------------------------------------------------------
# -----Solution 2-----Using Math Module-----
from math import floor, sqrt

def find_nb(m):
    # Used the formula for the sum of cubes: m = (n(n+1)/2)^2
    # Rearranged to find n^2 + n = n(n+1) ~= n^2 ~= 2sqrt(m),
    # so take square root and round down the result.
    n_canidate = int(floor(sqrt(2 * sqrt(m))))
    if (n_canidate * (n_canidate + 1) / 2 )**2 == m:
        return n_canidate
    else:
        return -1
#  1. Import the floor and sqrt functions from the math module.
#  2. Define a function named find_nb that takes an integer as input.
#  3. Calculate the candidate value for n using the formula n^2 ~= 2sqrt(m).
#  4. Check if the candidate value satisfies the equation for the sum of cubes.
#  5. If the candidate value satisfies the equation, return the candidate value.
#  6. If no solution is found, return -1.
