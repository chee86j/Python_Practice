# Complete the function that takes two integers 
# (a, b, where a < b) and return an array of all 
# integers between the input parameters, including them.

# For example:

# a = 1
# b = 4
# --> [1, 2, 3, 4]


# -------------------------------------------------------------------------------------
# -----Solution 1-----Range & List-----
def between(a,b):
    return list(range(a,b+1))
#   1. Convert the range of numbers from a to b into a list by using list()
#       - list() will convert the range of numbers into a list of numbers
#       - range() will create a range of numbers from a to b
#       - a is the starting number
#   2. Return the list of numbers
#   This solution is the most concise & readable solution with a time complexity 
#   of O(n) & a space complexity of O(n).


# -------------------------------------------------------------------------------------
# -----Solution 2-----List Comprehension & Range-----
def between(a,b):
    return [result for result in range(a,b+1)]
#   1. Create a list of numbers from a to b by using a list comprehension
#       - Create a list of numbers from a to b by using a for loop
#       - The for loop will iterate through the range of numbers from a to b
#       - The range of numbers is created by using the range() function
#       - The range() function will create a range of numbers from a to b
#       - The list comprehension will create a list of numbers from the range of numbers
#   2. Return the list of numbers
#   This solution is the most concise & readable solution with a time complexity
#   of O(n) & a space complexity of O(n).
#   Compared to the 1st solution, this solution uses a list comprehension to create
#   the list of numbers instead of using the list() function to convert the range of

# -------------------------------------------------------------------------------------
# -----Solution 3-----Manual Loop & Append-----
def between(a,b):
    arr = []
    for i in range(a, b + 1):
        arr.append(i)
    return arr
#   1. Create an empty list to store the range of numbers
#   2. Use a for loop to iterate through the range of numbers from a to b
#       - The for loop will iterate through the range of numbers from a to b
#       - The range of numbers is created by using the range() function
#       - The range() function will create a range of numbers from a to b
#   3. Append each number to the list
#       - Append each number to the list by using the append() function
#   4. Return the list of numbers
#   This solution is the most verbose solution with a time complexity of O(n) & a space
#   complexity of O(n).
#   Compared to the 1st & 2nd solutions, this solution uses a manual loop to iterate
#   through the range of numbers and append each number to the list. It is less concise
#   and readable than the 1st & 2nd solutions.

# -------------------------------------------------------------------------------------
# -----Solution 4-----
# function between(a,b){
#     var arr = [];
#     for (var i = a; i <= b; i++){
#         arr.push(i);
#     }
#     return arr;
# }
#   This solution is the same as Solution 3, but it is written in JavaScript.
#   This solution is the most verbose solution with a time complexity of O(n) & a space
#   complexity of O(n).
#   Compared to the 1st & 2nd solutions, this solution uses a manual loop to iterate
#   through the range of numbers and append each number to the list. It is less concise
#   and readable than the 1st & 2nd solutions.