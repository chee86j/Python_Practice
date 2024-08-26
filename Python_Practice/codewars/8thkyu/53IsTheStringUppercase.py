# Create a method to see whether the string is ALL CAPS.

# Examples (input -> output)

# "c" -> False
# "C" -> True
# "hello I AM DONALD" -> False
# "HELLO I AM DONALD" -> True
# "ACSKLDFJSgSKLDFJSKLDFJ" -> False
# "ACSKLDFJSGSKLDFJSKLDFJ" -> True

# In this Kata, a string is said to be in ALL CAPS whenever 
# it does not contain any lowercase letter so any string 
# containing no letters at all is trivially considered to be in ALL CAPS.

# -------------------------------------------------------------------------------------
# -----Solution 1----upper()-----
def is_uppercase(inp):
    return inp.upper()==inp
#   1.  Convert the input str to uppercase using upper() & checks if the result is equal
#       to the original str
#   2.  If they are the same, it means the original str was already in all uppercase letters
#   This has a O(n) time & space complexity where n is the length of the atr. This is 
#   because upper() needs to process each character & potentially allocate space for a new string.

# -------------------------------------------------------------------------------------
# -----Solution 2----upper() & similar syntax-----
def is_uppercase(inp):
    return inp == inp.upper()
#   1.  Comparitively similar to Solution 1, this also uses the upper() method & compares 
#       the result with the original str. It's essentially the same approach with a 
#       different syntax.
#   2.  This has a  O(n) time & space complexity for the same reasons as Solution 1.

# -------------------------------------------------------------------------------------
# -----Solution 3----Javascript Solution-----
# String.prototype.isUpperCase=function() {
#     return this == this.toUpperCase();
# }
#     1.  This `String.prototype.isUpperCase` adds a new method to the `String` prototype sot that
#         all string instances in Javascript will inherit this method to be used.
#         It operates on the `this` context & in comparison with the `this.toUpperCase()`
#     2.  `this == this.toUpperCase()` this checks if the original str (this) 
#         is equal to its uppercase version. If the str was already in all uppercase, 
#         these two will be identical, & the comparison will return true. Otherwise, 
#         it will return false.
#     This solution does not rely on external functions or complex logic which makes it fast &
#     lightweight
