# Kids drink toddy.
# Teens drink coke.
# Young adults drink beer.
# Adults drink whisky.
# Make a function that receive age, and return what they drink.

# Rules:

# Children under 14 old.
# Teens under 18 old.
# Young under 21 old.
# Adults have 21 or more.
# Examples: (Input --> Output)

# 13 --> "drink toddy"
# 17 --> "drink coke"
# 18 --> "drink beer"
# 20 --> "drink beer"
# 30 --> "drink whisky"

# -------------------------------------------------------------------------------------
# -----Solution 1-----If Statements-----
def people_with_age_drink(age):
    if age > 20: return "drink whisky"
    if age > 17: return "drink beer"
    if age > 13: return "drink coke"
    return "drink toddy"
#   1. Check if the age is greater than 20
#       - If the age is greater than 20, return "drink whisky"
#       - If the age is greater than 17, return "drink beer"
#       - If the age is greater than 13, return "drink coke"
#       - If the age is less than or equal to 13, return "drink toddy"
#   This is the most clear & concise solution with a time complexity of O(1) & a space
#   complexity of O(1). Each condition directly returns the appropriate drink based on
#   the age.


# -------------------------------------------------------------------------------------
# -----Solution 2-----If & Elif Statements-----
def people_with_age_drink(age):
    if age <= 13:
        beverage = 'toddy'
    elif age > 13 and age <= 17:
        beverage = 'coke'
    elif age > 17 and age <= 20:
        beverage = 'beer'
    elif age > 20:
        beverage = 'whisky'
    return 'drink ' + beverage
#   1. Check if the age is less than or equal to 13
#       - If the age is less than or equal to 13, set the beverage to 'toddy'
#       - Else if the age is greater than 13 and less than or equal to 17, set the
#         beverage to 'coke'
#       - Else if the age is greater than 17 and less than or equal to 20, set the
#         beverage to 'beer'
#       - Else if the age is greater than 20, set the beverage to 'whisky'
#   2. Return the drink and beverage
#       - Return the drink and beverage by concatenating the strings
#   This solution is more verbose than the 1st solution, but it is still clear & concise
#   with a time complexity of O(1) & a space complexity of O(1). Each condition sets the
#   appropriate beverage based on the age.

# -------------------------------------------------------------------------------------
# -----Solution 3-----Single Line If Statements-----
def people_with_age_drink(age):
    return 'drink ' + ('toddy' if age < 14 else 'coke' if age < 18 else 'beer' if age < 21 else 'whisky')
#   1. Return the drink and beverage
#       - Return the drink and beverage by using a single line if statement
#       - If the age is less than 14, return 'toddy'
#       - Else if the age is less than 18, return 'coke'
#       - Else if the age is less than 21, return 'beer'
#       - Else return 'whisky'
#   This solution is condensed using nested ternary operators to return the appropriate
#   beverage based on the age. It is the most concise solution with a time complexity of
#   O(1) & a space complexity of O(1) although it is less readable than the 1st & 2nd.

# -------------------------------------------------------------------------------------
# -----Solution 4-----Javascript Solution-----Arrow Function & Ternary Operator-----
# const peopleWithAgeDrink = (age) => {
#     age < 14 ? 'drink toddy' : age < 18 ? 'drink coke' : age < 21 ? 'drink beer' : 'drink whisky';
# }
#   1. Return the drink and beverage
#       - Return the drink and beverage by using a single line arrow function
#       - If the age is less than 14, return 'drink toddy'
#       - Else if the age is less than 18, return 'drink coke'
#       - Else if the age is less than 21, return 'drink beer'
#       - Else return 'drink whisky'
#   This solution is a direct translation of the 3rd solution into Javascript. It is the
#   most concise solution with a time complexity of O(1) & a space complexity of O(1).
