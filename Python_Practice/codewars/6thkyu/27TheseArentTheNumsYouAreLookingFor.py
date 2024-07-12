# You should find a searched number by approximation.

# The searched number will always be between 0 and 100.

# You have to write a method, that will get only a function 
# to compare your guess number with the searched number.
# Your method have to find the number with a precision of 5 
# fractional digits.
# The tolerance for the value: The difference from the 
# searched number must be smaller than 0.00002.

# The compare-function, that your method will get as 
# parameter, takes the guessed number as parameter and 
# returns 0 for the correct number, -1 if your number is 
# smaller than the searched number and 1 if your guessed 
# number is greater than the searched number.

# Example:
# Searched number: 6

# Compare(1); -> -1
# Compare(10); -> 1
# Compare(6); -> 0

# You do not need a Compare-Call, that returns 0. If your 
# number has a precision of 5 fractional digits, and you 
# are sure, it is the searched number, you can return the 
# number.

# You will always get the compare-method! So there is no 
# need for a check for null.

# -------------------------------------------------------------------------------------
# -----Solution 1-----Comparison Function & Binary Search & If/Else-----
def find_number(compare, lo=0, hi=100, tolerance=1e-5):
    mid = None
    while hi - lo > tolerance:
        mid = (lo + hi) / 2
        if compare(mid) == 0: return mid
        if compare(mid) < 0: lo = mid
        else: hi = mid
    return mid

#  1. The function find_number takes in 4 parameters: compare (comparison function), lo (lower bound), hi (upper bound), and tolerance (desired precision).
#  2. Initialize mid to None.
#  3. Use a while loop to approximate the searched number within the given tolerance.
#  4. Inside the loop:
#     - Calculate mid as the average of lo and hi.
#     - Use compare(mid) to determine the relationship between mid and the searched number:
#       - Return mid if compare(mid) returns 0, indicating mid is the searched number.
#       - Adjust lo or hi based on whether mid is smaller or larger than the searched number.
#  5. Once the loop exits, return mid, which approximates the searched number within the specified tolerance.

#   Example usage:
#   - Searched number: 6
#   - If compare(1) returns -1 (indicating 1 is smaller than 6):
#     - Adjust lo to 1.
#   - If compare(10) returns 1 (indicating 10 is larger than 6):
#     - Adjust hi to 10.
#   - Repeat until the searched number (6) is found with the desired precision.



# -------------------------------------------------------------------------------------
# -----Solution 2-----Javascript Solution-----Compare Function & Binary Search & Switch Statement-----
# function findNumber(compare) {
#   var min = 0;
#   var max = 100;
#   while (max - min > 1e-5) { 
#     var guess = (max + min)/2;
#     switch (compare(guess)) {
#       case -1: min = guess; break;
#       case 0: return guess;
#       case 1: max = guess;
#     }
#   }
#   return guess;
# }

#  1. The function findNumber takes in 1 parameter, compare (a comparison function).
#  2. Initialize min to 0 and max to 100.
#  3. Use a while loop to approximate the searched number with a precision of 5 fractional digits.
#  4. Inside the loop:
#     - Calculate guess as the average of max and min.
#     - Use the comparison function compare(guess) to determine the relationship between guess and the searched number:
#       - Return guess if compare(guess) returns 0, indicating guess is the searched number.
#       - Adjust min or max based on whether guess is smaller or larger than the searched number.
#  5. Once the loop exits, return guess, which approximates the searched number within the specified tolerance.

#   Example usage:
#   - Searched number: 6
#   - If compare(1) returns -1 (indicating 1 is smaller than 6):
#     - Adjust min to 1.
#   - If compare(10) returns 1 (indicating 10 is larger than 6):
#     - Adjust max to 10.
#   - Repeat until the searched number (6) is found with the desired precision.