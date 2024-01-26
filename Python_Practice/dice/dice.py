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
# Solution w/Median & w/Mode using Counter
import random
import math 
from collections import Counter # import Counter from collections module
# helper data structure that is used to count the number of occurrences of each value in a list

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

# For finding the Median
mid = num_rolls // 2 # integer division
sorted_rolls = sorted(rolls) # sort rolls
median = sorted_rolls[mid]
if num_rolls % 2 == 0:
    median += sorted_rolls
    median /= 2

# For finding the Mode
most_common = Counter(rolls).most_common()
mode_vals = most_common[0][0]
mode_count = most_common[0][1]
for val, count in most_common:
    if count == mode_count:
        mode_vals.append(val)
    else:
        break
    
print(f"""--- Stats ---
Min: {mn}
Mean: {total/num_rolls:.2f} 
Median: {median}
Mode: [', '.join(str(x) for x in mode_vals)] (each appeared {mode_count} time(s))
Max: {mx}
Num Doubles: {doubles}""")

# -------------------------------------------------------------------------------------------------------------------------------------
# Key Takeaways for Above Solution
import random
import math 
from collections import Counter  # Counter is like a specialized dictionary for counting occurrences

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
    
# Calculate the median
mid = num_rolls // 2  # Get the middle index (integer division, like Math.floor in JS)
sorted_rolls = sorted(rolls)  # Sort the rolls to find the median
median = sorted_rolls[mid]  # Get the middle value for the median
if num_rolls % 2 == 0:
    median = (median + sorted_rolls[mid - 1]) / 2  # If even number of rolls, average the two middle values

# Calculate the mode
most_common = Counter(rolls).most_common()  # Reference 1
mode_vals = [most_common[0][0]]  # Reference 2
mode_count = most_common[0][1]  # Reference 3

for val, count in most_common[1:]:  # Reference 4
    if count == mode_count:  # If the count is the same as the mode count
        mode_vals.append(val) # Add the value to the list of mode values
                              # append() is a method that adds an element to the end of a list
    else:
        break  # Stop if a different count is found

# Print final stats
print(f"""--- Stats ---
Min: {mn}
Mean: {total/num_rolls:.2f} 
Median: {median}
Mode: {', '.join(str(x) for x in mode_vals)} (each appeared {mode_count} time(s))
Max: {mx}
Num Doubles: {doubles}""")

# ---Ref 1---
    # Counter and Most Common: Counter(rolls).most_common() creates a Counter object from 
    # the rolls list and then applies the most_common() method. This method returns a list 
    # of tuples, where each tuple contains a value from rolls and its count. 
    # A tuple is a data structure that is similar to a list, but it is immutable (i.e.,
    # it cannot be changed). For example, (1, 2) is a tuple containing the values 1 and 2.
    # The list is sorted in descending order based on the counts.
# ---Ref 2---
    # Initializing Mode Values: mode_vals = [most_common[0][0]] initializes a list with the 
    # first element of the most_common list. This element is the value that has the highest 
    # count (i.e., the most frequent value). The [0][0] part means you're accessing the first 
    # element of the first tuple, which is the value itself (not its count).
# ---Ref 3---
    # Mode Count: mode_count = most_common[0][1] stores the count of the most frequent value. 
    # The [0][1] part accesses the count from the first tuple.
# ---Ref 4---
    # Loop Through Remaining Elements: The for loop iterates over the rest of the elements in 
    # the most_common list (excluding the first one, which is already in mode_vals).
