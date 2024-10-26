# Take 2 strings s1 and s2 including only letters 
# from a to z. Return a new sorted string 
# (alphabetical ascending), the longest possible, 
# containing distinct letters - each taken only 
# once - coming from s1 or s2.

# Examples:
    
# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# longest(a, b) -> "abcdefklmopqwxy"

# a = "abcdefghijklmnopqrstuvwxyz"
# longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

# -------------------------------------------------------------------------------------
# -----Solution 1-----set & sorted-----
def longest(a1, a2):
    return ''.join(sorted(set(a1 + a2)))
#   1.  Start by concatenating the two input strs a1 & a2.
#   2.  Use the set function to remove duplicate chars from the concatenated str.
#   3.  Use the sorted function to sort the chars in alphabetical order.
#   4.  Use the join function to combine the sorted chars into a single str.
#   5.  Return the resulting str.

#   This solution has a time complexity of O(n log n) due to the sorting operation & a space complexity
#   of O(n) due to the creation of a set containing the unique chars from the concatenated str.
#   Sorting could be inefficient for large inputs, but it guarantees the correct order of chars

# -------------------------------------------------------------------------------------
# -----Solution 2-----looping through the alphabet-----
def longest(s1, s2):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s = s1 + s2
    y = ""

    for x in alphabet:
      if x not in s:
        continue
      if x in s:
        y = y + x  
    return y
#   1.  Create a str variable alphabet containing all the lowercase letters of the alphabet.
#   2.  Concatenate the input strs s1 & s2 into a single str s.
#   3.  Create an empty str variable y to store the unique chars from s.
#   4.  Iterate through each char x in the alphabet.
#   5.  Check if x is not in the concatenated str s using the not in operator.
#   6.  If x is not in s, continue to the next iteration of the loop.
#   7.  If x is in s, append it to the str y.
#   8.  Return the resulting str y.

#   This solution has a time complexity of O(n) due to the loop through the alphabet & a space complexity
#   of O(n) due to the creation of the str y to store the unique chars from the concatenated str.
#   It is more efficient than the previous solution for large inputs as it avoids sorting the chars, but
#   it is inefficient for longer strs with many unique chars.

# -------------------------------------------------------------------------------------
# -----Solution 3-----set union & sorted-----
def longest(s1, s2):
    return ''.join(sorted(set(s1) | set(s2)))
#   1.  Use the set function to create sets of unique chars from the input strs s1 & s2.
#   2.  Use the union operator | to combine the two sets into a single set containing all unique chars.
#   3.  Use the sorted function to sort the chars in alphabetical order.
#   4.  Use the join function to combine the sorted chars into a single str.
#   5.  Return the resulting str.

#   This solution has a time complexity of O(n log n) due to the sorting operation & a space complexity
#   of O(n) due to the creation of sets containing the unique chars from the input strs.
#   It is similar to Solution 1 but uses set operations to combine the unique chars from both strs.
#   If s1 and s2 have many duplicate chars, this solution may be more efficient than Solution 1.


# -------------------------------------------------------------------------------------
# -----Solution 4-----Javascript Solution-----Set & Array.from-----
# function longest(s1, s2) {
#     return Array.from(new Set(s1 + s2)).sort().join('');
# }

#   1.  Concatenate the input strs s1 & s2.
#   2.  Create a new Set object from the concatenated str to remove duplicate chars.
#   3.  Convert the Set object to an array using Array.from to allow sorting.
#   4.  Sort the array of chars in alphabetical order.
#   5.  Join the sorted array of chars into a single str.
#   6.  Return the resulting str.

#   This solution has a time complexity of O(n log n) due to the sorting operation & a space complexity
#   of O(n) due to the creation of a Set object containing the unique chars from the concatenated str.
#   It is similar to Solution 1 but uses Set objects and Array.from to manipulate the chars in JavaScript.
#   The use of Set objects ensures that only unique chars are included in the final str.