# Create a method that takes as input a name, city, and state to welcome a person. 
# Note that name will be an array consisting of one or more values that should be 
# joined together with one space between each, and the length of the name array 
# in test cases will vary.

# Example:

# ['John', 'Smith'], 'Phoenix', 'Arizona'

# This example will return the string Hello, John Smith! Welcome to Phoenix, Arizona!

def say_hello(name, city, state):
    return f"Hello, {' '.join(name)}! Welcome to {city}, {state}!"

#  This method takes in three arguments: a list of names, a city, and a state.
#  The list of names is joined together with a space in between each name.
#  The city and state are concatenated with the names and returned as a string.
#  The f-string is used to format the string with the values of the variables,
#  in which the list of names is joined together with a space in between each name.