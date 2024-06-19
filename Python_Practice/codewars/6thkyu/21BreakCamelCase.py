# Complete the solution so that the function will break up 
# camel casing, using a space between words.

# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""

# -------------------------------------------------------------------------------------
# -----Solution 1-----One Liner w/ Join & List Comprehension & isupper using for loop-----
def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)
#   1.  Return the str w/ a space before each uppercase letter
#   2.  Join the str w/ a space before each uppercase letter
#   3.  Check if the character is uppercase
#   4.  Return the character if it is not uppercase
#   5.  Return the character w/ a space before it if it is uppercase

# -------------------------------------------------------------------------------------
# -----Solution 2-----For Loop & isupper & if/else-----
def solution(s):
    newStr = ""
    for letter in s:
        if letter.isupper():
            newStr += " "
        newStr += letter
    return newStr

#   1.  Create a var to store the new str
#   2.  Iterate through the str
#   3.  Check if the letter is uppercase
#   4.  Add a space before the letter if it is uppercase
#   5.  Add the letter to the new str
#   6.  Return the new str

# -------------------------------------------------------------------------------------
# -----Solution 3-----Javascript Solution-----Regex & replace-----
# function solution(str) {
#     return str.replace(/([A-Z])/g, ' $1');
# }

# #   1.  Return the str w/ a space before each uppercase letter
# #   2.  Use the replace method to add a space before each uppercase letter
# #   3.  Use a regex to match uppercase letters
# #   4.  Add a space before each uppercase letter


# -------------------------------------------------------------------------------------
# -----Solution 4-----Javascript Solution-----Split & Map & Join w/ Uppercase Check-----
# function solution(str) {
#   str = str.split('').map(function (el) {
#     if (el === el.toUpperCase()) {
#       el = ' ' + el
#     }
#     return el
#   })
#   return str.join('')
# }

# #   1.  Split the str into an array of characters
# #   2.  Iterate through the array
# #   3.  Check if the character is uppercase
# #   4.  Add a space before the character if it is uppercase
# #   5.  Return the array joined as a str
