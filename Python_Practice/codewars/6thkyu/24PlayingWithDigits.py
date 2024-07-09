# Some numbers have funny properties. For example:

# 89 --> 8¹ + 9² = 89 * 1
# 695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
# 46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

# Given two positive integers n and p, we want to find a positive integer k, 
# if it exists, such that the sum of the digits of n raised to consecutive 
# powers starting from p is equal to k * n.

# In other words, writing the consecutive digits of n as a, b, c, d ..., 
# is there an integer k such that :

# (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

# If it is the case we will return k, if not return -1.

# Note: n and p will always be strictly positive integers.


# Examples:

# n = 89; p = 1 ---> 1 since 8¹ + 9² = 89 = 89 * 1

# n = 92; p = 1 ---> -1 since there is no k such that 9¹ + 2² equals 92 * k

# n = 695; p = 2 ---> 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2

# n = 46288; p = 3 ---> 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

# -------------------------------------------------------------------------------------
# -----Solution 1-----For Loop & Enumerate-----
def dig_pow(n, p):
    s = 0
    for i,c in enumerate(str(n)):
        s += pow(int(c),p+i)
    return s/n if s%n==0 else -1
#   This solution uses a for loop to iterate through the digits of the number n.
#   The enumerate function is used to get the index and value of each digit.
#   The value of each digit is raised to the power of p plus the index and added to the sum s.
#   If the sum s is divisible by n, the function returns the quotient of the sum divided by n.
#   If the sum s is not divisible by n, the function returns -1.

#   Using the example n = 695 and p = 2:
#   The digits of n are 6, 9, and 5.
#   The sum of the digits raised to consecutive powers starting from p is calculated as follows:
#   6^2 + 9^3 + 5^4 = 36 + 729 + 625 = 1390
#   Since 1390 is divisible by 695, the function returns 2.

# -------------------------------------------------------------------------------------
# -----Solution 2-----Similar to Solution 1, but without Enumerate-----
def dig_pow(n, p):
    sum = 0
    for c in str(n):
        sum += int(c) ** p
        p += 1
    if sum % n == 0:
        return sum / n
    else:
        return -1
#   This solution uses a for loop to iterate through the digits of the number n.
#   In each iteration, the digit is converted to an integer and raised to the power of p.
#   The result of the power operation is added to the sum variable.
#   The power variable is incremented by 1 in each iteration.
#   After the loop is completed, the sum is checked to see if it is divisible by n.
#   If the sum is divisible by n, the function returns the quotient of the sum divided by n.
#   If the sum is not divisible by n, the function returns -1.

    
# -------------------------------------------------------------------------------------
# -----Solution 3-----Javascript Solution-----
# function digPow(n, p){
#     let sum = 0;
#     for (let c of n.toString()) {
#         sum += Math.pow(parseInt(c), p);
#         p++;
#     }
#     return sum % n === 0 ? sum / n : -1;
# }

#  1. The function takes in two positive integers, n and p.
#  2. The sum variable is initialized to 0.
#  3. A for loop is used to iterate through each digit of the number n.
#  4. In each iteration, the digit is converted to an integer and raised to the power of p.
#  5. The result of the power operation is added to the sum variable.
#  6. The power variable is incremented by 1 in each iteration.
#  7. After the loop is completed, the sum is checked to see if it is divisible by n.
#  8. If the sum is divisible by n, the function returns the quotient of the sum divided by n.
#  9. If the sum is not divisible by n, the function returns -1.