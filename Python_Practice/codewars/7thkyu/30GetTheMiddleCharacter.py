# You are going to be given a word. Your job is to return the 
# middle character of the word. If the word's length is odd, 
# return the middle character. If the word's length is even, 
# return the middle 2 characters.

# #Examples:

# Kata.getMiddle("test") should return "es"

# Kata.getMiddle("testing") should return "t"

# Kata.getMiddle("middle") should return "dd"

# Kata.getMiddle("A") should return "A"
# #Input

# A word (string) of length 0 < str < 1000 (In javascript you 
# may get slightly more than 1000 in some test cases due to an 
# error in the test cases). You do not need to test for this. 
# This is only here to tell you that you do not need to worry 
# about your solution timing out.

# #Output

# The middle character(s) of the word represented as a string.

# -------------------------------------------------------------------------------------
# -----Solution 1-----divmod & if/else-----
def get_middle(s):
    index, odd = divmod(len(s), 2)
    return s[index] if odd else s[index - 1:index + 1]
#   1.  Create a var to store the idx & remainder of the length of the string divided by 2
#       divmod is a built-in function that returns a tuple of the quotient and remainder
#       For example, divmod(5, 2) returns (2, 1).  
#   2.  Return the middle character if the length of the string is odd
#   3.  Return the middle 2 characters if the length of the string is even

# -------------------------------------------------------------------------------------
# -----Solution 2-----Math Module & if/else-----
import math

def get_middle(s):
    x = len(s)
    y = int(x/2)
    if x%2==0:
        return s[y-1:y+1]
    else:
        return s[y:y+1]
#   1.  Import the math module
#   2.  Create a var to store the length of the string
#   3.  Create a var to store the middle idx of the string
#   4.  Return the middle 2 characters if the length of the string is even
#   5.  Return the middle character if the length of the string is odd

# -------------------------------------------------------------------------------------
# -----Solution 3-----Javascript Solution-----
# function getMiddle(s) {
#   var middle = s.length / 2;
#   return (s.length % 2) 
#     ? s.charAt(Math.floor(middle))
#     : s.slice(middle - 1, middle + 1);
# }

#  1.  Create a var to store the middle idx of the string
#  2.  Return the middle character if the length of the string is odd using
#      the charAt method to return the character at the specified index
#  3.  Return the middle 2 characters if the length of the string is even using
#      the slice method to return the characters between the specified indices




