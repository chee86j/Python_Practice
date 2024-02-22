# DESCRIPTION:
# Your function takes two arguments:

# current father's age (years)
# current age of his son (years)
# Сalculate how many years ago the father was twice as old as his son 
# (or in how many years he will be twice as old). The answer is always 
# greater or equal to 0, no matter if it was in the past or it is in the future.

# -------------------------------------------------------------------------------------
# -----Solution 1-----Absolute difference-----
def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old - 2 * son_years_old)
    # 1. return absolute difference between father's age & twice son's age
    #    using abs function to return absolute value of difference
    
# -------------------------------------------------------------------------------------
# -----Solution 2-----If/else While-----
def twice_as_old(d, s):
    count = 0
    if s == 0:
        return d
    elif d / s > 2:
        while s * 2 != d:
            d += 1
            s += 1
            count += 1
        return count
    elif d / s < 2:
        while s * 2 != d:
            d -= 1
            s -= 1
            count += 1
        return count
    else:
        return 0
    # 1. create a count variable to keep track of number of years
    # 2. if son's age is 0, return father's age
    # 3. else if father's age divided by son's age is greater than 2
    #    iterate through while loop until father's age is twice son's age
    #    increment count by 1 each iteration
    #    return count
    # 4. else if father's age divided by son's age is less than 2
    #    iterate through while loop until father's age is twice son's age
    #    decrement count by 1 each iteration
    #    return count
    # 5. else return 0
    
    
    