# Write a function that takes an array of numbers (integers for the tests) 
# and a target number. It should find two different items in the array that, 
# when added together, give the target value. The indices of these items 
# should then be returned in a tuple / list (depending on your language) 
# like so: (index1, index2).

# For the purposes of this kata, some tests may have multiple answers; 
# any valid solutions will be accepted.

# The input will always be valid (numbers will be an array of length 2 
# or greater, and all of the items will be numbers; target will always 
# be the sum of two different items from that array).

# Based on: https://leetcode.com/problems/two-sum/

# two_sum([1, 2, 3], 4) # returns (0, 2) or (2, 0)
# two_sum([3, 2, 4], 6) # returns (1, 2) or (2, 1)

# -------------------------------------------------------------------------------------
# -----Solution 1-----Brute Force Solution w/ Nested Loops & Enumerate-----
def two_sum(nums, t):
    for i, x in enumerate(nums):
        for j, y in enumerate(nums):
            if i != j and x + y == t:
                return [i, j]
#  1.  This solution has a time complexity of O(n^2) because of the nested loops used and
#      is not the most efficient solution
#  2.  The enumerate function is used to get the index and value of each element by iterating
#      through the nums array. Enumerate in Python is used to loop through the iterable and
#      return the index of each item in the iterable and the item itself for example:
#      for i, num in enumerate(nums):
#          print(i, num)
#      The above code will print the index and the value of each element in the
#      nums array
#  3.  The if statement checks if the indices are not the same and if the sum of the
#      two numbers is equal to the target. If the condition is met, the indices are
#      returned as a list

# -------------------------------------------------------------------------------------
# -----MOST EFFICIENT Solution 2-----Hash Map Solution w/ Dictionary & Enumerate & Unpacking & Ternary Operator-----
def two_sum(nums, target):
    d = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in d:
            return [d[diff], i]
        d[num] = i
#  1.  This solution has a time complexity of O(n) because it uses a dictionary to store
#      the difference between the target and the current number and the index of the
#      current. It is more efficient than the first solution
#  2.  The enumerate function is used to get the index and value of each element by iterating
#      through the nums array
#  3.  The diff variable is used to store the difference between the target and the current
#      number
#  4.  The if statement checks if the difference is in the dictionary. If it is, the indices
#      are returned as a list
#  5.  The d[num] = i line is used to store the current number and its index in the dictionary


# -------------------------------------------------------------------------------------
# -----Solution 3-----Optimized Brute Force Solution w/ Nested Loops & Len-----
def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if (numbers[i] + numbers[j]) == target:
                return [i, j]
#  1.  This solution has a time complexity of O(n) because it uses two nested loops to
#      iterate through the numbers array. It is less efficient than the second solution and
#      more efficient than the first solution, but it is a valid approach to solving
#      the problem.
#  2.  The range(len(numbers)) function is used to generate a range of numbers from 0 to
#      the length of the numbers array
#  3.  The range(i+1, len(numbers)) function is used to generate a range of numbers from
#      i+1 to the length of the numbers array. This is done to avoid comparing the same
#      numbers twice
#  4.  The if statement checks if the sum of the two numbers is equal to the target. If it
#      is, the indices are returned as a list

# -------------------------------------------------------------------------------------
# -----Solution 4-----Javascript Solution using Map & For Loop & Ternary Operator & Set & Get-----
# function twoSum(numbers, target) {
#   let seen = new Map();
#   for (let i = 0; i < numbers.length; i++) {
#     let x = numbers[i], y = target - x;
#     if (seen.has(y))
#       return [seen.get(y), i];
#     seen.set(x, i);
#   }
# }
#  1.  This solution is similar to the second solution in Python and has a time complexity
#      of O(n) because it uses a Map to store the difference between the target and the
#      current number and the index of the current number. It is an efficient solution
#      to the problem.
#  2.  The Map object is used to store key-value pairs. In this case, the key is
#      the difference between the target and the current number, and the value is the
#      index of the current number.
#  3.  The for loop is used to iterate through the numbers array
#  4.  The x and y variables are used to store the current number and the difference
#      between the target and the current number
#  5.  The if statement checks if the Map contains the difference. If it does, the
#      indices are returned as an array
#  6.  The set method is used to add the current number and
#      its index to the Map