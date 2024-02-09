# DESCRIPTION:
# In this little assignment you are given a string of space separated numbers, and 
# have to return the highest and lowest number.

# Examples
# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"
# Notes
# All numbers are valid Int32, no need to validate them.
# There will always be at least one number in the input string.
# Output string must be two numbers separated by a single space, and highest number 
# is first.

# -------------------------------------------------------------------------------------
# -----Solution 1-----Loop w/ format specifier %i and max & min built-in functions-----
def high_and_low(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]   
    return "%i %i" % (max(nn),min(nn))          
    # 1. split input str into individual nums & convert to int
    # 2. return the highest and lowest numbers as a string separated by a space
    #    using the %i format specifier to insert the values of max(nn) and min(nn) into the string
    #    %i is used to format an integer number by inserting the number into the string and returning the result
    #    max & min are built-in functions that return the highest and lowest numbers in a list, respectively

# -------------------------------------------------------------------------------------
# -----Solution 2-----Loop w/ f-string and max & min built-in functions-----
def high_and_low(numbers):
  numbers = [int(c) for c in numbers.split(' ')]
  return f"{max(numbers)} {min(numbers)}"
  # 1. split input str into individual nums & convert to int
  # 2. return the highest and lowest numbers as a string separated by a space

# -------------------------------------------------------------------------------------
# -----Solution 3-----Sorted w/ key=int-----
def high_and_low(numbers):
    nums = sorted(numbers.split(), key=int)
    return '{} {}'.format(nums[-1], nums[0])
    # 1. split input str into individual nums & sort them in ascending order
    #    using the key=int argument to sort the numbers as integers by converting them to int
    #    key is a function that is used to sort the numbers in the list
    # 2. return the highest and lowest numbers as a string separated by a space

# -------------------------------------------------------------------------------------
# -----Solution 4-----Single Line w/ max & min built-in functions-----
def high_and_low(numbers):
    return " ".join(x(numbers.split(), key=int) for x in (max, min))
    # 1. split input str into individual nums & convert to int
    # 2. return the highest and lowest numbers as a string separated by a space
    #    using the join method to join the results of the max and min functions into a single string

# -------------------------------------------------------------------------------------
# -----Solution 5-----
def high_and_low(numbers):
    num_list = list(map(int, numbers.split()))
    highest = max(num_list)
    lowest = min(num_list)
    
    return f"{highest} {lowest}"
    # 1. split input str into individual numbers
    # 2. find highest and lowest numbers using max() & min() functions
    # 3. return highest and lowest numbers as a str separated by a space