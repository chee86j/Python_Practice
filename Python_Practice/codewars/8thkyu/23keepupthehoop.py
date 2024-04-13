# Alex just got a new hula hoop, he loves it but feels discouraged 
# because his little brother is better than him

# Write a program where Alex can input (n) how many times the hoop 
# goes round and it will return him an encouraging message :)

# If Alex gets 10 or more hoops, return the string "Great, now move on to tricks".
# If he doesn't get 10 hoops, return the string "Keep at it until you get it".

# -------------------------------------------------------------------------------------
# -----Solution 1-----Single Line If/Else-----
def hoopCount(n):
    return "Keep at it until you get it" if n<10 else "Great, now move on to tricks"
#   1. using a single line if else statement
#   2. if n is less than 10, return "Keep at it until you get it"
#   3. else return "Great, now move on to tricks"

# -------------------------------------------------------------------------------------
# -----Solution 2-----If Else-----
def hoop_count(n):
    if n >=10:
        return "Great, now move on to tricks"
    else:
        return "Keep at it until you get it"