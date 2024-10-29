# altERnaTIng cAsE <=> ALTerNAtiNG CaSe

# Define String.prototype.toAlternatingCase (or a similar 
# function/method such as to_alternating_case/toAlternatingCase/ToAlternatingCase 
# in your selected language; see the initial solution for details) such that each 
# lowercase letter becomes uppercase and each uppercase letter becomes lowercase. 

# For example:

# "hello world".toAlternatingCase() === "HELLO WORLD"
# "HELLO WORLD".toAlternatingCase() === "hello world"
# "hello WORLD".toAlternatingCase() === "HELLO world"
# "HeLLo WoRLD".toAlternatingCase() === "hEllO wOrld"
# "12345".toAlternatingCase()       === "12345"                   // Non-alphabetical characters are unaffected
# "1a2b3c4d5e".toAlternatingCase()  === "1A2B3C4D5E"
# "String.prototype.toAlternatingCase".toAlternatingCase() === "sTRING.PROTOTYPE.TOaLTERNATINGcASE"

# As usual, your function/method should be pure, i.e. it should not mutate the original string.

# -------------------------------------------------------------------------------------
# -----Solution 1-----Built-in Function swapcase()-----
def to_alternating_case(string):
    return string.swapcase()
#   This uses the built-in function swapcase() to swap the case of the string
#   swapcase() is a built-in function in Python that swaps the case of the string.
#   It returns a new str with the case of the characters swapped.
#   It does not mutate the original string and is a pure function.

#   The time complexity of this solution is O(n) where n is the length of the string.
#   The space complexity of this solution is O(n) where n is the length of the string.

# -------------------------------------------------------------------------------------
# -----Solution 2-----For Loop w/Conditional Case Conversion-----
def to_alternating_case(string):
    strn = ""
    for i in string:
        if i.isupper():
            strn += i.lower()
        else:
            strn += i.upper()
    return strn
#   This solution uses a for loop to iterate through the string.
#   It checks if the character is uppercase or lowercase and converts it to the opposite case.
#   It then appends the converted character to a new string.
#   The new string is returned at the end.
#   This solution does not mutate the original string and is a pure function.

#   The time complexity of this solution is O(n) where n is the length of the string.
#   The space complexity of this solution is O(n) where n is the length of the string.
#   This is not as efficient as the previous solution because of the repeated string concatenation.

# -------------------------------------------------------------------------------------
# -----Solution 3-----List Comprehension w/Conditional Expression-----
def to_alternating_case(string):
    return ''.join([c.upper() if c.islower() else c.lower() for c in string])
#   This solution uses a list comprehension to iterate through the string.
#   It checks if the character is lowercase or uppercase and converts it to the opposite case.
#   The converted characters are then joined together to form a new string.
#   The new string is returned at the end.
#   This solution does not mutate the original string and is a pure function.

#   The time complexity of this solution is O(n) where n is the length of the string.
#   The space complexity of this solution is O(n) where n is the length of the string.
#   This solution is more efficient than the previous one as it avoids repeated string concatenation.


# -------------------------------------------------------------------------------------
# -----Solution 4-----Javascript Version-----toAlternatingCase()-----
# String.prototype.toAlternatingCase = function () {
#     return this.split("").map(a => a === a.toUpperCase()? a.toLowerCase(): a.toUpperCase()).join('')
# }
#   This solution is the same as the previous one but written in JavaScript using the prototype method.
#   It uses the map() method to iterate through the characters of the string.
#   It checks if the character is uppercase or lowercase and converts it to the opposite case.
#   The converted characters are then joined together to form a new string.

#   The time complexity of this solution is O(n) where n is the length of the string.
#   The space complexity of this solution is O(n) where n is the length of the string.
#   This solution is more efficient than the previous one as it avoids repeated string concatenation.