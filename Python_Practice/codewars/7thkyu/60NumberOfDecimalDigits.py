# Determine the total number of digits in the integer (n>=0) 
# given as input to the function. For example, 9 is a single 
# digit, 66 has 2 digits and 128685 has 6 digits. Be careful 
# to avoid overflows/underflows.

# All inputs will be valid.

# -------------------------------------------------------------------------------------
# -----Solution 1-----
def digits(n):
    return len(str(n))

# -------------------------------------------------------------------------------------
# -----Solution 2-----
def digits(n):
    digits = 1
    while n // 10 > 0:
        n //= 10
        digits += 1
    
    return digits

# -------------------------------------------------------------------------------------
# -----Solution 3-----Javascript Solution-----
# function digits(n) {
#     return n.toString().length;
# }