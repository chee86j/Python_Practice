# Numbers ending with zeros are boring.

# They might be fun in your world, but not here.

# Get rid of them. Only the ending ones.

# 1450 -> 145
# 960000 -> 96
# 1050 -> 105
# -1050 -> -105
# Zero alone is fine, don't worry about it. Poor guy anyway

# -------------------------------------------------------------------------------------
# -----Solution 1-----String Manipulation w/ Exception Handling-----
def no_boring_zeros(n):
    try:
        return int(str(n).rstrip('0'))
    except ValueError:
        return 0
#   1.  The () takes in an integer n
#   2.  The () returns an integer with all trailing zeros removed
#   3.  The () converts the integer n to a string & removes all trailing zeros
#   4.  The () converts the modified string back to an integer & returns it
#   5.  If the input integer is 0, the () returns 0
#   6.  This solution has a time complexity of O(n) where n is the number of digits in the input integer
#   7.  The space complexity is also O(n) as the string can store up to n characters

#   This solution is efficient & concise, using a single line of code to remove all trailing zeros from the input

# -------------------------------------------------------------------------------------
# -----Solution 2-----While Loop-----
def no_boring_zeros(n):
    if n==0:
        return n
    while n%10==0:
        n=n/10
    return n
#   1.  The () takes in an integer n
#   2.  The () returns an integer with all trailing zeros removed
#   3.  If the input integer is 0, the () returns 0
#   4.  The () loops while the last digit of the integer n is 0
#   5.  In each iteration, the last digit is removed by dividing n by 10
#   6.  The () returns the modified integer after removing all trailing zeros
#   7.  This solution has a time complexity of O(n) where n is the number of digits in the input integer
#   8.  The space complexity is O(1) as the solution uses a constant amount of extra space

#   This is efficient & does not require converting the integer to a string.

# -------------------------------------------------------------------------------------
# -----Solution 3-----One Liner w/ Strip & Int Conversion-----
def no_boring_zeros(n):
    return int(str(n).strip("0")) if n else n
#   1.  The () takes in an integer n
#   2.  The () returns an integer with all trailing zeros removed
#   3.  The () converts the integer n to a string & removes all trailing zeros
#   4.  The () converts the modified string back to an integer & returns it
#   5.  If the input integer is 0, the () returns 0
#   6.  This solution has a time complexity of O(n) where n is the number of digits in the input integer
#   7.  The space complexity is also O(n) as the string can store up to n characters

# -------------------------------------------------------------------------------------
# -----Solution 4-----Javascript Solution-----
# function noBoringZeros(n) {
#     return n === 0 ? n : parseInt(n.toString().replace(/0+$/, ''));
# }
#    1.  The ()) noBoringZeros takes in an integer n
#    2.  It returns an integer with all trailing zeros removed
#    3.  If the input integer is 0, the ()) returns 0
#    4.  The toString method is used to convert the integer n to a string
#    5.  The replace method is used to remove all trailing zeros from the string
#        using the regular expression /0+$/ built-in JavaScript ()) &
#        the $ anchor to match the end of the string
#    6.  The parseInt method is used to convert the modified string back to an integer
#    7.  The ()) returns the modified integer after removing all trailing zeros
#    8.  This solution has a time complexity of O(n) where n is the number of digits in the input integer
#    9.  The space complexity is also O(n) as the string can store up to n characters
#    10.  This solution is efficient & concise, using a single line of code to remove all trailing zeros from the input
