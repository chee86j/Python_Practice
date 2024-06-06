# A child is playing with a ball on the nth floor of a tall building. 
# The height of this floor above ground level, h, is known.

# He drops the ball out of the window. The ball bounces (for example), 
# to two-thirds of its height (a bounce of 0.66).

# His mother looks out of a window 1.5 meters from the ground.

# How many times will the mother see the ball pass in front of her 
# window (including when it's falling and bouncing)?

# Three conditions must be met for a valid experiment:
# Float parameter "h" in meters must be greater than 0
# Float parameter "bounce" must be greater than 0 and less than 1
# Float parameter "window" must be less than h.
# If all three conditions above are fulfilled, return a positive integer, 
# otherwise return -1.

# Note:
# The ball can only be seen if the height of the rebounding ball is 
# strictly greater than the window parameter.

# Examples:
# - h = 3, bounce = 0.66, window = 1.5, result is 3

# - h = 3, bounce = 1, window = 1.5, result is -1 

# (Condition 2) not fulfilled).

# -------------------------------------------------------------------------------------
# -----Solution 1-----If & While Loop-----
def bouncingBall(h, bounce, window):
    if not 0 < bounce < 1: return -1
    count = 0
    while h > window:
        count += 1
        h *= bounce
        if h > window: count += 1
    return count or -1
#   1.  Check if bounce is greater than 0 and less than 1
#   2.  Return -1 if bounce is not within range
#   3.  Create a variable to store number of times ball passes window
#   4.  While height is greater than window, increment count by 1
#   5.  Multiply height by bounce
#   6.  Check if height is greater than window
#   7.  Increment count by 1 if height is greater than window
#   8.  Return count if count is greater than 0, else return -1

# -------------------------------------------------------------------------------------
# -----Solution 2-----
def bouncingBall(h, bounce, window):
    seen = -1
    
    if 0 < bounce < 1:
        while h > window > 0:
            seen += 2
            h *= bounce
    
    return seen
#   1.  Create a variable to store number of times ball passes window
#   2.  Check if bounce is greater than 0 and less than 1
#   3.  While height is greater than window, increment seen by 2
#   4.  Multiply height by bounce
#   5.  Return number of times ball passes window

# -------------------------------------------------------------------------------------
# -----Solution 3-----Javascript Solution-----
# function bouncingBall(h,  bounce,  window) {
#   var rebounds = -1;
#   if (bounce > 0 && bounce < 1) while (h > window) rebounds+=2, h *= bounce;
#   return rebounds;
# }

#  1.  Create a variable to store number of rebounds
#  2.  Check if bounce is greater than 0 and less than 1
#  3.  While height is greater than window, increment rebounds by 2
#  4.  Multiply height by bounce
#  5.  Return number of rebounds
