# You are given two interior angles (in degrees) of a triangle.

# Write a function to return the 3rd.

# Note: only positive integers will be tested.

# -------------------------------------------------------------------------------------
# -----Solution 1-----Simple Calculation-----
def other_angle(a, b):
    return 180 - a - b
#   1. Calculate the 3rd angle of the triangle by subtracting the sum of the two given angles
#      from 180 degrees `return 180 - a - b`
#   2. This solution assumes that the input angles are positive integers & does not handle
#      the case where negative angles are provided. It has a time complexity of O(1) & a space
#      complexity of O(1).

# -------------------------------------------------------------------------------------
# -----Solution 2-----Conditional Check for Negative Angles-----
def other_angle(a, b):
    if (a or b) < 0:
        return "angle cannot be smaller than 0"
    
    else:
        return 180-(a+b)
#   1. Check if either of the given angles is negative using the condition `(a or b) < 0`
#   2. If either angle is negative, return the message "angle cannot be smaller than 0"
#   3. Otherwise, calculate the 3rd angle of the triangle by subtracting the sum of the two given
#      angles from 180 degrees `return 180-(a+b)`
#   4. This solution handles the case where negative angles are provided as input & returns an
#      appropriate message. It has a time complexity of O(1) & a space complexity of O(1). Compared
#      to the previous solution, this solution includes an additional conditional check for negative
#      angles. It is more robust & provides better error h&ling for negative inputs.

# -------------------------------------------------------------------------------------
# -----Solution 3-----Javascript Solution-----
# function otherAngle(a, b) {
#   return 180 - a - b;
# }
#   This is a JavaScript solution that calculates the 3rd angle of a triangle by subtracting
#   the sum of the two given angles from 180 degrees. The time complexity & space complexity
#   of this solution are O(1) since it only performs a few mathematical operations & uses a
#   few variables. This solution is equivalent to the 1st Python solution but written in
#   JavaScript. It is concise & efficient for calculating the 3rd angle of a triangle.