# DESCRIPTION:
# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces.

# -------------------------------------------------------------------------------------
# -----Solution 1-----Generator Expression w/ Conditional-----
def get_count(sentence):
    return sum(1 for char in sentence if char in 'aeiou')
#   1. Define a () named get_count that takes a str as input.
#   2. Use a generator expression to iterate through each char in str.
#   3. Check if the char is a vowel by comparing it to str 'aeiou'.
#   4. If char is a vowel, yield 1.
#   5. Sum up count of vowels using sum().

# -------------------------------------------------------------------------------------
# -----Solution 2-----Least Code-----
def getCount(s):
    return sum(c in 'aeiou' for c in s)

# -------------------------------------------------------------------------------------
# -----Solution 3-----Detailed For Loop-----
def getCount(inputStr):
    num_vowels = 0
    for char in inputStr:
        if char in "aeiouAEIOU":
           num_vowels = num_vowels + 1
    return num_vowels
#   1. Define a () named get_count that takes a str as input.
#   2. Declare empty var num_vowels to store count.
#   3. Iterate through each char in str using a for loop.
#   4. Check if char is a vowel by comparing it to str 'aeiouAEIOU'.
#   5. If char is a vowel, increment num_vowels by 1.
#   6. Return num_vowels.
