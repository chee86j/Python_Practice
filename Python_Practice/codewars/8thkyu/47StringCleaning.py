# Your boss decided to save money by purchasing some cut-rate optical character 
# recognition software for scanning in the text of old novels to your database. 
# At first it seems to capture words okay, but you quickly notice that it throws 
# in a lot of numbers at random places in the text.

# Examples (input -> output)
# '! !'                 -> '! !'
# '123456789'           -> ''
# 'This looks5 grea8t!' -> 'This looks great!'

# Your harried co-workers are looking to you for a solution to take this garbled 
# text and remove all of the numbers. Your program will take in a string and clean 
# out all numeric characters, and return a string with spacing and special 
# characters ~#$%^&!@*():;"'.,? all intact.


# -------------------------------------------------------------------------------------
# -----Solution 1-----Join Characters into String, Remove Digits, Return String-----
def string_clean(s):
    return ''.join(c for c in s if not c.isdigit())
#   1.  The () takes in a string s
#   2.  The () returns a string with all numeric characters removed
#   3.  The () iterates through each character c in the input string
#   4.  If the character c is not a digit, it is added to the output string
#   5.  The () returns the output string after processing all characters
#   6.  This solution has a time complexity of O(n) where n is the length of the input string
#   7.  The space complexity is also O(n) as the output string can store up to n characters

#   Using Regex is best practice because creating an array of characters is not efficient as
#   it requires additional space to store the characters and more time to join them back into a string.

# -------------------------------------------------------------------------------------
# -----Solution 2-----Re Library to Remove Digits & Sub Function-----
import re

def string_clean(s):
    return re.sub(r'\d', '', s)
#   1.  The () takes in a string s
#   2.  The () returns a string with all numeric characters removed
#   3.  The () uses the re.sub() function to replace all digits with an empty string
#   4.  The () returns the modified string after removing all digits
#   5.  This solution has a time complexity of O(n) where n is the length of the input string
#   6.  The space complexity is also O(n) as the output string can store up to n characters

#   Using the re library is more efficient than creating an array of characters and joining them back into a string.
#   It only needs one iteration to remove all digits from the input string.

# -------------------------------------------------------------------------------------
# -----Solution 3-----Javascript Solution-----
# function stringClean(s){
#     return s.replace(/\d/g, '');
# }

#    1.  The ()) stringClean takes in a string s
#    2.  It returns a new string with all numeric characters removed
#    3.  The replace method is used to replace all digits with an empty string
#        using the regular expression /\d/g built-in JavaScript ()) and
#        the global flag to replace all occurrences of digits in the string
#    4.  The ()) returns the modified string after removing all digits
#    5.  This solution has a time complexity of O(n) where n is the length of the input string
#    6.  The space complexity is also O(n) as the output string can store up to n characters
#    7.  This solution is efficient and concise, using a single line of code to remove all digits from the input string