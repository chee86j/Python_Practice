# This function should test if the factor is a factor of base.

# Return true if it is a factor or false if it is not.

# ABOUT FACTORS
# Factors are numbers you can multiply together to get another number.

# 2 and 3 are factors of 6 because: 2 * 3 = 6

# You can find a factor by dividing numbers. If the remainder is 0 
# then the number is a factor.

# You can use the mod operator (%) in most languages to check for a 
# remainder

# For example 2 is not a factor of 7 because: 7 % 2 = 1

# Note: base is a non-negative number, factor is a positive number.
# -------------------------------------------------------------------------------------
# -----Solution 1-----Modulo Operator-----
def check_for_factor(base, factor):
    return base % factor == 0
# 1.  The function check_for_factor takes in two parameters, base and factor.
# 2.  The modulo operator (%) is used to check if the factor is a factor of the base.
# 3.  If the remainder of the division of the base by the factor is 0, the factor is a 
#     factor of the base.
# 4.  The function returns True if the factor is a factor of the base and False otherwise.

# The time complexity of this solution is O(1) since the modulo operator is a constant 
# time operation. The space complexity of this solution is O(1) since only a single 
# comparison is made and a boolean value is returned.

# In terms of efficiency, this solution is optimal as it uses the modulo operator to
# check if the factor is a factor of the base.


# -------------------------------------------------------------------------------------
# -----Solution 2-----JavaScript Version-----
# function checkForFactor (base, factor) {
#   return base % factor === 0;
# }
# 1.  The function checkForFactor takes in two parameters, base and factor.
# 2.  The modulo operator (%) is used to check if the factor is a factor of the base.
# 3.  If the remainder of the division of the base by the factor is 0, the factor is a
#     factor of the base.
# 4.  The function returns true if the factor is a factor of the base and false otherwise.

# The time complexity of this solution is O(1) since the modulo operator is a constant
# time operation. The space complexity of this solution is O(1) since only a single
# comparison is made and a boolean value is returned.

# This solution is efficient as it uses the modulo operator to check if the factor is a
# factor of the base. It is concise and easy to understand.
