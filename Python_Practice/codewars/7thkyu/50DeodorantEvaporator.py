# Description:
# This program tests the life of an evaporator containing a gas.

# We know the content of the evaporator (content in ml), the percentage of foam or 
# gas lost every day (evap_per_day) and the threshold (threshold) in percentage beyond 
# which the evaporator is no longer useful. All numbers are strictly positive.

# The program reports the nth day (as an integer) on which the evaporator will be out of use.

# Example:
# evaporator(10, 10, 5) -> 29

# Note:
# Content is in fact not necessary in the body of the function "evaporator", you can use 
# it or not use it, as you wish. Some people might prefer to reason with content, some 
# other with percentages only. It's up to you but you must keep it as a parameter because 
# the tests have it as an argument.

# My Notes:
# The evaporator's content decreases at a percentage rate each day, whoch is a classic
# case of exponential decay.
# ----- We know the content decreases by a certain percentage each day and we want to find out
#       how many days it will take for the content to reach a certain threshold.
# ----- Instead of simulating each day, we can use a mathematical formula to calculate the
#       number of days directly by using logarithms to directly calculate the number of days it
#       will take for the content to reach the threshold.

# -------------------------------------------------------------------------------------
# -----Solution 1-----Iterative Reduction-----
def evaporator(content, evap_per_day, threshold):
    n = 0
    current = 100
    percent = 1 - evap_per_day / 100.0
    while current > threshold:
        current *= percent
        n += 1
    return n
#   1.  n is the number of days the evaporator will last before it is no longer useful.
#   2.  current is the current percentage of the evaporator's content.
#   3.  percent is the percentage of the evaporator's content that is lost each day.
#   4.  The while loop continues until the current percentage is less than the threshold.
#   5.  The current percentage is multiplied by the percentage lost each day.
#       which then becomes the new current percentage. 
#   6.  n is incremented by 1 each iteration.

#   This solution simulates each day by reducing the current content by the evaporation
#   rate (evap_per_day) until the content is less than the threshold. It then returns the
#   number of days it took to reach that point. It is the most simple & easy to understand
#   w/o using any mathematical formulas.

#   The time complexity of this solution is O(n) where n is the number of days it takes
#   for the content to reach the threshold. The space complexity is O(1) since the only
#   variables used are n, current, & percent.

# -------------------------------------------------------------------------------------
# -----Solution 2-----Mathematical Approach w/ math.ceil-----
import math

def evaporator(content, evap_per_day, threshold):
	return math.ceil(math.log(threshold / 100.0) / math.log(1.0 - evap_per_day / 100.0))
#   1.  The formula for the number of days it takes for the evaporator to reach the threshold
#       is log(threshold/100) / log(1-evap_per_day/100).
#   2.  math.ceil is used to round up to the nearest whole number.

#   This solution uses the logarithmic relatition to calculate the number of days in a single
#   expression. It finds the day when the content percentage first drops below the threshold
#   using the formula `log(threshold/100) / log(1-evap_per_day/100)` (exponential decay formula).
#   This solition is more efficient than the iterative solution since it only requires a single
#   mathematical expression. It is usefule when using large datasets or when `n` is very large.

#   The time complexity of this solution is O(1) since it only uses a single mathematical expression.
#   The space complexity is also O(1) since the only variables used are the input parameters.

# -------------------------------------------------------------------------------------
# -----Solution 3-----Mathematical Approach w/ math.ceil & math.log-----
from math import log,ceil

def evaporator(content, evap_per_day, threshold):
    return ceil(log(threshold/100,1-evap_per_day/100))
#   This solution is similar to the previous solution, but it uses the `log` function with a base
#   parameter to calculate the number of days. It then uses `ceil` to round up to the nearest whole
#   number. It is simpler to understand for those who familiar with logarithms.

#   It avoids loops which makes it less expensive in terms of time complexity. It is also more
#   efficient than the iterative solution since it only requires a single mathematical expression.
#   It has a space complexity of O(1) since the only variables used are the input parameters &
#   a time complexity of O(1) since it only uses a single mathematical expression.

# -------------------------------------------------------------------------------------
# -----Solution 4-----Javascript Solution-----
# function evaporator(content, evap_per_day, threshold){ 
# var days = 0;
# var gas = 100;
#   while(gas >= threshold){
#     gas -= gas * evap_per_day / 100;
#     days++;
# }
#   return days;
# }

#  This Javascript solution is similar to the first solution in Python. It uses a while loop to
#  simulate each day by reducing the current content by the evaporation rate until the content
#  is less than the threshold. It then returns the number of days it took to reach that point.

#  It is best suited for smaller datasets or when the number of days is relatively small. It has
#  a time complexity of O(n) where n is the number of days it takes for the content to reach the
#  threshold & a space complexity of O(1) since the only variables used are days, gas, & the
#  input parameters.