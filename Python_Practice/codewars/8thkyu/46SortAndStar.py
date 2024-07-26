# You will be given a list of strings. You must sort it 
# alphabetically (case-sensitive, and based on the ASCII 
# values of the chars) and then return the first value.

# The returned value must be a string, and have "***" 
# between each of its letters.

# You should not remove or add elements from/to the array.

# -------------------------------------------------------------------------------------
# -----Solution 1-----min() & join()-----
def two_sort(lst):
    return '***'.join(min(lst))
#   1.  this solution uses the min() function to find the smallest string in the list, 
#       which is built-in to Python.
#   2.  then, it uses the join() function to join the characters of the string with '***'
#       between each character. 
#   This solution is the most efficient because it only requires the least amount of 
#   code to complete the task compared to other solutions.
# -------------------------------------------------------------------------------------
# -----Solution 2-----
def two_sort(array):
    return '***'.join(sorted(array)[0])
#   1.  this solution uses the sorted() function to sort the list of strings, which is 
#       automatically sorted alphabetically and case-sensitive.
#   2.  then, it uses the join() function to join the characters of the first string in 
#       the sorted list with '***' between each character.

# -------------------------------------------------------------------------------------
# -----Solution 3-----Javascript Solution-----
# function twoSort(s) {
#     return s.sort()[0].split('').join('***');
# }

#   1.  this solution uses the sort() function to sort the list of strings, which is 
#       automatically sorted alphabetically and case-sensitive.
#   2.  then, it uses the split() function to split the characters of the first string
#       in the sorted list.
#   3.  finally, it uses the join() function to join the characters of the first string
