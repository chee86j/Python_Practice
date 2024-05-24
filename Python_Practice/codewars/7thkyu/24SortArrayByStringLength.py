# DESCRIPTION:
# Write a function that takes an array of strings as an argument 
# and returns a sorted array containing the same strings, ordered 
# from shortest to longest.

# For example, if this array were passed as an argument:

# ["Telescopes", "Glasses", "Eyes", "Monocles"]

# Your function would return the following array:

# ["Eyes", "Glasses", "Monocles", "Telescopes"]

# All of the strings in the array passed to your function will 
# be different lengths, so you will not have to decide how to order 
# multiple strings of the same length.

# -------------------------------------------------------------------------------------
# -----Solution 1-----
def sort_by_length(arr):
    return sorted(arr, key=len)
# 1.  Return a sorted array of strings using the sorted function
#     which sorts the array by the length of the strings
#     using the key parameter to specify the length of the strings


# -------------------------------------------------------------------------------------
# -----Solution 2-----Javascript Solution-----
# function sortByLength (array) {
#   return array.sort((a,b) => a.length - b.length);
# };

# 1.  Sort the array of strings by length using the sort method
# 2.  Return the sorted array