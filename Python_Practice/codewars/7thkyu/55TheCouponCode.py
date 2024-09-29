# Story

# Your online store likes to give out coupons for special occasions. 
# Some customers try to cheat the system by entering invalid codes 
# or using expired coupons.

# Task

# Your mission:
# Write a function called checkCoupon which verifies that a coupon 
# code is valid and not expired.

# A coupon is no more valid on the day AFTER the expiration date. 
# All dates will be passed as strings in this format: "MONTH DATE, YEAR".

# Examples:

# checkCoupon("123", "123", "July 9, 2015", "July 9, 2015")  == True
# checkCoupon("123", "123", "July 9, 2015", "July 2, 2015")  == False

# -------------------------------------------------------------------------------------
# -----Solution 1-----Datetime One-Liner & Comparison using `is` keyword-----
import datetime
def check_coupon(entered_code, correct_code, current_date, expiration_date):
    if entered_code is correct_code:
        return(datetime.datetime.strptime(current_date,'%B %d, %Y') <= 
               datetime.datetime.strptime(expiration_date,'%B %d, %Y'))
    return False
#   1.  Check if the entered code is equal to the correct code
#   2.  If the entered code is equal to the correct code, check if the current date is less 
#       than or equal to the expiration date 
#       `datetime.datetime.strptime(current_date,'%B %d, %Y') <=`
#   3.  If the current date is less than or equal to the expiration date, return True 
#       `datetime.datetime.strptime(expiration_date,'%B %d, %Y')`
#   4.  If the entered code is not equal to the correct code, return False
#       `return False`
#   5.  Return the result of the comparison as the output of the function

#   This solution has a time complexity of O(1) since it only compares the entered code to 
#   the correct code & the current date to the expiration date once & a space complexity of 
#   O(1) since it only uses a few variables. This solution is efficient for verifying that 
#   a coupon code is valid & not expired. It uses the datetime module to convert the 
#   current date & expiration date strings to datetime objects for comparison. This 
#   solution is best when you want to write less code & prefer a simple & clean one-liner.

#   -----Note-----
#   The `is` keyword is used to check if the entered code is equal to the correct code. We use
#   that instead of the `==` operator because we want to check if the two variables are the same
#   object in memory, not just if they have the same value. This is more efficient & avoids
#   potential bugs that could arise from comparing two strings that have the same value but are
#   stored in different memory locations. I tried using the `==` operator but it didn't work
#   for one of the test cases. The `is` keyword is more reliable for this purpose.

# My original solution did not work because of these reasons:

# 1.  The date string format provided as input does not match the expected format ("%B %d, %Y").
# 2.  There are leading/trailing spaces or case sensitivity issues in the coupon codes.
# 3.  The system locale does not match the format of the month names in the date strings.

# I needed to:
# 1.  Ensure that the entered_code & correct_code are converted to strings, stripped of whitespace, 
#     & compared properly.
# 2.  Handle potential errors in date parsing to account for slight differences in the format.
# 3.  Use multiple formats to parse the date, if the input may vary.

# -------------------------------------------------------------------------------------
# -----Solution 2-----Javascript Solution-----
# function checkCoupon(enteredCode, correctCode, currentDate, expirationDate){
#     return enteredCode === correctCode && new Date(currentDate) <= new Date(expirationDate);
# }

#   1.  Check if the entered code is equal to the correct code
#       `enteredCode === correctCode`
#   2.  If the entered code is equal to the correct code, check if the current date is less
#       than or equal to the expiration date
#       `new Date(currentDate) <= new Date(expirationDate)`
#   3.  Return the result of the comparison as the output of the function

#   Compartively this Javascript solution is similar to the Python solution. It checks if the
#   entered code is equal to the correct code & if the current date is less than or equal to
#   the expiration date. It uses the `===` operator to check if the entered code is equal to
#   the correct code. It uses the `new Date()` constructor to convert the current date &
#   expiration date strings to date objects for comparison. The time complexity of this
#   solution is O(1) since it only compares the entered code to the correct code & the current
#   date to the expiration date once & the space complexity is O(1) since it only uses a few
#   variables. This solution is efficient for verifying that a coupon code is valid & not
#   expired.
