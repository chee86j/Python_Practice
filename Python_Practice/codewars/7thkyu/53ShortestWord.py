# Description:

# Simple, given a string of words, return 
# the length of the shortest word(s).

# String will never be empty and you do not 
# need to account for different data types.

# -------------------------------------------------------------------------------------
# -----Solution 1-----min(), split(), len()-----
def find_short(s):
    return min(len(x) for x in s.split())
#   1. This () takes one argument s.
#   2. It then splits the string into a list of words. `s.split()`
#   3. Then proceeds to iterate through the list of words. `for x in s.split()`
#   4. The length of each word is then calculated. `len(x)`
#   5. The min() function is then used to return the length of the shortest word.
#   6. The length of the shortest word is then returned.

#   This solution's space complexity is O(1) because we are not using any additional
#   data structures using a constant amount of space. This solution is the most efficient 
#   in terms of time complexity (O(n)) as it iterates through all the words in the list to 
#   find the shortest word.
# -------------------------------------------------------------------------------------
# -----Solution 2-----min() w/ key function-----
def find_short(s):
    return len(min(s.split(' '), key=len))
#   1. This () takes one argument s. 
#   2. It then splits the string into a list of words. `s.split(' ')`
#   3. The min() function is then used to return the shortest word in the list.
#   4. The length of the shortest word is then calculated. `len()`
#   5. The length of the shortest word is then returned.

#   Similar to solution 1, this solution's space complexity is O(1) because we are not using 
#   any additional data structures using a constant amount of space & time. What varies is the use of
#   the key parameter in the min() function to return the shortest word in the list. 

# -------------------------------------------------------------------------------------
# -----Solution 3-----Javascript Solution-----map(), Math.min() & split()-----
# function findShort(s){
#     return Math.min(...s.split(" ").map (s => s.length));
# }
#   1. This function takes one argument s.
#   2. It then splits the string into a list of words. `s.split(" ")`
#   3. The map() function is then used to iterate through the list of words.
#   4. The length of each word is then calculated. `s => s.length`
#   5. The Math.min() function is then used to return the length of the shortest word.
#   6. The length of the shortest word is then returned.

#   Solutions 1 & 2 are slightly more efficient than this solution because they do not use the 
#   spread operator. The spread operator is used to unpack the elements of the array into the
#   Math.min() function. This solution's space complexity is O(1) because we are not using any
#   additional data structures using a constant amount of space. The time complexity of this
#   solution is O(n) because the map() function iterates through all the words in the list to
#   find the shortest word.

