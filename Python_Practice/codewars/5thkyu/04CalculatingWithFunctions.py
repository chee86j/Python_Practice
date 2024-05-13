# DESCRIPTION:
# This time we want to write calculations using functions and get the results. 
# Let's have a look at some examples:

# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3
# Requirements:

# There must be a function for each number from 0 ("zero") to 9 ("nine")

# There must be a function for each of the following mathematical operations: 
# plus, minus, times, divided_by

# Each calculation consist of exactly one operation and two numbers

# The most outer function represents the left operand, the most inner function 
# represents the right operand

# Division should be integer division. For example, this should return 2, not 
# 2.666666...:
# eight(divided_by(three()))


# ---------------------Background Information------------------------------------------
# Numerical Calculation System using Functions as First-Class Citizens

# Lambda in Python is a first-class citizen. A first-class citizen (sometimes
# called first-class objects) in a programming language is an entity which supports
# all the operations generally available to other entities. These operations typically
# include being passed as an argument, returned from a function, and assigned to a
# variable. In Python, functions are first-class citizens. This means that they can
# be passed as arguments to other functions, returned as values from other functions,
# and assigned to variables and stored in data structures.

# -------------------------------------------------------------------------------------
# -----Solution 1-----Higher Order Functions & Lambdas-----
def identity(a): return a

def zero(f=identity): return f(0)
def one(f=identity): return f(1)
def two(f=identity): return f(2)
def three(f=identity): return f(3)
def four(f=identity): return f(4)
def five(f=identity): return f(5)
def six(f=identity): return f(6)
def seven(f=identity): return f(7)
def eight(f=identity): return f(8)
def nine(f=identity): return f(9)

def plus(b): return lambda a: a + b
def minus(b): return lambda a: a - b
def times(b): return lambda a: a * b
def divided_by(b): return lambda a: a // b

#  1.  NUMBER functions (zero through nine) are defined with an optional () argument
#      'f', with a default of 'identity' which returns the argument passed to it.
#  2.  If no () is passed, the number is returned by calling 'identity(number)'
#  3.  If a () is provided, that () is called with the number as an argument

#  4.  OPERATOR functions (plus, minus, times, divided_by): with each of these ()s
#      returns a lambda () that takes an argument 'a' and returns the result of
#      the operation on 'a' and 'b'. For example, 'plus' returns 'lambda a: a + b'.
#  5.  The returned lambda is then passed to one of the number functions. For example,
#      'seven(plus(five()))', 'times(five())' returns 'lambda a: a * 5', which is then
#      passed to 'seven()', which calls the lambda with 7 , returning '7 * 5'.

# -------------------------------------------------------------------------------------
# -----Solution 2-----Eval (Less Reliable Solution-----
# -----Eval can execute arbitrary code leading to security vulnerabilities-----
def zero(arg=""):  return eval("0" + arg)
def one(arg=""):   return eval("1" + arg)
def two(arg=""):   return eval("2" + arg)
def three(arg=""): return eval("3" + arg)
def four(arg=""):  return eval("4" + arg)
def five(arg=""):  return eval("5" + arg)
def six(arg=""):   return eval("6" + arg)
def seven(arg=""): return eval("7" + arg)
def eight(arg=""): return eval("8" + arg)
def nine(arg=""):  return eval("9" + arg)

def plus(n):       return '+' + str(n)
def minus(n):      return '-' + str(n)
def times(n):      return '*' + str(n)
def divided_by(n): return '//' + str(n)

#  1.  NUMBER functions (zero through nine) are defined with an optional "" argument
#      'arg', which is passed to 'eval' as a string.
#  2.  If no operand is passes to the number (), it simply returns the number.
#  3.  If an operand is passed to the number (), it is concatenated to the number using
#      and evaluates the resulting string using 'eval'.

#  4.  OPERATOR functions (plus, minus, times, divided_by): with each of these ()s
#      returns a string that represents the operation on the number. For example,
#      'plus(5)' returns '+5'.
#  5.  The returned string is then passed to one of the number functions, which
#      concatenates the string to the number and evaluates the resulting string.
