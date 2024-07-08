# Complete the function which converts a binary number 
# (given as a string) to a decimal number.

# -------------------------------------------------------------------------------------
# -----Solution 1-----Int-----
def bin_to_decimal(inp):
    return int(inp, 2)

#   1. The function takes in a binary number as a string. For example, '1101'.
#   2. Using the int method, the binary number is converted to a decimal number by
#      passing the binary number and 2 as arguments. The 2 represents the base of the binary number.
#   3. The decimal number is then returned. In the case of the example, the decimal number is 13.

# -------------------------------------------------------------------------------------
# -----Solution 2-----Int & Slicing using For Loop-----
def bin_to_decimal(inp):
    num = 0
    inp = inp[::-1]
    for i in range(len(inp)):
        num += int(inp[i]) * 2 ** i
    return num
#   1. The function takes in a binary number as a string. For example, '1101'.
#   2. The binary number is reversed using the slicing technique. For example, '1011'.
#   3. The variable num is initialized to 0.
#   4. A for loop is used to iterate through the reversed binary number.
#   5. In each iteration, the integer value of the binary digit is multiplied by 2 raised to the power of the index.
#   6. The result of the multiplication is added to the num variable.
#   7. After the loop is completed, the decimal number is returned. In the case of the example, the decimal number is 13.

# -------------------------------------------------------------------------------------
# -----Solution 3-----Javascript Solution-----parseInt-----
# function binToDec(bin){
#     return parseInt(bin, 2);
# }

# 1. The function takes in a binary number as a string. For example, '1101'.
# 2. Using the parseInt method, the binary number is converted to a decimal number by
#    passing the binary number and 2 as arguments. The 2 represents the base of the binary number.
# 3. The decimal number is then returned. In the case of the example, the decimal number is 13.