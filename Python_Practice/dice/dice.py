# Basic Dice Rolling Simulator Solution
import random # import random module

num_rolls = 3 # set variable for number of rolls

die1 = random.randint(1, 6) # set function for die1 & die 2 using random module and randint function
die2 = random.randint(1, 6) # this is similar to JS Math.floor(Math.random() * 6) + 1
print(die1, die2) # print results of die1 and die2

# ---------------------------------------------------------------------------------------------------

# Solution using List Comprehension
import random

num_rolls = 10

for _i in range(num_rolls):  # A 'for' loop, iterating 'num_rolls' times.
    # List comprehension to roll 2 six-sided dice.
    dice = [random.randint(1,6) for _i in range(2)] 
    # List comprehension is a compact way to create lists. It's like a concise form of a for loop in JavaScript.
    # 'random.randint(1,6)' generates a random integer between 1 and 6 (inclusive), simulating a dice roll.
    # The list comprehension creates a list of two such random numbers, simulating the roll of two dice.
    print(dice) 

# ---------------------------------------------------------------------------------------------------

import random

num_rolls = 10
total, doubles, mn, mx = 0, 0, math.inf, -math.inf
rolls = []

for _i in range(num_rolls):
    dice = [random.randint(1,6) for _i in range(2)]
    roll = sum(dice)
    roll
    print(*dice, f"\t({roll})")
    
    #stats
    mn = min(mn, roll)
    mx = max(mx, roll)
    total += roll
    doubles += (len(set(dice)) == 1)
    
print(f"""--- Stats ---
Min: {mn}
Mean: {total/num_rolls:.2f}
Max: {mx}
Num Doubles: {doubles}""")