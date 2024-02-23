# DESCRIPTION:
# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

# Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

# Note: The function accepts an integer and returns an integer.

# Happy Coding!

# -------------------------------------------------------------------------------------
# -----Solution 1-----
def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)
    # 1. set ret as an empty string
    # 2. iterate through each digit in number
    # 3. convert each digit to an integer and square it
    # 4. convert squared digit to a string and add to ret
    # 5. convert ret to an integer and return result
    
# -------------------------------------------------------------------------------------
# -----Solution 2-----
def square_digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))
    # 1. iterate through each digit in number
    # 2. convert each digit to an integer and square it
    # 3. join squared digits into a single string
    # 4. convert string to an integer and return result