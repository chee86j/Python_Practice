# You will be given an array and a limit value. 
# You must check that all values in the array are 
# below or equal to the limit value. If they are, 
# return true. Else, return false.

# You can assume all values in the array are numbers.

# -------------------------------------------------------------------------------------
# -----Solution 1-----max()-----
def small_enough(array, limit):
    return max(array)<=limit
#   1. Check if the maximum value in the array is less than or equal to the limit
#       - Use the max() function to find the maximum value in the array
#       - Check if the maximum value is less than or equal to the limit
#   2. Return the result
#   This solution is very simple & concise with a time complexity of O(n) & a space
#   complexity of O(1). The max() function is used to find the maximum value in the
#   array & compare it to the limit. It is not the most efficient solution since it
#   finds the maximum value in the array, but it is still a valid solution.

# -------------------------------------------------------------------------------------
# -----Solution 2-----all() w/ Generator Expression-----
def small_enough(array, limit):
    return all(a <= limit for a in array)
#   1. Check if all values in the array are less than or equal to the limit
#       - Use the all() function to check if all values in the array are less than or equal to the limit
#       - Use a generator expression to iterate through each value in the array & check if it is less than or 
#         equal to the limit
#   2. Return the result
#   This solution is simple & concise with a time complexity of O(n) & a space complexity of O(1). The all() 
#   function is used to check if all values in the array are less than or equal to the limit. 
#   It is a More Efficient solution than the 1st solution since it does not find the maximum value in the array.

# -------------------------------------------------------------------------------------
# -----Solution 3-----Manual Loop-----
def small_enough(array, limit):
    for e in array:
        if not e <= limit: return False
    return True
#   1. Iterate through each value in the array
#       - Use a for loop to iterate through each value in the array
#   2. Check if the value is less than or equal to the limit
#       - Check if the value is less than or equal to the limit
#       - If the value is greater than the limit, return False
#   3. Return True if all values are less than or equal to the limit
#   This solution is the most verbose with a time complexity of O(n) & a space complexity of O(1). It uses a
#   manual loop to iterate through each value in the array & check if it is less than or equal to the limit.
#   It is less concise & efficient than the 2nd solution, but it is still a valid solution.


# -------------------------------------------------------------------------------------
# -----Solution 4-----Javascript Solution-----
# function smallEnough(a, limit){
#   return Math.max(...a) <= limit
# }
#   1. Check if the maximum value in the array is less than or equal to the limit
#       - Use the Math.max() function to find the maximum value in the array
#       - Check if the maximum value is less than or equal to the limit
#   2. Return the result
#   This solution is the same as the 1st solution, but it is written in JavaScript. It uses the Math.max() function
#   to find the maximum value in the array & compare it to the limit. It is a valid solution with a time complexity
#   of O(n) & a space complexity of O(1).


#   Notes:
#   The all() function & manual loop are particularly useful for scenarios where 
#   short-circuiting is likely to save time. The max() function approach, while extremely concise, 
#   always runs through the entire list even if the first element already fails the condition.

#   Solution 2 is the most efficient solution since it uses the all() function with a generator expression &
#   clarity. In terms of efficiency Solution 2 & 3 are the best solutions to potentially reduce the number
#   of operations as they make use of short-circuiting. 