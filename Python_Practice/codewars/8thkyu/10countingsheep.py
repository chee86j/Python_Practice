# Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

# For example,

# [True,  True,  True,  False,
#   True,  True,  True,  True ,
#   True,  False, True,  False,
#   True,  False, False, True ,
#   True,  True,  True,  True ,
#   False, False, True,  True]

# The correct answer would be 17.

# Hint: Don't forget to check for bad values like null/undefined

# -------------------------------------------------------------------------------------
# -----Solution 1-----Count Method-----
def count_sheeps(sheep_array):
    return sheep_array.count(True)
    # python has a built in count method that counts the number of times a value appears in a list
    # the JS equivalent would be .filter() and .length
    # the count method is a lot more efficient than a for loop

# -------------------------------------------------------------------------------------
# -----Solution 2-----For In Loop-----
def count_sheeps(array_of_sheep):
  count = 0
  for sheep in array_of_sheep:
      if sheep:
          count += 1 
  return count
    # this is a for in loop that loops through the array and
    # if the value is true it adds 1 to the count