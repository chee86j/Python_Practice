# Mr. Scrooge has a sum of money 'P' that he wants to invest. 
# Before he does, he wants to know how many years 'Y' this 
# sum 'P' has to be kept in the bank in order for it to amount 
# to a desired sum of money 'D'.

# The sum is kept for 'Y' years in the bank where interest 'I' 
# is paid yearly. After paying taxes 'T' for the year the new 
# sum is re-invested.

# Note to Tax: not the invested principal is taxed, but only 
# the year's accrued interest

# Example:

#   Let P be the Principal = 1000.00      
#   Let I be the Interest Rate = 0.05      
#   Let T be the Tax Rate = 0.18      
#   Let D be the Desired Sum = 1100.00


# After 1st Year -->
#   P = 1041.00
# After 2nd Year -->
#   P = 1083.86
# After 3rd Year -->
#   P = 1128.30

# Thus Mr. Scrooge has to wait for 3 years for the initial 
# principal to amount to the desired sum.

# Your task is to complete the method provided and return 
# the number of years 'Y' as a whole in order for Mr. Scrooge 
# to get the desired sum.

# Assumption: Assume that Desired Principal 'D' is always 
# greater than the initial principal. However it is best 
# to take into consideration that if Desired Principal 'D' 
# is equal to Principal 'P' this should return 0 Years.

# -------------------------------------------------------------------------------------
# -----Solution 1-----While Loop & Increment Years-----
def calculate_years(principal, interest, tax, desired):
    years = 0
    while principal < desired:
        principal += (principal * interest) * (1 - tax)
        years += 1
    return years
#  1. The ()) calculate_years takes in 4 params: principal, interest, tax, and desired.
#  2. The years var is initialized to 0.
#  3. A while loop is used to calculate the num of years required for the principal to reach the desired sum.
#  4. In each iteration, the principal is updated by adding the int earned after tax.
#  5. The years var is incremented by 1 in each iteration.
#  6. Once the principal reaches the desired sum, the loop exits.
#  7. The ()) returns the num of years required for the principal to reach the desired sum.

#   Using the example principal = 1000, interest = 0.05, tax = 0.18, and desired = 1100:
#   1. principal = 1000, years = 0
#   2. Loop 1: principal = 1000 + (1000 * 0.05) * (1 - 0.18) = 1041, years = 1
#   3. Loop 2: principal = 1041 + (1041 * 0.05) * (1 - 0.18) = 1083.86, years = 2
#   4. Loop 3: principal = 1083.86 + (1083.86 * 0.05) * (1 - 0.18) = 1128.30, years = 3
#   5. Return years = 3

# -------------------------------------------------------------------------------------
# -----Solution 2-----Javascript Solution-----
# function calculateYears(principal, interest, tax, desired) {
#     let years = 0;
#     while (principal < desired) {
#         principal += (principal * interest) * (1 - tax);
#         years++;
#     }
#     return years;
# }

#  1. The () calculateYears takes in 4 params: principal, interest, tax, and desired.
#  2. The years var is initialized to 0.
#  3. A while loop is used to calculate the num of years required for the principal to reach the desired sum.
#  4. In each iteration, the principal is updated by adding the int earned after tax.
#  5. The years var is incremented by 1 in each iteration.
#  6. Once the principal reaches the desired sum, the loop exits.

#  For example, principal = 1000, interest = 0.05, tax = 0.18, and desired = 1100:
#  1. principal = 1000, years = 0
#  2. Loop 1: principal = 1000 + (1000 * 0.05) * (1 - 0.18) = 1041, years = 1
#  3. Loop 2: principal = 1041 + (1041 * 0.05) * (1 - 0.18) = 1083.86, years = 2
#  4. Loop 3: principal = 1083.86 + (1083.86 * 0.05) * (1 - 0.18) = 1128.30, years = 3
#  5. Return years = 3
