# This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.

# -------------------------------------------------------------------------------------
# -----Solution 1-----Ternary Operator-----
def simple_multiplication(number) :
    return number * 9 if number % 2 else number * 8 # we can also use ternary operators in python

# -------------------------------------------------------------------------------------
# -----Solution 2-----Modulo Operator-----
def simple_multiplication(n) :
    return n * (8 + n%2) # we can also use the modulo operator in python

# -------------------------------------------------------------------------------------
# -----Solution 3-----If Else-----
def simple_multiplication(number):
    if number % 2 == 0:     # remember unlike JS, python does not need () around conditionals
        return number * 8   # nor does python need ; at the end of lines
    else:                   # but python does need : at the end of conditionals
        return number * 9

# -------------------------------------------------------------------------------------
# -----Solution 4-----Ternary Operator citing the condition first-----
def simple_multiplication(number) :
    return number * 8 if number % 2 == 0 else number * 9
