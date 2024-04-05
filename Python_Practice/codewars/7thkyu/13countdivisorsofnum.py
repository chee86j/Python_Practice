# Count the number of divisors of a positive integer n.

# Random tests go up to n = 500000.

# Examples (input --> output)
# 4 --> 3 // 3 divisors: 1, 2, & 4
# 5 --> 2 // 2 divisors: 1 & 5
# 12 --> 6 // 6 divisors: 1, 2, 3, 4, 6, & 12
# 30 --> 8 // 8 divisors: 1, 2, 3, 5, 6, 10, 15, & 30
# Note you should only return a number, the count of divisors. 
# Parentheses indicate which numbers are counted in each case.

# -------------------------------------------------------------------------------------
# -----Solution 1-----Lambda function-----
divisors = lambda n: sum([n % x == 0 for x in range(1, n + 1)])
# 1. the python Lambda function defines a function in a single line
# 2. lambda is a keyword in Python used for anonymous functions
# 3. this solution uses a lambda function to define the divisors function
# 4. then uses a list comprehension to iterate from 1 to n, checking if n is divisible by each number
# 5. then creates a list of boolean values based on the result of the modulo operation
# 6. sum() function is used to calculate the count of divisors by summing up the True values

# -------------------------------------------------------------------------------------
# -----BEST PRACTICE---------------------------------------------------------------
# -----Solution 2-----Regular function definition-----
def divisors(n):
    return  len([l_div for l_div in range(1, n + 1) if n % l_div == 0]);
# 1. this uses regular function definition with the def keyword
# 2. uses a list comprehension to iterate from 1 to n, checking if n is divisible by each number
# 3. creates a list of divisors and returns the length of that list, which is the count of divisors

# -------------------------------------------------------------------------------------
# -----Solution 3-----Regular function definition w/ list comprehension-----
def divisors(n):
    return sum([n % x == 0 for x in range(1, n + 1)])
# 1. this is similar to solution 1 but without using a lambda function
# 2. it defines the divisors function using a regular function definition
# 3. then uses a list comprehension to iterate from 1 to n, checking if n is divisible by each number
# 4. then creates a list of boolean values based on the result of the modulo operation

# -------------------------------------------------------------------------------------
# -----Solution 4-----If-else statement in list comprehension-----
def divisors(n):
    return sum([True if n % x == 0 else False for x in range(1, n + 1)])
# 1. this solution uses an if-else statement inside the list comprehension
# 2. if n is divisible by x, it will return True, otherwise False
# 3. sum() function is used to calculate the count of divisors by summing up the True values
