# DESCRIPTION:
# Write a function that takes a list of strings as an argument and 
# returns a filtered list containing the same elements but with 
# the 'geese' removed.

# The geese are any strings in the following array, which is 
# pre-populated in your solution:

#   ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
# For example, if this array were passed as an argument:

#  ["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", 
#   "Blue Swedish"]
# Your function would return the following array:

# ["Mallard", "Hook Bill", "Crested", "Blue Swedish"]
# The elements in the returned array should be in the same order as in 
# the initial array passed to your function, albeit with the 'geese' 
# removed. Note that all of the strings will be in the same case as 
# those provided, and some elements may be repeated.

# -------------------------------------------------------------------------------------
# -----Solution 1-----List Comprehension & If & For Loop-----
geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    return [bird for bird in birds if bird not in geese]
#  1.  Return a list comprehension that filters out the geese
#  2.  The list comprehension loops through the birds
#  3.  If the bird is not in the geese, it is added to the list
#  4.  The list is returned

# -------------------------------------------------------------------------------------
# -----Solution 2-----Filter & Lambda & For Loop-----
geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    return list(filter(lambda x: x not in geese, birds))
#  1.  Return a list of the filtered birds
#  2.  Filter the birds using a lambda function
#  3.  The lambda function checks if the bird is not in the geese
#  4.  The filtered birds are returned as a list

# -------------------------------------------------------------------------------------
# -----Solution 3-----Javascript Solution-----
# const geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"];

# function gooseFilter (birds) {
#   return birds.filter(bird => !geese.includes(bird));
# }

#  1.  Return a list of the filtered birds
#  2.  using the filter method on the birds
#  3.  The filter method checks if the bird is not in the geese
#  4.  and includes the bird in the list of filtered birds