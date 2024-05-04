# Jamie is a programmer, and James' girlfriend. She likes diamonds, 
# and wants a diamond string from James. Since James doesn't know 
# how to make this happen, he needs your help.

# Task
# You need to return a string that looks like a diamond shape when 
# printed on the screen, using asterisk (*) characters. Trailing 
# spaces should be removed, and every line must be terminated with 
# a newline character (\n).

# Return null/nil/None/... if the input is an even number or negative, 
# as it is not possible to print a diamond of even or negative size.

# Examples
# A size 3 diamond:

#  *
# ***
#  *
# ...which would appear as a string of " *\n***\n *\n"

# A size 5 diamond:

#   *
#  ***
# *****
#  ***
#   *
# ...that is:

# "  *\n ***\n*****\n ***\n  *\n

# -------------------------------------------------------------------------------------
# -----Solution 1-----If-Else, While Loop, & String Concatenation-----
def diamond(n):
    if n < 0 or n % 2 == 0:
        return None
    
    result = "*" * n + "\n";
    spaces = 1;
    n = n - 2
    while n > 0:
        current = " " * spaces + "*" * n + "\n"
        spaces = spaces + 1
        n = n - 2
        result = current + result + current
    
    return result
#   1. If n is less than 0 or n is even, return None
#   2. Set result with n number of '*' and a newline character
#   3. Set spaces with 1 and n with n - 2
#   4. While n is greater than 0, do the following
#       a. Create a var current with spaces number of spaces and n number of '*' and a newline character
#       b. Increment spaces by 1
#       c. Decrement n by 2
#       d. Update result with current + result + current
#   5. Return result
#   This solution is more efficient than Solution 2 below because it uses a while loop instead of two for loops

# -------------------------------------------------------------------------------------
# -----Solution 2-----If-Else, For Loop, & String Concatenation-----
def diamond(n):
    if n % 2 == 0 or n < 0:
        return None
    diamond = ''
    for i in range(1, n+1, 2):
        diamond += ' ' * ((n-i)//2) + '*' * i + '\n'
    for i in range(n-2, 0, -2):
        diamond += ' ' * ((n-i)//2) + '*' * i + '\n'
    return diamond
#   1. If n is even or n is less than 0, return None
#   2. Set diamond with an empty string
#   3. Loop through range of 1 to n+1 with a step of 2
#       a. Update diamond with (n-i)//2 number of spaces and i number of '*' and a newline character
#   4. Loop through range of n-2 to 0 with a step of -2
#       a. Update diamond with (n-i)//2 number of spaces and i number of '*' and a newline character
#   5. Return diamond
#   This solution uses two for loops to create diamond shape compared to Solution 1 above which uses a while loop
