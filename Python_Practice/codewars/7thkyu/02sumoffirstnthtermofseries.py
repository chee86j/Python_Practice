# Description:
# Task:

# Your task is to write a function which returns the sum of following series upto nth term(parameter).

# Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...

# Rules:

#     You need to round the answer to 2 decimal places and return it as String.

#     If the given value is 0 then it should return 0.00

#     You will only be given Natural Numbers as arguments.

# Examples:(Input --> Output)

# 1 --> 1 --> "1.00"
# 2 --> 1 + 1/4 --> "1.25"
# 5 --> 1 + 1/4 + 1/7 + 1/10 + 1/13 --> "1.57"

# -------------------------------------------------------------------------------------
# -----Solution 1-----Using a Generator Expression-----
def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))
    # {:.2f}.format formats the sum to 2 decimal places
    # we then calculate the sum of the series using a generator expression
    # the generator expression calculates the sum of the series using the formula 1.0/(3 * i + 1) for i in range(n)
    
    # Examples:
    # if n = 5, the generator expression will calculate 1.0/(3 * 0 + 1) + 1.0/(3 * 1 + 1) + 1.0/(3 * 2 + 1) + 1.0/(3 * 3 + 1) + 1.0/(3 * 4 + 1) resulting in 1.57
    
    # if n = 3, the generator expression will calculate 1.0/(3 * 0 + 1) + 1.0/(3 * 1 + 1) + 1.0/(3 * 2 + 1) resulting in 1.39
    
# -------------------------------------------------------------------------------------
# -----Solution 2-----Using a Generator Expression w/ Float-----
def series_sum(n):
    sum = 0.0
    for i in range(0,n):
        sum += 1 / (1 + 3 * float(i))
    return '%.2f' % sum 
    # sum is initialized to 0.0
    # we then calculate the sum of the series using a for loop
    # the for loop calculates the sum of the series using the formula 1 / (1 + 3 * float(i)) for i in range(n)
    # finally, we return the sum rounded to 2 decimal places using '%.2f' % sum
    
    # Examples:
    # if n = 2, the for loop will calculate 1 / (1 + 3 * 0) + 1 / (1 + 3 * 1) resulting in 1.25