# The main idea is to count all the occurring characters in a string. 
# If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

# What if the string is empty? Then the result should be empty object literal, {}.


# -------------------------------------------------------------------------------------
# -----Solution 1-----Counter from collections module-----
from collections import Counter

def count(string):
    return Counter(string)
#   1. use Counter from collections module to count occurrences of each char
#   2. return the Counter object
#   3. where keys are unique characters and values are their counts


# -------------------------------------------------------------------------------------
# -----Solution 2-----Dictionary Comprehension-----
def count(string):
    return {i: string.count(i) for i in string}
#   1. use dictionary comprehension to iterate through the string
#   2. count the occurrences of each character in the string
#   3. string.count() is used to count the occurrences of each character
#   4. return the dictionary as key-value pairs

# -------------------------------------------------------------------------------------
# -----Solution 3-----For Loop with If/Else-----
def count(string):
    r = {}
    for c in string:
        if c in r:
            r[c] += 1
        else:
            r[c] = 1
    return r
#   1.  initialize an empty dictionary
#   2.  iterate through the string
#   3.  check if the character is already in the dictionary then increment the value by 1
#   4.  if the character is not in the dictionary then add the character to the dictionary with value 1
#   5.  return the dictionary

# -------------------------------------------------------------------------------------
# -----Solution 4-----Get Method-----
def count(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count
#   1. initialize empty dictionary
#   2. iterate through the string
#   3. check if the character is already in the dictionary then increment the value by 1
#   4. if the character is not in the dictionary then add the character to the dictionary with value 1
#   5. return the dictionary