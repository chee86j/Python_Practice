# Two tortoises named A and B must run a race. A starts with an average 
# speed of 720 feet per hour. Young B knows she runs faster than A, and 
# furthermore has not finished her cabbage.

# When she starts, at last, she can see that A has a 70 feet lead but B's 
# speed is 850 feet per hour. How long will it take B to catch A?

# More generally: given two speeds v1 (A's speed, integer > 0) and v2 
# (B's speed, integer > 0) and a lead g (integer > 0) how long will 
#  it take B to catch A?

# The result will be an array [hour, min, sec] which is the time needed 
# in hours, minutes and seconds (round down to the nearest second) or a 
# string in some languages.

# If v1 >= v2 then return nil, nothing, null, None or {-1, -1, -1} for 
# C++, C, Go, Nim, Pascal, COBOL, Erlang, [-1, -1, -1] for Perl,[] for 
# Kotlin or "-1 -1 -1" for others.

# Examples:
# (form of the result depends on the language)

#----- race(720, 850, 70) => [0, 32, 18] or "0 32 18" -----
#----- race(80, 91, 37)   => [3, 21, 49] or "3 21 49" -----

# Note:
# See other examples in "Your test cases".

# In Fortran - as in any other language - the returned string is not 
# permitted to contain any redundant trailing whitespace: you can use 
# dynamically allocated character strings.

# ** Hints for people who don't know how to convert to hours, minutes, seconds:

# Tortoises don't care about fractions of seconds
# Think of calculation by hand using only integers (in your code use or 
# simulate integer division) or Google: "convert decimal time to hours minutes seconds"


# -------------------------------------------------------------------------------------
# -----Solution 1-----Direct Calculation w/Manual Time Conversion-----
def race(v1, v2, g):
    if v1 >= v2:
        return None
    time = g / (v2 - v1)
    hours = int(time)
    minutes = int((time * 60) % 60)
    seconds = int((time * 3600) % 60)
    return [hours, minutes, seconds]
#   This method directly calculates the time using basic arithmetic operations & floor
#   division w/o using any external libraries tp avoid decimals.
#   1. Check if v1 is greater than or equal to v2, return None if true.
#   2. Calculate the time it takes for B to catch A using the formula `g / (v2 - v1)`.
#   3. Extract the hours, minutes, & seconds from the time using integer division & modulo.
#   4. Return the time as an array [hours, minutes, seconds].

#   Time complexity is O(1) because the calculations are done in constant time &
#   space complexity is O(1) because the array returned is of fixed size.
        

# -------------------------------------------------------------------------------------
# -----Solution 2-----Calculations & Conditional Return-----
def race(v1, v2, g):
    t = 3600 * g/(v2-v1)
    return [t/3600, t/60%60, t%60] if v2 > v1 else None
#   This solution is similar to the first solution, but it uses a conditional return statement
#   to calculate the time & return it as an array in a single line.
#   1. Calculate the time t using the formula `3600 * g/(v2-v1)`.
#   2. Return the time as an array [t/3600, t/60%60, t%60] if v2 is greater than v1, otherwise return None.

#   Time complexity is O(1) because the calculations are done in constant time &
#   space complexity is O(1) because the array returned is of fixed size.


# -------------------------------------------------------------------------------------
# -----Solution 3-----Datetime & Timedelta-----
from datetime import datetime, timedelta

def race(v1, v2, g):
    if v1 >= v2:
        return None
    else:
        sec = timedelta(seconds=int((g*3600/(v2-v1))))
        d = datetime(1,1,1) + sec
        
        return [d.hour, d.minute, d.second]
#   This solution uses the datetime & timedelta classes from the datetime module to calculate the time.
#   1. Check if v1 is greater than or equal to v2, return None if true.
#   2. Calculate the time in seconds using the formula `g*3600/(v2-v1)`.
#   3. Create a timedelta object sec with the calculated seconds, which is then converted to a datetime object d.
#   4. Extract the hours, minutes, & seconds from the datetime object d & return them as an array.

#   Time complexity is O(1) because the calculations are done in constant time &
#   space complexity is O(1) because the array returned is of fixed size.
#   Note: This solution fails when hours are greater than 24.
        
# -------------------------------------------------------------------------------------
# -----Solution 3-----JavaScript Solution-----Calculations & Conditional Return-----
# function race(v1, v2, g){
#   let time=g/(v2-v1);
#   return v2>v1 ? [Math.floor(time),Math.floor(time*60%60),Math.floor(time*3600%60)] : null;
# }
#   This solution is similar to the second Python solution, using a conditional return statement
#   to calculate the time & return it as an array in a single line.
#   1. Calculate the time using the formula `g/(v2-v1)`.
#   2. Return the time as an array [Math.floor(time),Math.floor(time*60%60),Math.floor(time*3600%60)]
#   if v2 is greater than v1, otherwise return null.

#   This solution is concise & easy to understand, using the Math.floor function to round down
#   the time to the nearest integer. The time complexity is O(1) because the calculations are done
#   in constant time & space complexity is O(1) because the array returned is of fixed size.