# Make a program that filters a list of strings and 
# returns a list with only your friends name in it.

# If a name has exactly 4 letters in it, you can be 
# sure that it has to be a friend of yours! Otherwise, 
# you can be sure he's not...

# Input = ["Ryan", "Kieran", "Jason", "Yous"]
# Output = ["Ryan", "Yous"]

# Input = ["Peter", "Stephen", "Joe"]
# Output = []

# Input strings will only contain letters. Note: keep 
# the original order of the names in the output.

# -------------------------------------------------------------------------------------
# -----Solution 1-----List Comprehension-----
def friend(x):
    return [i for i in x if len(i) == 4]
#   1. Create a list comprehension that iterates through the list
#      over each element 'i' in the list 'x' w/ for loop.
#   2. For each name 'i', it checks if 'len(i)' is equal to 4.
#   3. The name is included in the list if the condition is met.
#   4. This has a time complexity of O(n) where n is the length of the list 'x' and a
#      space complexity of O(n) where n is the length of the list 'x'.
#      It is efficent for small lists but not for large lists.  


# -------------------------------------------------------------------------------------
# -----Solution 2-----For Loop-----
def friend(x):
    names = []
    for name in x:
        if len(name) == 4:
            names.append(name)
    return names
#   1. Create an empty list 'names' to store the names that meet the condition.
#   2. Iterate through the list 'x' using a for loop.
#   3. For each name in the list, check if the length of the name is equal to 4 w/len().
#   4. If the condition is met, append the name to the 'names' list.
#   5. Return the 'names' list.
#   6. This has a time complexity of O(n) where n is the length of the list 'x' and a
#      space complexity of O(n) where n is the length of the list 'x'.
#      It is efficent for small lists but not for large lists and is useful for more
#      complex filtering conditions.

# -------------------------------------------------------------------------------------
# -----Solution 3----Javascript Solution-----
# function friend(friends){
#     return friends.filter(n => n.length === 4)
# }
#   1. This is the same as Solution 1 but in Javascript.
#   2. The filter() method creates a new array with all elements that pass the test
#      implemented by the provided function.
#   3. The arrow function 'n => n.length === 4' is the test function that checks if the
#      length of the name is equal to 4.
#   4. The filter() method returns a new array with the names that meet the condition.
#   5. This has a time complexity of O(n) where n is the length of the list 'friends' and a
#      space complexity of O(n) where n is the length of the list 'friends'.
#      It is efficent for small lists but not for large lists.
