# You ask a small girl,"How old are you?" She always says, "x years old", 
# where x is a random number between 0 and 9.

# Write a program that returns the girl's age (0-9) as an integer.

# Assume the test input string is always a valid string. For example, the 
# test input may be "1 year old" or "5 years old". The first character in 
# the string is always a number.

# -------------------------------------------------------------------------------------
# -----Solution 1-----Indexing-----
def get_age(age):
    return int(age[0])
#   1. Define a function named get_age that takes a string as input.
#   2. Return first character of string as an integer.

# -------------------------------------------------------------------------------------
# -----Solution 2-----Indexing w/ Split-----
def get_age(age):
    return int(age.split()[0])
#   1. Define a function named get_age that takes a string as input.
#   2. Split string by whitespace and return first element as an integer.

# -------------------------------------------------------------------------------------
# -----Solution 3-----Indexing w/ Filter-----
def get_age(age):
    return int(''.join(filter(str.isdigit, age)))
#   1. Define a function named get_age that takes a string as input.
#   2. Use filter to extract digits from string.
#   3. Join digits together and convert to an integer.
