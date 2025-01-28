# Dashatize It - https://www.codewars.com/kata/58223370aef9fc03fd000071/train/python
# Given an integer, return a string with dash '-' marks before and after 
# each odd digit, but do not begin or end the string with a dash mark.

# Ex:

# 274 -> '2-7-4'
# 6815 -> '68-1-5'

# -------------------------------------------------------------------------------------
# -----Solution 1-----List Comprehension-----
import re
def dashatize(num):
    try:
        return ''.join(['-'+i+'-' if int(i)%2 else i for i in str(abs(num))]).replace('--','-').strip('-')
    except:
        return 'None'
#   1.  Import the re module to use regular expressions.
#   2.  Use a try-except block to catch any errors that may occur.
#   3.  Use a list comprehension to iterate over each digit in the absolute 
#       value of the input number.
#       a.  If the digit is odd, add a dash before & after it.
#           'if int(i)%2' is used to check if the digit is odd.
#       b.  If the digit is even, add the digit as is.
#           'else i' is used to add the digit as is.
#   4.  Use the join() method to combine the list of characters into a single string.
#   5.  Use the replace() method to remove any double dashes that may have been created.
#           'replace('--','-')' is used to replace any double dashes w/ a single dash.
#   6.  Use the strip() method to remove any leading or trailing dashes.
#   7.  If an error occurs, return 'None'.

#   The time complexity is O(n), where n is the number of digits in the input number.
#   The space complexity is also O(n), as the list comprehension creates a new list of characters.
#   This is best for large datasets where efficiency is a concern.

# -------------------------------------------------------------------------------------
# -----Solution 2-----Iterative Replace-----
def dashatize(num):
    num_str = str(num)
    for i in ['1','3','5','7','9']:
        num_str = num_str.replace(i,'-' + i + '-')
    return num_str.strip('-').replace('--','-')
#   1.  Convert the input number to a string.
#   2.  Use a for loop to iterate over each odd digit.
#       'for i in ['1','3','5','7','9']' 
#   3.  Use the replace() method to add a dash before & after each odd digit.
#       'replace(i,'-' + i + '-')'
#   4.  Use the strip() method to remove any leading or trailing dashes.
#       'strip('-')'
#   5.  Use the replace() method to remove any double dashes that may have been created.
#       'replace('--','-')'
#   6.  Return the modified string.

#   The time complexity is O(n), where n is the number of digits in the input number.
#   The space complexity is also O(n), as the string is stored in memory.

#   Compared to the list comprehension solution, this solution is more readable & easier to underst&.
#   However, it may be less efficient due to the repeated calls to the replace() method. This is suited
#   for small datasets where efficiency is not a concern.


# -------------------------------------------------------------------------------------
# -----Solution 3-----Regex Split-----
import re

def dashatize(num):
  return 'None' if num is None else '-'.join(w for w in re.split(r'([13579])', str(abs(num))) if len(w)>0)

#   1.  Use a regular expression to split the input number into a list of strings.
#       're.split(r'([13579])', str(abs(num)))'
#   2.  Use a list comprehension to iterate over the list of strings.
#   3.  Add a dash before each odd digit.
#       'if len(w)>0' is used to exclude empty strings.
#   4.  Join the list of strings w/ dashes.
#       "'-'.join(w for w in ...)"
#   5.  If the input number is None, return 'None'.

#   The time complexity is O(n), where n is the number of digits in the input number.
#   The space complexity is also O(n), as the list of strings is stored in memory.

#   Compared to Solutions 1 & 2, this solution uses regular expressions to split the input number into a 
#   list of strings. It is concise & easy to read, but may be less efficient due to the use of regular expressions.

# -------------------------------------------------------------------------------------
# -----Solution 4-----JavaScript Solution-----
# function dashatize(num) {
#   return String(num)
#     .replace(/([13579])/g, "-$1-")
#     .replace(/--+/g, "-")
#     .replace(/(^-|-$)/g, "")
# }

#   This JavaScript solution uses regular expressions to add dashes before & after each odd digit,
#   remove any double dashes, & remove any leading or trailing dashes. The regular expressions are
#   similar to the ones used in Solution 3. The time complexity & space complexity of this solution
#   are also O(n), where n is the number of digits in the input number.

#   The time complexity is O(n), where n is the number of digits in the input number.
#   The space complexity is also O(n), as the list of strings is stored in memory.
#   This is best for general-purpose datasets
