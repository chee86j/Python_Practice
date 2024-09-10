# Clock shows h hours, m minutes and s seconds after midnight.

# Your task is to write a function which returns the time since 
# midnight in milliseconds.

# Example:
# h = 0
# m = 1
# s = 1

# result = 61000
# Input constraints:

# 0 <= h <= 23
# 0 <= m <= 59
# 0 <= s <= 59

# -------------------------------------------------------------------------------------
# -----Solution 1-----
def past(h, m, s):
    return (3600*h + 60*m + s) * 1000
#   1.  3600*h converts hours to seconds
#   2.  60*m converts minutes to seconds
#   3.  3600*h + 60*m + s converts the time to seconds

#   This solution is efficient & easy to understand. 
#   It multiplies the total seconds by 1000 to convert to milliseconds.

# -------------------------------------------------------------------------------------
# -----Solution 2-----
def past(h, m, s):
    return (h * 3600000) + (m * 60000) + (s * 1000)
#   1.  h * 3600000 converts hours to milliseconds
#   2.  m * 60000 converts minutes to milliseconds
#   3.  s * 1000 converts seconds to milliseconds

#   Compared to the previous solution, this solution is more readable & easier to understand.
#   It multiplies the total milliseconds by 1000 to convert to milliseconds.


# -------------------------------------------------------------------------------------
# -----Solution 3-----Javascript Solution-----
# function past(h, m, s){
#     return (h * 3600000) + (m * 60000) + (s * 1000)
# }

#   This is the same as the second solution, but written in JavaScript.
#   It multiplies the total milliseconds by 1000 to convert to milliseconds.
