# In this kata you are required to, given a string, replace every letter 
# with its position in the alphabet.

# If anything in the text isn't a letter, ignore it and don't return it.

# "a" = 1, "b" = 2, etc.

# Example
# alphabet_position("The sunset sets at twelve o' clock.")
# Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 
# 15 3 12 15 3 11" ( as a string )

# -------------------------------------------------------------------------------------
# -----Solution 1-----ORD() and ISALPHA()-----
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
#   1. Define a () named alphabet_position that takes a string as input.
#   2. Convert string to lowercase using lower method and iterate through each character 
#      in string.
#   3. Check if character is an alphabet using isalpha method which returns True if 
#      character is an alphabet.
#   4. If character is an alphabet, convert it to its position in alphabet using ord ().
#      Ord () returns ASCII value of a char. ASCII is a 7-bit character set
#      containing 128 characters.
#   5. Subtract 96 from ASCII value of character to get position in alphabet.
#   6. Use a list comprehension to create a list of positions for each alphabet in string.
#   7. Join list of positions into a single string separated by spaces using join method.
#   8. Return resulting string.
    
    
# -------------------------------------------------------------------------------------
# -----Solution 2-----ORD() and ISALPHA() and SUBTRACT VAL "A"-----
def alphabet_position(s):
  return " ".join(str(ord(c)-ord("a")+1) for c in s.lower() if c.isalpha())
#   1. Same as Solution 1 but instead of subtracting 96 from ASCII value of character 
#      to get position in alphabet, subtract ASCII value of "a" from ASCII value of in
#      in Step 5


# -------------------------------------------------------------------------------------
# -----Solution 3-----FOR LOOP with IF ELSE-----
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def alphabet_position(text):
    if type(text) == str:
        text = text.lower()
        result = ''
        for letter in text:
            if letter.isalpha() == True:
                result = result + ' ' + str(alphabet.index(letter) + 1)
        return result.lstrip(' ')
#   1. Define a global variable named alphabet containing all alphabets in lowercase.
#   2. Define a function named alphabet_position that takes a string as input.
#   3. Check if input is a string using type function.
#   4. Convert input string to lowercase using lower method.
#   5. Initialize an empty string named result to store position of each alphabet.
#   6. Iterate through each character in input string using a for loop.
#   7. Check if character is an alphabet using isalpha method.
#   8. If character is an alphabet, find its position in alphabet using index method.
#   9. Add 1 to index value to get position of alphabet.
#   10. Append position to result string.
#   11. Remove leading whitespace from result string using lstrip method.
#       Lstrip() method returns a copy of string with leading characters removed.
#   12. Return result string.
