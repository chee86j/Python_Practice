# John has invited some friends. His list is:

# s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";

# Could you make a program that
# -makes this string uppercase
# -gives it sorted in alphabetical order by last name.

# When the last names are the same, sort them by first name. 
# Last name and first name of a guest come in the result between parentheses separated by a comma.

# So the result of function meeting(s) will be:

# "(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)"

# It can happen that in two distinct families with the same family name two people have the same first name too.

# Notes:
# You can see another examples in the "Sample tests".

# -------------------------------------------------------------------------------------
# -----Solution 1-----Single Line Solution-----
def meeting(s):
    return ''.join(sorted('({1}, {0})'.format(*(x.split(':'))) for x in s.upper().split(';')))
#   1. Convert the input str to uppercase using `s.upper()`
#   2. Split the string using `s.split(';')` & iterate over the list
#   3. Use a generator to format the string in the required format
#   4. Sort the list using `sorted()`
#   5. Join the list using `join()`

#   Time Complexity: O(nlogn) - due to the sorting operation
#   Space Complexity: O(n) - to store the sorted list of tuples

# -------------------------------------------------------------------------------------
# -----Solution 2-----Using For Loop-----
def meeting(s):
  s = s.upper()
  s = s.split(';')
  array = []
  string = ""
  for i in s:
    i = i.split(':')
    string = '('+i[1]+', '+i[0]+')'
    array.append(string)
  array.sort()
  output = ""
  for j in array:
    output += j
  return output
#   1. Convert the input str to uppercase using `s.upper()`
#   2. Split the string using `s.split(';')` & iterate over the list
#   3. Split the string using `split(':')`
#   4. Format the string in the required format
#   5. Sort the list using `sort()`
#   6. Join the list using `join()`

#   Time Complexity: O(nlogn) - due to the sorting operation
#   Space Complexity: O(n) - to store the sorted list of tuples

# -------------------------------------------------------------------------------------
# -----Solution 3-----Using List Comprehension-----
def meeting(s):
    return ''.join(f'({a}, {b})' for a, b in sorted(name.split(':')[::-1] for name in s.upper().split(';')))
#   1. Convert the input str to uppercase using `s.upper()`
#   2. Split the string using `s.split(';')` & iterate over the list
#   3. Split the string using `split(':')`
#   4. Reverse the list using `[::-1]`
#   5. Sort the list using `sort()`
#   6. Join the list using `join()`

#   Time Complexity: O(nlogn) - due to the sorting operation
#   Space Complexity: O(n) - to store the sorted list of tuples

# -------------------------------------------------------------------------------------
# -----Solution 4-----JavaScript Solution-----
# function meeting(s) {
#   let string = s.toUpperCase().split(';')
#                 .map(x => x.split(':').reverse().join(', '))
#                 .sort()
#                 .join(')(')
#   return '(' + string + ')'
# }
#   1. Convert the input str to uppercase using `s.toUpperCase()`
#   2. Split the string using `split(';')` & iterate over the list
#   3. Split the string using `split(':')`
#   4. Reverse the list using `reverse()`
#   5. Sort the list using `sort()`
#   6. Join the list using `join()`

#   Time Complexity: O(nlogn) - due to the sorting operation
#   Space Complexity: O(n) - to store the sorted list of tuples

#   All four solutions have the same time & space complexity. The single line solution is the most concise & readable.
#   The easiest for beginners would be the for loop solution. The list comprehension solution is the most pythonic.
