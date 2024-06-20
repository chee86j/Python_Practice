# Write a function that returns a string in which 
# firstname is swapped with last name.

# Example(Input --> Output)

# "john McClane" --> "McClane john"

# -------------------------------------------------------------------------------------
# -----Solution 1-----
def name_shuffler(str_):
    return " ".join(str_.split()[::-1])
#   1. Split the string into a list of words
#   2. Reverse the list of words by using [::-1] which 
#      returns a reversed copy of the list
#   3. Join the list of words into a string with a space in between each word
#   4. Return the string

# -------------------------------------------------------------------------------------
# -----Solution 2-----Javascript Solution-----Split & Reverse & Join-----
# function nameShuffler(str) {
#     return str.split(' ').reverse().join(' ');
# }
 
#   1. Split the string into a list of words
#   2. Reverse the list of words
#   3. Join the list of words into a string with a space in between each word
#   4. Return the string
