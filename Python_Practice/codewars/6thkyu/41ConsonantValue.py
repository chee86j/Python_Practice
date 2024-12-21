# Given a lowercase string that has alphabetic characters only and no spaces, return 
# the highest value of consonant substrings. Consonants are any letters of the alphabet except "aeiou".

# We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.

# For example, for the word "zodiacs", let's cross out the vowels. We get: "z o d ia c"

# "zodiac" -> 26

# The consonant substrings are: "z", "d" and "c" with values "z" = 26, "di" = 4 and "c" = 3. The highest is 26.

# "strength" -> 57

# The consonant substrings are: "str" and "ngth" with values "str" = 19 + 20 + 18 = 57 
# and "ngth" = 14 + 7 + 20 + 8 = 49. The highest is 57.

# For C: do not mutate input.

# -------------------------------------------------------------------------------------
# Problem Summary

# Given a lowercase string of alphabetic characters, the goal is to:

#     Identify substrings consisting only of consonants (non-vowel characters).
#     Compute the sum of the alphabetic values of each substring.
#     Return the maximum sum among these substrings.

# Consonant values are based on their position in the alphabet (e.g., a=1, b=2, ..., z=26).

# -------------------------------------------------------------------------------------
# -----Solution 1-----Using re.split and ord-----
import re

def solve(s):
    return max(sum(ord(c)-96 for c in subs) for subs in re.split('[aeiou]+', s))
#   1.  We are using re.split() function to split the string 's' based on the regex
#       '[aeiou]+' which will split the string based on the vowels
#   2.  Next we are iterating through the substrings and calculating the sum of the
#       ascii values of the characters in the substring
#   3.  Finally we are returning the maximum sum of the substrings

#   The time complexity of this solution is O(n) where n is the number of characters in
#   the string 's' & the space complexity is O(n) as we are storing the substrings in a list

#   This is an efficient and concise solution, leveraging regular expressions to handle 
#   the splitting step seamlessly.

# -------------------------------------------------------------------------------------
# -----Solution 2-----Using Manual Replacement and Iteration-----
def solve(s):
    alphabet = "-abcdefghijklmnopqrstuvwxyz"
    for vowel in "aeiou":
        s = s.replace(vowel, " ")
    values = []
    for item in s.split():
        sum = 0
        for letter in item:
            sum += alphabet.index(letter)
        values.append(sum)        
    return max(values)
#   1.  We are replacing the vowels in the string 's' with a space
#   2.  Next we are iterating through the substrings and calculating the sum of the
#       ascii values of the characters in the substring
#   3.  Finally we are returning the maximum sum of the substrings

#   The time complexity of this solution is O(n) where n is the number of characters in
#   the string 's' & the space complexity is O(n) as we are storing the substrings in a list

#   This solution is slightly less elegant than Solution 1, as it relies on manual 
#   replacements and indexing. However, it achieves the same complexity.


# -------------------------------------------------------------------------------------
# -----Solution 3-----Using Iterative Character-by-Character Parsing-----
def solve(s):
    max_sum = 0
    current_sum = 0
    for c in s:
        if c in 'aeiou':
            current_sum = 0  # Reset on encountering a vowel
        else:
            current_sum += ord(c) - 96
            max_sum = max(max_sum, current_sum)
    return max_sum

#   1.  We are iterating through the characters in the string 's'
#   2.  If the character is a vowel, we are resetting the current_sum to 0
#   3.  If the character is a consonant, we are adding the ascii value of the character
#       to the current_sum
#   4.  Finally we are returning the maximum sum of the substr

#    The time complexity of this solution is O(n) where n is the number of characters in
#    the string 's' & the space complexity is O(1) as we are not storing the substrings

#    This is the most efficient solution in terms of space and time, as it processes 
#    the string in a single pass without creating intermediate substrings.