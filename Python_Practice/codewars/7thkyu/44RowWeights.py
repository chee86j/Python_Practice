# Scenario:
# Several people are standing in a row divided into two teams.
# The first person goes into team 1, the second goes into team 2, 
# the third goes into team 1, and so on.

# Task:
# Given an array of positive integers (the weights of the people), return a new array/tuple of two integers, 
# where the first one is the total weight of team 1, and the second one is the total weight of team 2.

# Notes:
# -Array size is at least 1.
# -All numbers will be positive.

# Input >> Output Examples:
# rowWeights([13, 27, 49])  ==>  return (62, 27)

# Explanation:
# The first element 62 is the total weight of team 1, and the second element 27 is the total weight of team 2.

# rowWeights([50, 60, 70, 80])  ==>  return (120, 140)

# Explanation:
# The first element 120 is the total weight of team 1, and the second element 140 is the total weight of team 2.

# rowWeights([80])  ==>  return (80, 0)

# Explanation:
# The first element 80 is the total weight of team 1, and the second element 0 is the total weight of team 2.

# -------------------------------------------------------------------------------------
# -----Solution 1----Sum() & Slicing-----
def row_weights(array):
    return sum(array[::2]), sum(array[1::2])
#   1.  () takes an arr of positive integers as input.
#   2.  [::2] & [1::2] slices the arr into two parts. The [::2] takes every other element
#       starting from the first element (index 0) & [1::2] takes every other element starting
#       from the second element (index 1).
#   3.  sum() calculates the total weight of each team.
#   4.  The return statement returns a tuple containing the total weight of team 1 & team 2.
#   5.  This solution has a time complexity of O(n) where n is the length of the input arr.
#       This is because the slicing operation takes O(n) time to create a new arr with every
#       other element. The sum() function also takes O(n) time to calculate the sum of the arr.
#       The space complexity is O(1) because the function uses a constant amount of extra space
#       regardless of the size of the input arr.


# -------------------------------------------------------------------------------------
# -----Solution 2----Conditional & For Loop-----
def row_weights(array):
    odd = 0
    even = 0
    for i in range(len(array)):
        if i%2 == 0:
            odd += array[i]
        else:
            even += array[i]
    return odd, even
#   1.  () initializes two vars `odd` & `even` to store the total weight of team 1 & team 2.
#   2.  A for loop iterates over the input arr using the range() function to get the index of each element.
#   3.  The if statement then checks if the index is even or odd using the modulo operator (%). If the index is even,
#       the element is added to the `odd` var. Otherwise, it is added to the `even` var.
#   4.  The return statement returns a tuple containing the total weight of team 1 & team 2.
#   5.  This solution has a time complexity of O(n) where n is the length of the input arr. This is because the for loop
#       iterates over each element of the arr, and the if statement has a constant time complexity. The space complexity
#       is O(1) because the function uses a constant amount of extra space regardless of the size of the input arr.
#       Compared to Solution 1, this solution is more verbose and requires more lines of code to achieve the same result.

# -------------------------------------------------------------------------------------
# -----Solution 3----List Comprehension & Sum()-----
def row_weights(array):
    a = array[::2]
    b = array[1::2]
    return sum(a),sum(b)
#   1.  () slices the input arr into two parts using list slicing. The [::2] takes every other element starting from the first
#       element (index 0) & [1::2] takes every other element starting from the second element (index 1).
#   2.  sum() calculates the total weight of each team.
#   3.  The return statement returns a tuple containing the total weight of team 1 & team 2.
#   4.  This solution has a time complexity of O(n) where n is the length of the input arr. This is because the slicing operation
#       takes O(n) time to create a new arr with every other element. The sum() function also takes O(n) time to calculate the sum
#       of the arr. The space complexity is O(1) because the function uses a constant amount of extra space regardless of the size
#       of the input arr.
#       Compared to Solution 1, this solution is more concise and uses list comprehension to create the sliced arrs & compared to
#       Solution 2, this solution is more concise and does not require a for loop to iterate over the input arr. Of the three solutions,
#       Solution 3 is the most concise and readable.

# -------------------------------------------------------------------------------------
# -----Solution 4----Javascript Solution-----Filter() & Reduce()-----
# function rowWeights(array){
#   let t1 = array.filter((x, i)=>i%2==0).reduce((a,item)=>a+item,0);
#   let t2 = array.filter((x, i)=>i%2!=0).reduce((a,item)=>a+item,0);
#   return [t1, t2];
# }
#   1.  Filter() method creates a new arr with all elements that pass the test implemented by the provided function.
#       In this case, the test checks if the index is even or odd using the modulo operator (%).
#   2.  The reduce() method applies a ()) against an accumulator and each element in the arr (from left to right) to reduce it to a single value.
#       In this case, the ()) calculates the sum of the elements in the filtered arr.
#   3.  The return statement then returns an arr containing the total weight of team 1 & team 2.
#   4.  This solution has a time complexity of O(n) where n is the length of the input arr. This is because the filter() method iterates over
#       each element of the arr to check if it passes the test, and the reduce() method also iterates over each element to calculate the sum.
#       The space complexity is O(n) because the filter() method creates a new arr with the filtered elements, which could be the same size as the
#       input arr. This solution is similar to Solution 2 but uses the filter() and reduce() methods instead of a for loop to filter and sum the elements.
