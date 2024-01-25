# -----Instructions-----
# Complete the solution so that it reverses the string passed into it.

# 'world'  =>  'dlrow'
# 'word'   =>  'drow'

# -------------------------------------------------------------------------------------
# -----Solution 1-----
def solution(string):
    # Pythonic way :)
    return string[::-1]
    
    # For beginners it's good practise 
    # to know how reverse() or [::-1]
    # works on the surface
    # for char in range(len(string)-1,-1,-1):
        #return string[char]

# -------------------------------------------------------------------------------------
# -----Solution 2-----
def solution(string):
    reversed_string = ''  # Initialize an empty string to store the reversed result
    
    for char in string:  # Loop through each character in the input string
        reversed_string = char + reversed_string  # Prepend the current character to the reversed_string
    
    return reversed_string  # Return the reversed string

# -------------------------------------------------------------------------------------

