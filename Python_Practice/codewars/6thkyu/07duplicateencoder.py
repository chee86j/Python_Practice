# The goal of this exercise is to convert a string to a new string where each character 
# in the new string is "(" if that character appears only once in the original string, 
# or ")" if that character appears more than once in the original string. Ignore 
# capitalization when determining if a character is a duplicate.

# Examples
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))((" 
# Notes
# Assertion messages may be unclear about what they display in some languages. If you 
# read "...It Should encode XXX", the "XXX" is the expected result, not the input!

# -------------------------------------------------------------------------------------
# -----Solution 1-----List Comprehension & Join-----
def duplicate_encode(word):
    return ''.join(['(' if word.lower().count(char) == 1 else ')' for char in word.lower()])
#   1. Return a string by joining a list comprehension.
#   2. Iterate over each character in word, converted to lowercase.
#   3. If count of character in word is equal to 1, return '('.
#   4. If count of character in word is greater than 1, return ')'.

# -------------------------------------------------------------------------------------
# -----Solution 2-----Counter & Join-----
from collections import Counter

def duplicate_encode(word):
    word = word.lower()
    counter = Counter(word)
    return ''.join(('(' if counter[c] == 1 else ')') for c in word)
#   1. Convert word to lowercase.
#   2. Create a variable named counter and set it equal to result of calling Counter on word.
#   3. Return a string by joining a generator expression.
#   4. Iterate over each character in word.
#   5. If value of character in counter is equal to 1, return '('.
#   6. If value of character in counter is greater than 1, return ')'.

# -------------------------------------------------------------------------------------
# -----Solution 3-----Collections & Defaultdict-----
import collections
def duplicate_encode(word):
    new_string = ''
    word = word.lower()

    d = collections.defaultdict(int)
    for c in word:
        d[c] += 1
    for c in word:
        new_string = new_string + ('(' if d[c] == 1 else ')')
    return new_string
#   1. Create a variable named new_string and set it equal to an empty string.
#   2. Convert word to lowercase.
#   3. Create a defaultdict named d and set it equal to a defaultdict object.
#      defaultdict is a subclass of the built-in dict class. It overrides one method and adds 
#      one writable instance variable. In python, a defaultdict is a dictionary that allows
#      default values for keys that have not been set yet
#   http://stackoverflow.com/questions/991350/counting-repeated-characters-in-a-string-in-python
#   4. Create a for loop to iterate over each character in word.
#   5. Add 1 to value of character in d.
#   6. Create a for loop to iterate over each character in word.
#   7. If value of character in d is equal to 1, add '(' to new_string.
#   8. If value of character in d is greater than 1, add ')' to new_string.
#   9. Return new_string.
