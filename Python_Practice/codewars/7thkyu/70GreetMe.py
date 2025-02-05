# Write a method that takes one argument as name and then greets that name, 
# capitalized and ends with an exclamation point.

# Example:

# "riley" --> "Hello Riley!"
# "JACK"  --> "Hello Jack!"

# -----------------------------------------------------------------------------------------
# -----Solution 1-----title() Method-----
def greet(name): 
    return f'Hello {name.title()}!'
#   1.  We start by defining a function called greet that takes a single argument 
#       called name.
#   2.  We then use an f-string to return the string "Hello" followed by the name
#       argument with the title() method applied to it. The title() method capitalizes
#       the first letter of each word in a string.
#   3.  We then add an exclamation point to the end of the string and return the result.

#   The time and space complexity of this solution is O(n) since the title() method is
#   applied to the name argument, where n is the length of the name string created.

#   This solution is the most efficient and concise of the three solutions presented because
#   of the built-in title() method. It is also the most readable and easy to understand.

# -----------------------------------------------------------------------------------------
# -----Solution 2-----capitalize() Method-----
def greet(name):
    return f"Hello {name.capitalize()}!"
#   1.  We start by defining a function called greet that takes a single argument
#       called name.
#   2.  We then use an f-string to return the string "Hello" followed by the name
#       argument with the capitalize() method applied to it. The capitalize() method
#       capitalizes the first letter of a string.
#   3.  We then add an exclamation point to the end of the string and return the result.

#   The time and space complexity of this solution is O(n) since the capitalize() method
#   is applied to the name argument, where n is the length of the name string created.

#   This solution is less efficient than the title() method because it only capitalizes
#   the first letter of the name string, rather than the first letter of each word. However,
#   it is still a valid and readable solution.

# -----------------------------------------------------------------------------------------
# -----Solution 3-----JavaScript Solution-----
# String.prototype.capitalize = function() {
#     return this.charAt(0).toUpperCase() + this.slice(1).toLowerCase();
# }

# var greet = function(name) {
# return "Hello " + name.capitalize() + "!";
# };

#   1.  This solution is a JavaScript solution that uses a prototype method to capitalize
#       the first letter of a string. This bakes in the capitalize() method to the String
#       prototype so that it can be called on any string.
#   2.  The capitalize() method returns the first letter of the string capitalized, followed
#       by the rest of the string in lowercase.
#   3.  The greet function then uses the capitalize() method to capitalize the first letter
#       of the name argument and returns the result with the string "Hello" and an exclamation
#       point.

#   This solution is similar to the capitalize() method in Solution 2, but it is more flexible
#   because it can be used on any string, rather than just the name argument. It is also more
#   verbose and less readable than the other solutions.