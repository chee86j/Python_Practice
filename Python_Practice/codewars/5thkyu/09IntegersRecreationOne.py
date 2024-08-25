# 1, 246, 2, 123, 3, 82, 6, 41 are the divisors of number 246. Squaring these divisors 
# we get: 1, 60516, 4, 15129, 9, 6724, 36, 1681. The sum of these squares is 84100 
# which is 290 * 290.

# Task
# Find all integers between m and n (m and n integers with 1 <= m <= n) such that 
# the sum of their squared divisors is itself a square.

# We will return an array of subarrays or of tuples (in C an array of Pair) or a 
# string. The subarrays (or tuples or Pairs) will have two elements: first the 
# number the squared divisors of which is a square and then the sum of the squared divisors.

# Example:
# list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
# list_squared(42, 250) --> [[42, 2500], [246, 84100]]
# The form of the examples may change according to the language, see "Sample Tests".

# Note
# In Fortran - as in any other language - the returned string is not permitted to 
# contain any redundant trailing whitespace: you can use dynamically allocated character strings.

# -------------------------------------------------------------------------------------
# -----Solution 1----Cache Divisors----
CACHE = {}

def squared_cache(number):
    if number not in CACHE:
        divisors = [x for x in range(1, number + 1) if number % x == 0]
        CACHE[number] = sum([x * x for x in divisors])
        return CACHE[number] 
    
    return CACHE[number]

def list_squared(m, n):
    ret = []

    for number in range(m, n + 1):
        divisors_sum = squared_cache(number)
        if (divisors_sum ** 0.5).is_integer():
            ret.append([number, divisors_sum])

    return ret
#   1. Create a cache to store the sum of squared divisors for each number.
#   2. Iterate over the range of numbers from m to n.
#   3. Calculate the sum of squared divisors for each number.
#   4. Check if the square root of the sum of squared divisors is an integer.
#   5. If it is, append the number & the sum of squared divisors to the result list.
#   6. Return the result list.

#   This solution could be efficient in scenarios w/ repeated calculations for the same numbers,
#   but it's not the best solution for one-time calculations over wide ranges due to
#   the overhead of the cache & non-optimized divisor calculation. It has a time complexity of 
#   O(n^2) & space complexity of O(n).

# -------------------------------------------------------------------------------------
# -----Solution 2----Loops & Sets----
def list_squared(m, n):
    out = []
    for i in range(m,n+1):
        # Finding all divisors below the square root of i
        possibles = set([x for x in range (1,int(i**0.5)+1) if i%x == 0])
        # And adding their counterpart
        possibles.update([i/x for x in possibles])
        # Doubles in the possibles are solved due to the set
        val = sum(x**2 for x in possibles)
        # Checking for exact square
        if (int(val**0.5))**2 == val: out.append([i, val])
    return out
#   1. Iterate over the range of numbers from m to n.
#   2. Find all divisors below the square root of the number.
#   3. Add the counterpart of each divisor to the set of divisors.
#   4. Calculate the sum of squared divisors.
#   5. Check if the square root of the sum of squared divisors is an integer.
#   6. If it is, append the number & the sum of squared divisors to the result list.
#   7. Return the result list.

#   This solution is more efficient than the previous one as it avoids the overhead of the cache
#   & uses a set to store the divisors, which eliminates duplicates. It has a time complexity of
#   O(n^2) & space complexity of O(n). It balances computational efficiency & readability in
#   cases where `m` & `n` are not too large.

# -------------------------------------------------------------------------------------
# -----Solution 3----Helper Function & Iteration----
from math import floor, sqrt, pow

def sum_squared_factors(n):
    s, res, i = 0, [], 1
    while (i <= floor(sqrt(n))):
        if (n % i == 0):
            s += i * i
            nf = n // i
            if (nf != i):
                s += nf * nf
        i += 1
    if (pow(int(sqrt(s)), 2) == s):
        res.append(n)
        res.append(s)
        return res
    else:
        return None
        
def list_squared(m, n):
    res, i = [], m
    while (i <= n):
        r = sum_squared_factors(i)
        if (r != None):
            res.append(r);
        i += 1
    return res
#   1. Define a helper function to calculate the sum of squared factors for a given number.
#   2. Initialize an empty list to store the results.
#   3. Iterate over the range of numbers from m to n.
#   4. Calculate the sum of squared factors for each number.
#   5. If the sum of squared factors is a perfect square, append the number & the sum of squared factors to the result list.
#   6. Return the result list.

#   This solution offers a clear separation of concerns but may slightly lag in execution time
#   efficiency due to function call overheads & the use of floating-point arithmetic for checking
#   perfect squares. It has a time complexity of O(n^2) & space complexity of O(n).


# -------------------------------------------------------------------------------------
# -----Solution 4----JavaScript Solution----For Loop & Math.sqrt----
# function listSquared(m, n) {
#     let results = [];
#     for (let i = m; i <= n; i++) {
#         let sum = 0;
#         for (let j = 1; j <= Math.sqrt(i); j++) {
#             if (i % j === 0) {
#                 sum += j * j;  // Add square of the divisor
#                 if (j !== i / j) { // Add square of the complement divisor if not the same
#                     sum += (i / j) * (i / j);
#                 }
#             }
#         }
#         let sqrtSum = Math.sqrt(sum);
#         if (Number.isInteger(sqrtSum)) {
#             results.push([i, sum]);
#         }
#     }
#     return results;
# }
#   1. Initialize an empty array to store the results.
#   2. Iterate over the range of numbers from m to n.
#   3. Calculate the sum of squared divisors for each number.
#   4. Check if the square root of the sum of squared divisors is an integer.
#   5. If it is, append the number & the sum of squared divisors to the result array.
#   6. Return the result array.

#   This solution is similar to the previous one but uses a more concise syntax for checking
#   perfect squares. It has a time complexity of O(n^2) & space complexity of O(n). It is 
#   straightforward & easy to understand.
