# ---Task---

# Given a string str, reverse it and omit all non-alphabetic characters.

# ---Example---

# For str = "krishan", the output should be "nahsirk".

# For str = "ultr53o?n", the output should be "nortlu".

# ---Input/Output---

# [input] string str
# A string consists of lowercase latin letters, digits and symbols.

# [output] a string

# -------------------------------------------------------------------------------------
# -----Solution 1-----List Comprehension & Join-----
def reverse_letter(s):
  return ''.join([i for i in s if i.isalpha()])[::-1]
#   1.  Start by defining a () called reverse_letter that takes a str as input.
#   2.  Use a list comprehension to iterate through each car in the input str.
#   3.  Then the isalpha() method to check if the char is an alphabet.
#   4.  Use slicing to reverse the list of alphabets.
#   5.  Finally, join the reversed list of alphabets & return the result.

#   The time complexity of this solution is O(n) because all the operations 
#   (filtering, reversing, joining) are done in a single (linear)  pass through the input str.
#   The space complexity is also O(n) because we create a list to store the alphabetic chars.


# -------------------------------------------------------------------------------------
# -----Solution 2-----filter(), reversed(), join()-----
def reverse_letter(string):
    return ''.join(filter(str.isalpha, reversed(string)))
#   1.  We define a () called reverse_letter that takes a string as input.
#   2.  Then the reversed() function to reverse the string.
#   3.  Next we use the filter() function to filter out non-alphabetic chars.
#   4.  Then use the str.isalpha() method to check if the char is an alphabet.
#   5.  Finally, we join the filtered char & return the result.

#   The time complexity of this solution is O(n) because all the operations
#   (filtering, reversing, joining) are done in a single (linear) pass through the input string.
#   The space complexity is also O(n) because we create a list to store the alphabetic chars.
#   Compared to Solution 1, this solution is more concise & uses built-in functions to reverse the string.


# -------------------------------------------------------------------------------------
# -----Solution 3-----String Slice & Join & Generator Expression-----
def reverse_letter(string):
    return ''.join(c for c in string[::-1] if c.isalpha())
#   1.  We define a () called reverse_letter that takes a str as input.
#   2.  Then we use slicing to reverse the string.
#   3.  Next we use a generator expression to iterate through each char in the reversed str.
#   4.  Then use the isalpha() method to check if the char is an alphabet.
#   5.  Finally, we join the alphabetic char & return the result.

#   The time complexity of this solution is O(n) because all the operations
#   (filtering, reversing, joining) are done in a single (linear) pass through the input string.
#   The space complexity is also O(n) because we create a list to store the alphabetic char.
#   This solution is more concise & uses a generator expression to iterate through the reversed string.