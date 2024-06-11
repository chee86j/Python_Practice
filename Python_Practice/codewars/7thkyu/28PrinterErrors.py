# In a factory a printer prints labels for boxes. For one 
# kind of boxes the printer has to use colors which, for 
# the sake of simplicity, are named with letters from a 
# to m.

# The colors used by the printer are recorded in a control 
# string. For example a "good" control string would be 
# aaabbbbhaijjjm meaning that the printer used three times 
# color a, four times color b, one time color h then one 
# time color a...

# Sometimes there are problems: lack of colors, technical 
# malfunction and a "bad" control string is produced 
# e.g. aaaxbbbbyyhwawiwjjjwwm with letters not from a to m.

# You have to write a function printer_error which given a 
# string will return the error rate of the printer as a 
# string representing a rational whose numerator is the 
# number of errors and the denominator the length of the 
# control string. Don't reduce this fraction to a simpler 
# expression.

# The string has a length greater or equal to one and 
# contains only letters from ato z.
# Examples:

# s="aaabbbbhaijjjm"
# printer_error(s) => "0/14"

# s="aaaxbbbbyyhwawiwjjjwwm"
# printer_error(s) => "8/22"

# -------------------------------------------------------------------------------------
# -----Solution 1----sub(), format(), and len()----
# -----One-liner with not so readable code----
from re import sub
def printer_error(s):
    return "{}/{}".format(len(sub("[a-m]",'',s)),len(s))
# sub() - This function is used to replace all occurences of a pattern in a str w/ a replacement.
# format() - This function formats a string into a nicer output.
# len() - This function returns the length of an object.
#   1. Use the sub() function to replace all the letters in the
#      string that are not between 'a' and 'm' with an empty string.
#   2. Use format() function to format the output of the string 's' where '{}' is 
#      replaced by the number of errors and the length of the string.
#   3. Finally, we return the formatted string.


# -------------------------------------------------------------------------------------
# -----Solution 2----format(), len(), for loop, and if statement with list comprehension----
# -----One-liner with better readable code----
def printer_error(s):
    return "{}/{}".format(len([x for x in s if x not in "abcdefghijklm"]), len(s))
#   1. List comprehension to iterate through each char in 's' and check if the char is 
#      not in the string 'abcdefghijklm'.
#   2. Format the output of the string 's' where '{}' is replaced by the number of errors
#      and the length of the string 's'.
#   3. Finally, we return the formatted string that represents the error rate of the printer.

# -------------------------------------------------------------------------------------
# -----Solution 3-----For Loop, Unicode Values & Concatenation-----
# -----When you try to compare 2 symbols, Python actually compare their decimal number in 
# Unicode table: https://en.wikipedia.org/wiki/List_of_Unicode_characters-----
def printer_error(s):
    errors = 0
    count = len(s)
    for i in s:
        if i > "m":
            errors += 1
    return str(errors) + "/" + str(count)
#   1. Initialize two variables 'errors' and 'count' to 0 and the length of the string 's'.
#   2. Iterate through each character in the string 's' with a for loop.
#   3. If the character is greater than 'm', increment the 'errors' variable by 1.
#   4. Return the errors and the count of the string 's' as a string by concatenating the two.

# -------------------------------------------------------------------------------------
# -----Solution 4-----JavaScript Solution-----For Loops and Unicode Values-----

# function printerError(s) {
#     var count = 0;
#     for (var i = 0; i < s.length; i++) {
#         if (s[i] > "m") {
#             count++;
#         }
#     }
#     return count + "/" + s.length;
# }

#   1. Initialize a variable 'count' to 0.
#   2. Iterate through each character in the string 's' with a for loop.
#   3. If the character is greater than 'm' (it does this by comparing
#      the character's unicode value.), increment the 'count' variable by 1.
#   4. Return the count and the length of the string 's' as a string by concatenating the two.
