# Filter the number
# Oh, no! The number has been mixed up with the text. Your goal is to retrieve the 
# number from the text, can you return the number back to its original state?

# Task
# Your task is to return a number from a string.

# Details
# You will be given a string of numbers and letters mixed up, you have to return 
# all the numbers in that string in the order they occur.

# -----------------------------------------------------------------------------------------
# -----Solution 1-----Filter & Str.isdigit-----
def filter_string(string):
    return int(''.join(filter(str.isdigit, string)))
#   i.e.  filter_string("a1b2c3") => 123
#   1.  Define filter_string that takes a single argument to check if the string 
#       is a digit. 
#           'a1b2c3' is the string that will be passed to the function.
#   2.  Filter() applies the str.isdigit method to the string to remove non-digit
#       characters.
#           '1', '2', and '3' are the digits that remain after filtering.
#   3.  Join() concatenates the remaining digits into a single string.
#           '123' is the result of joining the digits.
#   4.  The int() function converts the string of digits into an integer.
#           123 is the final result that is returned.

#   The time complexity of this solution is O(n), since we iterate through the 
#   string once to filter out the digits, where n is the length of the string.
#   The space complexity is also O(n), as we create a new string to store the
#   filtered digits.

# -----------------------------------------------------------------------------------------
# -----Solution 2-----List Comprehension & Str.isdigit-----
def filter_string(string):
    return int(''.join(a for a in string if a.isdigit()))
#   i.e.  filter_string("a1b2c3") => 123
#   1.  Define filter_string that takes a single argument to check if the string
#       is a digit.
#           'a1b2c3' is the string that will be passed to the function.
#   2.  List comprehension iterates through each character in the string, keeping
#       only the digits.
#           '1', '2', and '3' are the digits that remain after filtering.
#   3.  Join() concatenates the remaining digits into a single string.
#           '123' is the result of joining the digits.

#   The time complexity and space complexity of this solution are the same as the
#   previous solution, O(n), where n is the length of the string.

#   Compared to Solution 1, this solution is slightly faster than the filter()
#   since it avoids an extra function call.

# -----------------------------------------------------------------------------------------
# -----Solution 3-----Regex-----
import re
def filter_string(string):
    nb = re.sub(r'\D', '' ,string)
    return int(nb)
#   i.e.  filter_string("a1b2c3") => 123
#   1.  Define filter_string that takes a single argument to check if the string
#       is a digit.
#           'a1b2c3' is the string that will be passed to the function.
#   2.  The re.sub() function replaces all non-digit characters in the string with
#       an empty string.
#           '123' is the result of removing the non-digit characters.
#   3.  The int() function converts the string of digits into an integer.
#           123 is the final result that is returned.

#   The time complexity of this solution is O(n), but is slightly slower than the
#   filter() or list comprehension solutions due to the overhead of regular
#   expression processing. The space complexity is also O(n), as we create a new
#   string to store the filtered digits.

#   Compared to the previous solutions, this solution is usefeul for complex patterns,
#   but is slower for simple filtering tasks whereas filter() or list comprehension
#   is more efficient.

# -----------------------------------------------------------------------------------------
# -----Solution 4-----JavaScript Solution-----
# let filterString = function(value) {
# return +value.replace(/\D/g, '')
# }

#   1.  This solution is a JavaScript solution that uses a regular expression to
#       remove all non-digit characters from a string.
#   2.  The replace() method replaces all non-digit characters in the string with
#       an empty string.
#   3.  The unary plus operator (+) is used to convert the resulting string of
#       digits into a number.
#   4.  The resulting number is then returned.

#   This solution is similar to the regex solution in Python, but it is more 
#   concise due to the use of the unary plus operator (+) for type conversion.
#   It is also more flexible because it can be used on any string, rather than
#   just the name argument. Note that in Javascript it is more efficient to use
#   compared to Python due to the overhead of regular expression processing.