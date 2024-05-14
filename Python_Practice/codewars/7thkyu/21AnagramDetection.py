# An anagram is the result of rearranging the letters 
# of a word to produce a new word (see wikipedia).

# Note: anagrams are case insensitive

# Complete the function to return true if the two arguments 
# given are anagrams of each other; return false otherwise.

# Examples
# "foefet" is an anagram of "toffee"

# "Buckethead" is an anagram of "DeathCubeK"

# -------------------------------------------------------------------------------------
# -----Solution 1-----Sorted & Lower-----
def is_anagram(test, original):
    return sorted(test.lower()) == sorted(original.lower())
# 1.  Sort chars in test and original strs
# 2.  Check if sorted test and original strs are equal
# 3.  Return True if strs are anagrams and False if they aren't

# -------------------------------------------------------------------------------------
# -----Solution 2-----Counter & Lower-----
from collections import Counter

def is_anagram(test, original):
    return Counter(test.lower()) == Counter(original.lower())
# 1.  Convert test and original strs to lowercase
# 2.  Using Counter class from collections module, 
#     count occurrences of each char in strs
# 3.  Check if counts of chars in test and original strs are equal
# 4.  Return True if strs are anagrams and False if they aren't

# -------------------------------------------------------------------------------------
# -----Solution 3-----Javascript Solution-----
# var isAnagram = function(test, original) {
#   var t = test.toLowerCase().split('').sort().join('');
#   var o = original.toLowerCase().split('').sort().join('');
#   return (t==o)?true:false;
# };

# 1.  Convert test and original strs to lowercase
# 2.  Split strs into arrays of chars
# 3.  Sort chars in arrays
# 4.  Join sorted chars into strings
# 5.  Check if sorted test and original strs are equal
# 6.  Return True if strs are anagrams and False if they aren't
