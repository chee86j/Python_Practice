# Let us begin with an example:

# A man has a rather old car being worth $2000. He saw a secondhand car being worth $8000.
# He wants to keep his old car until he can buy the secondhand one.

# He thinks he can save $1000 each month but the prices of his old car and of the new one
# decrease of 1.5 percent per month. Furthermore this percent of loss increases of 0.5 per
# cent at the end of every two months. Our man finds it difficult to make all these 
# calculations.

# Can you help him?

# How many months will it take him to save up enough money to buy the car he wants, and 
# how much money will he have left over?

# Parameters and return of function:

# parameter (positive int or float, guaranteed) start_price_old (Old car price)
# parameter (positive int or float, guaranteed) start_price_new (New car price)
# parameter (positive int or float, guaranteed) saving_per_month 
# parameter (positive float or int, guaranteed) percent_loss_by_month

# nbMonths(2000, 8000, 1000, 1.5) should return [6, 766] or (6, 766)

# Detail of the above example:
    
# end month 1: percent_loss 1.5 available -4910.0
# end month 2: percent_loss 2.0 available -3791.7999...
# end month 3: percent_loss 2.0 available -2675.964
# end month 4: percent_loss 2.5 available -1534.06489...
# end month 5: percent_loss 2.5 available -395.71327...
# end month 6: percent_loss 3.0 available 766.158120825...
# return [6, 766] or (6, 766)


# where 6 is the number of months at the end of which he can buy the new car and 766 is 
# the nearest integer to 766.158... (rounding 766.158 gives 766).

# Note:

# Selling, buying and saving are normally done at end of month. Calculations are 
# processed at the end of each considered month but if, by chance from the start, the 
# value of the old car is bigger than the value of the new one or equal there is no 
# saving to be made, no need to wait so he can at the beginning of the month buy the 
# new car:

# nbMonths(12000, 8000, 1000, 1.5) should return [0, 4000]
# nbMonths(8000, 8000, 1000, 1.5) should return [0, 0]

# We don't take care of a deposit of savings in a bank:-)

# -------------------------------------------------------------------------------------
# -----Solution 1-----While Loop & If Statement-----
def nbMonths(oldCarPrice, newCarPrice, saving, loss):
    months = 0
    budget = oldCarPrice
    
    while budget < newCarPrice:
        months += 1
        if months % 2 == 0:
            loss += 0.5
        
        oldCarPrice *= (100 - loss) / 100
        newCarPrice *= (100 - loss) / 100
        budget = saving * months + oldCarPrice
    
    return [months, round(budget - newCarPrice)]
#   1. Initialize months to 0 and budget to oldCarPrice.
#   2. While budget is less than newCarPrice, do the following:
#       a. Increment months by 1.
#       b. If months is divisible by 2, increment loss by 0.5.
#       c. Update oldCarPrice to be oldCarPrice * (100 - loss) / 100.
#       d. Update newCarPrice to be newCarPrice * (100 - loss) / 100.
#       e. Update budget to be saving * months + oldCarPrice.
#   3. Return [months, round(budget - newCarPrice)].

#   Note the use of '*=' to update oldCarPrice and newCarPrice in place. 
#   This is equivalent to JavaScript's oldCarPrice *= (100 - loss) / 100.

#   The time complexity of this solution is O(n), where n is the number of months 
#   it takes to save up enough money to buy the new car. 
#   The space complexity is O(1) as we use a constant amount of extra space.
#   This is a slightly wordy solution, but it is easy to understand and implement. 
#   This may lead to redundancy in large datasets, but it is a good starting point 
#   for beginners.


# -------------------------------------------------------------------------------------
# -----Solution 2-----While Loop & If Statement-----
def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    i = 0
    while savingperMonth * i + startPriceOld < startPriceNew:
        if i % 2:
            percentLossByMonth += 0.5
        startPriceOld -= startPriceOld * 0.01 * percentLossByMonth
        startPriceNew -= startPriceNew * 0.01 * percentLossByMonth
        i += 1
    return [i, round(savingperMonth * i + startPriceOld - startPriceNew)]
#   This solution is similar to the previous one, but it uses a different approach to
#   calculate the number of months and the leftover money. 
#   1. Initialize i to 0.
#   2. While savingperMonth * i + startPriceOld is less than startPriceNew, 
#      do the following:
#       a. If i is odd, increment percentLossByMonth by 0.5.
#       b. Update startPriceOld to be startPriceOld - startPriceOld * 0.01 * percentLossByMonth.
#       c. Update startPriceNew to be startPriceNew - startPriceNew * 0.01 * percentLossByMonth.
#       d. Increment i by 1.
#   3. Return [i, round(savingperMonth * i + startPriceOld - startPriceNew)].

#   The time complexity of this solution is O(n), where n is the number of months
#   it takes to save up enough money to buy the new car. 
#   The space complexity is O(1) as we use a constant amount of extra space.
#   This solution is less readable and compacter than Solution 1.


# -------------------------------------------------------------------------------------
# -----Solution 3-----While Loop & 2 If Statements-----
def nbMonths(priceold, pricenew, savingperMonth, percentloss):
    month = 0
    saving = 0
    
    while pricenew > saving + priceold:
        if priceold >= pricenew:
            break
        month += 1     
        if month%2==0 and month != 0:
            percentloss+=0.5
        pricenew -= (pricenew*percentloss)/100
        priceold -= (priceold*percentloss)/100
        saving += savingperMonth

    leftover = priceold - pricenew + saving
    return [month,round(leftover,0)]
#   Compared to the previous solutions, this solution is more concise and uses a
#   single while loop to calculate the number of months and the leftover money.
#   1. Initialize month to 0 and saving to 0.
#   2. While pricenew is greater than saving + priceold, do the following:
#       a. If priceold is greater than or equal to pricenew, break the loop.
#       b. Increment month by 1.
#       c. If month is divisible by 2 and not equal to 0, increment percentloss by 0.5.
#       d. Update pricenew to be pricenew - (pricenew * percentloss) / 100.
#       e. Update priceold to be priceold - (priceold * percentloss) / 100.
#       f. Update saving to be saving + savingperMonth.
#   3. Calculate leftover as priceold - pricenew + saving.
#   4. Return [month, round(leftover, 0)].

#   The time complexity of this solution is O(n), where n is the number of months
#   it takes to save up enough money to buy the new car.
#   The space complexity is O(1) as we use a constant amount of extra space.
#   This solution is concise and easy to understand, making it a good choice for
#   beginners and experienced programmers alike. It avoids unnecessary checks and
#   calculations when the old car price is greater than or equal to the new car price.

# -------------------------------------------------------------------------------------
# -----Solution 4-----JavaScript Solution-----
# function nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth){
#   var months = 0, moneySaved = 0;
# 	while (startPriceNew > startPriceOld + moneySaved){
# 		moneySaved += savingperMonth;
# 		startPriceOld -= (startPriceOld * (percentLossByMonth / 100));
# 		startPriceNew -= (startPriceNew * (percentLossByMonth / 100));
# 		months++;
# 		if (months % 2 == 1){
# 			percentLossByMonth += .5;
# 		}
# 	}
# 	return [months, Math.round(startPriceOld + moneySaved - startPriceNew)];
# }
#   This JavaScript solution is similar to the previous Python solutions.
#   1. Initialize months to 0 and moneySaved to 0.
#   2. While startPriceNew is greater than startPriceOld + moneySaved, do the following:
#       a. Increment moneySaved by savingperMonth.
#       b. Update startPriceOld to be startPriceOld - (startPriceOld * (percentLossByMonth / 100)).
#       c. Update startPriceNew to be startPriceNew - (startPriceNew * (percentLossByMonth / 100)).
#       d. Increment months by 1.
#       e. If months is odd, increment percentLossByMonth by 0.5.
#   3. Return [months, Math.round(startPriceOld + moneySaved - startPriceNew)].
#   Similar to the Python solutions, this has a time complexity of O(n) and a 
#   space complexity of O(1) due to the use of a constant amount of extra space.
