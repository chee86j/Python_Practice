# You live in the city of Cartesia where all roads are laid 
# out in a perfect grid. You arrived ten minutes too early 
# to an appointment, so you decided to take the opportunity 
# to go for a short walk. The city provides its citizens with 
# a Walk Generating App on their phones -- everytime you press 
# the button it sends you an array of one-letter strings 
# representing directions to walk (eg. ['n', 's', 'w', 'e']). 
# You always walk only a single block for each letter 
# (direction) and you know it takes you one minute to traverse 
# one city block, so create a function that will return true 
# if the walk the app gives you will take you exactly ten 
# minutes (you don't want to be early or late!) and will, 
# of course, return you to your starting point. 
# Return false otherwise.

# Note: you will always receive a valid array containing a 
# random assortment of direction letters ('n', 's', 'e', or 
# 'w' only). It will never give you an empty array (that's 
# not a walk, that's standing still!).

# -------------------------------------------------------------------------------------
# -----Solution 1-----One-Liner w/ Count-----
def is_valid_walk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')
#   1.  Return True if length of walk is equal to 10 and count of 'n' is equal 
#       to count of 's' and count of 'e' is equal to count of 'w'.
#   2.  Return False otherwise.

# -------------------------------------------------------------------------------------
# -----Solution 2-----If/Else-----
def isValidWalk(walk):
    if len(walk) != 10:
        return False

    x, y = 0, 0

    for direction in walk:
        if direction == 'n':
            y += 1
        elif direction == 's':
            y -= 1
        elif direction == 'e':
            x += 1
        elif direction == 'w':
            x -= 1
        else:
            return False

    return x == 0 and y == 0
#   1.  If length of walk is not equal to 10, return False.
#   2.  Create two variables x and y and set them equal to 0.
#   3.  Create a for loop to iterate over each direction in walk.
#   4.  If direction is equal to 'n', add 1 to y.
#   5.  If direction is equal to 's', subtract 1 from y.
#   6.  If direction is equal to 'e', add 1 to x.
#   7.  If direction is equal to 'w', subtract 1 from x.
#   8.  If direction is not equal to any of above, return False.
#   9.  Return True if x is equal to 0 and y is equal to 0.
#   10. Return False otherwise.