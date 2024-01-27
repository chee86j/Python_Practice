# Description:

# Our football team has finished the championship.

# Our team's match results are recorded in a collection of strings. Each match is represented by a string in the format "x:y", where x is our team's score and y is our opponents score.

# For example: ["3:1", "2:2", "0:1", ...]

# Points are awarded for each match as follows:

#     if x > y: 3 points (win)
#     if x < y: 0 points (loss)
#     if x = y: 1 point (tie)

# We need to write a function that takes this collection and returns the number of points our team (x) got in the championship by the rules given above.

# Notes:

#     our team always plays 10 matches in the championship
#     0 <= x <= 4
#     0 <= y <= 4

# -------------------------------------------------------------------------------------
# -----Solution 1-----Ternary Operator-----
def points(a):
    return sum((x >= y) + 2 * (x > y) for x, y in (s.split(":") for s in a))
    # we use the sum() function to add up the points and for x, y in (s.split(":") for s in a) 
    # to iterate through the list of strings and split them into x and y values

# -------------------------------------------------------------------------------------
# -----Solution 2-----Modulo Operator-----
def points(games):
    total_points = 0
    
    for game in games:
        x, y = map(int, game.split(':'))
        # the way the above line works is that it splits the string into x and y values
        # then maps the int() function to each of the values
        # then assigns the values to x and y respectively
        if x > y:
            total_points += 3
        elif x < y:
            total_points += 0
        else:
            total_points += 1
        
    return total_points
    
    