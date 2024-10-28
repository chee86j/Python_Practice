# You are given two arrays a1 and a2 of strings. Each string is 
# composed with letters from a to z. Let x be any string in the 
# first array and y be any string in the second array.

# Find max(abs(length(x) − length(y)))

# If a1 and/or a2 are empty return -1 in each language except in 
# Haskell (F#) where you will return Nothing (None).

# Example:
    
# a1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", 
#       "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
# a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
# mxdiflg(a1, a2) --> 13

# Bash note:
    
# input : 2 strings with substrings separated by ,
# output: number as a string

# -----Notes-----
# The task is to find the maximum absolute difference in length between any string in 
# array a1 and any string in array a2. If either array is empty, the function should return -1.
# For example, given the arrays a1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa",
# "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"] and a2 = ["cccooommaaqqoxii", "gggqaffhhh",
# "tttoowwwmmww"], the function should return 13, since the difference in length between the
# longest string in a1 and the shortest string in a2 is 13.

# -------------------------------------------------------------------------------------
# -----Solution 1-----max() & min() w/Direct Calculations-----
def mxdiflg(a1, a2):
    if a1 and a2:
        return max(
            len(max(a1, key=len)) - len(min(a2, key=len)),
            len(max(a2, key=len)) - len(min(a1, key=len)))
    return -1
#   1. Check if arrs are empty. If so, return -1.
#   2. Calculate the length extremes
#      a. 'max(a1, key=len)' returns the longest string in a1
#      b. 'min(a2, key=len)' returns the shortest string in a2
#   3. Absolute difference between the longest string in a1 & the shortest string in a2 w/
#      'len(max(a1, key=len)) - len(min(a2, key=len))'

#   The time complexity is O(n) where n is the length of the longest string in a1 or a2.
#   The space complexity is O(1) since the function only uses a constant amount of space.
#   This solutions is quick & easy to understand as it leverages the max() & min() functions.

# -------------------------------------------------------------------------------------
# -----Solution 2-----Double For Loop w/abs()-----
def mxdiflg(a1, a2):
    if a1 and a2:
        return max(abs(len(x) - len(y)) for x in a1 for y in a2)
    return -1
#   1. Check if arrs are empty. If so, return -1.
#   2. Double for loop to calculate the absolute difference between the lengths of each string
#      in a1 & a2.
#   3. Return the maximum absolute difference.

#   The time complexity is O(n^2) where n is the length of the longest string in a1 or a2.
#   The space complexity is O(1) since the function only uses a constant amount of space.
#   This solution is concise & uses a double for loop to calculate the absolute difference, but
#   it is less efficient than Solution 1 as it has a higher time complexity for large inputs.


# -------------------------------------------------------------------------------------
# -----Solution 3-----Separate Calculations-----
def mxdiflg(a1, a2):
    if not a1 or not a2: return -1
    
    max_a1 = max([len(x) for x in a1])
    min_a1 = min([len(x) for x in a1])
    
    max_a2 = max([len(x) for x in a2])
    min_a2 = min([len(x) for x in a2])
    
    return max(max_a1 - min_a2, max_a2 - min_a1)
#   1. Check if arrs are empty. If so, return -1.
#   2. Calculate the length extremes for a1 & a2 separately.
#   3. Return the maximum absolute difference between the longest string in a1 & the shortest
#      string in a2, & the longest string in a2 & the shortest string in a1.

#   The time complexity is O(n) where n is the length of the longest string in a1 or a2.
#   The space complexity is O(1) since the function only uses a constant amount of space.
#   This solution is easy to understand as it separates the calculations for a1 & a2, but it
#   is less efficient than Solution 1 as it has a higher time complexity for large inputs. The 
#   breakdown of the calculations makes it easier to understand & debug.

# -------------------------------------------------------------------------------------
# -----Solution 4-----Javascript Solution-----
# function mxdiflg(a1, a2) {
#   if (a1.length === 0 || a2.length === 0) return -1
#   let l1 = a1.map(str => str.length)
#   let l2 = a2.map(str => str.length)
#   return Math.max(Math.max(...l1) - Math.min(...l2), Math.max(...l2) - Math.min(...l1))
# }
#   1. Check if arrs are empty. If so, return -1.
#   2. Calculate the length extremes for a1 & a2 separately.
#   3. Return the maximum absolute difference between the longest string in a1 & the shortest
#      string in a2, & the longest string in a2 & the shortest string in a1.

#   The time complexity is O(n) where n is the length of the longest string in a1 or a2.
#   The space complexity is O(1) since the function only uses a constant amount of space.
#   This solution is similar to Solution 3 but uses the map() function to calculate the lengths
#   of the strings in a1 & a2. It then uses the spread operator to pass the lengths
#   to the Math.max() & Math.min() functions. This solution uses the same logic as Solution 3



#   Of the solutions, Solution 1 is the most optimal, Solution 3 or 4 is the most readable, 
#   & Solution 2 is the least efficient.
