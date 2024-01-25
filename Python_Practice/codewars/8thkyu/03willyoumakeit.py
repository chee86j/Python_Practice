# -----Instructions-----
# You were camping with your friends far away from home, but when it's time to go back, you realize that your fuel is running out and the nearest pump is 50 miles away! You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.

# Considering these factors, write a function that tells you if it is possible to get to the pump or not.

# Function should return TRUE if it is possible and FALSE if not.

# -------------------------------------------------------------------------------------
# -----Solution 1-----
def zeroFuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left
    # Calculate the maximum distance the car can go with the remaining fuel
    # This is done by multiplying the miles per gallon (mpg) by the fuel left
    # In JavaScript terms, it's like calculating maxDistance = mpg * fuelLeft
    # Then, check if the calculated max distance is greater than or equal to the distance to the pump
    # If it is, return true (meaning it's possible to reach the pump), otherwise return false
    

# -------------------------------------------------------------------------------------
# -----Solution 2-----
def zero_fuel(distance_to_pump, mpg, fuel_left):
    max_distance = mpg * fuel_left # Calculate the maximum distance the car can go with the fuel left
    
    return max_distance >= distance_to_pump
    # Return True if the maximum distance is greater than or equal to the distance to the pump
    # Return False otherwise

