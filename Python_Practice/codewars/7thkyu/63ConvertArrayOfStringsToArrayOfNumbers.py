# Oh no!

# Some really funny web dev gave you a sequence of numbers from 
# his API response as an sequence of strings!

# You need to cast the whole array to the correct type.

# Create the function that takes as a parameter a sequence of 
# numbers represented as strings and outputs a sequence of numbers.

# ie:["1", "2", "3"] to [1, 2, 3]

# Note that you can receive floats as well.

# -------------------------------------------------------------------------------------
# -----Solution 1-----
def to_float_array(arr): 
    return list(map(float, arr))
#   1.  The map() function takes two arguments, a function and a sequence iterable 
#       & applies the function to all the elements of the iterable. 
#   2.  Next we are converting the map object to a list using list() function, which
#       will convert all the elements of the list to float & return the list

#   The time complexity of this solution is O(n) where n is the number of elements in
#   the list 'arr' & the space complexity is O(n) as we are storing the result in a list



# -------------------------------------------------------------------------------------
# -----Solution 2-----
def to_float_array(arr):
    return [float(i) for i in arr]
#   1.  We are using list comprehension to iterate through the list of strings
#   2.  First we are converting the string to float using float() function
#   3.  Then we are returning the list 'arr' with all the elements converted to float

#   The time complexity of this solution is O(n) where n is the number of elements in 
#   the list 'arr' & the space complexity is O(n) as we are storing the result in a list

# -------------------------------------------------------------------------------------
# -----Solution 3-----Javacript Solution-----
# function toNumberArray(stringarray){
#   return stringarray.map(parseFloat)
# }
#   1.  The map() function takes two arguments, a function and a sequence iterable
#       & applies the function to all the elements of the iterable.
#   2.  Next we are converting the map object to a list using list() function, which
#       will convert all the elements of the list to float & return the list
#   3.  The parseFloat() function parses a string and returns a floating point number

#   The time complexity of this solution is O(n) where n is the number of elements in
#   the list 'arr' & the space complexity is O(n) as we are storing
