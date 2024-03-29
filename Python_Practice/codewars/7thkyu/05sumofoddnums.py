# Description:

# Given the triangle of consecutive odd numbers:

#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# ...

# Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

# 1 -->  1
# 2 --> 3 + 5 = 8

# -------------------------------------------------------------------------------------
# -----Solution 1-----Using the Formula n ** 3-----
def row_sum_odd_numbers(n):
    return n ** 3
    # we calculate the sum of the numbers in the nth row of the triangle using the formula n ** 3
    # this is because the sum of the numbers in the nth row of the triangle is equal to n ** 3
    # Examples:
    # if n = 1, the sum of the numbers in the 1st row of the triangle is 1
    # if n = 2, the sum of the numbers in the 2nd row of the triangle is 8

# -------------------------------------------------------------------------------------
# -----Solution 2-----If/Else Statement w/ Type Checking-----
def row_sum_odd_numbers(n):
    if type(n)==int and n>0:
        return n**3
    else:
        return "Input a positive integer"
    # we use an if/else statement to check if n is a positive integer
    # if n is a positive integer, we return n ** 3
    # if n is not a positive integer, we return "Input a positive integer"
    
# -------------------------------------------------------------------------------------
# -----Solution 3-----Using the sum() and range() functions-----
def row_sum_odd_numbers(n):
    return sum(range(n*(n-1)+1, n*(n+1), 2))
    # we calculate the sum of the numbers in the nth row of the triangle using the sum() and range() functions
    # the range() function generates a sequence of odd numbers starting at n*(n-1)+1 and ending at n*(n+1) with a step of 2
    # the sum() function calculates the sum of the sequence of odd numbers generated by the range() function