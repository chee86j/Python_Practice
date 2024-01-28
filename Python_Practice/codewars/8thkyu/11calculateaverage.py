# Description:

# Write a function which calculates the average of the numbers in a given list.

# Note: Empty arrays should return 0.

# -------------------------------------------------------------------------------------
# -----Solution 1-----Try/Except Block using sum() and len() functions-----
def find_average(array):
    try:
        return sum(array) / len(array)
    except ZeroDivisionError:
        return 0

# -------------------------------------------------------------------------------------  
    # -----Solution 2-----sum() and len() with if/else statement-----
def find_average(array):
    return sum(array) / len(array) if array else 0