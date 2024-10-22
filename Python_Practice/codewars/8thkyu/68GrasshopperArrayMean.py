# Find Mean

# Find the mean (average) of a list of numbers in an array.

# Information
# To find the mean (average) of a set of numbers add all of 
# the numbers together and divide by the number of values in the list.

# For an example list of 1, 3, 5, 7

# 1. Add all of the numbers

# 1+3+5+7 = 16

# 2. Divide by the number of values in the list. In this example 
# there are 4 numbers in the list.

# 16/4 = 4

# 3. The mean (or average) of this list is 4

# -------------------------------------------------------------------------------------
# -----Solution 1-----
def find_average(nums):
    return sum(nums) / len(nums) if nums else 0
#   1.  We define a () called find_average that takes a list of numbers as input.
#   2.  Then we calculate the sum of the numbers in the list using the sum().
#   3.  Next, we divide the sum by the length of the list using the len() to get the average.
#   4.  We use a conditional expression to check if the list is empty. If the list is empty, we return 0.
#   5.  Finally, we return the average of the numbers in the list.

#   This solution is concise & uses built-in functions to calculate the sum & length of the list.
#   It handles the case where the list is empty by returning 0. The time complexity of this solution
#   is O(n) where n is the number of elements in the list. The space complexity is O(1) since we only
#   use a few variables to store the sum & length of the list.

# -------------------------------------------------------------------------------------
# -----Solution 2-----
def find_average(nums):
    return float(sum(nums)) / len(nums) if len(nums) !=0 else 0
#   1.  We define a () called find_average that takes a list of numbers as input.
#   2.  Then calculate the sum of the numbers in the list using the sum().
#   3.  Use len() to get the length of the list & divide the sum by the length of the list.
#   4.  We use a conditional expression to check if the length of the list is not equal to 0.
#   5.  If the length of the list is 0, we return 0. Otherwise, we return the average of the numbers in the list.

#   This solution is similar to the previous one but uses a conditional expression to check if the length 
#   of the list is not equal to 0. It handles the case where the list is empty by returning 0. The time complexity 
#   of this solution is O(n) where n is the number of elements in the list. The space complexity is O(1) since we 
#   only use a few variables to store the sum & length of the list.



# -------------------------------------------------------------------------------------
# -----Solution 3-----
def find_average(nums):
    return sum(nums) / float(len(nums)) if nums else 0
#   1.  We define a () called find_average that takes a list of numbers as input.
#   2.  Then we calculate the sum of the numbers in the list using the sum().
#   3.  Next, we divide the sum by the length of the list using the len() to get the average.
#   4.  We use a conditional expression to check if the list is empty. If the list is empty, we return 0.
#   5.  Finally, we return the average of the numbers in the list.

#   This solution is similar to the first solution but uses the float()  to convert the length of the list
#   to a float before dividing the sum by the length. This ensures that the result is a floating-point number even
#   if the length of the list is an integer. The time complexity of this solution is O(n) where n is the number of
#   elements in the list. The space complexity is O(1) since we only use a few variables to store the sum & length
#   of the list.

#   Of the three, Solution 3 is the easiest & most backward-compatible. It is the best solution for this problem.
#   Solution 2 is also good but it is not as backward-compatible as Solution 3. Solution 1 is the least recommended
#   because it does not handle the case where the list is empty. 