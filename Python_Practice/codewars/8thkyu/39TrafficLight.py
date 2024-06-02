# You're writing code to control your town's traffic lights. 
# You need a function to handle each change from green, 
# to yellow, to red, and then to green again.

# Complete the function that takes a string as an argument 
# representing the current state of the light and returns a 
# string representing the state the light should change to.

# For example, when the input is green, output should be yellow.

# -------------------------------------------------------------------------------------
# -----Solution 1-----Single Line Dictionary-----
def update_light(current):
    return {"green": "yellow", "yellow": "red", "red": "green"}[current]
#   1.  Return value of key current in dictionary
#   2.  Dictionary contains key value pairs of current light and next light

# -------------------------------------------------------------------------------------
# -----Solution 2-----If Elif Else-----
def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    elif current == "red":
        return "green"
    else:
        return "This is not a traffic light color."
#   1.  Check if current is green & return yellow if true
#   2.  Check if current is yellow & return red if true
#   3.  Check if current is red & return green if true
#   4.  Return error message if current is not a traffic light color
