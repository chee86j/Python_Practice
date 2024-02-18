# Story
# Ben has a very simple idea to make some profit: he buys something and sells it again. Of course, this wouldn't give him any profit at all if he was simply to buy and sell it at the same price. Instead, he's going to buy it for the lowest possible price and sell it at the highest.

# Task
# Write a function that returns both the minimum and maximum number of the given list/array.

# Examples (Input --> Output)
# [1,2,3,4,5] --> [1,5]
# [2334454,5] --> [5,2334454]
# [1]         --> [1,1]
# Remarks
# All arrays or lists will always have at least one element, so you don't need to check the length. Also, your function will always get an array or a list, you don't have to check for null, undefined or similar.

# -------------------------------------------------------------------------------------
# -----Solution 1-----Using min and max built-in functions-----
def min_max(lst):
    return [min(lst), max(lst)]
    # 1. return the minimum and maximum numbers in the list as a list
    #    using the min and max built-in functions to return the minimum and maximum numbers in the list, respectively
    
# -------------------------------------------------------------------------------------
# -----Solution 2-----Using Sort & Indexing-----
def min_max(lst):
  lst.sort()
  tempor = [lst[0],lst[-1]]
  return tempor
    # 1. sort the list in ascending order
    # 2. return the minimum and maximum numbers in the list as a list
    #    using indexing to return the first and last elements in the sorted list
    