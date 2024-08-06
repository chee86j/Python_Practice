# Once upon a time, on a way through the old wild mountainous west,…

# … a man was given directions to go from one point to another. The 
# directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" 
# and "SOUTH" are opposite, "WEST" and "EAST" too.

# Going to one direction and coming back the opposite direction right 
# away is a needless effort. Since this is the wild west, with dreadful 
# weather and not much water, it's important to save yourself some 
# energy, otherwise you might die of thirst!
# How I crossed a mountainous desert the smart way.

# The directions given to the man are, for example, the following 
# (depending on the language):

# ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].
# or
# { "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" };
# or
# [North, South, South, East, West, North, West]

# You can immediately see that going "NORTH" and immediately "SOUTH" 
# is not reasonable, better stay to the same place! So the task is to 
# give to the man a simplified version of the plan. A better plan in 
# this case is simply:

# ["WEST"]
# or
# { "WEST" }
# or
# [West]

# Other examples:

# In ["NORTH", "SOUTH", "EAST", "WEST"], the direction "NORTH" + "SOUTH" 
# is going north and coming back right away.

# The path becomes ["EAST", "WEST"], now "EAST" and "WEST" annihilate 
# each other, therefore, the final result is [] (nil in Clojure).

# In ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"], "NORTH" and "SOUTH" 
# are not directly opposite but they become directly opposite after the 
# reduction of "EAST" and "WEST" so the whole path is reducible to ["WEST", "WEST"].

# TASK

# Write a function dirReduc which will take an array of strings and returns an array 
# of strings with the needless directions removed (W<->E or S<->N side by side).

#     *The Haskell version takes a list of directions with data Direction = North | East | West | South.
#     *The Clojure version returns nil when the path is reduced to nothing.
#     *The Rust version takes a slice of enum Direction {North, East, West, South}.

# See more examples in "Sample Tests:"

# Notes

#     Not all paths can be made simpler. The path ["NORTH", "WEST", "SOUTH", "EAST"] is not reducible. 
#     "NORTH" and "WEST", "WEST" and "SOUTH", "SOUTH" and "EAST" are not directly opposite of each other 
#     and can't become such. Hence the result path is itself : ["NORTH", "WEST", "SOUTH", "EAST"].

# -------------------------------------------------------------------------------------
# -----Solution 1-----Dictionary to Map Opposite Directions-----
opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}

def dirReduc(plan):
    new_plan = []
    for d in plan:
        if new_plan and new_plan[-1] == opposite[d]:
            new_plan.pop()
        else:
            new_plan.append(d)
    return new_plan
#   1.  The () uses a dictionary to map the opposite directions
#   2.  An empty list new_plan is initialized to store the simplified plan
#   3.  The () iterates through each direction in the input plan
#   4.  If the new_plan is not empty and the last direction in the new_plan is the opposite
#       of the current direction, the last element is removed
#   5.  Otherwise, the current direction is added to the new_plan
#   6.  The () returns the simplified plan after processing all directions
#   7.  This solution has a time complexity of O(n) where n is the number of directions in the input plan
#   8.  The space complexity is O(n) as the new_plan can store up to n directions
    
# -------------------------------------------------------------------------------------
# -----Solution 2-----Joins Directions into String, Removes Opposite Directions, Splits String Back into List-----
def dirReduc(arr):
    dir = " ".join(arr)
    dir2 = dir.replace("NORTH SOUTH",'').replace("SOUTH NORTH",'').replace("EAST WEST",'').replace("WEST EAST",'')
    dir3 = dir2.split()
    return dirReduc(dir3) if len(dir3) < len(arr) else dir3
#   1.  The () joins the directions in the input array into a single string
#   2.  The () replaces all opposite directions with an empty string
#   3.  The () splits the string back into a list of directions
#   4.  The () recursively calls itself with the new list of directions if the length
#       of the new list is less than the length of the original list
#   5.  Otherwise, the () returns the new list of directions
#   6.  This solution is inefficient as it uses string manipulation to remove opposite directions
#   7.  The time complexity is O(n^2) due to the repeated string replacements
#   8.  The space complexity is O(n) as the () uses additional space to store the simplified plan

# -------------------------------------------------------------------------------------
# -----Solution 3-----List Slicing & Recursion to Remove Opposite Directions-----
def dirReduc(arr):
    opposites = [{'NORTH', 'SOUTH'}, {'EAST', 'WEST'}]
    
    for i in range(len(arr)-1):
        if set(arr[i:i+2]) in opposites:
            del arr[i:i+2]
            return dirReduc(arr)
    
    return arr
#   1.  The () defines a list of sets opposites containing the opposite directions
#   2.  It then iterates through the input array using a for loop
#   3.  It then checks if the set of directions at index i and i+1 is in the opposites list
#   4.  If the set is in opposites, it removes the directions at index i and i+1 using del
#   5.  It then recursively calls itself with the updated array
#   6.  If no opposite directions are found, the () returns the array
#   7.  This solution is also inefficient as it uses recursion and list slicing to remove opposite directions
#   8.  The time complexity is O(n^2) due to the repeated list slicing
#   9.  The space complexity is O(n) as the () uses additional space to store the simplified plan

# -------------------------------------------------------------------------------------
# -----Solution 4-----Javascript Solution-----Reduce Method-----
# function dirReduc(plan) {
#   var opposite = {
#     'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'};
#   return plan.reduce(function(dirs, dir){
#       if (dirs[dirs.length - 1] === opposite[dir])
#         dirs.pop();
#       else
#         dirs.push(dir);
#       return dirs;
#     }, []);
# }

#   1.  The () uses an array reduce method to simplify the plan
#   2.  It defines an array of opposite directions
#   3.  The reduce method iterates through the plan array
#   4.  If the last direction in the dirs array is the opposite of the current direction,
#       the last element is removed using pop
#   5.  Otherwise, the current direction is added to the dirs array using push
#   6.  The () returns the simplified plan after processing all directions
#   7.  This solution is efficient and has a time complexity of O(n) where n is the number of directions in the input plan
#   8.  The space complexity is O(n) as the dirs array can store up to n directions