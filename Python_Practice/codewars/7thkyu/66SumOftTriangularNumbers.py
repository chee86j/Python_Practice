# Your task is to return the sum of Triangular Numbers up-to-and-including 
# the nth Triangular Number.

# Triangular Number: "any of the series of numbers (1, 3, 6, 10, 15, etc.) 
# obtained by continued summation of the natural numbers 1, 2, 3, 4, 5, etc."

# [01]
# 02 [03]
# 04 05 [06]
# 07 08 09 [10]
# 11 12 13 14 [15]
# 16 17 18 19 20 [21]

# e.g. If 4 is given: 1 + 3 + 6 + 10 = 20.

# Triangular Numbers cannot be negative so return 0 if a negative number is given.

# -------------------------------------------------------------------------------------
# -----Solution 1-----Single Line Solution-----
def sum_triangular_numbers(n):
    return n*(n+1)*(n+2)/6 if n>0 else 0
#   1. The formula for the sum of the first n triangular nums is n*(n+1)*(n+2)/6.
#   2. If n is less than or equal to 0, return 0.
#   3. Otherwise, return the sum of the first n triangular nums using the formula.

#   The time complexity of this solution is O(1) since it involves a single 
#   mathematical operation.
#   The space complexity is also O(1) since no additional data structures are used.
#   This is the most efficient solution for this problem as all the calculations are 
#   done in a single step. It is ideal for large values of n.

# -------------------------------------------------------------------------------------
# -----Solution 2-----Using Iterative Approach-----
def sum_triangular_numbers(n):
    total, a = 0,0
    for i in range(n):
        a += i+1
        total += a
    return total
#   1. Initialize a var total to store the sum of triangular nums and a to store the 
#      current triangular num.
#   2. Iterate through the range from 0 to n (exclusive).
#   3. Increment a by i+1 to get the next triangular num.
#   4. Add the current triangular num to total.
#   5. Return the total sum of triangular nums.

#   The time complexity of this solution is O(n) where n is the input number.
#   The space complexity is O(1) since no additional data structures are used.
#   Compared to Solution 1, this solution is less efficient as it involves iterating 
#   through the range of numbers. For larger values of n, this solution may take more
#   time to compute the sum of triangular nums.

# -------------------------------------------------------------------------------------
# -----Solution 3-----Using List Comprehension-----
def sum_triangular_numbers(n):
    return sum(sum(range(x+1)) for x in range(n+1))
#   1. Iterate through the range from 0 to n (inclusive).
#   2. For each value x, calculate the sum of the range from 0 to x+1.
#   3. Sum the results of the inner sum calculations.
#   4. Return the total sum of triangular nums.

#   The time complexity of this solution is O(n^2) where n is the input number.
#   The space complexity is O(1) since no additional data structures are used.
#   This solution is less efficient compared to the previous solutions as it involves
#   nested iterations and sum calculations.

# -------------------------------------------------------------------------------------
# -----Solution 4-----JavaScript Solution-----
# function sum_triangular_numbers(n) {
#     if (n <= 0) return 0;
#     return n * (n + 1) * (n + 2) / 6;
# }

#   1. This Solution is similar to Solution 1 but implemented in JavaScript. 
#   2. The formula for the sum of the first n triangular nums is n*(n+1)*(n+2)/6.
#   3. If n is less than or equal to 0, return 0.
#   4. Otherwise, return the sum of the first n triangular nums using the formula.

#   The time complexity of this solution is O(1) since it involves a single
#   mathematical operation. The space complexity is also O(1) since no additional
#   data structures are used. This is the most efficient solution for this problem as
#   all the calculations are done in a single step. It is ideal for large values of n.
