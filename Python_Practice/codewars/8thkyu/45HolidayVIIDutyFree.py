# The purpose of this kata is to work out just how many bottles of duty 
# free whiskey you would have to buy such that the savings over the normal 
# high street price would effectively cover the cost of your holiday.

# You will be given the high street price (normPrice, in £ (Pounds)), 
# the duty free discount (discount, in percent) and the cost of the 
# holiday (in £).

# For example, if a bottle costs £10 normally and the duty free discount 
# is 10%, you would save £1 per bottle. If your holiday will cost £500, 
# you would have to purchase 500 bottles to save £500, so the answer you 
# return should be 500.

# Another example: if a bottle costs £12 normally and the duty free 
# discount is 50%, you would save £6 per bottle. If your holiday will cost 
# £1000, you would have to purchase 166.66 bottles to save £1000, so your 
# answer should be 166 bottles.

# All inputs will be integers. Please return an integer. Round down.

# -------------------------------------------------------------------------------------
# -----Solution 1-----Integer Division-----
def duty_free(price, discount, holiday_cost):
  return holiday_cost // (price * (discount / 100))
#  1.  Calculate the savings per bottle by multiplying the price by the discount percentage.
#  2.  Calculate the number of bottles needed by dividing the holiday cost by the savings per bottle.
#  3.  Return the integer value of the number of bottles needed.

# -------------------------------------------------------------------------------------
# -----Solution 2-----Conversion to Integer-----
def duty_free(price, discount, holiday_cost):
    savings_per_bottle = price * (discount/100)
    number_of_bottles = holiday_cost / savings_per_bottle
    return int(number_of_bottles)
#  1.  Calculate the savings per bottle by multiplying the price by the discount percentage.
#  2.  Calculate the number of bottles needed by dividing the holiday cost by the savings per bottle.
#  3.  Return the integer value of the number of bottles by using the int() function.