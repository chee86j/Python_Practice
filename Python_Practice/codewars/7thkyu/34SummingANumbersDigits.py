# Write a function named sumDigits which takes a number as input and 
# returns the sum of the absolute value of each of the number's decimal digits.

# For example: (Input --> Output)

# 10 --> 1
# 99 --> 18
# -32 --> 5
# Let's assume that all numbers in the input will be integer values.

# -------------------------------------------------------------------------------------
# -----Solution 1-----Sum & ABS & List Comprehension-----
def sumDigits(number):
    return sum(int(digit) for digit in str(abs(number)))
#  1. The function takes in a number.
#  2. The number is converted to its absolute value using the abs method.
#  3. The absolute value of the number is converted to a string.
#  4. A generator expression is used to iterate through each digit in the string.
#  5. The digit is converted to an integer and summed.
#  6. The sum of the absolute value of each digit is returned.

# -------------------------------------------------------------------------------------
# -----Solution 2-----Sum & Map & Abs-----
def sum_digits(number):
    return sum(map(int, str(abs(number))))
#  1. The function takes in a number.
#  2. The number is converted to its absolute value using the abs method.
#  3. The absolute value of the number is converted to a string.
#  4. The map function is used to convert each digit in the string to an integer.
#  5. The sum function is used to sum the integers.
#  6. The sum of the absolute value of each digit is returned.

# -------------------------------------------------------------------------------------
# -----Solution 3-----Javascript Solution-----
# function sumDigits(number) {
#     return Math.abs(number).toString().split('').reduce((a, b) => +a + +b, 0);
# }
#  1. The function takes in a number.
#  2. The number is converted to its absolute value using the Math.abs method.
#  3. The absolute value of the number is converted to a string.
#  4. The string is split into an array of digits.
#  5. The reduce method is used to sum the digits.
#  6. The sum of the absolute value of each digit is returned.
