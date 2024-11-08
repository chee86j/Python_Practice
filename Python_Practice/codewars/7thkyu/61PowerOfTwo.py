# Complete the function power_of_two/powerOfTwo (or equivalent, depending 
# on your language) that determines if a given non-negative integer is a 
# power of two. From the corresponding Wikipedia entry:

# a power of two is a number of the form 2n where n is an integer, 
# i.e. the result of exponentiation with number two as the base and 
# integer n as the exponent.

# You may assume the input is always valid.

# Examples

# power_of_two(1024) ==> True
# power_of_two(4096) ==> True
# power_of_two(333)  ==> False

# Beware of certain edge cases - for example, 1 is a power of 2 
# since 2^0 = 1 and 0 is not a power of 2.

# -------------------------------------------------------------------------------------
# -----Solution 1-----Binary Counting-----
def power_of_two(num):
    return bin(num).count('1') == 1
#   1. Convert the number to binary by using `bin()` function.
#   2. Count the number of 1s in the binary number using `count()` function.
#   3. Return True if the count is 1, otherwise False.

#   The time complexity of this solution is O(log n) because the number of iterations
#   is proportional to the number of bits in the binary representation of the number.
#   The space complexity is O(1) because the number of variables used is constant.

#   This solution is reasonably efficient but less direct thant the bitwise & trick. Counting
#   the number of 1s involves more steps than simply checking if the number is a power of 2.

# -------------------------------------------------------------------------------------
# -----Solution 2-----Bitwise & Trick-----
def power_of_two(x):
    return x != 0 and ((x & (x - 1)) == 0)
#   1. Check if the number is not 0 using `x != 0`.
#   2. Check if the number is a power of 2 by using the bitwise & operator and the
#      expression `(x & (x - 1)) == 0`.
#   3. Return True if the number is a power of 2, otherwise False.

#   The time complexity of this solution is O(1) because the number of operations is constant.
#   The space complexity is O(1) because the number of variables used is constant.

#   This solution is the most efficient as it leverages the direct property of power of 2
#   resulting in low overhead and fast execution.


# -------------------------------------------------------------------------------------
# -----Solution 3-----Division Loop-----
def power_of_two(x):
    while x > 1 and x % 2 == 0:
        x = x // 2
    return x == 1
#   1. Check if the number is greater than 1 and divisible by 2 using `x > 1 and x % 2 == 0`.
#   2. Divide the number by 2 using `x = x // 2`.
#   3. Repeat the division until the number is no longer divisible by 2.

#   The time complexity of this solution is O(log n) because the number of iterations is
#   proportional to the number of times the number can be divided by 2.
#   The space complexity is O(1) because the number of variables used is constant.

#   This solution is less efficient than the bitwise & trick, but more efficient than 
#   Solution 1. It is a more direct approach to checking if a number is a power of 2.
#   It is a clear iterative solution that is easy to understand and implement.


# -------------------------------------------------------------------------------------
# -----Solution 4-----Javascript Version-----Logarithmic Check-----
# function isPowerOfTwo(n){
#     return Number.isInteger(Math.log2(n));
# }
#   1. Check if the number is a power of 2 by using the `Math.log2()` function.
#   2. Check if the result is an integer using the `Number.isInteger()` function.
#   3. Return True if the number is a power of 2, otherwise False.

#   This solution is similar to Solution 1 but uses the `Math.log2()` function to determine
#   if the number is a power of 2. It is a concise and elegant solution that works for
#   positive integers greater than 0. It is less efficient than the bitwise & trick but
#   more efficient than the division loop. This is a static method of the Number object,
#   and must be invoked through the Number object.
