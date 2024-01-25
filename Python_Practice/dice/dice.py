# Basic Dice Rolling Simulator Solution
import random # import random module

num_rolls = 3 # set variable for number of rolls

die1 = random.randint(1, 6) # set function for die1 & die 2 using random module and randint function
die2 = random.randint(1, 6) # this is similar to JS Math.floor(Math.random() * 6) + 1
print(die1, die2) # print results of die1 and die2

# -------------------------------------------------------------------------------------------------------------------------------------

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

# -------------------------------------------------------------------------------------------------------------------------------------

# Solution using List Comprehension and Unpacking Operator and f-strings
import random
import math 

num_rolls = 10
total, doubles, mn, mx = 0, 0, math.inf, -math.inf 
rolls = []

for _i in range(num_rolls): 
    dice = [random.randint(1,6) for _i in range(2)] 
    roll = sum(dice) 
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

# -------------------------------------------------------------------------------------------------------------------------------------

# Key Takeaways for Above Solution
import random
import math # import math module which provides access to the mathematical functions defined by the C standard

num_rolls = 10
total, doubles, mn, mx = 0, 0, math.inf, -math.inf 
rolls = []
# the variables total, doubles, mn, and mx are all set to 0, 
# while mn and mx are set to positive and negative infinity, respectively. math.inf is a float representing
# positive infinity, and -math.inf is a float representing negative infinity. to explain those two in more detail
# infinity is a concept in mathematics that refers to a quantity without bound or end. For example, the number 1
# is not infinity, but it is a finite number. In contrast, the number 1/0 is infinity, as is the number 1/0.0000001.
# In Python, infinity is represented by the float values math.inf and -math.inf. These values are used to represent
# positive and negative infinity, respectively. They are useful for comparing values to infinity, as we will see in
# the solution to this problem.

for _i in range(num_rolls): # loop to roll dice num_rolls times
    dice = [random.randint(1,6) for _i in range(2)] # list comprehension to roll 2 six-sided dice
    roll = sum(dice) # sum of the two dice
    print(*dice, f"\t({roll})") # print the two dice values and their sum
    # the asterisk (*) in front of dice is used to unpack the list. This is necessary because print() expects
    # multiple arguments, not a single list argument. The unpacking operator (*) is used to unpack the list into
    # multiple arguments. For example, if dice is [1, 2], then *dice is equivalent to 1, 2. Thus, the print()
    # statement is equivalent to print(dice[0], dice[1], f"\t({roll})").
    # the f-string (f"\t({roll})") is used to print the sum of the two dice. The f-string is a string literal
    #\t is used for tab spacing
    
    #stats
    mn = min(mn, roll) # minimum roll value
    mx = max(mx, roll) # maximum roll value
    total += roll # total of all rolls
    doubles += (len(set(dice)) == 1) # Incremented if both dice have the same value. This is 
    # set is a built-in Python data structure that represents an unordered collection of unique elements.
    # The set() function is used to create a set from a list. For example, set([1, 2, 3]) is equivalent to {1, 2, 3}.
    # The len() function is used to get the length of a list. For example, len([1, 2, 3]) is equivalent to 3.
    # checked by converting the dice list to a set and checking if its length is 1.
    
print(f"""--- Stats ---
Min: {mn}
Mean: {total/num_rolls:.2f} 
Max: {mx}
Num Doubles: {doubles}""")
# the :.2f in the f-string is used to format the mean to two decimal places. The f-string is equivalent to
# print(f"Mean: {total/num_rolls:.2f}"). The :.2f is a format specifier that tells Python to format the
# number total/num_rolls as a float with two decimal places. For example, 1.2345 is formatted as 1.23.

# -------------------------------------------------------------------------------------------------------------------------------------