# Trolls are attacking your comment section!

# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

# Your task is to write a function that takes a string and return a new string with all vowels removed.

# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

# Note: for this kata y isn't considered a vowel.

# -------------------------------------------------------------------------------------
# -----Solution 1-----Loop w/ join method and conditional statement-----
def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou")
    # 1. iterate through each character in the string
    # 2. return the characters that are not vowels
    #    using the join method to join the characters into a single string
    #    using the lower method to convert the character to lowercase and check if it is a vowel

# -------------------------------------------------------------------------------------
# -----Solution 2-----Loop w/ replace method-----
def disemvowel(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s
    # 1. iterate through each vowel in the string
    # 2. replace each vowel with an empty string
    # 3. return the string with the vowels removed

# -------------------------------------------------------------------------------------
# -----Solution 3-----Using re.sub and re.IGNORECASE flag-----
import re
def disemvowel(string):
    return re.sub('[aeiou]', '', string, flags = re.IGNORECASE)
    # 1. use the re.sub method to replace all vowels with an empty string.
    #    re.sub is used to replace all occurrences of a pattern in a string with a new string
    #    The re.IGNORECASE flag is used to perform a case-insensitive match
    #    re.IGNORECASE basically means that the pattern is case-insensitive and will match both uppercase and lowercase letters 
    # 2. return the string with the vowels removed