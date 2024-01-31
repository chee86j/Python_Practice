# DESCRIPTION:
# Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

# The binary number returned should be a string.

# Examples:(Input1, Input2 --> Output (explanation)))

# 1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
# 5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)

# -------------------------------------------------------------------------------------
# -----Solution 1-----Bin Function-----
def add_binary(a,b):
    return bin(a + b)[2:]
    # If a = 1 and b = 1, then a + b = 2.
    # bin() is a built-in function that converts an integer to binary. bin(2) returns '0b10'.
    # The [2:] is used to remove the first two characters of the binary number leaving only the binary number, '10'.

# -------------------------------------------------------------------------------------
# -----Solution 2-----Format Function w/ Binary Specifier-----
def add_binary(a,b):
    return "{0:b}".format(a + b)
    # If a = 1 and b = 1, then a + b = 2.
    # The {0:b} is a placeholder that is replaced by the binary number. 
    # The format() function is used to insert the binary number into the placeholder.

# -------------------------------------------------------------------------------------
# -----Solution 3-----Format Function-----
def add_binary(a,b):
    return format(a + b, 'b')
    # If a = 1 and b = 1, then a + b = 2.
    # The 'b' is a format specifier that tells the format() function to convert the number to binary.
    # It is similar to the :b in solution 4. 

# -------------------------------------------------------------------------------------
# -----Solution 4-----String Literal w/ Binary Specifier-----
def add_binary(a,b):
    return f'{a + b:b}'
    # If a = 1 and b = 1, then a + b = 2.
    # The f-string is a string literal that is prefixed with f.
    # ThE :b is a format specifier that tells the f-string to convert the number to binary.

# -------------------------------------------------------------------------------------
# -----Solution 5-----Binary Conversion separated into two variables-----
def add_binary(a,b):
    sum_decimal = a + b
    sum_binary = bin(sum_decimal)[2:]
    return sum_binary
    # If a = 1 and b = 1, then a + b = 2.
    # This solution is similar to solution 1, but it uses two variables to make the code easier to understand.
    # The first variable, sum_decimal, stores the sum of the two numbers in decimal.
    # The second variable, sum_binary, stores the binary conversion of the sum.