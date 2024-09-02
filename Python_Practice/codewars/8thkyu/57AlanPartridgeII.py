# As a treat, I'll let you read part of the script from a classic 
# `I'm Alan Partridge` episode:

# Lynn: Alan, there’s that teacher chap.
# Alan: Michael, if he hits me, will you hit him first?
# Michael: No, he’s a customer. I cannot hit customers. I’ve been told. 
#          I’ll go and get some stock.
# Alan: Yeah, chicken stock.
# Phil: Hello Alan.
# Alan: Lynn, hand me an apple pie. And remove yourself from the theatre of conflict.
# Lynn: What do you mean?
# Alan: Go and stand by the yakults. The temperature inside this apple turnover 
#       is 1,000 degrees. If I squeeze it, a jet of molten Bramley apple is going to 
#       squirt out. Could go your way, could go mine. Either way, one of us is going down.


# Alan is known for referring to the temperature of the apple turnover as Hotter 
# than the sun!. According to space.com the temperature of the sun's corona is 
# 2,000,000 degrees Celsius, but we will ignore the science for now.

# Task
# Your job is simple, if x squared is more than 1000, return It's hotter than 
# the sun!!, else, return Help yourself to a honeycomb Yorkie for the glovebox.

# Note: Input will either be a positive integer (or a string for untyped languages).

# -------------------------------------------------------------------------------------
# -----Solution 1----Ternary Operator-----
def apple(x):
  return "It's hotter than the sun!!" if int(x) ** 2 > 1000 else  "Help yourself to a honeycomb Yorkie for the glovebox."
#   1.  The () takes one argument, `x`, as input.
#   2.  It uses a conditional statement to check if the square of `x` is greater than 1000.
#   3.  If the square of `x` is greater than 1000, the () returns "It's hotter than the sun!!". Otherwise, it returns
#       "Help yourself to a honeycomb Yorkie for the glovebox."
#   4.  This solution has a time complexity of O(1) because the () performs a constant number of operations & a space complexity
#       of O(1) because the () uses a constant amount of extra space.

# -------------------------------------------------------------------------------------
# -----Solution 2----Simple If-Else Statement-----
def apple(x):
    if int(x)**2 > 1000:
        return "It's hotter than the sun!!"
    else:
        return "Help yourself to a honeycomb Yorkie for the glovebox."
#   This solution is similar to Solution 1. It uses an if-else statement to check if the square of `x` is greater than 1000.
#   If the square of `x` is greater than 1000, the () returns "It's hotter than the sun!!". Otherwise, it returns
#   "Help yourself to a honeycomb Yorkie for the glovebox."
#   Compared to solution 1, this solution has the same time & space complexity, but is
#   easier to read & understand.

# -------------------------------------------------------------------------------------
# -----Solution 3----
def apple(x):
    if int(x) > 31:
        return "It's hotter than the sun!!" 
    else:
        return "Help yourself to a honeycomb Yorkie for the glovebox."
#   This solution is similar to Solution 2. It uses an if-else statement to check if `x` is greater than 31.
#   If `x` is greater than 31, the () returns "It's hotter
#   than the sun!!". Otherwise, it returns "Help yourself to a honeycomb Yorkie for the glovebox."
#   Compared to the first two solutions, this solution has a different condition to check if the square of `x` is greater than 1000.
#   This solution has the same time & space complexity as the previous solutions.