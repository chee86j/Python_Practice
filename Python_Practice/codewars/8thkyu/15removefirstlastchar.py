# Description:

# It's pretty straightforward. Your goal is to create a function that 
# removes the first and last characters of a string. You're given one 
# parameter, the original string. You don't have to worry about strings 
# with less than two characters.

# -------------------------------------------------------------------------------------
# -----Solution 1-----String Slicing-----
def remove_char(s):
    return s[1:-1]
    # uses string slicing to remove the first and last characters of the string

# -------------------------------------------------------------------------------------
# -----Solution 2-----String Slicing with Conditional Check-----
def remove_char(s):
    return '' if len(s) <= 2 else s[1:-1]
    # returns empty string if the length of the string is less than or equal to 2