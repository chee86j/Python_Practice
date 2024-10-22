# Complete the function that receives as input a string, 
# and produces outputs according to the following table:
# Input 	Output
# "Jabroni" 	"Patron Tequila"
# "School Counselor" 	"Anything with Alcohol"
# "Programmer" 	"Hipster Craft Beer"
# "Bike Gang Member" 	"Moonshine"
# "Politician" 	"Your tax dollars"
# "Rapper" 	"Cristal"
# anything else 	"Beer"

# Note: anything else is the default case: if the input 
# to the function is not any of the values in the table, 
# then the return value should be "Beer".

# Make sure you cover the cases where certain words do 
# not show up with correct capitalization. For example, 
# the input "pOLitiCIaN" should still return "Your tax dollars".

# -------------------------------------------------------------------------------------
# -----Solution 1-----Dictionary Lookup-----
drinks = {
    "jabroni": "Patron Tequila",
    "school counselor": "Anything with Alcohol",
    "programmer": "Hipster Craft Beer",
    "bike gang member": "Moonshine",
    "politician": "Your tax dollars",
    "rapper": "Cristal"
}

def get_drink_by_profession(s):
    return drinks.get(s.lower(), "Beer")

#   1.  Return the val of the key in the dictionary that matches the input str in lowercase
#       `drinks.get(s.lower(), "Beer")`
#   2.  If the key is not found, return "Beer" as the default val
#       `drinks.get(s.lower(), "Beer")`
#   3.  Return the result of the dictionary lookup as the output
#       `return drinks.get(s.lower(), "Beer")`

# -------------------------------------------------------------------------------------
# -----Solution 2-----Variation of Solution 1 w/dictionary literal & title case-----
def get_drink_by_profession(param):
    return {
        "Jabroni": "Patron Tequila",
        "School Counselor": "Anything with Alcohol",
        "Programmer": "Hipster Craft Beer",
        "Bike Gang Member": "Moonshine",
        "Politician": "Your tax dollars",
        "Rapper": "Cristal"
    }.get(param.title(), "Beer")
#   1.  Return the val of the key in the dictionary that matches the input str in title case
#       `{"Jabroni": "Patron Tequila", "School Counselor": "Anything with Alcohol", "Programmer": "Hipster Craft Beer", "Bike Gang Member": "Moonshine", "Politician": "Your tax dollars", "Rapper": "Cristal"}.get(param.title(), "Beer")`
#   2.  If the key is not found, return "Beer" as the default val
#       `{"Jabroni": "Patron Tequila", "School Counselor": "Anything with Alcohol", "Programmer": "Hipster Craft Beer", "Bike Gang Member": "Moonshine", "Politician": "Your tax dollars", "Rapper": "Cristal"}.get(param.title(), "Beer")`
#   3.  Return the result of the dictionary lookup as the output
#       `return {"Jabroni": "Patron Tequila", "School Counselor": "Anything with Alcohol", "Programmer": "Hipster Craft Beer", "Bike Gang Member": "Moonshine", "Politician": "Your tax dollars", "Rapper": "Cristal"}.get(param.title(), "Beer")`

#   Compared to Solution 1, this solution uses a dictionary literal instead of a var to store the drinks. 
#   It also uses the title() method to convert the input string to title case before looking it up in 
#   the dictionary. This solution is more concise and easier to read than Solution 1. It has a time 
#   complexity of O(1) since it only performs a dictionary lookup and a space complexity of O(1) since 
#   it only uses a few variables. This solution is efficient for mapping professions to drinks and returning 
#   a default value if the profession is not found in the dictionary.
    
# -------------------------------------------------------------------------------------
# -----Solution 3-----Dictionary Lookup & Title Case & If-Else Statement-----
def get_drink_by_profession(param):
    d = {"Jabroni":"Patron Tequila", "School Counselor":"Anything with Alcohol", "Programmer":"Hipster Craft Beer", "Bike Gang Member":"Moonshine", "Politician":"Your tax dollars", "Rapper":"Cristal"}
    if param.title() in d:
        return d[param.title()]
    else:
        return "Beer"
#   1.  Create a dictionary with the profession as the key & the drink as the val
#       `d = {"Jabroni":"Patron Tequila", "School Counselor":"Anything with Alcohol", 
#       "Programmer":"Hipster Craft Beer", "Bike Gang Member":"Moonshine", "Politician":"Your tax dollars", "Rapper":"Cristal"}`
#   2.  Check if the title case of the input str is in the dictionary
#       `if param.title() in d:`
#   3.  If the title case of the input str is in the dictionary, return the val of the key
#       `return d[param.title()]`
#   4.  If the title case of the input str is not in the dictionary, return "Beer" as the default val
#       `else: return "Beer"`
#   5.  Return the result of the dictionary lookup as the output
#       `return d[param.title()]`

#   Compared to Solutions 1 & 2, this solution uses an if-else statement to check if 
#   the title case of the input string is in the dictionary. It returns the corresponding 
#   drink if the profession is found in the dictionary and "Beer" as the default value 
#   if it is not found. This solution is more verbose than Solutions 1 & 2 but achieves 
#   the same result. It has a time complexity of O(1) since it only performs a dictionary 
#   lookup and a space complexity of O(1) since it only uses a few variables. This 
#   solution is efficient for mapping professions to drinks and returning a default 
#   value if the profession is not found in the dictionary.