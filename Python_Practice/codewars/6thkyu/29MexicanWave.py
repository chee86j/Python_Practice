# The wave (known as the Mexican wave in the English-speaking 
# world outside North America) is an example of metachronal 
# rhythm achieved in a packed stadium when successive groups 
# of spectators briefly stand, yell, and raise their arms. 
# Immediately upon stretching to full height, the spectator 
# returns to the usual seated position.

# The result is a wave of standing spectators that travels 
# through the crowd, even though individual spectators never 
# move away from their seats. In many large arenas the crowd 
# is seated in a contiguous circuit all the way around the 
# sport field, and so the wave is able to travel continuously 
# around the arena; in discontiguous seating arrangements, 
# the wave can instead reflect back and forth through the 
# crowd. When the gap in seating is narrow, the wave can 
# sometimes pass through it. Usually only one wave crest will 
# be present at any given time in an arena, although 
# simultaneous, counter-rotating waves have been produced. 

# Task

# In this simple Kata your task is to create a function that 
# turns a string into a Mexican Wave. You will be passed a 
# string and you must return that string in an array where 
# an uppercase letter is a person standing up. 

# Rules

#  1.  The input string will always be lower case but maybe 
#  empty.

#  2.  If the character in the string is whitespace then pass 
#  over it as if it was an empty seat

# Example

# wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]

# -------------------------------------------------------------------------------------
# -----Solution 1-----Comprehensive List & isalpha() & upper() & slicing & for loop & if statement-----
def wave(str):
    return [str[:i] + str[i].upper() + str[i+1:] for i in range(len(str)) if str[i].isalpha()]
#   1.  this solution uses a list comprehension to iterate through the indices of the input string
#   2.  it then creates a new string by slicing the input string up to the current index, adding 
#       the uppercase version of the character at the current index, and then adding the rest of 
#       the input string
#   3.  it only includes the new string in the result if the character at the current index is an 
#       alphabet character
#   4.  finally, it returns the result

#   Compared to solution 2, this solution is more concise and uses a list comprehension instead of 
#   a for loop to generate the result. It also uses slicing to construct the new strings instead of 
#   creating a copy of the list of characters and joining it at the end. The use of isalpha() to check 
#   if a character is an alphabet character is also more explicit than checking if it is not a space.
#   It is more readable and easier to understand the intent of the code. 

# -------------------------------------------------------------------------------------
# -----Solution 2-----For Loop & isalpha() & copy & join & upper & append-----
def wave(words):
    result = []
    chars = list(words)
    for index, char in enumerate(chars):
        if char.isalpha():
            copy = chars[:]
            copy[index] = copy[index].upper()
            result.append(''.join(copy))
    return result
#   1.  this solution uses a for loop to iterate through the characters in the input string
#   2.  if the character is an alphabet character, it creates a copy of the list of characters
#   3.  it then replaces the character at the current index with the uppercase version
#   4.  it then appends the joined copy of the list to the result
#   5.  finally, it returns the result

#   Compared to solution 1, this solution uses a for loop to iterate through the characters in the 
#   input string instead of a list comprehension. It also creates a copy of the list of characters 
#   to modify instead of slicing the input string directly. The use of join() to concatenate the 
#   characters back into a string is also different. This solution is more verbose and uses more 
#   intermediate variables, which may make it harder to read and understand. 

# -------------------------------------------------------------------------------------
# -----Solution 3-----Javascript Solution-----
# function wave(str) {
#     return str.split('').map((char, i) => {
#         if (char === ' ') return;
#         return str.slice(0, i) + char.toUpperCase() + str.slice(i + 1);
#     }).filter(Boolean);
# }
#  1.  this solution uses the split() method to convert the input string into an array of characters
#  2.  it then uses the map() method to iterate through the characters in the array
#  3.  if the character is a space, it returns undefined to filter it out later
#  4.  otherwise, it constructs a new string by slicing the input string up to the current index,
#      adding the uppercase version of the character at the current index, and then adding the rest of
#      the input string
#  5.  it then filters out the undefined values using the filter() method
#  6.  finally, it returns the result

#  This solution is similar to solution 1 in Python, but it uses the split() method to convert the input
#  string into an array of characters and the map() method to iterate through the
#  characters. It also filters out the undefined values using the filter() method. The use of arrow
#  functions and array methods makes the code more concise and expressive.
