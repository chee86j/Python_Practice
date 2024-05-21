# DESCRIPTION:
# Write a function that checks if a given string 
# (case insensitive) is a palindrome.

# A palindrome is a word, number, phrase, or other 
# sequence of symbols that reads the same backwards 
# as forwards, such as madam or racecar.

# -------------------------------------------------------------------------------------
# -----Solution 1-----
def is_palindrome(s):
    return s.lower() == s[::-1].lower()


# -------------------------------------------------------------------------------------
# -----Solution 3-----Javascript Solution-----
# const isPalindrome = (x) => {
#   return x.split("").reverse().join("").toLowerCase() === x.toLowerCase() ? true : false
# }