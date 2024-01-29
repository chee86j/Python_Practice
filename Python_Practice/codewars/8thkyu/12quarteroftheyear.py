# Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.

# For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.

# Constraint:

# 1 <= month <= 12

# -------------------------------------------------------------------------------------
# -----Solution 1-----Using Range-----
def quarter_of(month):
    if month in range(1, 4): # generates a list of numbers from 1 to 3
        return 1
    elif month in range(4, 7):
        return 2
    elif month in range(7, 10):
        return 3
    elif month in range(10, 13):
        return 4
    
# -------------------------------------------------------------------------------------
# -----Solution 2-----Math Ceil-----
from math import ceil
def quarter_of(month):
    return ceil(month/3)

# In this solution, we are using the ceil() function from the math module to 
  # calculate the quarter.
# We simply divide the month by 3. If month is, for example, 4, then 4 / 3 
  # equals approximately 1.33.
# The ceil() function rounds this up to the nearest whole number, which is 2, 
  # indicating the second quarter.

# -------------------------------------------------------------------------------------
# -----Solution 3-----Floor Division-----
def quarter_of(n):
    return (n + 2) // 3

# In this solution, we are using floor division // to calculate the quarter.
# To ensure that the division rounds down to the nearest integer, we add 2 
  # to the month value before dividing by 3.
# For example, if month is 4, then 4 + 2 = 6, and 6 // 3 equals 2, which 
  # represents the second quarter.

# -------------------------------------------------------------------------------------
# -----Solution 4 -----If/Elif-----
def quarter_of(month):
    if month <= 3:
        return 1
    elif month <= 6:
        return 2
    elif month <= 9:
        return 3
    else:
        return 4