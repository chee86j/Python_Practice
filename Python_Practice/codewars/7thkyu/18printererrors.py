# DESCRIPTION:
# In a factory a printer prints labels for boxes. For one kind of boxes 
# the printer has to use colors which, for the sake of simplicity, are 
# named with letters from a to m.

# The colors used by the printer are recorded in a control string. For 
# example a "good" control string would be aaabbbbhaijjjm meaning that 
# the printer used three times color a, four times color b, one time 
# color h then one time color a...

# Sometimes there are problems: lack of colors, technical malfunction 
# and a "bad" control string is produced e.g. aaaxbbbbyyhwawiwjjjwwm 
# with letters not from a to m.

# You have to write a function printer_error which given a string will 
# return the error rate of the printer as a string representing a rational 
# whose numerator is the number of errors and the denominator the length 
# of the control string. Don't reduce this fraction to a simpler expression.

# The string has a length greater or equal to one and contains only letters 
# from ato z.

# Examples:
# s="aaabbbbhaijjjm"
# printer_error(s) => "0/14"

# s="aaaxbbbbyyhwawiwjjjwwm"
# printer_error(s) => "8/22"

# -------------------------------------------------------------------------------------
# -----Solution 1-----Dictionary w/ numbers as keys and their string representation as values-----
def switch_it_up(n):
    return ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine'][n]
#   1. Create a dictionary with numbers as keys and their string representation as values.
#   2. Return value of key number.


# -------------------------------------------------------------------------------------
# -----Solution 2-----Similar to Solution 1, but w/numbers as keys and their string representation as values-----
def switch_it_up(number):
    number_converter={0:"Zero",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}
    return number_converter[number]
#   1. Create a dictionary named number_converter and set it equal to a dictionary with numbers as keys and their 
#      string representation as values.
#   2. Return value of key number.