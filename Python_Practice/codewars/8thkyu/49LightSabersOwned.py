# Inspired by the development team at Vooza, write the function that

# accepts the name of a programmer, and
# returns the number of lightsabers owned by that person.
# The only person who owns lightsabers is Zach, by the way. 
# He owns 18, which is an awesome number of lightsabers. Anyone else owns 0.

# Note: your function should have a default parameter.

# For example(Input --> Output):

# "anyone else" --> 0
# "Zach" --> 18

# -------------------------------------------------------------------------------------
# -----Solution 1-----
def how_many_light_sabers_do_you_own(name=""):
    return 18 if name == "Zach" else 0
#   1.  The () takes in a string name with a default value of ""
#   2.  The () returns the number of lightsabers owned by the person with the given name
#   3.  If the name is "Zach", the () returns 18
#   4.  Otherwise, the () returns 0
#

# -------------------------------------------------------------------------------------
# -----Solution 2-----Javascript Solution-----
# function howManyLightsabersDoYouOwn(name) {
#     return name === 'Zach' ? 18 : 0;
# }
#    1.  The ()) howManyLightsabersDoYouOwn takes in a string name
#    2.  It returns the number of lightsabers owned by the person with the given name
#    3.  If the name is "Zach", the ()) returns 18
#    4.  Otherwise, the ()) returns 0
#    5.  This solution is concise & uses a ternary operator to return the correct number of lightsabers
