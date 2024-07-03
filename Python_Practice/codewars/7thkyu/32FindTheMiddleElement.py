# As a part of this Kata, you need to create a function 
# that when provided with a triplet, returns the index 
# of the numerical element that lies between the other 
# two elements.

# The input to the function will be an array of three 
# distinct numbers (Haskell: a tuple).

# For example:

# gimme([2, 3, 1]) => 0
# 2 is the number that fits between 1 and 3 and the index 
# of 2 in the input array is 0.

# Another example (just to make sure it is clear):

# gimme([5, 10, 14]) => 1
# 10 is the number that fits between 5 and 14 and the 
# index of 10 in the input array is 1.

# -------------------------------------------------------------------------------------
# -----Solution 1-----Index & Sorted-----
def gimme(input_array):
    return input_array.index(sorted(input_array)[1])
#   1. The function takes in an input_array of three distinct numbers.
#      For example, [2, 3, 1].
#   2. The input_array is sorted in ascending order using the sorted method.
#   3. The index of the middle number is then finally returned.

# -------------------------------------------------------------------------------------
# -----Solution 2-----Javascript Solution-----
# function gimme(arr) {
#     return arr.indexOf(arr.slice().sort((a, b) => a - b)[1]);
# }

#   1. The function takes in an arr of three distinct numbers.
#      For example, [2, 3, 1].
#   2. With this example next we have to sort the arr in
#      ascending order. [1, 2, 3].
#   3. Then we have to find the index of the middle number of the example by
#      using the indexOf method. The middle number is 2.
#   4. The indexOf method returns the index of the middle number which is the index of 1, 
#      which represents the middle number in the original arr, 2.
