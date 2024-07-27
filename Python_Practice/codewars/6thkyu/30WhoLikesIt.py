# You probably know the "like" system from Facebook and other pages. 
# People can "like" blog posts, pictures or other items. We want to 
# create the text that should be displayed next to such an item.

# Implement the function which takes an array containing the names 
# of people that like an item. It must return the display text as 
# shown in the examples:

# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

# Note: For 4 or more names, the number in "and 2 others" simply increases.

# -------------------------------------------------------------------------------------
# -----Solution 1-----Dictionary & String Formatting & Ternary Operator & Unpacking-----
def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)
#   1.  The function uses a dictionary to map the number of names to the appropriate
#       output string
#   2.  The 'min(4, n)' function is used to ensure that the number of names does not
#       exceed 4
#   3.  The 'format(*names[:3], others=n-2)' function is used to format the string
#       according to the number of names in the array
#   4.  The '*names[:3]' is used to unpack the first 3 names in the names array
#   5.  The 'others=n-2' is used to store the number of other names in the array
#   6.  This solution is efficient, easy to read and has a time complexity of O(1) and
#       string formatting are constant time operations

# -------------------------------------------------------------------------------------
# -----Solution 2-----If-Elif-Else Statements & String Formatting-----
def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return "%s likes this" % names[0]
    elif len(names) == 2:
        return "%s and %s like this" % (names[0], names[1])
    elif len(names) == 3:
        return "%s, %s and %s like this" % (names[0], names[1], names[2])
    else:
        return "%s, %s and %s others like this" % (names[0], names[1], len(names)-2)
#   1.  Using a series of if-elif-else statements to check the length of the names array
#       we can return the appropriate string
#   2.  The % operator is used for string formatting
#   3.  The len(names) is used to get the length of the names array
#   4.  The names[0], names[1], names[2] are used to get the
#       first, second and third names in the names array
#   5.  The len(names)-2 is used to get the number of other names in the array
#   6.  This solution is efficient with a time complexity of O(1), but involves
#       multiple conditional statements which can be hard to read and maintain

# -------------------------------------------------------------------------------------
# -----Solution 3-----Dictionary-Based Approach with Additional Length Calculation-----
def likes(names):
    d = {
        0: "no one likes this",
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        4: "{}, {} and {others} others like this"
        }
    length = len(names)
    return d[min(4, length)].format(*names, others = length - 2)
#   1.  Similar to the first solution, this solution uses a dictionary to map
#       the number of names to the appropriate output string
#   2.  The 'length = len(names)' is used to store the length of the names array
#   3.  The 'd[min(4, length)].format(*names, others = length - 2)' is used to format
#       the string according to the number of names in the array
#   4.  The '*names' is used to unpack all the names in the names array
#   5.  The 'others = length - 2' is used to store the number of other names in the array
#   6.  This solution is efficient, easy to read and has a time complexity of O(1)

# -------------------------------------------------------------------------------------
# -----Solution 4-----Javascript Solution-----Switch Statement-----
# function likes(names) {
#     names = names || [];
#     switch(names.length){
#         case 0: return 'no one likes this'; break;
#         case 1: return names[0] + ' likes this'; break;
#         case 2: return names[0] + ' and ' + names[1] + ' like this'; break;
#         case 3: return names[0] + ', ' + names[1] + ' and ' + names[2] + ' like this'; break;
#         default: return names[0] + ', ' + names[1] + ' and ' + (names.length - 2) + ' others like this';
#     }
# }

#   1.  We start with a default empty array if the names array is not provided
#       'names = names || []' ensures that we have an array to work with
#   2.  The switch statement is used to check the length of the names array
#       and return the appropriate string
#   3.  The 'break' statement is used to exit the switch statement after each case
#   4.  The default case is used to handle arrays with more than 3 names
#       -0 Names are returned as 'no one likes this'
#       -1 Name is returned as 'name likes this'
#       -2 Names are returned as 'name1 and name2 like this'
#       -3 Names are returned as 'name1, name2 and name3 like this'
#       -4 or more names are returned as 'name1, name2 and x others like this'
#   5.  This solution is efficient and easy to read, but the switch statement
#       can be less readable than if-elif-else statements