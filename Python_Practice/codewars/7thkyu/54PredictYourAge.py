# My grandfather always predicted how old people would get, 
# and right before he passed away he revealed his secret!

# In honor of my grandfather's memory we will write a function 
# using his formula!

#     Take a list of ages when each of your great-grandparent died.
#     Multiply each number by itself.
#     Add them all together.
#     Take the square root of the result.
#     Divide by two.

# Example

# predict_age(65, 60, 75, 55, 60, 63, 64, 45) == 86

# Note: the result should be rounded down to the nearest integer.

# Some random tests might fail due to a bug in the JavaScript 
# implementation. Simply resubmit if that happens to you.

# -------------------------------------------------------------------------------------
# -----Solution 1-----
def predict_age(*ages):
    return sum(a*a for a in ages)**.5//2
#   1.  Use a generator expression to square each age in the input list of ages
#   2.  Sum the squares of all ages in the list
#   3.  Take the square root of the sum of the squares of all ages
#   4.  Divide the square root of the sum of the squares of all ages by 2
#   5.  Return the result of the division as the predicted age

#   This solution has a time complexity of O(n) where n is the number of ages in the
#   input list of ages since it iterates over the list of ages to square each age &
#   sum the squares of all ages. It has a space complexity of O(1) since it only uses
#   a few variables. This solution is efficient for predicting the age based on the
#   formula provided. It uses a generator expression to calculate the sum of the squares
#   of all ages in the list.
#   This solution is best when you want to write less code and prefer a simple and clean one-liner.

# -------------------------------------------------------------------------------------
# -----Solution 2-----
import math

def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    arr=[age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
    result=int((math.sqrt(sum([i ** 2 for i in arr])))/2)
    return result

#   1.  Create a list `arr` containing all the ages passed as arguments
#   2.  Use a list comprehension to square each age in the list `arr`
#   3.  Sum the squares of all ages in the list `arr`
#   4.  Calculate the square root of the sum of the squares of all ages
#   5.  Divide the square root of the sum of the squares of all ages by 2
#   6.  Return the integer result of the division as the predicted age

#   This solution has a time complexity of O(1) since it only calculates the sum of the
#   squares of the ages once & a space complexity of O(1) since it only uses a few
#   variables. This solution is efficient for predicting the age based on the formula
#   provided. It uses a list comprehension to calculate the sum of the squares of all
#   ages in the list `arr`.
#   This is more verbose and easier to follow for beginners.

# -------------------------------------------------------------------------------------
# -----Solution 3-----Javascript Solution-----
# function predictAge(age1,age2,age3,age4,age5,age6,age7,age8){
#   let arr = [age1, age2, age3, age4, age5, age6, age7, age8]
#   return Math.floor(Math.sqrt(arr.map(a => a * a).reduce((b,c) => b + c)) / 2)
# }

#  This is a JS solution that predicts the age based on the formula provided. It creates
#  a list `arr` containing all the ages passed as arguments. It uses the map method to
#  square each age in the list `arr` & the reduce method to sum the squares of all ages
#  in the list `arr`. The square root of the sum of the squares of all ages is calculated
#  & divided by 2. The result is rounded down to the nearest integer using Math.floor.
#  The time complexity of this solution is O(1) since it only calculates the sum of the
#  squares of the ages once & the space complexity is O(1) since it only uses a few
#  variables. This solution is efficient for predicting the age based on the formula
#  provided. It uses the map & reduce methods to calculate the sum of the squares of all
#  ages in the list `arr`.
#  If you are comfortable with Javascript array methods, this solution is very readable.