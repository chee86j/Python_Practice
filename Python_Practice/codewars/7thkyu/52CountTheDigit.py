# Take an integer n (n >= 0) and a digit d (0 <= d <= 9) as an integer.

# Square all numbers k (0 <= k <= n) between 0 and n.

# Count the numbers of digits d used in the writing of all the k**2.

# Implement the function taking n and d as parameters and returning this count.
# Examples:

# n = 10, d = 1 
# the k*k are 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100
# We are using the digit 1 in: 1, 16, 81, 100. The total count is then 4.

# The function, when given n = 25 and d = 1 as argument, should return 11 since
# the k*k that contain the digit 1 are:
# 1, 16, 81, 100, 121, 144, 169, 196, 361, 441.
# So there are 11 digits 1 for the squares of numbers between 0 and 25.

# Note that 121 has twice the digit 1.

# -------------------------------------------------------------------------------------
# -----Solution 1-----List Comprehension One-Liner-----
def nb_dig(n, d):
    return sum(str(i*i).count(str(d)) for i in range(n+1))
#   1.  Use list comprehension to iterate over the range of nums from 0 to n
#       & count the occurrences of the digit d in the square of each num
#   2.  Sum the counts of the digit d in the squares of all nums from 0 to n
#   3.  Return the total count of the digit d in the squares of all nums from 0 to
#       n as the result of the function

#   This solution has a time complexity of O(n) where n is the input num n since
#   it iterates over the range of nums from 0 to n & a space complexity of O(1)
#   since it only uses a few variables. This solution is efficient for counting the
#   occurrences of a digit in the squares of nums up to n. It uses list comprehension
#   to calculate the count of the digit d in each square & sum the total count.
#   It may not be the most easily readable solution.


# -------------------------------------------------------------------------------------
# -----Solution 2-----Loop & Count-----
def nb_dig(n, d):
    
    tot_occur = 0;
    
    for i in range(n+1):
        #print(i**2)
        tot_occur += str(i**2).count(str(d))
        
    return tot_occur
#   1.  Initialize a var `tot_occur` to store the total occurrences of the digit d
#   2.  Iterate over the range of nums from 0 to n
#   3.  Calculate the square of each num & count the occurrences of the digit d
#       in the square
#   4.  Add the count of the digit d in the square to the total occurrences
#   5.  Return the total occurrences of the digit d in the squares of all nums from
#       0 to n as the result of the function

#   This solution has a time complexity of O(n) where n is the input num n since
#   it iterates over the range of nums from 0 to n & a space complexity of O(1)
#   since it only uses a few variables. This solution is efficient for counting the
#   occurrences of a digit in the squares of nums up to n. It uses a loop to calculate
#   the count of the digit d in each square & sum the total count. It is a more readable
#   solution compared to the list comprehension approach.

# -------------------------------------------------------------------------------------
# -----Solution 3-----Javascript Solution-----
# function nbDig(n, d) {
#     let count = 0;
#     for (let i = 0; i <= n; i++) {
#         count += (i * i).toString().split(d).length - 1;
#     }
#     return count;
# }

#  This is a JS solution that counts the occurrences of a digit d in the squares
#  of nums up to n. It uses a for loop to iterate over the range of nums from 0 to n
#  & calculates the square of each num. The count of the digit d in the square is
#  calculated using the split method & added to the total count. The time complexity of
#  this solution is O(n) where n is the input num n since it iterates over the range of
#  nums from 0 to n & the space complexity is O(1) since it only uses a few variables.
#  This solution is similar to the second Python solution but written in JavaScript.