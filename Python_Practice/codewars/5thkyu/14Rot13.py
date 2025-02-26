# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 
# 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

# Create a function that takes a string and returns the string ciphered with Rot13. 
# If there are numbers or special characters included in the string, they should be 
# returned as they are. Only letters from the latin/english alphabet should be 
# shifted, like in the original Rot13 "implementation".

# Please note that using encode is considered cheating.

# -------------------------------------------------------------------------------------
# -----Solution 1-----Index Lookup in Hardcoded Alphabet-----BEGINNER FRIENDLY-----
import string
from codecs import encode as _dont_use_this_

def rot13(message):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    outputMessage = ""
    for letter in message:
        if letter in alpha.lower():
            outputMessage += alpha[(alpha.lower().index(letter) +13) % 26].lower()
        elif letter in alpha:
            outputMessage += alpha[(alpha.index(letter) +13) % 26]
        else:
            outputMessage += letter
    return outputMessage

#   1.  Uppercase alphabet string (alpha) is defined
#   2.  Iterate through each character
#       a.  if lowercase, find its idx in lowercase alphabet, shift by 13, and appends it
#       b.  if uppercase, it shifts in the uppercase aphabet
#       c.  if not a letter, it remains unchanged
#   3.  Return result

#   This solution works well with external libraries.
#   It has a time complexity of O(m * 26) ≈ O(m) and a space complexity of O(m).
#   It is best suited for short strings and for beginners for a step by step breakdown.
#   This has too many index() lookups.
    

# -------------------------------------------------------------------------------------
# -----Solution 2-----Translate() with Maketrans()-----BEST PYTHONIC APPROACH-----
def rot13(message):
    return message.translate(message.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'))

#   1.  `maketrans()` creates a translation table for letter substitution:
#       a.  Each letter from A-Z maps to the letter 13 positions ahead in the alphabet.
#       b.  Each lowercase letter a-z does the same.
#   2.  `translate()` applies the translation table to the message.
#   3.  Non-alphabetic characters remain unchanged.
#   4.  The final transformed string is then returned.

#   This solution is the fastest since `translate()` runs in O(m) time complexity.
#   Space complexity is O(1) for the translation table, plus O(m) for the output string.
#   Best suited for large datasets and high-performance applications.


# -------------------------------------------------------------------------------------
# -----Solution 3-----ASCII (ord() and chr())-----WITHOUT EXTERNAL FUNCTIONS-----
import string
from codecs import encode as _dont_use_this_

def rot13(message):
    result = ''
    for char in message:
        if char.isalpha() and char.isupper():
            result += chr((((ord(char) - 65) + 13) % 26) + 65)
        elif char.isalpha() and char.islower():
            result += chr((((ord(char) - 97) + 13) % 26) + 97)
        else:
            result += char
    return result

#   1.  Initialize an empty string `result` to store the output.
#   2.  Iterate through each character in `message`:
#       a.  If uppercase (A-Z):
#           - Convert to ASCII (`ord(char)`)
#           - Normalize to 0-25 range by subtracting `65`
#           - Apply ROT13 shift: `(index + 13) % 26`
#           - Convert back to ASCII (`chr()`)
#       b.  If lowercase (a-z):
#           - Convert to ASCII, normalize using `97`, and apply the same ROT13 shift.
#       c.  If it's not a letter, append it unchanged.
#   3.  Finally we return the transformed string.

#   This solution has O(m) time complexity and O(m) space complexity.
#   It's slower than Solution 2 due to manual calculations but is a great alternative if 
#   built-in functions aren't allowed.
#   It works well for small to medium datasets.


# -------------------------------------------------------------------------------------
# -----Solution 4-----JavaScript Solution----
# function rot13(message) {
#   var a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#   var b = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
#   return message.replace(/[a-z]/gi, c => b[a.indexOf(c)])
# }

#   1.  Define two alphabet strings:
#       a.  `a` stores the original alphabet (lowercase + uppercase).
#       b.  `b` stores the shifted ROT13 alphabet.
#   2.  Use `.replace()` with a regular expression `/[a-z]/gi`:
#       a.  Finds each letter in the original string.
#       b.  Uses `.indexOf(c)` to find its position in `a`.
#       c.  Replaces it with the corresponding character from `b`.
#   3.  Finally we return the transformed message.

#   Time Complexity: O(m * 26) ≈ O(m) (indexOf() lookup for each letter).
#   Space Complexity: O(m) (stores the final transformed string).
#   This is a good balance between readability and efficiency for JavaScript.
#   It works well for small to medium datasets but is slower than dictionary-based approaches.