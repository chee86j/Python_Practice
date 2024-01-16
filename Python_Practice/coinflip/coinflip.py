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

# 4. Argument Parsing Module Unique to Python
import random
from argparse import ArgumentParser

# Create an instance of ArgumentParser with a program description
parser = ArgumentParser(description="Simulate coin flip and optionally show statistics.")

parser.add_argument("n", "--num_flips", type=int, default=1,
                    help="Specify number of coin flips to simulate [default: %(default)s]")
args = parser.parse_args()

total = 0 
for i in range(args.num_flips):
    flip = random.randint(0,1)
    total += flip 
    face = 'H' if flip else 'T' 
    print(f"Flip #{i+1}: {face}")

print(f"Result: {total} Heads, {NUM_FLIPS - total} Tails. "
      f"({total / NUM_FLIPS * 100:.2f}% heads)")


#-----------------------------------------------------------------------

# Explanation of above code:
# Import the random module for generating random numbers
import random
# Import ArgumentParser from the argparse module for command-line argument handling
from argparse import ArgumentParser

# Create an ArgumentParser object with a description for the coin flip simulator
parser = ArgumentParser(description="Simulate coin flip and optionally show statistics.")

# Add a command-line argument to specify the number of coin flips
# "n" is the positional argument, "--num_flips" is the optional argument
# type=int ensures the input is an integer
# default=1 sets the default number of flips to 1 if not specified
# help parameter describes this argument's purpose
parser.add_argument("n", "--num_flips", type=int, default=1,
                    help="Specify number of coin flips to simulate [default: %(default)s]")

# Parse the arguments provided at the command line
args = parser.parse_args()

# Initialize a variable to count the number of heads
total = 0 

# Loop for the number of times specified by the command-line argument
for i in range(args.num_flips):
    # Generate a random number: 0 for heads, 1 for tails
    flip = random.randint(0,1)
    
    # Add flip value to total; total increments if flip is 1 (heads)
    total += flip 
    
    # Determine if the flip is heads ('H') or tails ('T')
    # Python's shorthand for the ternary operator (condition ? exprIfTrue : exprIfFalse in JS)
    face = 'H' if flip else 'T' 

    # Print the result of each flip using string formatting
    print(f"Flip #{i+1}: {face}")

# Print the final results: total heads, total tails, and percentage of heads
# Here, NUM_FLIPS should be args.num_flips for correct execution
print(f"Result: {total} Heads, {args.num_flips - total} Tails. "
      f"({total / args.num_flips * 100:.2f}% heads)")

#   Key Takeaways:
#   The argparse module is used to define how the script should 
#   interpret command-line arguments. This allows the script to 
#   be more dynamic and user-interactive, similar to reading 
#   command-line arguments in a Node.js application but with 
#   a more structured approach.

#   This approach makes the script more flexible, allowing users 
#   to specify the number of coin flips directly from the command 
#   line when running the script. The argparse module automatically 
#   handles incorrect inputs and provides help messages, making the 
#   script more user-friendly.

#   When the script is run, the user can specify the number of flips 
#   using this argument. For example, running python scriptname.py 
#   --num_flips 10 would set the number of coin flips to 10.