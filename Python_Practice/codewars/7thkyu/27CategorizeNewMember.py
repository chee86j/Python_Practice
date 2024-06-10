# DESCRIPTION:
    
# The Western Suburbs Croquet Club has two categories of membership, 
# Senior and Open. They would like your help with an application form 
# that will tell prospective members which category they will be placed.

# To be a senior, a member must be at least 55 years old and have a handicap 
# greater than 7. In this croquet club, handicaps range from -2 to +26; the 
# better the player the lower the handicap.

# Input

# Input will consist of a list of pairs. Each pair contains information for 
# a single potential member. Information consists of an integer for the 
# person's age and an integer for the person's handicap.

# Output

# Output will consist of a list of string values (in Haskell and C: Open or 
# Senior) stating whether the respective member is to be placed in the senior 
# or open category.

# Example

# input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
# output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]

# -------------------------------------------------------------------------------------
# -----Solution 1-----Unpacking as a Tuple in List Comprehension-----
def open_or_senior(data):
    return ["Senior" if age >= 55 and handicap > 7 else "Open" for age, handicap in data]
#   1.  Return "Senior" if age is greater than or equal to 55 & handicap is greater 
#       than 7, else return "Open"
#   2.  Iterate through data & unpack age & handicap
#   3.  Return list of strings

# -------------------------------------------------------------------------------------
# -----Solution 2-----Similar to Solution 1 with Append-----
# This is a much more readable solution
def openOrSenior(data):
    res = []
    for i in data:
      if i[0] >= 55 and i[1] > 7:
        res.append("Senior")
      else:
        res.append("Open")
    return res
#  1.  Create an empty list to store results
#  2.  Iterate through data
#  3.  Check if age is greater than or equal to 55 & handicap is greater than 7
#  4.  Append "Senior" to res if condition is met, else append "Open"
#  5.  Return res

# -------------------------------------------------------------------------------------
# -----Solution 3-----Javascript Solution-----
# function openOrSenior(data){
#     return data.map(([age, handicap]) => age >= 55 && handicap > 7 ? 'Senior' : 'Open');
#     }

#   1.  Return "Senior" if age is greater than or equal to 55 & handicap is greater
#       than 7, else return "Open"
#   2.  Iterate through data & unpack age & handicap
#   3.  Return list of strings