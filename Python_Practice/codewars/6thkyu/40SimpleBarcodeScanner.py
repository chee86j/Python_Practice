# Many items that are available for sale have a barcode somewhere on them - 
# this allows them to be scanned at a checkout.

# Your task is to create an algorithm to convert a series of ones and
# zeroes from the scanner into an Universal Product Code (UPC). You can 
# learn more about UPC from Wikipedia. We will be using the UPC-A formatting.
# Specifications

# Each barcode follows the pattern: SLLLLLLMRRRRRRE

# S, M and E are guard bars (start, middle, end). These are constants.

# L and R are digits. They are 7 modules wide and are variables. They can 
# be of 1 of 10 patterns.

# Each item is described using the pattern below. The number indicates how 
# many modules wide, the letter is the colour of the bar: W for white and 
# B for black.

# The guard bars:

# S: 1B1W1B
# M: 1W1B1W1B1W
# E: 1B1W1B

# These are the L digits:

# 0: 3W2B1W1B
# 1: 2W2B2W1B
# 2: 2W1B2W2B
# 3: 1W4B1W1B
# 4: 1W1B3W2B
# 5: 1W2B3W1B    
# 6: 1W1B1W4B
# 7: 1W3B1W2B
# 8: 1W2B1W3B
# 9: 3W1B1W2B

# You will be provided with a preloaded dictionary DIGITS which contains 
# the above information (L digits and guard bar patterns).

# R digits are the inverse of L digits, e.g.:

# 0: 3B2W1B1W

# Your task

# Your function will receive a string consisting of ones (black) and 
# zeroes (white), and should return the UPC as a string. Each one or 
# zero will correspond to one module of width. Only valid barcodes 
# will be supplied, and they will always be presented from left to right. 
# They will start with the first black line of the guard bars.
# Example

# barcode_scanner("10101110110110111000101100010110101111011011101010111001011100101110010111001011011001000010101")
# => "789968000023"

# because:
# "101 0111011 0110111 0001011 0001011 0101111 0110111 01010 1110010 1110010 1110010 1110010 1101100 1000010 101"
# " S     7       8       9       9       6       8      M      0       0       0       0       2       3     E "

# -------------------------------------------------------------------------------------
# -----Solution 1-----Dictionary-----
import re

L_DIGITS = {
"0001101": "0",
"0011001": "1",
"0010011": "2",
"0111101": "3",
"0100011": "4",
"0110001": "5",	
"0101111": "6",
"0111011": "7",
"0110111": "8",
"0001011": "9"}

def barcode_scanner(barcode):
    leftized = barcode[3:45] + barcode[50:-3].translate(str.maketrans("01","10"))
    return re.sub('|'.join(L_DIGITS.keys()), lambda m: L_DIGITS[m.group(0)], leftized)

#   1. We are creating a dictionary 'L_DIGITS' that maps the L digits to the corresponding number
#   2. 'leftized' is the left side of the barcode excluding the guard bars and the middle guard bar
#   3. We are replacing the 0s with 1s and 1s with 0s in the right side of the barcode
#   4. We are using the re.sub() method to replace the L digits with the corresponding number
#   5. The re.sub() method replaces the matched pattern with the value returned by the lambda function
#   6. The lambda function returns the value of the matched pattern from the dictionary 'L_DIGITS'
#   7. The time complexity of this solution is O(1) as we are using a dictionary to store the L digits
#   8. The space complexity of this solution is O(1) as we are storing the L digits in a dictionary

#   To reiterate, we handle the guard bars first by removing them from the barcode. We separate them
#   the start, middle, and end guard bars from the rest of the barcode. Next we Invert the R-digits- the
#   str.maketrans and translate functions correctly transform R-digits into a format recognizable by L_DIGITS.
#   Regex is use to improve efficiency-The re.sub function processes the entire string efficiently, replacing 
#   all 7-bit patterns in a single pass. To handle all edge cases re.sub processes the string based on 
#   patterns, it doesn't rely on manual chunking or iteration.


# -------------------------------------------------------------------------------------
# -----Solution 1-----Dictionary & For Loop-----
L_DIGITS = {
    "0001101": "0",
    "0011001": "1",
    "0010011": "2",
    "0111101": "3",
    "0100011": "4",
    "0110001": "5",	
    "0101111": "6",
    "0111011": "7",
    "0110111": "8",
    "0001011": "9"
}

def barcode_scanner(barcode):
    # Extract left-side and right-side barcodes, remove guard bars, and invert R-digits
    left_digits = barcode[3:45]
    right_digits = barcode[50:-3].translate(str.maketrans("01", "10"))
    
    # Combine the left and right sections
    combined_digits = left_digits + right_digits
    
    # Decode each 7-bit chunk manually
    decoded = []
    for i in range(0, len(combined_digits), 7):
        chunk = combined_digits[i:i+7]
        decoded.append(L_DIGITS[chunk])  # Lookup the corresponding digit
    
    # Join all decoded digits into a single string
    return ''.join(decoded)

#   1. Start by creating a dictionary 'L_DIGITS' that maps the L digits to the corresponding number
#   2. Then, extract the left and right side of the barcode, remove the guard bars, and invert the R-digits
#   3. Combine the left and right sections to form the complete barcode
#   4. Decode each 7-bit chunk manually using a for loop
#   5. Lookup the corresponding digit from the dictionary 'L_DIGITS' for each chunk
#   6. Join all decoded digits into a single string and return the result
#   7. The time complexity of this solution is O(n) as we iterate through the barcode string
#   8. The space complexity of this solution is O(1) as we are storing the L digits in a dictionary
