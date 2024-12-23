# Happy Holidays fellow Code Warriors!

# Santa's senior gift organizer Elf developed a way to represent up to 26 gifts by 
# assigning a unique alphabetical character to each gift. After each gift was assigned 
# a character, the gift organizer Elf then joined the characters to form the gift ordering code.

# Santa asked his organizer to order the characters in alphabetical order, but the Elf 
# fell asleep from consuming too much hot chocolate and candy canes! Can you help him out?

# Sort the Gift Code
# Write a function called sortGiftCode/sort_gift_code/SortGiftCode that accepts a string 
# containing up to 26 unique alphabetical characters, and returns a string containing the 
# same characters in alphabetical order.

# Examples (Input -- => Output):

# "abcdef"                      -- => "abcdef"
# "pqksuvy"                     -- => "kpqsuvy"
# "zyxwvutsrqponmlkjihgfedcba"  -- => "abcdefghijklmnopqrstuvwxyz"

# -------------------------------------------------------------------------------------
# -----Solution 1-----Using sorted()-----
def sort_gift_code(code):
    return ''.join(sorted(code))
#   1. Using sorted() function, we can sort the string in alphabetical order.
#   2. sorted() function returns a list of sorted characters.
#   3. We can join the list of sorted characters into a string using join() function.
#   4. Return the sorted string.

#   Time complexity is O(nlogn) where n is the length of the input string.
#   Space complexity is O(n) where n is the length of the input string.

#   This is the most efficient solution for this problem because it uses the built-in
#   sorted() function which is optimized for sorting strings and lists. It is also the
#   most readable solution.

# -------------------------------------------------------------------------------------
# -----Solution 2-----Using list.sort()-----
def sort_gift_code(code):
    code_list = list(code)  # Convert string to list
    code_list.sort()        # Sort the list in-place
    return ''.join(code_list)  # Join sorted list into a string
#   1. Convert the input string into a list of characters.
#   2. Use the sort() method to sort the list in-place.
#   3. Join the sorted list into a string using join() method.
#   4. Return the sorted string.

#   Time complexity is O(nlogn) where n is the length of the input string.
#   Space complexity is O(n) where n is the length of the input string.

#   This solution is similar to the previous one, but it uses the sort() method to sort
#   the list in-place. This is slightly less efficient than using the sorted() function
#   because the sort() method modifies the original list, while the sorted() function
#   creates a new sorted list.
    
# -------------------------------------------------------------------------------------
# -----Solution 3-----Manual Sorting-----
def sort_gift_code(code):
    return ''.join(sorted([char for char in code]))
#   1. Use a list comprehension to create a list of characters from the input string.
#   2. Sort the list of characters using the sorted() function.
#   3. Join the sorted list into a string using the join() function.
#   4. Return the sorted string.

#   Time complexity is O(nlogn) where n is the length of the input string.
#   Space complexity is O(n) where n is the length of the input string.

#   This solution is similar to the first one, but it uses a list comprehension to create
#   the list of characters. It is less efficient than the first solution and the second
#   solution because it creates an intermediate list. However, it is still a valid and
#   readable solution.

# -------------------------------------------------------------------------------------
# -----Solution 4-----JavaScript Solution-----
# function sortGiftCode(code) {
#   return code.split('').sort().join('');
# }

#   This is the JavaScript equivalent of the first solution. It uses the split() method
#   to convert the input string into an array of characters, the sort() method to sort
#   the array, and the join() method to convert the sorted array back into a string.
