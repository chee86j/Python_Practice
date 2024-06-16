# There is a bus moving in the city which takes and 
# drops some people at each bus stop.

# You are provided with a list (or array) of integer 
# pairs. Elements of each pair represent the number 
# of people that get on the bus (the first item) and 
# the number of people that get off the bus 
# (the second item) at a bus stop.

# Your task is to return the number of people who are 
# still on the bus after the last bus stop 
# (after the last array). Even though it is the last 
# bus stop, the bus might not be empty and some people 
# might still be inside the bus, they are probably 
# sleeping there :D

# Take a look on the test cases.

# Please keep in mind that the test cases ensure that 
# the number of people in the bus is always >= 0. So 
# the returned integer can't be negative.

# The second value in the first pair in the array is 0, 
# since the bus is empty in the first bus stop.

# -------------------------------------------------------------------------------------
# -----Solution 1----List comprehension, for loop, and sum()----
def number(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])
#   1. Using an example value of bus_stops = [[10, 0], [3, 5], [5, 8]], we iterate through
#      each stop in the list of bus stops with a list comprehension.
#   2. We calculate the num of people that are still on the bus after each stop by
#      subtracting the num of people that get off the bus from the num of people that
#      get on the bus. In this example, we have [10, 0] -> 10 - 0 = 10, [3, 5] -> 3 - 5 = -2,
#      and [5, 8] -> 5 - 8 = -3.
#   3. The sum() is used to sum up the num of people that are still on the bus
#      after the last bus stop by adding 10 + (-2) + (-3) = 5.

# -------------------------------------------------------------------------------------
# -----Solution 2----Similar to Solution 1 but w/o list comprehension----
def number(stops):
    return sum(i - o for i, o in stops)
#   1. Using an example value of bus_stops = [[10, 0], [3, 5], [5, 8]], we iterate through
#      each stop in the list of bus stops with a for loop.
#   2. We calculate the num of people that are still on the bus after each stop by
#      subtracting the num of people that get off the bus from the num of people that
#      get on the bus. In this example, we have [10, 0] -> 10 - 0 = 10, [3, 5] -> 3 - 5 = -2,
#      and [5, 8] -> 5 - 8 = -3.
#   3. The sum() is used to sum up the num of people that are still on the bus
#      after the last bus stop by adding 10 + (-2) + (-3) = 5.

# -------------------------------------------------------------------------------------
# -----Solution 3----JavaScript Solution-----
# var number = function(busStops){
# 	var totalPeople = 0;
#   for (var i=0; i<busStops.length; i++) {
#   	totalPeople += busStops[i][0];
#     totalPeople -= busStops[i][1];
#   }
#   return totalPeople;
# }

#   1. Using an example value of bus_stops = [[10, 0], [3, 5], [5, 8]], 
#      we initialize a variable 'totalPeople' to 0.
#   2. We iterate through each stop in the list of bus stops with a for loop.
#   3. We calculate the num of people that are still on the bus after each stop by
#      adding the num of people that get on the bus and subtracting the num of people
#      that get off the bus. In this example, we have [10, 0] -> 10 - 0 = 10, [3, 5] -> 3 - 5 = -2,
#      and [5, 8] -> 5 - 8 = -3.
#   4. We return the total num of people that are still on the bus after the last bus stop by adding
#      10 + (-2) + (-3) = 5.

