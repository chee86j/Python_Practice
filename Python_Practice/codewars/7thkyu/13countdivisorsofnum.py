# Count number of divisors of a positive integer n.

# Random tests go up to n = 500000.

# Examples (input --> output)
# 4 --> 3 // 3 divisors: 1, 2, & 4
# 5 --> 2 // 2 divisors: 1 & 5
# 12 --> 6 // 6 divisors: 1, 2, 3, 4, 6, & 12
# 30 --> 8 // 8 divisors: 1, 2, 3, 5, 6, 10, 15, & 30
# Note you should only return a number, count of divisors. 
# Parentheses indicate which numbers are counted in each case.

# -------------------------------------------------------------------------------------
# -----Solution 1-----Lambda function-----
divisors = lambda n: sum([n % x == 0 for x in range(1, n + 1)])
# 1. This solution uses a lambda function, which is similar to anonymous functions in JavaScript.
# 2. It defines divisors function in a single line, using lambda keyword.
# 3. It then utilizes a list comprehension to generate an array of boolean values indicating divisibility.
# 4. Finally, it uses sum() function to count number of True values in array, giving count of divisors.

# -------------------------------------------------------------------------------------
# -----BEST PRACTICE---------------------------------------------------------------
# -----Solution 2-----Regular function definition-----
def divisors(n):
    return  len([l_div for l_div in range(1, n + 1) if n % l_div == 0]);
# 1. This solution uses a regular function definition, similar to function declarations in JavaScript.
# 2. It defines divisors function using def keyword, followed by function name & parameters.
# 3. It employs a list comprehension to create an array of divisors for given number.
# 4. len() function is then used to determine length of this array, providing count of divisors.

# -------------------------------------------------------------------------------------
# -----Solution 3-----Regular function definition w/ list comprehension-----
def divisors(n):
    return sum([n % x == 0 for x in range(1, n + 1)])
# 1. This solution is similar to Solution 1 but without using a lambda function.
# 2. It defines divisors function using a regular function definition, similar to Solution 2.
# 3. Instead of explicitly creating a list of divisors, it directly generates an array of boolean values.
# 4. sum() function is then applied to count number of True values, providing count of divisors.

# -------------------------------------------------------------------------------------
# -----Solution 4-----If-else statement in list comprehension-----
def divisors(n):
    return sum([True if n % x == 0 else False for x in range(1, n + 1)])
# 1. This solution incorporates an if-else statement inside a list comprehension.
# 2. If number is divisible by x, it returns True; otherwise, it returns False.
# 3. sum() function is then utilized to count number of True values, yielding count of divisors.
