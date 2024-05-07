# DESCRIPTION:
# Take an array and remove every second element from the array. 
# Always keep the first element and start removing with the next 
# element.

# Example:
# ["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> 
# ["Keep", "Keep", "Keep", ...]

# None of the arrays will be empty, so you don't have to 
# worry about that!

# -----Solution 1-----List Slicing-----
def remove_every_other(my_list):
    return my_list[::2]
#   Simply using python's list slicing feature to return the list with 
#   every 2nd element removed
#   [::2] means start at the beginning of the list and take every 2nd element

# -----Solution 2-----For Loop & Append-----
def remove_every_other(my_list):
    r=[]
    for i in range(0,len(my_list)):
        if i%2==0:
            r.append(my_list[i])
    return r
#  1.   Create an empty list r
#  2.   Loop through the list using the range function
#  3.   If the idx is even, use python's append method 
#       to add the element to the list r
#  4.   Return the list r