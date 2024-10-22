# Create a function called _if which takes 3 arguments: 
# a value bool and 2 functions (which do not take any parameters): func1 and func2

# When bool is truthy, func1 should be called, otherwise call the func2.

# Example:
# def truthy(): 
#   print("True")
  
# def falsey(): 
#   print("False")
  
# _if(True, truthy, falsey)
# prints 'True' to the console

# -------------------------------------------------------------------------------------
# -----Solution 1-----If / Else-----
def _if(bool, func1, func2):
  func1() if bool else func2()
#   This solution defines a function _if that takes a boolean value & two functions as arguments.
#   It uses a ternary operator to call func1 if the boolean value is truthy (i.e., evaluates to True),
#   otherwise it calls func2. It has a time complexity of O(1) & a space complexity of O(1) since it
#   only performs a single comparison & calls one of the two functions before returning the result.


# -------------------------------------------------------------------------------------
# -----Solution 2-----If / Else w/ Return-----
def _if(bool, func1, func2):
    if bool:
        return func1()
    else:
        return func2()
#   This solution defines a function _if that takes a boolean value & two functions as arguments.
#   It checks if the boolean value is truthy (i.e., evaluates to True) & calls func1 if it is,
#   otherwise it calls func2. It has a time complexity of O(1) & a space complexity of O(1) since
#   it only performs a single comparison & calls one of the two functions before returning the result.

# -------------------------------------------------------------------------------------
# -----Solution 3-----JavaScript Version-----
# function _if(bool, func1, func2) {
#   return bool ? func1() : func2();
# }
#   This solution is the JavaScript equivalent of the Python Solution 1. It defines a function _if
#   that takes a boolean value & two functions as arguments. It uses a ternary operator to call func1
#   if the boolean value is truthy (i.e., evaluates to true), otherwise it calls func2. It has a time
#   complexity of O(1) & a space complexity of O(1) since it only performs a single comparison & calls
#   one of the two functions before returning the result.