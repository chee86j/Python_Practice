# Write a function named setAlarm/set_alarm/set-alarm/setalarm 
# (depending on language) which receives two parameters. 
# The first parameter, employed, is true whenever you are employed 
# and the second parameter, vacation is true whenever you are on vacation.

# The function should return true if you are employed and not on vacation 
# (because these are the circumstances under which you need to set an alarm). 
# It should return false otherwise. Examples:

# employed | vacation 
# true     | true     => false
# true     | false    => true
# false    | true     => false
# false    | false    => false

# -------------------------------------------------------------------------------------
# -----Solution 1-----And Not-----
def set_alarm(employed, vacation):
    return employed and not vacation

#  1. The function takes in two parameters, employed and vacation.
#  2. It returns True if employed is True and vacation is False.
#  3. It returns False otherwise.
#  Python uses 'and not' to check if both conditions are met.
#  If both conditions are met, the function returns True.

# -------------------------------------------------------------------------------------
# -----Solution 2-----Javascript Solution-----
# function setAlarm(employed, vacation) {
#     return employed && !vacation;
# }
#  1. The function takes in two parameters, employed and vacation.
#  2. It returns true if employed is true and vacation is false.
#  3. It returns false otherwise.
#  JavaScript uses '&&' to check if both conditions are met.
#  If both conditions are met, the function returns true.
