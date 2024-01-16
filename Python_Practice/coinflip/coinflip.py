# This project focuses on building a simple yet functional 
# command-line interface (CLI) application to simulate coin 
# flips. Simulating a coin flip boils down to random number 
# generation, but we've enhanced the functionality with the 
# argparse library to create a more user-friendly interface, 
# as well as computing statistical results. 

# 1. Basic Coin Flip Simulation with Random Number Generation
import random # like JS this is a module that allows us to generate random numbers like JS's Math.random()

print(random.randint(0,1)) # randint is a method that generates a random integer between the two arguments passed to it
# Ctrl + f5 to run the program in the terminal
# So, when you run this Python script, it's like rolling a 
# two-sided die (think of a coin) where you can get either 
# 0 (one side of the die) or 1 (the other side). Each time 
# you run the script, Python's random.randint(0, 1) picks 
# one of these numbers at random, and print outputs it to 
# the console.

#-----------------------------------------------------------------------

# 2. More Detail
# Coin Flip Simulation with Command-Line Arguments
# Using the Ternal Operator and printing out the 
# result of each coin flip
import random

for i in range(10):
    flip = random.randint(0,1)
    face = 'H' if flip else 'T' # ternary operator like JS's condition ? expression1 : expression2

    print(f"Flip #{i+1}: {face}")
    # Print the result of each coin flip
    # f-string is used for string formatting. It embeds expressions inside string literals.
    # {i+1} is used to print the flip number (starting from 1 instead of 0)
    # {face} prints 'H' for heads or 'T' for tails

#-----------------------------------------------------------------------

# 3. Track outcomes and calculate percentages with a fixed number of flips
# and print the results of the coin flips
import random

NUM_FLIPS = 10 # defining the number of flips as a constant

total = 0 # initializing a var to keep track of the total number of heads
for i in range(NUM_FLIPS):
    flip = random.randint(0,1)
    total += flip # add to flip count if flip is 1 (heads)
    face = 'H' if flip else 'T' 
    print(f"Flip #{i+1}: {face}") # f-string for formating like JS (`${expression}`)

print(f"Result: {total} Heads, {NUM_FLIPS - total} Tails. "
      f"({total / NUM_FLIPS * 100:.2f}% heads)")
# Print the final results
# Calculate and print the number of heads, tails, and the percentage of heads
# {:.2f} in f-string is for formatting to 2 decimal places, akin to toFixed(2) in JS

#-----------------------------------------------------------------------
