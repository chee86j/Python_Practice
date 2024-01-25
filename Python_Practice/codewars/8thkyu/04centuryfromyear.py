# -----Instructions-----
# Introduction

# The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.
# Task

# Given a year, return the century it is in.
# Examples

# 1705 --> 18
# 1900 --> 19
# 1601 --> 17
# 2000 --> 20

# Note: this kata uses strict construction as shown in the description and the examples, you can read more about it here
# https://en.wikipedia.org/wiki/Century


# -------------------------------------------------------------------------------------
# -----Solution 1-----
def century(year):
    return (year + 99) // 100
    # Add 99 to the year, then divide by 100 and round down to the nearest integer
    # of course, this only works if the year is a positive integer
    # the JS equivalent is Math.floor((year + 99) / 100)
    
# -------------------------------------------------------------------------------------
# -----Solution 2-----
import math

def century(year):
    return math.ceil(year / 100)
    # We can use the import math module to use the ceil function
    # The ceil function rounds up to the nearest integer
    # The JS equivalent is Math.ceil(year / 100)
    
# -------------------------------------------------------------------------------------
# -----Solution 3-----
def century(year):
    if year%100==0: # return the year divided by 100 giving the century directly
        return year//100
    else:
        return year//100+1 # otherwise, return the year divided by 100 plus 1
