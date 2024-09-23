# Description:
# After a hard quarter in the office you decide to get some rest on a vacation. 
# So you will book a flight for you and your girlfriend and try to leave all 
# the mess behind you.

# You will need a rental car in order for you to get around in your vacation. 
# The manager of the car rental makes you some good offers.

# Every day you rent the car costs $40. If you rent the car for 7 or more days, 
# you get $50 off your total. Alternatively, if you rent the car for 3 or more 
# days, you get $20 off your total.

# Write a code that gives out the total amount for different days(d).

# -------------------------------------------------------------------------------------
# -----Solution 1-----Conditional If-Else Statements-----
def rental_car_cost(d):
    result = d * 40
    if d >= 7:
        result -= 50
    elif d >= 3:
        result -= 20
    return result
#   1.  This () takes the number of days as input & calculates the total cost of renting a car
#       for that number of days. 
#   2.  It first calculates the total cost by multiplying the number of days by the daily rate
#       of $40.
#   3.  Then checks if the number of days is greater than or equal to 7. If so, it subtracts
#       $50 from the total cost.
#   4.  If the number of days is not greater than or equal to 7, it checks if the number of days
#       is greater than or equal to 3. If so, it subtracts $20 from the total cost.

#   This is the most direct & easy to understand solution. It uses conditional if-else statements
#   to check the number of days & apply the appropriate discount. It is simple & easy to read.


# -------------------------------------------------------------------------------------
# -----Solution 2-----Mathematical Approach w/ Ternary Operator-----
def rental_car_cost(d):
  return d * 40 - (d > 2) * 20 - (d > 6) * 30
#   1.  This solution uses a mathematical approach to calculate the total cost of renting a car
#       for a given number of days.
#   2.  It first calculates the total cost by multiplying the number of days by the daily rate
#       of $40.
#   3.  Then uses the ternary operator to subtract the appropriate discount based on the number
#       of days. If the number of days is greater than 2, it subtracts $20 from the total cost. If
#       the number of days is greater than 6, it subtracts an additional $30 from the total cost.

#   This solution is more concise than the previous one as it uses a mathematical approach & the
#   ternary operator to calculate the total cost. It is more efficient than the previous solution
#   since it avoids multiple if-else statements. It is useful when dealing with large datasets or
#   when the number of days is very large. However it may be less readable for some people.


# -------------------------------------------------------------------------------------
# -----Solution 3-----Javascript Solution-----
# function baseCost(days, rate) {
#   return days * rate;
# }

# function discountRate(days) {
#   if ( days >= 7 ) {
#     return 50;
#   }
#   else if ( days >= 3 ) {
#     return 20;
#   }
#   else {
#     return 0;
#   }
# }

# function rentalCarCost(days) {
#   return baseCost(days, 40) - discountRate(days);
# }

#   1.  This solution breaks down the problem into two separate functions: 
#       `baseCost` & `discountRate`.
#   2.  The `baseCost` function calculates the total cost of renting a car for a given number
#       of days based on the daily rate of $40.
#   3.  The `discountRate` function calculates the discount based on the number of days rented.
#   4.  The `rentalCarCost` function then calculates the total cost by subtracting the discount
#       from the base cost.
#   5.  This solution is more modular & easier to understand as it breaks down the problem into
#       smaller functions. It is useful when dealing with more complex problems or when the code
#       needs to be reused in multiple places.


