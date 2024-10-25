# Description:
# Create a function that accepts a string and a single character, 
# and returns an integer of the count of occurrences the 2nd 
# argument is found in the first one.

# If no occurrences can be found, a count of 0 should be returned.

# ("Hello", 'o')  =>  1
# ("Hello", 'l')  =>  2
# ("", 'z')       =>  0

# Notes:
# The first argument can be an empty string
# In languages with no distinct character data type, the second argument 
# will be a string of length 1

# -------------------------------------------------------------------------------------
# -----Solution 1-----Count Method-----
def str_count(string, letter):
    return string.count(letter)
#   1.  Using the built-in count method of strings, we can easily count the occurrences 
#       of a character in a string.

#   This has a time complexity of O(n) where n is the length of the string, as the count
#   method iterates over the string to count the occurrences of the character. The space
#   complexity is O(1) as we are not using any additional space besides the few variables.

# -------------------------------------------------------------------------------------
# -----Solution 2-----For Loop-----
def str_count(strng, letter):
    counter = 0
    
    for chr in strng:
        if chr == letter:
            counter += 1
        
    return counter
#   1.  This involves the manual counting of occurrences of a character in a string using 
#       a for loop.
#   2.  We initialize a counter variable to 0 and iterate over each character in the string.
#   3.  If the character matches the given letter, we increment the counter.
#   4.  Finally, we return the counter value, which represents the number of occurrences of
#       the letter in the string.

#   This has a time complexity of O(n) where n is the length of the string, as we iterate over
#   each character in the string. The space complexity is O(1) as we are not using any additional
#   space besides the few variables. Definitely a more verbose approach compared to the count method.

# -------------------------------------------------------------------------------------
# -----Solution 3-----Direct Comparison-----
strCount = str.count
#   This is the shorthand version of the count method, which is a built-in method for strings.
#   It is a concise way to count the occurrences of a character in a string. It has a time
#   complexity of O(n) where n is the length of the string, as the count method iterates over
#   the string to count the occurrences of the character. The space complexity is O(1) as we are
#   not using any additional space besides the few variables.

# -------------------------------------------------------------------------------------
# -----Solution 4-----Javascript Version-----
# function strCount(str, letter){
#   return str.split(letter).length - 1;
# }

#   1.  This solution uses the split method to split the string at the given letter.
#   2.  The length of the resulting array minus 1 gives the count of occurrences of the letter.
#   3.  This approach works because the split method removes the letter from the string,
#       so the length of the array will be one more than the number of occurrences of the letter.

#   The time complexity of this solution is O(n) where n is the length of the string, as the
#   split method iterates over the string to split it at the given letter. The space complexity
#   is O(n) as the split method creates a new array to store the split parts of the string.

