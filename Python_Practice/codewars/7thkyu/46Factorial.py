# Description:
# Your task is to write function factorial.

# https://en.wikipedia.org/wiki/Factorial

# -------------------------------------------------------------------------------------
# -----Solution 1-----math.factorial-----
from math import factorial
#   1.  Import the factorial function from the math module which
#       calculates the factorial of a number.

#   This method is the most efficient & concise way to calculate because
#   it uses the built-in math.factorial function from the math module within Python.

# -------------------------------------------------------------------------------------
# -----Solution 2-----For Loop & Multiplication-----
def factorial(n):
    j = 1
    for i in range(1, n+1):
       j *= i
    return j 
#   1.  Initialize a variable j to 1.
#   2.  Iterate through the range from 1 to n+1.
#   3.  Multiply j by the current value of i.
#   4.  Return the final value of j.

#   This solution is efficient & easy to understand. It calculates the factorial
#   by iterating through the range from 1 to n+1 & multiplying the current value
#   by the running total. It has a time complexity of O(n) & a space complexity of O(1).
#   Compared to the first solution, this solution is more verbose but does not require importing
#   any external modules.

# -------------------------------------------------------------------------------------
# -----Solution 3-----reduce & imul-----
from functools import reduce
from operator import imul

def factorial(n):
  return reduce(imul, range(1, n+1), 1)
#   1.  Import the reduce function from the functools module & the imul operator from 
#       the operator module.
#   2.  Use the reduce function to apply the imul operator to the range from 1 to n+1.
#   3.  The initial value is set to 1 to h&le the case when n is 0.
#   4.  The reduce function multiplies the elements of the range together to calculate the factorial.
#   5.  Return the result.

#   This solution is concise & uses the reduce function to multiply the elements of the range
#   together. It has a time complexity of O(n) & a space complexity of O(1). Compared to the
#   previous solution, this solution is more concise & uses the reduce function to perform the
#   multiplication operation, but compared to the first solution, it is more verbose.

# -------------------------------------------------------------------------------------
# -----Solution 4-----Javascript Solution-----Recursive----
# function factorial(n){
#   return n <= 1 ? 1 : n * factorial(n - 1);
# }
#   1.  This is a recursive solution that calculates the factorial of n.
#   2.  If n is less than or equal to 1, it returns 1.
#   3.  Otherwise, it multiplies n by the factorial of n-1.

#   This solution is concise & uses recursion to calculate the factorial. It has a time complexity
#   of O(n) & a space complexity of O(n) due to the recursive calls. It is similar to the second
#   Python solution but uses recursion instead of a loop to calculate the factorial.
#   While recursion is elegant, it may not be as efficient as an iterative solution due to the
#   overhead of function calls.

# -------------------------------------------------------------------------------------
# -----Solution 5-----Javascript Solution-----Iterative----
# function factorial(n){
#   let result = 1;
#   for(let i = 1; i <= n; i++){
#     result *= i;
#   }
#   return result;
# }
#   This solution uses a for loop to calculate the factorial iteratively. It has a time complexity
#   of O(n) & a space complexity of O(1). It is similar to the second Python solution but written
#   in JavaScript. The iterative solution is generally more efficient than the recursive solution
#   due to the overhead of function calls in recursion.