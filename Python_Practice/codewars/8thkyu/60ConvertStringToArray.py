# Write a function to split a string and convert it into an array of words.
# Examples (Input ==> Output):

# "Robin Singh" ==> ["Robin", "Singh"]

# "I love arrays they are my favorite" ==>
# ["I", "love", "arrays", "they", "are", "my", "favorite"]

# -------------------------------------------------------------------------------------
# -----Solution 1----Split w/Space Separator----
def string_to_array(string):
    return string.split(" ")
#   Using the built-in split() method, we can split the str into an arr of words 
#   by passing a space as the separator. This will split the string at each space char
#   & return an arr of words. If the input string is empty, we should return an arr 
#   containing an empty str to match the expected output. This is the most straightforward 
#   solution to the problem.

# -------------------------------------------------------------------------------------
# -----Solution 2----If Else Conditional----
def string_to_array(string=''):
    return string.split() if string else ['']
#   This solution uses a conditional expression to check if the input str is empty.
#   If the str is empty, it returns an arr containing an empty str. If the str is not empty,
#   it uses the split() method to split the str into an arr of words. As a one-liner, this
#   solution is concise & easy to read. 

# -------------------------------------------------------------------------------------
# -----Solution 3----Default Argument----
def string_to_array(string):
    return string.split() or ['']
#   This solution uses the or operator to return an empty arr if the split() method 
#   returns an empty arr. This is a concise way to handle the case where the input str is empty. 

# -------------------------------------------------------------------------------------
# -----Solution 4----Javascript Solution----
# function stringToArray(string){
#     return string.split(' ');
# }
# #   This JavaScript solution uses the split() method to split the str into an arr of words
# #   using a space as the separator. The split() method returns an arr of words, which is then
# #   returned by the function. This solution is concise & easy to read, making it a good choice
# #   for splitting a str into an arr of words.