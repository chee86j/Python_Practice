# DESCRIPTION:
# Your job is to write a function which increments 
# a string, to create a new string.

# If the string already ends w/ a number, the 
# number should be incremented by 1.
# If the string does not end w/ a number. the 
# number 1 should be appended to the new string.
# Examples:

# foo -> foo1

# foobar23 -> foobar24

# foo0042 -> foo0043

# foo9 -> foo10

# foo099 -> foo100

# Attention: If the number has leading zeros the 
# amount of digits should be considered.

# -----Solution 1-----
def increment_string(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    return head + str(int(tail) + 1).zfill(len(tail))

#   1. Set head w/ strng w/o numbers at the end
#   2. Set tail w/ strng from length of head to the end
#   3. If tail is an empty string, return strng + "1"
#   4. Return head + str(int(tail) + 1).zfill(len(tail))
#       a. Convert tail to an integer and increment by 1
#       b. Convert result to a string and fill w/ zeros to the length of tail

#   This solution is more efficient than Solution 2 below because it uses an 
#   if statement instead of two if statements

# -----Solution 2-----
def increment_string(strng):
    stripped = strng.rstrip('1234567890')
    ints = strng[len(stripped):]
    
    if len(ints) == 0:
        return strng + '1'
    else:
        length = len(ints)
    
        new_ints = 1 + int(ints)
        new_ints = str(new_ints).zfill(length)
    
        return stripped + new_ints
#   1. Set stripped w/ strng w/o numbers at the end
#   2. Set ints w/ strng from length of stripped to the end
#   3. If length of ints is 0, return strng + '1'
#   4. Else, set length w/ length of ints
#   5. Increment new_ints by 1 and convert to an integer
#   6. Convert new_ints to a string and fill w/ zeros to the length of ints
#   7. Return stripped + new_ints