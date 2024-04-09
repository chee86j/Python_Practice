# THE MUSUEM OF INCREDIBLY DULL THINGS
# The museum of incredibly dull things wants to get rid of some exhibits. 
# Miriam, the interior architect, comes up with a plan to remove the most 
# boring exhibits. She gives them a rating, and then removes the one with 
# the lowest rating.

# However, just as she finished rating all exhibits, she's off to an important 
# fair, so she asks you to write a program that tells her the ratings of the 
# exhibits after removing the lowest one. Fair enough.

# TASK
# Given an array of integers, remove the smallest value. Do not mutate the 
# original array/list. If there are multiple elements with the same value, 
# remove the one with the lowest index. If you get an empty array/list, 
# return an empty array/list.

# Don't change the order of the elements that are left.

# Examples
# * Input: [1,2,3,4,5], output = [2,3,4,5]
# * Input: [5,3,2,1,4], output = [5,3,2,4]
# * Input: [2,2,1,2,1], output = [2,2,2,1]

# -------------------------------------------------------------------------------------
# -----Solution 1-----Slicing-----
def remove_smallest(numbers):
    a = numbers[:]
    if a:
        a.remove(min(a))
    return a
#   1. create a copy of input array using slicing.
#   2. use [:] to copy array, so that original array is not mutated.
#   3. check if array is not empty.
#   4. remove smallest element from copied array.

# -------------------------------------------------------------------------------------
# -----Solution 2-----Index-----
def remove_smallest(numbers):
    if len(numbers) < 1: 
        return numbers
    idx = numbers.index(min(numbers))
    return numbers[0:idx] + numbers[idx+1:]
#   1. check if length of input array is less than 1.
#   2. If so, return input array as is.
#   3. get index of smallest element in input array.
#   4. return all elements before smallest element + all elements after smallest element.
#   5. effectively removing smallest element from input array.