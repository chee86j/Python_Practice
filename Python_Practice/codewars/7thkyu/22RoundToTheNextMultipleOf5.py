# Given an integer as input, can you round it to the next 
# (meaning, "greater than or equal") multiple of 5?

# Examples:

# input:    output:
# 0    ->   0
# 2    ->   5
# 3    ->   5
# 12   ->   15
# 21   ->   25
# 30   ->   30
# -2   ->   0
# -5   ->   -5
# etc.
# Input may be any positive or negative integer (including 0).

# You can assume that all inputs are valid integers.

# -------------------------------------------------------------------------------------
# -----Solution 1-----Modulo-----
def round_to_next5(n):
    return n + (5 - n) % 5

# -------------------------------------------------------------------------------------
# -----Solution 2-----While Loop-----
def round_to_next5(n):
    while n%5!=0:
        n+=1
    return n
    
# -------------------------------------------------------------------------------------
# -----Solution 2-----Math Module-----
import math
def round_to_next5(n):
    return math.ceil(n/5)*5

# -----Solution 2-----Javascript Version-----
# function roundToNext5(n){
#     return Math.ceil(n/5)*5;
# }