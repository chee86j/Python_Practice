# Your team is writing a fancy new text editor and 
# you've been tasked with implementing the line numbering.

# Write a function which takes a list of strings and 
# returns each line prepended by the correct number.

# The numbering starts at 1. The format is n: string. 
# Notice the colon and space in between.

# Examples: (Input --> Output)

# [] --> []
# ["a", "b", "c"] --> ["1: a", "2: b", "3: c"]

# -------------------------------------------------------------------------------------
# -----Solution 1-----Enumerate & List Comprehension & String Formatting-----
def number(lines):
  return ['%d: %s' % v for v in enumerate(lines, 1)]
#   1.  Return a list comprehension that generates a tuple of line number and line
#   2.  The line number starts at 1 and increments by 1
#   3.  The tuple is then formatted as a string with line number followed by line
#   4.  Finally, return list of formatted strings

# -------------------------------------------------------------------------------------
# -----Solution 2-----Enumerate & List Comprehension & F-String-----
def number(lines):
    return [f"{counter}: {line}" for counter, line in enumerate(lines, start=1)]
#   1.  Return a list comprehension that generates a formatted string with line number and line
#   2.  The line number starts at 1 and increments by 1
#   3.  Return list of formatted strings

#   This solution is similar to first solution but uses f-strings for string formatting
#   The f-string is used to format string with line number and line
#   It is enclosed in curly braces and variables are inserted inside curly braces

# -------------------------------------------------------------------------------------
# -----Solution 3-----Javascript Solution-----
# var number = function(array) {
#   return array.map(function (line, index) {
#     return (index + 1) + ": " + line;
#   });
# }

#   1.  Use the map method to iterate over the array of lines
#   2.  For each line, return the line number and line as a formatted string
#   3.  The line number is the index incremented by 1
#   4.  Return the array of formatted strings