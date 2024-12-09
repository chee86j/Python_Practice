# Your friend invites you out to a cool floating pontoon around 1km off the beach. 
# Among other things, the pontoon has a huge slide that drops you out right into 
# the ocean, a small way from a set of stairs used to climb out.

# As you plunge out of the slide into the water, you see a shark hovering in the 
# darkness under the pontoon... Crap!

# You need to work out if the shark will get to you before you can get to the pontoon. 
# To make it easier... as you do the mental calculations in the water you either 
# freeze when you realise you are dead, or swim when you realise you can make it!

# You are given 5 variables;

# sharkDistance = distance from the shark to the pontoon. The shark will eat you if 
# it reaches you before you escape to the pontoon.

# -----sharkSpeed = how fast it can move in metres/second.

# -----pontoonDistance = how far you need to swim to safety in metres.

# -----youSpeed = how fast you can swim in metres/second.

# -----dolphin = a boolean, if true, you can half the swimming speed of the shark as 
#      the dolphin will attack it.

# -----The pontoon, you, and the shark are all aligned in one dimension.

# If you make it, return "Alive!", if not, return "Shark Bait!".

# -------------------------------------------------------------------------------------
# -----Solution 1-----Using Simple Arithmetic Operations-----
def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    if dolphin:
        shark_speed /= 2

    time_you = pontoon_distance / you_speed
    time_shark = shark_distance / shark_speed

    return "Alive!" if time_you < time_shark else "Shark Bait!"

#   1. First check if there is a dolphin present. If there is, halve the shark's speed.
#   2. Calculate time it will take for you to reach pontoon by dividing pontoon distance 
#      by your speed.
#   3. Calculate time it will take for shark to reach you by dividing shark distance by 
#      shark speed.
#   4. Compare the two times & return "Alive!" if you reach pontoon before shark reaches 
#      you, else return "Shark Bait!".

# The time complexity of this solution is O(1) because it performs a constant number of
# operations regardless of the input values. The space complexity is also O(1) because
# the function uses a constant amount of memory to store variables & return the result.

# This solution is efficient as it calculates the time it takes for you & the shark to reach
# their respective destinations and compares them to determine the outcome. It handles the
# case where a dolphin is present by halving the shark's speed if needed.

# -------------------------------------------------------------------------------------
# -----Solution 2-----Using Single Line Return Statement-----
def shark(pontoonDistance, sharkDistance, youSpeed, sharkSpeed, dolphin):
    return "Alive!" if (pontoonDistance / youSpeed) < sharkDistance / (sharkSpeed - (sharkSpeed * 0.5 * dolphin)) else "Shark Bait!"
#   1. Calculate the time it will take for you to reach the pontoon by dividing the pontoon
#      distance by your speed.
#   2. Calculate the time it will take for the shark to reach you by dividing the shark
#      distance by the shark speed minus half the shark speed if a dolphin is present.
#   3. Compare the two times and return "Alive!" if you reach the pontoon before the shark
#      reaches you, else return "Shark Bait!".

# Same as Solution 1 but in a single line return statement. It calculates the time it takes
# for you and the shark to reach their destinations and compares them to determine the outcome.
# It also accounts for the presence of a dolphin by halving the shark's speed if needed. This is
# less modular and harder to read than Solution 1, but it achieves the same result.

# -------------------------------------------------------------------------------------
# -----Solution 3-----Using Minimal Variables-----
def shark(d1, d2, v1, v2, x):
    return "Alive!" if d1 / v1 < d2 / v2 * (x + 1) else "Shark Bait!"
#   1. Calculate the time it will take for you to reach the pontoon by dividing the pontoon
#      distance by your speed.
#   2. Calculate the time it will take for the shark to reach you by dividing the shark
#      distance by the shark speed multiplied by the dolphin modifier (1 if no dolphin, 2 if
#      dolphin).
#   3. Compare the two times and return "Alive!" if you reach the pontoon before the shark
#      reaches you, else return "Shark Bait!".

# This solution uses minimal variables to calculate the time it takes for you and the shark to
# reach their destinations and compares them to determine the outcome. It also accounts for the
# presence of a dolphin by using a dolphin modifier to adjust the shark's speed. This solution
# is concise and achieves the same result as the previous solutions but is the hardest to read.

# -------------------------------------------------------------------------------------
# -----Solution 4-----JavaScript Solution-----
# function shark(pontoonDistance, sharkDistance, youSpeed, sharkSpeed, dolphin){
#     if(dolphin){
#         sharkSpeed /= 2;
#     }
#     return pontoonDistance / youSpeed < sharkDistance / sharkSpeed ? "Alive!" : "Shark Bait!";
# }

# This is the same as Solution 1 but in JavaScript. The function takes the same parameters
# and performs the same calculations to determine if you will make it to the pontoon before
# the shark reaches you. It also accounts for the presence of a dolphin by halving the shark's
# speed if needed. The function returns "Alive!" if you reach the pontoon before the shark
# reaches you, and "Shark Bait!" otherwise.

# Time complexity: O(1) because it uses simple arithmetic operations to calculate the time
# taken for you and the shark to reach their destinations. The number of operations remains
# constant regardless of the input values.
# Space complexity: O(1) because the function uses a constant amount of memory to store
# variables and return the result.
