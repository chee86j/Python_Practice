# In John's car the GPS records every s seconds the distance travelled from an origin (distances are measured 
# in an arbitrary but consistent unit). For example, below is part of a record with s = 15:

# x = [0.0, 0.19, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25]

# The sections are:

# 0.0-0.19, 0.19-0.5, 0.5-0.75, 0.75-1.0, 1.0-1.25, 1.25-1.50, 1.5-1.75, 1.75-2.0, 2.0-2.25

# We can calculate John's average hourly speed on every section and we get:

# [45.6, 74.4, 60.0, 60.0, 60.0, 60.0, 60.0, 60.0, 60.0]

# Given s and x the task is to return as an integer the *floor* of the maximum average speed per hour obtained 
# on the sections of x. If x length is less than or equal to 1 return 0 since the car didn't move.

# Example:

# With the above data your function gps(s, x) should return 74
# Note

# With floats it can happen that results depends on the operations order. To calculate hourly speed you can use:

#  (3600 * delta_distance) / s.

# Happy coding!

# -------------------------------------------------------------------------------------
# -----Solution 1-----max() & generator expression-----
def gps(s, x):
    if len(x) < 2:
        return 0
    a = max(x[i] - x[i-1] for i in range(1, len(x))) 
    return a * 3600.0 / s
#   1.  We start by using a generator expression to calculate the difference between each 
#       pair of consecutive elements in the input list x.
#       'x[i] - x[i-1] for i in range(1, len(x))'
#   2.  We then use the max() function to find the maximum value in the list of differences.
#       'max(x[i] - x[i-1] for i in range(1, len(x)))'
#   3.  Finally, we multiply the maximum difference by 3600.0 and divide by s to get the
#       maximum average speed per hour.
#       'a * 3600.0 / s'

#   This checks if the list x has fewer than 2 elements and returns 0 if it does.
#   It has a time complexity of O(n) where n is the length of the input list x.
#   The space complexity is O(1) as we only use a constant amount of extra space.

# -------------------------------------------------------------------------------------
# -----Solution 2-----zip() & max()-----
def gps(s, x):
    return max([(n-m)*3600/s for (m,n) in zip(x,x[1:])])
#   1.  We use the zip() function to pair each element in the input list x with the next element.
#       'zip(x, x[1:])'
#   2.  We then use a list comprehension to calculate the difference between each pair of elements,
#       multiply by 3600, and divide by s to get the average speed per hour.
#       '[(n-m)*3600/s for (m,n) in zip(x,x[1:])]'
#   3.  Finally, we use the max() function to find the maximum value in the list of average speeds.
#       'max([(n-m)*3600/s for (m,n) in zip(x,x[1:])])'

#   This solution has a time complexity of O(n) where n is the length of the input list x.
#   The space complexity is O(1) as we only use a constant amount of extra space.

#   Compared to Solution 1, this solution uses zip() to pair elements in the input list x,
#   which may be more intuitive for some readers. However, it is functionally equivalent to
#   Solution 1 and has the same time and space complexity.

# -------------------------------------------------------------------------------------
# -----Solution 3-----Javacript Solution-----Loop & Math.max()-----
# const gps = (s, x) => {

#   if (x.length<=1) {
#     return 0;
#   }
  
#   let output = [];
#   for (let i = 0; i < x.length-1; i++) { 
#     output.push((x[i+1]-x[i])*3600/s);
#   }
  
#   return Math.max(...output);
# }

#   1.  We start by checking if the length of the input list x is less than or equal to 1.
#       If it is, we return 0.
#       'if (x.length<=1) { return 0; }'
#   2.  We then initialize an empty array called output to store the calculated average speeds.
#       'let output = [];'
#   3.  We use a for loop to iterate over the elements of the input list x, calculating the
#       difference between each pair of consecutive elements, multiplying by 3600, and dividing
#       by s to get the average speed per hour. We push each calculated value to the output array.
#       'for (let i = 0; i < x.length-1; i++) { output.push((x[i+1]-x[i])*3600/s); }'
#   4.  Finally, we use the Math.max() function with the spread operator (...) to find the maximum
#       value in the output array and return it.
#       'return Math.max(...output);'

#   This solution has a time complexity of O(n) where n is the length of the input list x.
#   The space complexity is O(n) as we create an array to store the calculated average speeds.

#   This solution is functionally equivalent to the Python solutions and follows a similar approach
#   of calculating the differences between consecutive elements in the input list x and finding the
#   maximum value. The key difference is the use of the Math.max() function in JavaScript to find
#   the maximum value in an array. Note that this is not memory efficient as it requires creating
#   an array to store the calculated values.
